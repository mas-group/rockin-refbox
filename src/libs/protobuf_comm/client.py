#! /usr/bin/python
"""
A module that defines a class to implement a TCP socket connection using the framing
protocol to receive and transmit messages from and to a ProtobufStreamServer class, as
defined by the Referee Box for the RoboCup Logistics League sponsored by Festo (LLSF)
integration manual.

"""

import struct
import socket
import threading
import errno

import tornado.ioloop
import protobuf_comm.message_register as message_register


mutex = threading.Lock()


class IOLoopThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.io_loop = tornado.ioloop.IOLoop.instance()

    def run(self):
        self.io_loop.start()

    def shutdown(self):
        self.io_loop.stop()


class ProtobufStreamClient(object):
    """
    Class to implement a TCP socket connection using the framing protocol to receive
    and transmit messages from and to a ProtobufStreamServer class.

    """
    # The frame header, according to the Referee Box integration manual, consists of
    # four unsigned chars (B) followed by one unsigned integer (I))
    FRAME_HEADER_STRUCT = '4BI'
    # Therefore its size is:
    FRAME_HEADER_SIZE = 8       # in bytes

    # The message header, according to the Referee Box integration manual, consists of
    # two unsigned shorts (H)
    MESSAGE_HEADER_STRUCT = '2H'
    # Therefore its size is:
    MESSAGE_HEADER_SIZE = 4     # in bytes

    def __init__(self, host, port, socket_id, buffer_size=1024):
        """
        Creates a instance of IOLoop from tornado and an instance from MessageRegister.

        :param host: Host to connect to.
        :type host: str

        :param port: Port of the host to connect to.
        :type port: int

        :param socket_id: Number to identify the socket connection.
        :type socket_id: int

        :param buffer_size: Default number of bytes to read from the buffer.
        :type buffer_size: int

        """
        self.id = socket_id
        self.buffer_size = buffer_size
        self.host = host
        self.port = port
        self.io_loop = tornado.ioloop.IOLoop.instance()

        self.signal_received = None
        self.signal_connected = None
        self.signal_disconnected = None
        self.client_socket = None

        self.message_register = message_register.MessageRegister()

        self.data = ''
        # Payload size changes from message to message (in bytes)
        self.payload_size = 0

    def signal_received_cb(self, callback):
        """
        Invoked when a signal is received.

        """
        self.signal_received = callback

    def signal_connected_cb(self, callback):
        """
        Invoked when the connection has been established.

        """
        self.signal_connected = callback

    def signal_disconnected_cb(self, callback):
        """
        Invoked when the connection has been closed.

        """
        self.signal_disconnected = callback

    def start(self):
        """
        Creates a TCP socket connection and defines the required callbacks.

        """
        # 1. Establish a TCP connection to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.connect((self.host, self.port))

        # Non-blocking socket
        self.client_socket.setblocking(False)

        if self.signal_connected is not None:
            self.signal_connected()

        events_desired = self.io_loop.READ | self.io_loop.WRITE | self.io_loop.ERROR
        events_to_update = self.io_loop.READ | self.io_loop.WRITE

        # 2. Add to tornado for receiving a callback when we receive data
        self.io_loop.add_handler(
            self.client_socket.fileno(), self._handle_events, events_desired
        )
        self.io_loop.update_handler(self.client_socket.fileno(), events_to_update)

    def _handle_events(self, fd, events):
        """
        Handles the socket's events.

        """
        if not self.client_socket:
            print("Got events for closed stream {0}".format(fd))
            return
        if events & self.io_loop.READ:
            self._handle_read()
        if events & self.io_loop.WRITE:
            self._handle_write('')
        if events & self.io_loop.ERROR:
            self._close_socket()
            return

    def _close_socket(self):
        """
        Closes the socket connection.

        """
        try:
            self.io_loop.remove_handler(self.client_socket.fileno())
        except Exception:
            pass

        if self.client_socket:
            if self.signal_disconnected is not None:
                self.signal_disconnected()
            self.client_socket.close()
            self.client_socket = None

    def _handle_write(self, message):
        """
        Writes a serialized message when available. Signal provided by epoll.

        :param message: Message to send to the server.
        :type message: str

        """
        if not message:
            return

        mutex.acquire()
        try:
            total_sent = 0
            while total_sent < len(message):
                bytes_sent = self.client_socket.send(message[total_sent:])
                if bytes_sent == 0:
                    raise RuntimeError("Connection has been lost.")
                total_sent += bytes_sent
        finally:
            mutex.release()

    def send(self, message, protocol_version=2, cipher=0, reserved_2=0, reserved_3=0):
        """
        Sends a message to the server.

        :param message: Message to send to the server.
        :type message: google.protobuf.message.Message

        """
        if (message is None) or (self.signal_connected is None):
            return None

        component_id = socket.htons(message.COMP_ID)
        message_type = socket.htons(message.MSG_TYPE)

        serialized_message = self.message_register.serialize(
            message, component_id, message_type
        )
        if serialized_message is None:
            print("Failed to serialized message")
            return None

        msg_header = struct.pack(self.MESSAGE_HEADER_STRUCT, component_id, message_type)
        payload_size = socket.htonl(len(msg_header + serialized_message))

        frame_header = struct.pack(
            self.FRAME_HEADER_STRUCT, protocol_version,
            cipher, reserved_2, reserved_3, payload_size
        )
        my_msg = frame_header + msg_header + serialized_message

        self._handle_write(my_msg)

    def _handle_read(self):
        """
        Reads new data when it becomes available. Signal provided by epoll.

        """
        # 1. Read header, and obtain payload size
        self.data = self.read(self.FRAME_HEADER_SIZE)
        if self.data is not None:
            self.payload_size = self.handle_read_header(self.data[:self.FRAME_HEADER_SIZE])
        else:
            return None

        # 1.1 Update data
        self.data = self.data[self.FRAME_HEADER_SIZE:]

        # 2. Read message, plus its header, according to payload size
        self.data += self.read(self.payload_size)
        if self.data is not None:
            message = self.handle_read_message(self.data[:self.payload_size])
        else:
            return None

        # 2.1 Update data
        self.data = self.data[self.payload_size:]
        if (message is not None) and (self.signal_received is not None):
            self.signal_received(message)

    def read(self, bytes_to_read=None):
        """
        Reads from a socket the amount of bytes specified.

        :param bytes_to_read: Number of bytes that should be read from the buffer.
        Defaults to self.buffer_size.
        :type bytes_to_read: int

        :return: The data received from the socket connection. If an error occurs,
        or a the socket connection is lost, then None is returned.
        :rtype: str or None

        """
        if bytes_to_read is None:
            bytes_to_read = self.buffer_size

        received_data = ''

        # Receive data until the length of data received matches what is expected
        while len(received_data) < bytes_to_read:
            try:
                received_data += self.client_socket.recv(bytes_to_read)
            except socket.error, e:
                if e[0] in (errno.EWOULDBLOCK, errno.EAGAIN):
                    return None
                else:
                    print("Read error on {0}:\n{1}".format(self.client_socket.fileno, e))
                    self._close_socket()
                    return None

            # Empty data means closed socket
            if not received_data:
                self._close_socket()
                return None

        return received_data

    def handle_read_header(self, received_data):
        """
        Reads the frame_header and obtains the payload_size.

        :param received_data: The header as a string.
        :type received_data: str

        :return: The payload size of the message.
        :rtype: long

        """
        unpacked_message = struct.unpack(self.FRAME_HEADER_STRUCT, received_data)
        protocol_version, cipher, reserved_2, reserved_3, payload_size = unpacked_message

        payload_size = socket.ntohl(payload_size)

        return payload_size

    def handle_read_message(self, received_data):
        """
        Deserializes the received data, assuming it contains a Protobuf message plus
        its message header.

        :param received_data: A message header with its protobuf message.
        :type received_data: str

        :return: The deserialized Protobuf message. If the deserialization fails, then
        None is returned.
        :rtype: google.protobuf.message.Message or None

        """
        component_id, message_type = struct.unpack(
            self.MESSAGE_HEADER_STRUCT, received_data[:self.MESSAGE_HEADER_SIZE]
        )
        component_id = socket.ntohs(component_id)
        message_type = socket.ntohs(message_type)

        return self.message_register.deserialize(
            received_data[self.MESSAGE_HEADER_SIZE:], component_id, message_type
        )
