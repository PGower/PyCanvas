"""PollChoices API Tests for Version 1.0.

This is a testing template for the generated PollChoicesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.poll_choices import PollChoicesAPI
from pycanvas.apis.poll_choices import Pollchoice


class TestPollChoicesAPI(unittest.TestCase):
    """Tests for the PollChoicesAPI."""

    def setUp(self):
        self.client = PollChoicesAPI(secrets.instance_address, secrets.access_token)

    def test_list_poll_choices_in_poll(self):
        """Integration test for the PollChoicesAPI.list_poll_choices_in_poll method."""
        poll_id = None  # Change me!!

        r = self.client.list_poll_choices_in_poll(poll_id)

    def test_get_single_poll_choice(self):
        """Integration test for the PollChoicesAPI.get_single_poll_choice method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_poll_choice(id, poll_id)

    def test_create_single_poll_choice(self):
        """Integration test for the PollChoicesAPI.create_single_poll_choice method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_poll_choice(self):
        """Integration test for the PollChoicesAPI.update_single_poll_choice method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_poll_choice(self):
        """Integration test for the PollChoicesAPI.delete_poll_choice method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_poll_choice(id, poll_id)

