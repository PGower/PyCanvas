"""Courses API Tests for Version 1.0.

This is a testing template for the generated CoursesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.courses import CoursesAPI
from pycanvas.apis.courses import Course
from pycanvas.apis.courses import Term
from pycanvas.apis.courses import Courseprogress
from pycanvas.apis.courses import Calendarlink


class TestCoursesAPI(unittest.TestCase):
    """Tests for the CoursesAPI."""

    def setUp(self):
        self.client = CoursesAPI(secrets.instance_address, secrets.access_token)

    def test_list_your_courses(self):
        """Integration test for the CoursesAPI.list_your_courses method."""

        r = self.client.list_your_courses(enrollment_role=None, enrollment_role_id=None, enrollment_type=None, include=None, state=None)

    def test_create_new_course(self):
        """Integration test for the CoursesAPI.create_new_course method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_upload_file(self):
        """Integration test for the CoursesAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_students(self):
        """Integration test for the CoursesAPI.list_students method."""
        course_id = None  # Change me!!

        r = self.client.list_students(course_id)

    def test_list_users_in_course_users(self):
        """Integration test for the CoursesAPI.list_users_in_course_users method."""
        course_id = None  # Change me!!

        r = self.client.list_users_in_course_users(course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, user_id=None)

    def test_list_users_in_course_search_users(self):
        """Integration test for the CoursesAPI.list_users_in_course_search_users method."""
        course_id = None  # Change me!!

        r = self.client.list_users_in_course_search_users(course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, user_id=None)

    def test_list_recently_logged_in_students(self):
        """Integration test for the CoursesAPI.list_recently_logged_in_students method."""
        course_id = None  # Change me!!

        r = self.client.list_recently_logged_in_students(course_id)

    def test_get_single_user(self):
        """Integration test for the CoursesAPI.get_single_user method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_user(id, course_id)

    def test_preview_processed_html(self):
        """Integration test for the CoursesAPI.preview_processed_html method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_course_activity_stream(self):
        """Integration test for the CoursesAPI.course_activity_stream method."""
        course_id = None  # Change me!!

        r = self.client.course_activity_stream(course_id)

    def test_course_activity_stream_summary(self):
        """Integration test for the CoursesAPI.course_activity_stream_summary method."""
        course_id = None  # Change me!!

        r = self.client.course_activity_stream_summary(course_id)

    def test_course_todo_items(self):
        """Integration test for the CoursesAPI.course_todo_items method."""
        course_id = None  # Change me!!

        r = self.client.course_todo_items(course_id)

    def test_conclude_course(self):
        """Integration test for the CoursesAPI.conclude_course method."""
        id = None  # Change me!!
        event = None  # Change me!!

        r = self.client.conclude_course(id, event)

    def test_get_course_settings(self):
        """Integration test for the CoursesAPI.get_course_settings method."""
        course_id = None  # Change me!!

        r = self.client.get_course_settings(course_id)

    def test_update_course_settings(self):
        """Integration test for the CoursesAPI.update_course_settings method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_single_course_courses(self):
        """Integration test for the CoursesAPI.get_single_course_courses method."""
        id = None  # Change me!!

        r = self.client.get_single_course_courses(id, include=None)

    def test_get_single_course_accounts(self):
        """Integration test for the CoursesAPI.get_single_course_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_course_accounts(id, account_id, include=None)

    def test_update_course(self):
        """Integration test for the CoursesAPI.update_course method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_courses(self):
        """Integration test for the CoursesAPI.update_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_reset_course(self):
        """Integration test for the CoursesAPI.reset_course method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_course_copy_status(self):
        """Integration test for the CoursesAPI.get_course_copy_status method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_course_copy_status(id, course_id)

    def test_copy_course_content(self):
        """Integration test for the CoursesAPI.copy_course_content method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

