"""Admins API Tests for Version 1.0.

This is a testing template for the generated AdminsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.admins import AdminsAPI
from pycanvas.apis.admins import Admin


class TestAdminsAPI(unittest.TestCase):
    """Tests for the AdminsAPI."""

    def setUp(self):
        self.client = AdminsAPI(secrets.instance_address, secrets.access_token)

    def test_make_account_admin(self):
        """Integration test for the AdminsAPI.make_account_admin method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_account_admin(self):
        """Integration test for the AdminsAPI.remove_account_admin method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.remove_account_admin(user_id, account_id, role=None, role_id=None)

    def test_list_account_admins(self):
        """Integration test for the AdminsAPI.list_account_admins method."""
        account_id = None  # Change me!!

        r = self.client.list_account_admins(account_id, user_id=None)

