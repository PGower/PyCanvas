"""AccountDomainLookups API Tests for Version 1.0.

This is a testing template for the generated AccountDomainLookupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.account_domain_lookups import AccountDomainLookupsAPI


class TestAccountDomainLookupsAPI(unittest.TestCase):
    """Tests for the AccountDomainLookupsAPI."""

    def setUp(self):
        self.client = AccountDomainLookupsAPI(secrets.instance_address, secrets.access_token)

    def test_search_account_domains(self):
        """Integration test for the AccountDomainLookupsAPI.search_account_domains method."""

        r = self.client.search_account_domains(domain=None, latitude=None, longitude=None, name=None)

