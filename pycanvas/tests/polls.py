"""Polls API Tests for Version 1.0.

This is a testing template for the generated PollsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.polls import PollsAPI
from pycanvas.apis.polls import Poll


class TestPollsAPI(unittest.TestCase):
    """Tests for the PollsAPI."""

    def setUp(self):
        self.client = PollsAPI(secrets.instance_address, secrets.access_token)

    def test_list_polls(self):
        """Integration test for the PollsAPI.list_polls method."""

        r = self.client.list_polls()

    def test_get_single_poll(self):
        """Integration test for the PollsAPI.get_single_poll method."""
        id = None  # Change me!!

        r = self.client.get_single_poll(id)

    def test_create_single_poll(self):
        """Integration test for the PollsAPI.create_single_poll method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_poll(self):
        """Integration test for the PollsAPI.update_single_poll method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_poll(self):
        """Integration test for the PollsAPI.delete_poll method."""
        id = None  # Change me!!

        r = self.client.delete_poll(id)

