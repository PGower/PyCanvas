"""QuizQuestionGroups API Tests for Version 1.0.

This is a testing template for the generated QuizQuestionGroupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quiz_question_groups import QuizQuestionGroupsAPI
from pycanvas.apis.quiz_question_groups import Quizgroup


class TestQuizQuestionGroupsAPI(unittest.TestCase):
    """Tests for the QuizQuestionGroupsAPI."""

    def setUp(self):
        self.client = QuizQuestionGroupsAPI(secrets.instance_address, secrets.access_token)

    def test_create_question_group(self):
        """Integration test for the QuizQuestionGroupsAPI.create_question_group method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_question_group(self):
        """Integration test for the QuizQuestionGroupsAPI.update_question_group method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_question_group(self):
        """Integration test for the QuizQuestionGroupsAPI.delete_question_group method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_question_group(id, quiz_id, course_id)

    def test_reorder_question_groups(self):
        """Integration test for the QuizQuestionGroupsAPI.reorder_question_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

