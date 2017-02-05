"""PollSessions API Tests for Version 1.0.

This is a testing template for the generated PollSessionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.poll_sessions import PollSessionsAPI
from pycanvas.apis.poll_sessions import Pollsession


class TestPollSessionsAPI(unittest.TestCase):
    """Tests for the PollSessionsAPI."""

    def setUp(self):
        self.client = PollSessionsAPI(secrets.instance_address, secrets.access_token)

    def test_list_poll_sessions_for_poll(self):
        """Integration test for the PollSessionsAPI.list_poll_sessions_for_poll method."""
        poll_id = None  # Change me!!

        r = self.client.list_poll_sessions_for_poll(poll_id)

    def test_get_results_for_single_poll_session(self):
        """Integration test for the PollSessionsAPI.get_results_for_single_poll_session method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_results_for_single_poll_session(id, poll_id)

    def test_create_single_poll_session(self):
        """Integration test for the PollSessionsAPI.create_single_poll_session method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_poll_session(self):
        """Integration test for the PollSessionsAPI.update_single_poll_session method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_poll_session(self):
        """Integration test for the PollSessionsAPI.delete_poll_session method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_poll_session(id, poll_id)

    def test_open_poll_session(self):
        """Integration test for the PollSessionsAPI.open_poll_session method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.open_poll_session(id, poll_id)

    def test_close_opened_poll_session(self):
        """Integration test for the PollSessionsAPI.close_opened_poll_session method."""
        poll_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.close_opened_poll_session(id, poll_id)

    def test_list_opened_poll_sessions(self):
        """Integration test for the PollSessionsAPI.list_opened_poll_sessions method."""

        r = self.client.list_opened_poll_sessions()

    def test_list_closed_poll_sessions(self):
        """Integration test for the PollSessionsAPI.list_closed_poll_sessions method."""

        r = self.client.list_closed_poll_sessions()

