"""PollSubmissions API Tests for Version 1.0.

This is a testing template for the generated PollSubmissionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.poll_submissions import PollSubmissionsAPI
from pycanvas.apis.poll_submissions import Pollsubmission


class TestPollSubmissionsAPI(unittest.TestCase):
    """Tests for the PollSubmissionsAPI."""

    def setUp(self):
        self.client = PollSubmissionsAPI(secrets.instance_address, secrets.access_token)

    def test_get_single_poll_submission(self):
        """Integration test for the PollSubmissionsAPI.get_single_poll_submission method."""
        poll_id = None  # Change me!!
        poll_session_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_poll_submission(id, poll_id, poll_session_id)

    def test_create_single_poll_submission(self):
        """Integration test for the PollSubmissionsAPI.create_single_poll_submission method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

