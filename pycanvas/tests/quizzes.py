"""Quizzes API Tests for Version 1.0.

This is a testing template for the generated QuizzesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.quizzes import QuizzesAPI
from pycanvas.apis.quizzes import Quizpermissions
from pycanvas.apis.quizzes import Quiz


class TestQuizzesAPI(unittest.TestCase):
    """Tests for the QuizzesAPI."""

    def setUp(self):
        self.client = QuizzesAPI(secrets.instance_address, secrets.access_token)

    def test_list_quizzes_in_course(self):
        """Integration test for the QuizzesAPI.list_quizzes_in_course method."""
        course_id = None  # Change me!!

        r = self.client.list_quizzes_in_course(course_id, search_term=None)

    def test_get_single_quiz(self):
        """Integration test for the QuizzesAPI.get_single_quiz method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_quiz(id, course_id)

    def test_create_quiz(self):
        """Integration test for the QuizzesAPI.create_quiz method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_quiz(self):
        """Integration test for the QuizzesAPI.edit_quiz method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_quiz(self):
        """Integration test for the QuizzesAPI.delete_quiz method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_quiz(id, course_id)

    def test_reorder_quiz_items(self):
        """Integration test for the QuizzesAPI.reorder_quiz_items method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

