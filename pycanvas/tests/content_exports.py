"""ContentExports API Tests for Version 1.0.

This is a testing template for the generated ContentExportsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.content_exports import ContentExportsAPI
from pycanvas.apis.content_exports import Contentexport


class TestContentExportsAPI(unittest.TestCase):
    """Tests for the ContentExportsAPI."""

    def setUp(self):
        self.client = ContentExportsAPI(secrets.instance_address, secrets.access_token)

    def test_list_content_exports_courses(self):
        """Integration test for the ContentExportsAPI.list_content_exports_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_content_exports_courses(course_id)

    def test_list_content_exports_groups(self):
        """Integration test for the ContentExportsAPI.list_content_exports_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_content_exports_groups(group_id)

    def test_list_content_exports_users(self):
        """Integration test for the ContentExportsAPI.list_content_exports_users method."""
        user_id = None  # Change me!!

        r = self.client.list_content_exports_users(user_id)

    def test_show_content_export_courses(self):
        """Integration test for the ContentExportsAPI.show_content_export_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_content_export_courses(id, course_id)

    def test_show_content_export_groups(self):
        """Integration test for the ContentExportsAPI.show_content_export_groups method."""
        group_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_content_export_groups(id, group_id)

    def test_show_content_export_users(self):
        """Integration test for the ContentExportsAPI.show_content_export_users method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_content_export_users(id, user_id)

    def test_export_content_courses(self):
        """Integration test for the ContentExportsAPI.export_content_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_export_content_groups(self):
        """Integration test for the ContentExportsAPI.export_content_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_export_content_users(self):
        """Integration test for the ContentExportsAPI.export_content_users method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

