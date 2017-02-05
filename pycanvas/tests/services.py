"""Services API Tests for Version 1.0.

This is a testing template for the generated ServicesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.services import ServicesAPI


class TestServicesAPI(unittest.TestCase):
    """Tests for the ServicesAPI."""

    def setUp(self):
        self.client = ServicesAPI(secrets.instance_address, secrets.access_token)

    def test_get_kaltura_config(self):
        """Integration test for the ServicesAPI.get_kaltura_config method."""

        r = self.client.get_kaltura_config()

    def test_start_kaltura_session(self):
        """Integration test for the ServicesAPI.start_kaltura_session method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

