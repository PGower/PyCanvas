"""AuthenticationsLog API Tests for Version 1.0.

This is a testing template for the generated AuthenticationsLogAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.authentications_log import AuthenticationsLogAPI
from pycanvas.apis.authentications_log import Authenticationevent


class TestAuthenticationsLogAPI(unittest.TestCase):
    """Tests for the AuthenticationsLogAPI."""

    def setUp(self):
        self.client = AuthenticationsLogAPI(secrets.instance_address, secrets.access_token)

    def test_query_by_login(self):
        """Integration test for the AuthenticationsLogAPI.query_by_login method."""
        login_id = None  # Change me!!

        r = self.client.query_by_login(login_id, end_time=None, start_time=None)

    def test_query_by_account(self):
        """Integration test for the AuthenticationsLogAPI.query_by_account method."""
        account_id = None  # Change me!!

        r = self.client.query_by_account(account_id, end_time=None, start_time=None)

    def test_query_by_user(self):
        """Integration test for the AuthenticationsLogAPI.query_by_user method."""
        user_id = None  # Change me!!

        r = self.client.query_by_user(user_id, end_time=None, start_time=None)

