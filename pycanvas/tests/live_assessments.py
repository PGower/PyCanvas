"""LiveAssessments API Tests for Version 1.0.

This is a testing template for the generated LiveAssessmentsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.live_assessments import LiveAssessmentsAPI
from pycanvas.apis.live_assessments import Assessment
from pycanvas.apis.live_assessments import Result
from pycanvas.apis.live_assessments import Resultlinks


class TestLiveAssessmentsAPI(unittest.TestCase):
    """Tests for the LiveAssessmentsAPI."""

    def setUp(self):
        self.client = LiveAssessmentsAPI(secrets.instance_address, secrets.access_token)

    def test_create_live_assessment_results(self):
        """Integration test for the LiveAssessmentsAPI.create_live_assessment_results method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_live_assessment_results(self):
        """Integration test for the LiveAssessmentsAPI.list_live_assessment_results method."""
        course_id = None  # Change me!!
        assessment_id = None  # Change me!!

        r = self.client.list_live_assessment_results(course_id, assessment_id, user_id=None)

    def test_create_or_find_live_assessment(self):
        """Integration test for the LiveAssessmentsAPI.create_or_find_live_assessment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_live_assessments(self):
        """Integration test for the LiveAssessmentsAPI.list_live_assessments method."""
        course_id = None  # Change me!!

        r = self.client.list_live_assessments(course_id)

