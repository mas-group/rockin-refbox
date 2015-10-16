#! /usr/bin/python
"""
A module that defines required classes to register messages as defined by the
Referee Box for the RoboCup Logistics League sponsored by Festo (LLSF)
integration manual.

"""

import sys
import socket


class MessageRegister(object):
    """
    Class to register messages to react to. Messages types must be registered
    with the message register so that the client or peer can know how to
    deserialize incoming messages. Messages of an unknown type are ignored.

    """
    def __init__(self):
        self.message_table = {}

    def add_message_type(self, class_description):
        """
        Updates the message table with the class description specified. The key is
         a tuple composed of the class's component id and message type.

        :param class_description: Protobuf class to be added to the message table.
        :type class_description: google.protobuf.reflection.GeneratedProtocolMessageType

        """
        key = (class_description.COMP_ID, class_description.MSG_TYPE)
        self.message_table[key] = class_description

    def remove_message_type(self, comp_id, msg_type):
        """
        Removes a message type from the message table, given the component id and its
        message type.

        :param comp_id: ID of the component to remove from the message table.
        :type comp_id: int

        :param msg_type: Message type of the component to remove from the message table.
        :type msg_type: int

        """
        key = (comp_id, msg_type)
        assert self.message_table.get(key, None) is not None, \
            "The given component_id '{0}' and  msg_type '{1}' are not part of the " \
            "message table: {2}.".format(comp_id, msg_type, self.message_table)

        del self.message_table[key]

    def serialize(self, message, component_id, message_type):
        """
        Serializes the given message based on its component ID and message type,
        and updates the frame and message headers.

        :param message: Message to serialize.
        :type message: google.protobuf.message.Message

        :param component_id: ID of the component this message type belongs to. It must be
        encoded in network byte order (big-endian).
        :type component_id: int

        :param message_type: Message type. It must be encoded in network byte order
        (big-endian).
        :type message_type: int

        :return: The protobuf message as a serialized message. If a message cannot be
        serialized, then it returns None.
        :rtype: str or None

        """
        comp_id = socket.htons(component_id)
        msg_type = socket.htons(message_type)

        if self.message_table.get((comp_id, msg_type), None) is None:
            print("Message type {0}:{1} is not registered.".format(comp_id, msg_type))
            return None

        try:
            serialized_message = message.SerializeToString()
        except Exception as e:
            print("Cannot serialize message.\n{0}".format(e))
            raise e

        return serialized_message

    def deserialize(self, message, component_id, message_type):
        """
        Deserializes the given message based on its component ID and message type,
        and updates the frame and message headers.

        :param message: Message to deserialize.
        :type message: str

        :return: The deserialized message as a protobuf message. If a message cannot be
        crated, then it returns None.
        :rtype: google.protobuf.message.Message or None

        """
        protobuf_message = self.message_table.get((component_id, message_type), None)
        if protobuf_message is None:
            return None

        deserialized_message = protobuf_message()
        try:
            deserialized_message.ParseFromString(message)
        except Exception as e:
            print("Failed to parse message.\n{0}".format(sys.exc_info()[0]))
            raise e

        return deserialized_message
