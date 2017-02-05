"""GradeChangeLog API Tests for Version 1.0.

This is a testing template for the generated GradeChangeLogAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.grade_change_log import GradeChangeLogAPI
from pycanvas.apis.grade_change_log import Gradechangeevent
from pycanvas.apis.grade_change_log import Gradechangeeventlinks


class TestGradeChangeLogAPI(unittest.TestCase):
    """Tests for the GradeChangeLogAPI."""

    def setUp(self):
        self.client = GradeChangeLogAPI(secrets.instance_address, secrets.access_token)

    def test_query_by_assignment(self):
        """Integration test for the GradeChangeLogAPI.query_by_assignment method."""
        assignment_id = None  # Change me!!

        r = self.client.query_by_assignment(assignment_id, end_time=None, start_time=None)

    def test_query_by_course(self):
        """Integration test for the GradeChangeLogAPI.query_by_course method."""
        course_id = None  # Change me!!

        r = self.client.query_by_course(course_id, end_time=None, start_time=None)

    def test_query_by_student(self):
        """Integration test for the GradeChangeLogAPI.query_by_student method."""
        student_id = None  # Change me!!

        r = self.client.query_by_student(student_id, end_time=None, start_time=None)

    def test_query_by_grader(self):
        """Integration test for the GradeChangeLogAPI.query_by_grader method."""
        grader_id = None  # Change me!!

        r = self.client.query_by_grader(grader_id, end_time=None, start_time=None)

