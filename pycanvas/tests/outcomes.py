"""Outcomes API Tests for Version 1.0.

This is a testing template for the generated OutcomesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.outcomes import OutcomesAPI
from pycanvas.apis.outcomes import Outcome


class TestOutcomesAPI(unittest.TestCase):
    """Tests for the OutcomesAPI."""

    def setUp(self):
        self.client = OutcomesAPI(secrets.instance_address, secrets.access_token)

    def test_show_outcome(self):
        """Integration test for the OutcomesAPI.show_outcome method."""
        id = None  # Change me!!

        r = self.client.show_outcome(id)

    def test_update_outcome(self):
        """Integration test for the OutcomesAPI.update_outcome method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

