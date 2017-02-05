"""NotificationPreferences API Tests for Version 1.0.

This is a testing template for the generated NotificationPreferencesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.notification_preferences import NotificationPreferencesAPI
from pycanvas.apis.notification_preferences import Notificationpreference


class TestNotificationPreferencesAPI(unittest.TestCase):
    """Tests for the NotificationPreferencesAPI."""

    def setUp(self):
        self.client = NotificationPreferencesAPI(secrets.instance_address, secrets.access_token)

    def test_list_preferences_communication_channel_id(self):
        """Integration test for the NotificationPreferencesAPI.list_preferences_communication_channel_id method."""
        user_id = None  # Change me!!
        communication_channel_id = None  # Change me!!

        r = self.client.list_preferences_communication_channel_id(user_id, communication_channel_id)

    def test_list_preferences_type(self):
        """Integration test for the NotificationPreferencesAPI.list_preferences_type method."""
        user_id = None  # Change me!!
        type = None  # Change me!!
        address = None  # Change me!!

        r = self.client.list_preferences_type(type, user_id, address)

    def test_get_preference_communication_channel_id(self):
        """Integration test for the NotificationPreferencesAPI.get_preference_communication_channel_id method."""
        user_id = None  # Change me!!
        communication_channel_id = None  # Change me!!
        notification = None  # Change me!!

        r = self.client.get_preference_communication_channel_id(user_id, notification, communication_channel_id)

    def test_get_preference_type(self):
        """Integration test for the NotificationPreferencesAPI.get_preference_type method."""
        user_id = None  # Change me!!
        type = None  # Change me!!
        address = None  # Change me!!
        notification = None  # Change me!!

        r = self.client.get_preference_type(type, user_id, address, notification)

    def test_update_preference_communication_channel_id(self):
        """Integration test for the NotificationPreferencesAPI.update_preference_communication_channel_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_preference_type(self):
        """Integration test for the NotificationPreferencesAPI.update_preference_type method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_multiple_preferences_communication_channel_id(self):
        """Integration test for the NotificationPreferencesAPI.update_multiple_preferences_communication_channel_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_multiple_preferences_type(self):
        """Integration test for the NotificationPreferencesAPI.update_multiple_preferences_type method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

