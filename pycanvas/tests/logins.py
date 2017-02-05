"""Logins API Tests for Version 1.0.

This is a testing template for the generated LoginsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.logins import LoginsAPI


class TestLoginsAPI(unittest.TestCase):
    """Tests for the LoginsAPI."""

    def setUp(self):
        self.client = LoginsAPI(secrets.instance_address, secrets.access_token)

    def test_list_user_logins_accounts(self):
        """Integration test for the LoginsAPI.list_user_logins_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_user_logins_accounts(account_id)

    def test_list_user_logins_users(self):
        """Integration test for the LoginsAPI.list_user_logins_users method."""
        user_id = None  # Change me!!

        r = self.client.list_user_logins_users(user_id)

    def test_create_user_login(self):
        """Integration test for the LoginsAPI.create_user_login method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_user_login(self):
        """Integration test for the LoginsAPI.edit_user_login method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_user_login(self):
        """Integration test for the LoginsAPI.delete_user_login method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_user_login(id, user_id)

