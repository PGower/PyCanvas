"""GradingStandards API Tests for Version 1.0.

This is a testing template for the generated GradingStandardsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.grading_standards import GradingStandardsAPI
from pycanvas.apis.grading_standards import Gradingstandard
from pycanvas.apis.grading_standards import Gradingschemeentry


class TestGradingStandardsAPI(unittest.TestCase):
    """Tests for the GradingStandardsAPI."""

    def setUp(self):
        self.client = GradingStandardsAPI(secrets.instance_address, secrets.access_token)

    def test_create_new_grading_standard_accounts(self):
        """Integration test for the GradingStandardsAPI.create_new_grading_standard_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_new_grading_standard_courses(self):
        """Integration test for the GradingStandardsAPI.create_new_grading_standard_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

