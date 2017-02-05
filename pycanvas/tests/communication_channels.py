"""CommunicationChannels API Tests for Version 1.0.

This is a testing template for the generated CommunicationChannelsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.communication_channels import CommunicationChannelsAPI
from pycanvas.apis.communication_channels import Communicationchannel


class TestCommunicationChannelsAPI(unittest.TestCase):
    """Tests for the CommunicationChannelsAPI."""

    def setUp(self):
        self.client = CommunicationChannelsAPI(secrets.instance_address, secrets.access_token)

    def test_list_user_communication_channels(self):
        """Integration test for the CommunicationChannelsAPI.list_user_communication_channels method."""
        user_id = None  # Change me!!

        r = self.client.list_user_communication_channels(user_id)

    def test_create_communication_channel(self):
        """Integration test for the CommunicationChannelsAPI.create_communication_channel method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_communication_channel_id(self):
        """Integration test for the CommunicationChannelsAPI.delete_communication_channel_id method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_communication_channel_id(id, user_id)

    def test_delete_communication_channel_type(self):
        """Integration test for the CommunicationChannelsAPI.delete_communication_channel_type method."""
        user_id = None  # Change me!!
        type = None  # Change me!!
        address = None  # Change me!!

        r = self.client.delete_communication_channel_type(type, user_id, address)

