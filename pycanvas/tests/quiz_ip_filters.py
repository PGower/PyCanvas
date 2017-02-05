"""QuizIpFilters API Tests for Version 1.0.

This is a testing template for the generated QuizIpFiltersAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_ip_filters import QuizIpFiltersAPI
from pycanvas.apis.quiz_ip_filters import Quizipfilter


class TestQuizIpFiltersAPI(unittest.TestCase):
    """Tests for the QuizIpFiltersAPI."""

    def setUp(self):
        self.client = QuizIpFiltersAPI(secrets.instance_address, secrets.access_token)

    def test_get_available_quiz_ip_filters(self):
        """Integration test for the QuizIpFiltersAPI.get_available_quiz_ip_filters method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.get_available_quiz_ip_filters(quiz_id, course_id)

