"""AccountReports API Tests for Version 1.0.

This is a testing template for the generated AccountReportsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.account_reports import AccountReportsAPI
from pycanvas.apis.account_reports import Report
from pycanvas.apis.account_reports import Reportparameters


class TestAccountReportsAPI(unittest.TestCase):
    """Tests for the AccountReportsAPI."""

    def setUp(self):
        self.client = AccountReportsAPI(secrets.instance_address, secrets.access_token)

    def test_list_available_reports(self):
        """Integration test for the AccountReportsAPI.list_available_reports method."""
        account_id = None  # Change me!!

        r = self.client.list_available_reports(account_id)

    def test_start_report(self):
        """Integration test for the AccountReportsAPI.start_report method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_index_of_reports(self):
        """Integration test for the AccountReportsAPI.index_of_reports method."""
        account_id = None  # Change me!!
        report = None  # Change me!!

        r = self.client.index_of_reports(report, account_id)

    def test_status_of_report(self):
        """Integration test for the AccountReportsAPI.status_of_report method."""
        account_id = None  # Change me!!
        report = None  # Change me!!
        id = None  # Change me!!

        r = self.client.status_of_report(id, report, account_id)

    def test_delete_report(self):
        """Integration test for the AccountReportsAPI.delete_report method."""
        account_id = None  # Change me!!
        report = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_report(id, report, account_id)

