"""AnnouncementExternalFeeds API Tests for Version 1.0.

This is a testing template for the generated AnnouncementExternalFeedsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.announcement_external_feeds import AnnouncementExternalFeedsAPI
from pycanvas.apis.announcement_external_feeds import Externalfeed


class TestAnnouncementExternalFeedsAPI(unittest.TestCase):
    """Tests for the AnnouncementExternalFeedsAPI."""

    def setUp(self):
        self.client = AnnouncementExternalFeedsAPI(secrets.instance_address, secrets.access_token)

    def test_list_external_feeds_courses(self):
        """Integration test for the AnnouncementExternalFeedsAPI.list_external_feeds_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_external_feeds_courses(course_id)

    def test_list_external_feeds_groups(self):
        """Integration test for the AnnouncementExternalFeedsAPI.list_external_feeds_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_external_feeds_groups(group_id)

    def test_create_external_feed_courses(self):
        """Integration test for the AnnouncementExternalFeedsAPI.create_external_feed_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_external_feed_groups(self):
        """Integration test for the AnnouncementExternalFeedsAPI.create_external_feed_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_external_feed_courses(self):
        """Integration test for the AnnouncementExternalFeedsAPI.delete_external_feed_courses method."""
        course_id = None  # Change me!!
        external_feed_id = None  # Change me!!

        r = self.client.delete_external_feed_courses(course_id, external_feed_id)

    def test_delete_external_feed_groups(self):
        """Integration test for the AnnouncementExternalFeedsAPI.delete_external_feed_groups method."""
        group_id = None  # Change me!!
        external_feed_id = None  # Change me!!

        r = self.client.delete_external_feed_groups(group_id, external_feed_id)

