"""QuizSubmissionQuestions API Tests for Version 1.0.

This is a testing template for the generated QuizSubmissionQuestionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_submission_questions import QuizSubmissionQuestionsAPI
from pycanvas.apis.quiz_submission_questions import Quizsubmissionquestion


class TestQuizSubmissionQuestionsAPI(unittest.TestCase):
    """Tests for the QuizSubmissionQuestionsAPI."""

    def setUp(self):
        self.client = QuizSubmissionQuestionsAPI(secrets.instance_address, secrets.access_token)

    def test_get_all_quiz_submission_questions(self):
        """Integration test for the QuizSubmissionQuestionsAPI.get_all_quiz_submission_questions method."""
        quiz_submission_id = None  # Change me!!

        r = self.client.get_all_quiz_submission_questions(quiz_submission_id, include=None)

    def test_get_single_quiz_submission_question(self):
        """Integration test for the QuizSubmissionQuestionsAPI.get_single_quiz_submission_question method."""
        quiz_submission_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_quiz_submission_question(id, quiz_submission_id, include=None)

    def test_answering_questions(self):
        """Integration test for the QuizSubmissionQuestionsAPI.answering_questions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_flagging_question(self):
        """Integration test for the QuizSubmissionQuestionsAPI.flagging_question method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_unflagging_question(self):
        """Integration test for the QuizSubmissionQuestionsAPI.unflagging_question method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

