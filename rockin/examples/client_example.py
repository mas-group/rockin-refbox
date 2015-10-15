#! /usr/bin/python
"""
An example of a client TCP socket connection.

"""


import sys
import time
import socket
import protobuf_comm.client as client
import msgs.AttentionMessage_pb2 as AttentionMessage


class ExampleClient(object):
    """
    Example to implement a ProtobufStreamClient.

    """
    def __init__(self, host, port, socket_id=0, node_rate=10):
        # Node rate specified in Hz but used in seconds.
        self.node_rate = 1. / node_rate

        # Create client and register a message
        self.example_client = client.ProtobufStreamClient(host, port, socket_id)
        self.example_client.message_register.add_message_type(
            AttentionMessage.AttentionMessage
        )

        self.example_client.signal_connected_cb(self.client_connected)
        self.example_client.signal_disconnected_cb(self.client_disconnected)
        self.example_client.signal_received_cb(self.client_msg)

        self.referee_box_running = False

    def client_connected(self):
        """
        Prints a message when a signal, representing a established connection, is
        received. And sets the status of the referee box to 'running'.

        """
        print("Client connected")
        self.referee_box_running = True

    def client_disconnected(self):
        """
        Prints a message when a signal, representing a closed connection, is received.
        And sets the status of the referee box to 'not running'.

        """
        print("Client DISconnected")
        self.referee_box_running = False

    def client_msg(self, message):
        """
        Prints a message when a signal receives a message.

        """
        print("Message received:\n{0}".format(message.__str__()))

    def start(self):
        """
        Starts the state machine of this example.

        """
        state = 'IDLE'
        while True:
            if state == 'IDLE':
                state = self.idle_state()
            elif state == 'RUNNING':
                state = self.running_state()
            time.sleep(self.node_rate)

    def idle_state(self):
        """
        Executes the IDLE state of the state machine.

        :return: The updated state.
        :rtype: str

        """
        if self.referee_box_running:
            return 'RUNNING'
        else:
            self.referee_box_running = True
            return 'IDLE'

    def running_state(self):
        """
        Executes the RUNNING state of the state machine.

        :return: The updated state.
        :rtype: str

        """
        try:
            self.example_client.start()
            self.referee_box_running = True
            while self.referee_box_running:
                time.sleep(self.node_rate)
            return 'RUNNING'
        except socket.error:
            # e.g. the server is not ready
            self.referee_box_running = False
            self.client_disconnected()
            return 'IDLE'
        except Exception as e:
            self.referee_box_running = False
            print("Unexpected exception occurred:\n{0}".format(e))
            return 'IDLE'


if __name__ == "__main__":
    # Create and start a thread
    my_thread = client.IOLoopThread()
    my_thread.start()

    my_client = ExampleClient('127.0.0.1', 4444, node_rate=30)
    try:
        my_client.start()
    except KeyboardInterrupt:
        print("\nClosing application...")
        sys.exit(0)
    finally:
        my_thread.shutdown()
