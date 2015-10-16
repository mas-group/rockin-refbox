#! /usr/bin/python
"""
Tests for the message_register.py module.

"""

import socket
import unittest
import protobuf_comm.message_register as message_register
import msgs.AttentionMessage_pb2 as AttentionMessage


class TestMessageRegister(unittest.TestCase):
    """
    Tests for the message_register.py module.

    """
    def test_add_message_type_basic(self):
        """
        Test that the MessageRegister class is able to add a new message type.

        """
        my_msg_register = message_register.MessageRegister()

        # Values for an AttentionMessage
        component_id = 2000
        message_type = 2
        expected = {
            (component_id, message_type): AttentionMessage.AttentionMessage
        }

        my_msg_register.add_message_type(AttentionMessage.AttentionMessage)
        actual = my_msg_register.message_table
        self.assertEqual(actual, expected)

    def test_remove_message_type_basic(self):
        """
        Test that the MessageRegister class is able to remove the given message type.

        """
        my_msg_register = message_register.MessageRegister()
        # First add a new message to be delete it afterwards
        my_msg_register.add_message_type(AttentionMessage.AttentionMessage)

        # Values for an AttentionMessage
        component_id = 2000
        message_type = 2
        expected = {}

        my_msg_register.remove_message_type(component_id, message_type)
        actual = my_msg_register.message_table
        self.assertEqual(actual, expected)

    def test_remove_message_type_missing_key(self):
        """
        Test that the MessageRegister class is able to handle a request to remove
        a message type that is not in the message table.

        """
        my_msg_register = message_register.MessageRegister()

        # Values for an AttentionMessage
        component_id = 2000
        message_type = 2

        with self.assertRaises(AssertionError):
            my_msg_register.remove_message_type(component_id, message_type)

    def test_serialize_basic(self):
        """
        Tests that a Protobuf message is serialized.

        """
        # Create message register
        my_msg_register = message_register.MessageRegister()

        # Create Protobuf message and add it to the table
        message_to_serialize = AttentionMessage.AttentionMessage()
        message_to_serialize.message = "Test message"
        component_id = socket.ntohs(2000)
        message_type = socket.ntohs(2)
        my_msg_register.add_message_type(AttentionMessage.AttentionMessage)

        expected = "\n\x0cTest message"
        actual = my_msg_register.serialize(
            message_to_serialize, component_id, message_type
        )

        self.assertEqual(actual, expected)

    def test_deserialize_basic(self):
        """
        Tests that a Protobuf message is deserialized.

        """
        # Create message register
        my_msg_register = message_register.MessageRegister()

        # Create Protobuf message and add it to the table
        message_to_serialize = AttentionMessage.AttentionMessage()
        message_to_serialize.message = "Test message"
        component_id = 2000
        message_type = 2
        my_msg_register.add_message_type(AttentionMessage.AttentionMessage)

        expected = AttentionMessage.AttentionMessage()
        expected.message = "Test message"

        serialized_message = "\n\x0cTest message"

        actual = my_msg_register.deserialize(
            serialized_message, component_id, message_type
        )

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
