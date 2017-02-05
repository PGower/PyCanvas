"""Enrollments API Tests for Version 1.0.

This is a testing template for the generated EnrollmentsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.enrollments import EnrollmentsAPI
from pycanvas.apis.enrollments import Grade
from pycanvas.apis.enrollments import Enrollment


class TestEnrollmentsAPI(unittest.TestCase):
    """Tests for the EnrollmentsAPI."""

    def setUp(self):
        self.client = EnrollmentsAPI(secrets.instance_address, secrets.access_token)

    def test_list_enrollments_courses(self):
        """Integration test for the EnrollmentsAPI.list_enrollments_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_enrollments_courses(course_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None, user_id=None)

    def test_list_enrollments_sections(self):
        """Integration test for the EnrollmentsAPI.list_enrollments_sections method."""
        section_id = None  # Change me!!

        r = self.client.list_enrollments_sections(section_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None, user_id=None)

    def test_list_enrollments_users(self):
        """Integration test for the EnrollmentsAPI.list_enrollments_users method."""
        user_id = None  # Change me!!

        r = self.client.list_enrollments_users(user_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None)

    def test_enrollment_by_id(self):
        """Integration test for the EnrollmentsAPI.enrollment_by_id method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.enrollment_by_id(id, account_id)

    def test_enroll_user_courses(self):
        """Integration test for the EnrollmentsAPI.enroll_user_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_enroll_user_sections(self):
        """Integration test for the EnrollmentsAPI.enroll_user_sections method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_conclude_deactivate_or_delete_enrollment(self):
        """Integration test for the EnrollmentsAPI.conclude_deactivate_or_delete_enrollment method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.conclude_deactivate_or_delete_enrollment(id, course_id, task=None)

    def test_re_activate_enrollment(self):
        """Integration test for the EnrollmentsAPI.re_activate_enrollment method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

