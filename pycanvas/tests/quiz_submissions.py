"""QuizSubmissions API Tests for Version 1.0.

This is a testing template for the generated QuizSubmissionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_submissions import QuizSubmissionsAPI
from pycanvas.apis.quiz_submissions import Quizsubmission


class TestQuizSubmissionsAPI(unittest.TestCase):
    """Tests for the QuizSubmissionsAPI."""

    def setUp(self):
        self.client = QuizSubmissionsAPI(secrets.instance_address, secrets.access_token)

    def test_get_all_quiz_submissions(self):
        """Integration test for the QuizSubmissionsAPI.get_all_quiz_submissions method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.get_all_quiz_submissions(quiz_id, course_id, include=None)

    def test_get_quiz_submission(self):
        """Integration test for the QuizSubmissionsAPI.get_quiz_submission method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.get_quiz_submission(quiz_id, course_id, include=None)

    def test_get_single_quiz_submission(self):
        """Integration test for the QuizSubmissionsAPI.get_single_quiz_submission method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_quiz_submission(id, quiz_id, course_id, include=None)

    def test_create_quiz_submission_start_quiz_taking_session(self):
        """Integration test for the QuizSubmissionsAPI.create_quiz_submission_start_quiz_taking_session method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_student_question_scores_and_comments(self):
        """Integration test for the QuizSubmissionsAPI.update_student_question_scores_and_comments method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_complete_quiz_submission_turn_it_in(self):
        """Integration test for the QuizSubmissionsAPI.complete_quiz_submission_turn_it_in method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_current_quiz_submission_times(self):
        """Integration test for the QuizSubmissionsAPI.get_current_quiz_submission_times method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_current_quiz_submission_times(id, quiz_id, course_id)

