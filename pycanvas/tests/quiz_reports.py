"""QuizReports API Tests for Version 1.0.

This is a testing template for the generated QuizReportsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_reports import QuizReportsAPI
from pycanvas.apis.quiz_reports import Quizreport


class TestQuizReportsAPI(unittest.TestCase):
    """Tests for the QuizReportsAPI."""

    def setUp(self):
        self.client = QuizReportsAPI(secrets.instance_address, secrets.access_token)

    def test_retrieve_all_quiz_reports(self):
        """Integration test for the QuizReportsAPI.retrieve_all_quiz_reports method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.retrieve_all_quiz_reports(quiz_id, course_id, includes_all_versions=None)

    def test_create_quiz_report(self):
        """Integration test for the QuizReportsAPI.create_quiz_report method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_quiz_report(self):
        """Integration test for the QuizReportsAPI.get_quiz_report method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_quiz_report(id, quiz_id, course_id, include=None)

    def test_abort_generation_of_report_or_remove_previously_generated_one(self):
        """Integration test for the QuizReportsAPI.abort_generation_of_report_or_remove_previously_generated_one method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.abort_generation_of_report_or_remove_previously_generated_one(id, quiz_id, course_id)

