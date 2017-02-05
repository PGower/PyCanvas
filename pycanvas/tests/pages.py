"""Pages API Tests for Version 1.0.

This is a testing template for the generated PagesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.pages import PagesAPI
from pycanvas.apis.pages import Pagerevision
from pycanvas.apis.pages import Page


class TestPagesAPI(unittest.TestCase):
    """Tests for the PagesAPI."""

    def setUp(self):
        self.client = PagesAPI(secrets.instance_address, secrets.access_token)

    def test_show_front_page_courses(self):
        """Integration test for the PagesAPI.show_front_page_courses method."""
        course_id = None  # Change me!!

        r = self.client.show_front_page_courses(course_id)

    def test_show_front_page_groups(self):
        """Integration test for the PagesAPI.show_front_page_groups method."""
        group_id = None  # Change me!!

        r = self.client.show_front_page_groups(group_id)

    def test_update_create_front_page_courses(self):
        """Integration test for the PagesAPI.update_create_front_page_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_create_front_page_groups(self):
        """Integration test for the PagesAPI.update_create_front_page_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_pages_courses(self):
        """Integration test for the PagesAPI.list_pages_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_pages_courses(course_id, order=None, published=None, search_term=None, sort=None)

    def test_list_pages_groups(self):
        """Integration test for the PagesAPI.list_pages_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_pages_groups(group_id, order=None, published=None, search_term=None, sort=None)

    def test_create_page_courses(self):
        """Integration test for the PagesAPI.create_page_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_page_groups(self):
        """Integration test for the PagesAPI.create_page_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_page_courses(self):
        """Integration test for the PagesAPI.show_page_courses method."""
        course_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.show_page_courses(url, course_id)

    def test_show_page_groups(self):
        """Integration test for the PagesAPI.show_page_groups method."""
        group_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.show_page_groups(url, group_id)

    def test_update_create_page_courses(self):
        """Integration test for the PagesAPI.update_create_page_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_create_page_groups(self):
        """Integration test for the PagesAPI.update_create_page_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_page_courses(self):
        """Integration test for the PagesAPI.delete_page_courses method."""
        course_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.delete_page_courses(url, course_id)

    def test_delete_page_groups(self):
        """Integration test for the PagesAPI.delete_page_groups method."""
        group_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.delete_page_groups(url, group_id)

    def test_list_revisions_courses(self):
        """Integration test for the PagesAPI.list_revisions_courses method."""
        course_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.list_revisions_courses(url, course_id)

    def test_list_revisions_groups(self):
        """Integration test for the PagesAPI.list_revisions_groups method."""
        group_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.list_revisions_groups(url, group_id)

    def test_show_revision_courses_latest(self):
        """Integration test for the PagesAPI.show_revision_courses_latest method."""
        course_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.show_revision_courses_latest(url, course_id, summary=None)

    def test_show_revision_groups_latest(self):
        """Integration test for the PagesAPI.show_revision_groups_latest method."""
        group_id = None  # Change me!!
        url = None  # Change me!!

        r = self.client.show_revision_groups_latest(url, group_id, summary=None)

    def test_show_revision_courses_revision_id(self):
        """Integration test for the PagesAPI.show_revision_courses_revision_id method."""
        course_id = None  # Change me!!
        url = None  # Change me!!
        revision_id = None  # Change me!!

        r = self.client.show_revision_courses_revision_id(url, course_id, revision_id, summary=None)

    def test_show_revision_groups_revision_id(self):
        """Integration test for the PagesAPI.show_revision_groups_revision_id method."""
        group_id = None  # Change me!!
        url = None  # Change me!!
        revision_id = None  # Change me!!

        r = self.client.show_revision_groups_revision_id(url, group_id, revision_id, summary=None)

    def test_revert_to_revision_courses(self):
        """Integration test for the PagesAPI.revert_to_revision_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_revert_to_revision_groups(self):
        """Integration test for the PagesAPI.revert_to_revision_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

