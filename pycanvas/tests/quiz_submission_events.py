"""QuizSubmissionEvents API Tests for Version 1.0.

This is a testing template for the generated QuizSubmissionEventsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_submission_events import QuizSubmissionEventsAPI
from pycanvas.apis.quiz_submission_events import Quizsubmissionevent


class TestQuizSubmissionEventsAPI(unittest.TestCase):
    """Tests for the QuizSubmissionEventsAPI."""

    def setUp(self):
        self.client = QuizSubmissionEventsAPI(secrets.instance_address, secrets.access_token)

    def test_submit_captured_events(self):
        """Integration test for the QuizSubmissionEventsAPI.submit_captured_events method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_retrieve_captured_events(self):
        """Integration test for the QuizSubmissionEventsAPI.retrieve_captured_events method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.retrieve_captured_events(id, quiz_id, course_id, attempt=None)

