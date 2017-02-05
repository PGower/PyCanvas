"""CourseAuditLog API Tests for Version 1.0.

This is a testing template for the generated CourseAuditLogAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.course_audit_log import CourseAuditLogAPI
from pycanvas.apis.course_audit_log import Createdeventdata
from pycanvas.apis.course_audit_log import Courseevent
from pycanvas.apis.course_audit_log import Courseeventlink
from pycanvas.apis.course_audit_log import Updatedeventdata


class TestCourseAuditLogAPI(unittest.TestCase):
    """Tests for the CourseAuditLogAPI."""

    def setUp(self):
        self.client = CourseAuditLogAPI(secrets.instance_address, secrets.access_token)

    def test_query_by_course(self):
        """Integration test for the CourseAuditLogAPI.query_by_course method."""
        course_id = None  # Change me!!

        r = self.client.query_by_course(course_id, end_time=None, start_time=None)

