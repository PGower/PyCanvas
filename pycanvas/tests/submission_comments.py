"""SubmissionComments API Tests for Version 1.0.

This is a testing template for the generated SubmissionCommentsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.submission_comments import SubmissionCommentsAPI


class TestSubmissionCommentsAPI(unittest.TestCase):
    """Tests for the SubmissionCommentsAPI."""

    def setUp(self):
        self.client = SubmissionCommentsAPI(secrets.instance_address, secrets.access_token)

    def test_upload_file(self):
        """Integration test for the SubmissionCommentsAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

