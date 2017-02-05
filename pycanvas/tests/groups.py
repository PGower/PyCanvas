"""Groups API Tests for Version 1.0.

This is a testing template for the generated GroupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.groups import GroupsAPI
from pycanvas.apis.groups import Group
from pycanvas.apis.groups import Groupmembership


class TestGroupsAPI(unittest.TestCase):
    """Tests for the GroupsAPI."""

    def setUp(self):
        self.client = GroupsAPI(secrets.instance_address, secrets.access_token)

    def test_list_your_groups(self):
        """Integration test for the GroupsAPI.list_your_groups method."""

        r = self.client.list_your_groups(context_type=None)

    def test_list_groups_available_in_context_accounts(self):
        """Integration test for the GroupsAPI.list_groups_available_in_context_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_groups_available_in_context_accounts(account_id, only_own_groups=None)

    def test_list_groups_available_in_context_courses(self):
        """Integration test for the GroupsAPI.list_groups_available_in_context_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_groups_available_in_context_courses(course_id, only_own_groups=None)

    def test_get_single_group(self):
        """Integration test for the GroupsAPI.get_single_group method."""
        group_id = None  # Change me!!

        r = self.client.get_single_group(group_id, include=None)

    def test_create_group_groups(self):
        """Integration test for the GroupsAPI.create_group_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_group_group_categories(self):
        """Integration test for the GroupsAPI.create_group_group_categories method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_group(self):
        """Integration test for the GroupsAPI.edit_group method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_group(self):
        """Integration test for the GroupsAPI.delete_group method."""
        group_id = None  # Change me!!

        r = self.client.delete_group(group_id)

    def test_invite_others_to_group(self):
        """Integration test for the GroupsAPI.invite_others_to_group method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_group_s_users(self):
        """Integration test for the GroupsAPI.list_group_s_users method."""
        group_id = None  # Change me!!

        r = self.client.list_group_s_users(group_id, include=None, search_term=None)

    def test_upload_file(self):
        """Integration test for the GroupsAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_preview_processed_html(self):
        """Integration test for the GroupsAPI.preview_processed_html method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_group_activity_stream(self):
        """Integration test for the GroupsAPI.group_activity_stream method."""
        group_id = None  # Change me!!

        r = self.client.group_activity_stream(group_id)

    def test_group_activity_stream_summary(self):
        """Integration test for the GroupsAPI.group_activity_stream_summary method."""
        group_id = None  # Change me!!

        r = self.client.group_activity_stream_summary(group_id)

    def test_list_group_memberships(self):
        """Integration test for the GroupsAPI.list_group_memberships method."""
        group_id = None  # Change me!!

        r = self.client.list_group_memberships(group_id, filter_states=None)

    def test_create_membership(self):
        """Integration test for the GroupsAPI.create_membership method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_membership_memberships(self):
        """Integration test for the GroupsAPI.update_membership_memberships method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_membership_users(self):
        """Integration test for the GroupsAPI.update_membership_users method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_leave_group_memberships(self):
        """Integration test for the GroupsAPI.leave_group_memberships method."""
        group_id = None  # Change me!!
        membership_id = None  # Change me!!

        r = self.client.leave_group_memberships(group_id, membership_id)

    def test_leave_group_users(self):
        """Integration test for the GroupsAPI.leave_group_users method."""
        group_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.leave_group_users(user_id, group_id)

