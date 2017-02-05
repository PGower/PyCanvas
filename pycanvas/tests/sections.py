"""Sections API Tests for Version 1.0.

This is a testing template for the generated SectionsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.sections import SectionsAPI
from pycanvas.apis.sections import Section


class TestSectionsAPI(unittest.TestCase):
    """Tests for the SectionsAPI."""

    def setUp(self):
        self.client = SectionsAPI(secrets.instance_address, secrets.access_token)

    def test_list_course_sections(self):
        """Integration test for the SectionsAPI.list_course_sections method."""
        course_id = None  # Change me!!

        r = self.client.list_course_sections(course_id, include=None)

    def test_create_course_section(self):
        """Integration test for the SectionsAPI.create_course_section method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_cross_list_section(self):
        """Integration test for the SectionsAPI.cross_list_section method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_de_cross_list_section(self):
        """Integration test for the SectionsAPI.de_cross_list_section method."""
        id = None  # Change me!!

        r = self.client.de_cross_list_section(id)

    def test_edit_section(self):
        """Integration test for the SectionsAPI.edit_section method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_section_information_courses(self):
        """Integration test for the SectionsAPI.get_section_information_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_section_information_courses(id, course_id)

    def test_get_section_information_sections(self):
        """Integration test for the SectionsAPI.get_section_information_sections method."""
        id = None  # Change me!!

        r = self.client.get_section_information_sections(id)

    def test_delete_section(self):
        """Integration test for the SectionsAPI.delete_section method."""
        id = None  # Change me!!

        r = self.client.delete_section(id)

