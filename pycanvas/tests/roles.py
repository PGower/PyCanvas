"""Roles API Tests for Version 1.0.

This is a testing template for the generated RolesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.roles import RolesAPI
from pycanvas.apis.roles import Rolepermissions
from pycanvas.apis.roles import Role


class TestRolesAPI(unittest.TestCase):
    """Tests for the RolesAPI."""

    def setUp(self):
        self.client = RolesAPI(secrets.instance_address, secrets.access_token)

    def test_list_roles(self):
        """Integration test for the RolesAPI.list_roles method."""
        account_id = None  # Change me!!

        r = self.client.list_roles(account_id, show_inherited=None, state=None)

    def test_get_single_role(self):
        """Integration test for the RolesAPI.get_single_role method."""
        id = None  # Change me!!
        account_id = None  # Change me!!
        role_id = None  # Change me!!

        r = self.client.get_single_role(id, role_id, account_id, role=None)

    def test_create_new_role(self):
        """Integration test for the RolesAPI.create_new_role method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_deactivate_role(self):
        """Integration test for the RolesAPI.deactivate_role method."""
        account_id = None  # Change me!!
        id = None  # Change me!!
        role_id = None  # Change me!!

        r = self.client.deactivate_role(id, role_id, account_id, role=None)

    def test_activate_role(self):
        """Integration test for the RolesAPI.activate_role method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_role(self):
        """Integration test for the RolesAPI.update_role method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

