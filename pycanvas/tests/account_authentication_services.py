"""AccountAuthenticationServices API Tests for Version 1.0.

This is a testing template for the generated AccountAuthenticationServicesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.account_authentication_services import AccountAuthenticationServicesAPI
from pycanvas.apis.account_authentication_services import Accountauthorizationconfig
from pycanvas.apis.account_authentication_services import Discoveryurl


class TestAccountAuthenticationServicesAPI(unittest.TestCase):
    """Tests for the AccountAuthenticationServicesAPI."""

    def setUp(self):
        self.client = AccountAuthenticationServicesAPI(secrets.instance_address, secrets.access_token)

    def test_list_authorization_configs(self):
        """Integration test for the AccountAuthenticationServicesAPI.list_authorization_configs method."""
        account_id = None  # Change me!!

        r = self.client.list_authorization_configs(account_id)

    def test_create_authorization_config(self):
        """Integration test for the AccountAuthenticationServicesAPI.create_authorization_config method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_authorization_config(self):
        """Integration test for the AccountAuthenticationServicesAPI.update_authorization_config method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_authorization_config(self):
        """Integration test for the AccountAuthenticationServicesAPI.get_authorization_config method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_authorization_config(id, account_id)

    def test_delete_authorization_config(self):
        """Integration test for the AccountAuthenticationServicesAPI.delete_authorization_config method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_authorization_config(id, account_id)

    def test_get_discovery_url(self):
        """Integration test for the AccountAuthenticationServicesAPI.get_discovery_url method."""
        account_id = None  # Change me!!

        r = self.client.get_discovery_url(account_id)

    def test_set_discovery_url(self):
        """Integration test for the AccountAuthenticationServicesAPI.set_discovery_url method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_discovery_url(self):
        """Integration test for the AccountAuthenticationServicesAPI.delete_discovery_url method."""
        account_id = None  # Change me!!

        r = self.client.delete_discovery_url(account_id)

