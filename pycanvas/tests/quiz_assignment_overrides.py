"""QuizAssignmentOverrides API Tests for Version 1.0.

This is a testing template for the generated QuizAssignmentOverridesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_assignment_overrides import QuizAssignmentOverridesAPI
from pycanvas.apis.quiz_assignment_overrides import Quizassignmentoverride
from pycanvas.apis.quiz_assignment_overrides import Quizassignmentoverridesetcontainer
from pycanvas.apis.quiz_assignment_overrides import Quizassignmentoverrideset


class TestQuizAssignmentOverridesAPI(unittest.TestCase):
    """Tests for the QuizAssignmentOverridesAPI."""

    def setUp(self):
        self.client = QuizAssignmentOverridesAPI(secrets.instance_address, secrets.access_token)

    def test_retrieve_assignment_overridden_dates_for_quizzes(self):
        """Integration test for the QuizAssignmentOverridesAPI.retrieve_assignment_overridden_dates_for_quizzes method."""
        course_id = None  # Change me!!

        r = self.client.retrieve_assignment_overridden_dates_for_quizzes(course_id, quiz_assignment_overrides_0_quiz_ids=None)

