"""GradingPeriods API Tests for Version 1.0.

This is a testing template for the generated GradingPeriodsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.grading_periods import GradingPeriodsAPI
from pycanvas.apis.grading_periods import Gradingperiod


class TestGradingPeriodsAPI(unittest.TestCase):
    """Tests for the GradingPeriodsAPI."""

    def setUp(self):
        self.client = GradingPeriodsAPI(secrets.instance_address, secrets.access_token)

    def test_list_grading_periods_courses(self):
        """Integration test for the GradingPeriodsAPI.list_grading_periods_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_grading_periods_courses(course_id)

    def test_list_grading_periods_accounts(self):
        """Integration test for the GradingPeriodsAPI.list_grading_periods_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_grading_periods_accounts(account_id)

    def test_get_single_grading_period_courses(self):
        """Integration test for the GradingPeriodsAPI.get_single_grading_period_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_grading_period_courses(id, course_id)

    def test_get_single_grading_period_accounts(self):
        """Integration test for the GradingPeriodsAPI.get_single_grading_period_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_grading_period_accounts(id, account_id)

    def test_create_single_grading_period_courses(self):
        """Integration test for the GradingPeriodsAPI.create_single_grading_period_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_single_grading_period_accounts(self):
        """Integration test for the GradingPeriodsAPI.create_single_grading_period_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_grading_period_courses(self):
        """Integration test for the GradingPeriodsAPI.update_single_grading_period_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_grading_period_accounts(self):
        """Integration test for the GradingPeriodsAPI.update_single_grading_period_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_grading_period_courses(self):
        """Integration test for the GradingPeriodsAPI.delete_grading_period_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_grading_period_courses(id, course_id)

    def test_delete_grading_period_accounts(self):
        """Integration test for the GradingPeriodsAPI.delete_grading_period_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_grading_period_accounts(id, account_id)

