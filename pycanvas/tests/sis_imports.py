"""SisImports API Tests for Version 1.0.

This is a testing template for the generated SisImportsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.sis_imports import SisImportsAPI
from pycanvas.apis.sis_imports import Sisimport
from pycanvas.apis.sis_imports import Sisimportcounts
from pycanvas.apis.sis_imports import Sisimportdata


class TestSisImportsAPI(unittest.TestCase):
    """Tests for the SisImportsAPI."""

    def setUp(self):
        self.client = SisImportsAPI(secrets.instance_address, secrets.access_token)

    def test_get_sis_import_list(self):
        """Integration test for the SisImportsAPI.get_sis_import_list method."""
        account_id = None  # Change me!!

        r = self.client.get_sis_import_list(account_id, created_since=None)

    def test_import_sis_data(self):
        """Integration test for the SisImportsAPI.import_sis_data method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_sis_import_status(self):
        """Integration test for the SisImportsAPI.get_sis_import_status method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_sis_import_status(id, account_id)

