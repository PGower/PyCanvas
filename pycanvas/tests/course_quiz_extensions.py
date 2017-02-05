"""CourseQuizExtensions API Tests for Version 1.0.

This is a testing template for the generated CourseQuizExtensionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.course_quiz_extensions import CourseQuizExtensionsAPI
from pycanvas.apis.course_quiz_extensions import Coursequizextension


class TestCourseQuizExtensionsAPI(unittest.TestCase):
    """Tests for the CourseQuizExtensionsAPI."""

    def setUp(self):
        self.client = CourseQuizExtensionsAPI(secrets.instance_address, secrets.access_token)

    def test_set_extensions_for_student_quiz_submissions(self):
        """Integration test for the CourseQuizExtensionsAPI.set_extensions_for_student_quiz_submissions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

