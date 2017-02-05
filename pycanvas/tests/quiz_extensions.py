"""QuizExtensions API Tests for Version 1.0.

This is a testing template for the generated QuizExtensionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_extensions import QuizExtensionsAPI
from pycanvas.apis.quiz_extensions import Quizextension


class TestQuizExtensionsAPI(unittest.TestCase):
    """Tests for the QuizExtensionsAPI."""

    def setUp(self):
        self.client = QuizExtensionsAPI(secrets.instance_address, secrets.access_token)

    def test_set_extensions_for_student_quiz_submissions(self):
        """Integration test for the QuizExtensionsAPI.set_extensions_for_student_quiz_submissions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

