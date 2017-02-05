"""Search API Tests for Version 1.0.

This is a testing template for the generated SearchAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.search import SearchAPI


class TestSearchAPI(unittest.TestCase):
    """Tests for the SearchAPI."""

    def setUp(self):
        self.client = SearchAPI(secrets.instance_address, secrets.access_token)

    def test_find_recipients_conversations(self):
        """Integration test for the SearchAPI.find_recipients_conversations method."""

        r = self.client.find_recipients_conversations(context=None, exclude=None, from_conversation_id=None, permissions=None, search=None, type=None, user_id=None)

    def test_find_recipients_search(self):
        """Integration test for the SearchAPI.find_recipients_search method."""

        r = self.client.find_recipients_search(context=None, exclude=None, from_conversation_id=None, permissions=None, search=None, type=None, user_id=None)

    def test_list_all_courses(self):
        """Integration test for the SearchAPI.list_all_courses method."""

        r = self.client.list_all_courses(open_enrollment_only=None, public_only=None, search=None)

