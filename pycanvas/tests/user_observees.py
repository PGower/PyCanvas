"""UserObservees API Tests for Version 1.0.

This is a testing template for the generated UserObserveesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.user_observees import UserObserveesAPI


class TestUserObserveesAPI(unittest.TestCase):
    """Tests for the UserObserveesAPI."""

    def setUp(self):
        self.client = UserObserveesAPI(secrets.instance_address, secrets.access_token)

    def test_list_observees(self):
        """Integration test for the UserObserveesAPI.list_observees method."""
        user_id = None  # Change me!!

        r = self.client.list_observees(user_id)

    def test_add_observee_with_credentials(self):
        """Integration test for the UserObserveesAPI.add_observee_with_credentials method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_observee(self):
        """Integration test for the UserObserveesAPI.show_observee method."""
        user_id = None  # Change me!!
        observee_id = None  # Change me!!

        r = self.client.show_observee(user_id, observee_id)

    def test_add_observee(self):
        """Integration test for the UserObserveesAPI.add_observee method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_observee(self):
        """Integration test for the UserObserveesAPI.remove_observee method."""
        user_id = None  # Change me!!
        observee_id = None  # Change me!!

        r = self.client.remove_observee(user_id, observee_id)

