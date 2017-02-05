"""QuizStatistics API Tests for Version 1.0.

This is a testing template for the generated QuizStatisticsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_statistics import QuizStatisticsAPI
from pycanvas.apis.quiz_statistics import Quizstatisticsquestionstatistics
from pycanvas.apis.quiz_statistics import Quizstatistics
from pycanvas.apis.quiz_statistics import Quizstatisticsanswerpointbiserial
from pycanvas.apis.quiz_statistics import Quizstatisticsanswerstatistics
from pycanvas.apis.quiz_statistics import Quizstatisticslinks
from pycanvas.apis.quiz_statistics import Quizstatisticssubmissionstatistics


class TestQuizStatisticsAPI(unittest.TestCase):
    """Tests for the QuizStatisticsAPI."""

    def setUp(self):
        self.client = QuizStatisticsAPI(secrets.instance_address, secrets.access_token)

    def test_fetching_latest_quiz_statistics(self):
        """Integration test for the QuizStatisticsAPI.fetching_latest_quiz_statistics method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.fetching_latest_quiz_statistics(quiz_id, course_id, all_versions=None)

