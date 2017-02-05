"""AccountNotifications API Tests for Version 1.0.

This is a testing template for the generated AccountNotificationsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.account_notifications import AccountNotificationsAPI
from pycanvas.apis.account_notifications import Accountnotification


class TestAccountNotificationsAPI(unittest.TestCase):
    """Tests for the AccountNotificationsAPI."""

    def setUp(self):
        self.client = AccountNotificationsAPI(secrets.instance_address, secrets.access_token)

    def test_index_of_active_global_notification_for_user(self):
        """Integration test for the AccountNotificationsAPI.index_of_active_global_notification_for_user method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.index_of_active_global_notification_for_user(user_id, account_id)

    def test_show_global_notification(self):
        """Integration test for the AccountNotificationsAPI.show_global_notification method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_global_notification(id, user_id, account_id)

    def test_close_notification_for_user(self):
        """Integration test for the AccountNotificationsAPI.close_notification_for_user method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.close_notification_for_user(id, user_id, account_id)

    def test_create_global_notification(self):
        """Integration test for the AccountNotificationsAPI.create_global_notification method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_global_notification(self):
        """Integration test for the AccountNotificationsAPI.update_global_notification method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

