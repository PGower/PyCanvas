"""CommMessages API Tests for Version 1.0.

This is a testing template for the generated CommMessagesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.comm_messages import CommMessagesAPI
from pycanvas.apis.comm_messages import Commmessage


class TestCommMessagesAPI(unittest.TestCase):
    """Tests for the CommMessagesAPI."""

    def setUp(self):
        self.client = CommMessagesAPI(secrets.instance_address, secrets.access_token)

    def test_list_of_commmessages_for_user(self):
        """Integration test for the CommMessagesAPI.list_of_commmessages_for_user method."""
        user_id = None  # Change me!!

        r = self.client.list_of_commmessages_for_user(user_id, end_time=None, start_time=None)

