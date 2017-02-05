"""Conversations API Tests for Version 1.0.

This is a testing template for the generated ConversationsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.conversations import ConversationsAPI
from pycanvas.apis.conversations import Conversation


class TestConversationsAPI(unittest.TestCase):
    """Tests for the ConversationsAPI."""

    def setUp(self):
        self.client = ConversationsAPI(secrets.instance_address, secrets.access_token)

    def test_list_conversations(self):
        """Integration test for the ConversationsAPI.list_conversations method."""

        r = self.client.list_conversations(filter=None, filter_mode=None, include=None, include_all_conversation_ids=None, interleave_submissions=None, scope=None)

    def test_create_conversation(self):
        """Integration test for the ConversationsAPI.create_conversation method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_running_batches(self):
        """Integration test for the ConversationsAPI.get_running_batches method."""

        r = self.client.get_running_batches()

    def test_get_single_conversation(self):
        """Integration test for the ConversationsAPI.get_single_conversation method."""
        id = None  # Change me!!

        r = self.client.get_single_conversation(id, auto_mark_as_read=None, filter=None, filter_mode=None, interleave_submissions=None, scope=None)

    def test_edit_conversation(self):
        """Integration test for the ConversationsAPI.edit_conversation method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_all_as_read(self):
        """Integration test for the ConversationsAPI.mark_all_as_read method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_conversation(self):
        """Integration test for the ConversationsAPI.delete_conversation method."""
        id = None  # Change me!!

        r = self.client.delete_conversation(id)

    def test_add_recipients(self):
        """Integration test for the ConversationsAPI.add_recipients method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_add_message(self):
        """Integration test for the ConversationsAPI.add_message method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_message(self):
        """Integration test for the ConversationsAPI.delete_message method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_batch_update_conversations(self):
        """Integration test for the ConversationsAPI.batch_update_conversations method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_find_recipients(self):
        """Integration test for the ConversationsAPI.find_recipients method."""

        r = self.client.find_recipients()

    def test_unread_count(self):
        """Integration test for the ConversationsAPI.unread_count method."""

        r = self.client.unread_count()

