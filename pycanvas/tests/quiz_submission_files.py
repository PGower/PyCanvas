"""QuizSubmissionFiles API Tests for Version 1.0.

This is a testing template for the generated QuizSubmissionFilesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_submission_files import QuizSubmissionFilesAPI


class TestQuizSubmissionFilesAPI(unittest.TestCase):
    """Tests for the QuizSubmissionFilesAPI."""

    def setUp(self):
        self.client = QuizSubmissionFilesAPI(secrets.instance_address, secrets.access_token)

    def test_upload_file(self):
        """Integration test for the QuizSubmissionFilesAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

