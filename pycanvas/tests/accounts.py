"""Accounts API Tests for Version 1.0.

This is a testing template for the generated AccountsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.accounts import AccountsAPI
from pycanvas.apis.accounts import Account


class TestAccountsAPI(unittest.TestCase):
    """Tests for the AccountsAPI."""

    def setUp(self):
        self.client = AccountsAPI(secrets.instance_address, secrets.access_token)

    def test_list_accounts(self):
        """Integration test for the AccountsAPI.list_accounts method."""

        r = self.client.list_accounts(include=None)

    def test_list_accounts_for_course_admins(self):
        """Integration test for the AccountsAPI.list_accounts_for_course_admins method."""

        r = self.client.list_accounts_for_course_admins()

    def test_get_single_account(self):
        """Integration test for the AccountsAPI.get_single_account method."""
        id = None  # Change me!!

        r = self.client.get_single_account(id)

    def test_get_sub_accounts_of_account(self):
        """Integration test for the AccountsAPI.get_sub_accounts_of_account method."""
        account_id = None  # Change me!!

        r = self.client.get_sub_accounts_of_account(account_id, recursive=None)

    def test_list_active_courses_in_account(self):
        """Integration test for the AccountsAPI.list_active_courses_in_account method."""
        account_id = None  # Change me!!

        r = self.client.list_active_courses_in_account(account_id, by_subaccounts=None, by_teachers=None, completed=None, enrollment_term_id=None, enrollment_type=None, hide_enrollmentless_courses=None, include=None, published=None, search_term=None, state=None, with_enrollments=None)

    def test_update_account(self):
        """Integration test for the AccountsAPI.update_account method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_user_from_root_account(self):
        """Integration test for the AccountsAPI.delete_user_from_root_account method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.delete_user_from_root_account(user_id, account_id)

    def test_create_new_sub_account(self):
        """Integration test for the AccountsAPI.create_new_sub_account method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

