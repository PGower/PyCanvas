"""Conferences API Tests for Version 1.0.

This is a testing template for the generated ConferencesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.conferences import ConferencesAPI
from pycanvas.apis.conferences import Conference
from pycanvas.apis.conferences import Conferencerecording


class TestConferencesAPI(unittest.TestCase):
    """Tests for the ConferencesAPI."""

    def setUp(self):
        self.client = ConferencesAPI(secrets.instance_address, secrets.access_token)

    def test_list_conferences_courses(self):
        """Integration test for the ConferencesAPI.list_conferences_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_conferences_courses(course_id)

    def test_list_conferences_groups(self):
        """Integration test for the ConferencesAPI.list_conferences_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_conferences_groups(group_id)

