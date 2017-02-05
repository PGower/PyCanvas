"""Users API Tests for Version 1.0.

This is a testing template for the generated UsersAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.users import UsersAPI
from pycanvas.apis.users import Profile
from pycanvas.apis.users import Coursenickname
from pycanvas.apis.users import Pageview
from pycanvas.apis.users import Pageviewlinks
from pycanvas.apis.users import User
from pycanvas.apis.users import Userdisplay
from pycanvas.apis.users import Avatar


class TestUsersAPI(unittest.TestCase):
    """Tests for the UsersAPI."""

    def setUp(self):
        self.client = UsersAPI(secrets.instance_address, secrets.access_token)

    def test_list_users_in_account(self):
        """Integration test for the UsersAPI.list_users_in_account method."""
        account_id = None  # Change me!!

        r = self.client.list_users_in_account(account_id, search_term=None)

    def test_list_activity_stream_self(self):
        """Integration test for the UsersAPI.list_activity_stream_self method."""

        r = self.client.list_activity_stream_self()

    def test_list_activity_stream_activity_stream(self):
        """Integration test for the UsersAPI.list_activity_stream_activity_stream method."""

        r = self.client.list_activity_stream_activity_stream()

    def test_activity_stream_summary(self):
        """Integration test for the UsersAPI.activity_stream_summary method."""

        r = self.client.activity_stream_summary()

    def test_list_todo_items(self):
        """Integration test for the UsersAPI.list_todo_items method."""

        r = self.client.list_todo_items(include=None)

    def test_list_upcoming_assignments_calendar_events(self):
        """Integration test for the UsersAPI.list_upcoming_assignments_calendar_events method."""

        r = self.client.list_upcoming_assignments_calendar_events()

    def test_list_missing_submissions(self):
        """Integration test for the UsersAPI.list_missing_submissions method."""
        user_id = None  # Change me!!

        r = self.client.list_missing_submissions(user_id)

    def test_hide_stream_item(self):
        """Integration test for the UsersAPI.hide_stream_item method."""
        id = None  # Change me!!

        r = self.client.hide_stream_item(id)

    def test_hide_all_stream_items(self):
        """Integration test for the UsersAPI.hide_all_stream_items method."""

        r = self.client.hide_all_stream_items()

    def test_upload_file(self):
        """Integration test for the UsersAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_user_details(self):
        """Integration test for the UsersAPI.show_user_details method."""
        id = None  # Change me!!

        r = self.client.show_user_details(id)

    def test_create_user(self):
        """Integration test for the UsersAPI.create_user method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_self_register_user(self):
        """Integration test for the UsersAPI.self_register_user method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_user_settings(self):
        """Integration test for the UsersAPI.update_user_settings method."""
        id = None  # Change me!!

        r = self.client.update_user_settings(id, collapse_global_nav=None, manual_mark_as_read=None)

    def test_get_custom_colors(self):
        """Integration test for the UsersAPI.get_custom_colors method."""
        id = None  # Change me!!

        r = self.client.get_custom_colors(id)

    def test_get_custom_color(self):
        """Integration test for the UsersAPI.get_custom_color method."""
        id = None  # Change me!!
        asset_string = None  # Change me!!

        r = self.client.get_custom_color(id, asset_string)

    def test_update_custom_color(self):
        """Integration test for the UsersAPI.update_custom_color method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_dashboard_postions(self):
        """Integration test for the UsersAPI.get_dashboard_postions method."""
        id = None  # Change me!!

        r = self.client.get_dashboard_postions(id)

    def test_update_dashboard_positions(self):
        """Integration test for the UsersAPI.update_dashboard_positions method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_user(self):
        """Integration test for the UsersAPI.edit_user method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_merge_user_into_another_user_destination_user_id(self):
        """Integration test for the UsersAPI.merge_user_into_another_user_destination_user_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_merge_user_into_another_user_accounts(self):
        """Integration test for the UsersAPI.merge_user_into_another_user_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_split_merged_users_into_separate_users(self):
        """Integration test for the UsersAPI.split_merged_users_into_separate_users method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_user_profile(self):
        """Integration test for the UsersAPI.get_user_profile method."""
        user_id = None  # Change me!!

        r = self.client.get_user_profile(user_id)

    def test_list_avatar_options(self):
        """Integration test for the UsersAPI.list_avatar_options method."""
        user_id = None  # Change me!!

        r = self.client.list_avatar_options(user_id)

    def test_list_user_page_views(self):
        """Integration test for the UsersAPI.list_user_page_views method."""
        user_id = None  # Change me!!

        r = self.client.list_user_page_views(user_id, end_time=None, start_time=None)

    def test_store_custom_data(self):
        """Integration test for the UsersAPI.store_custom_data method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_load_custom_data(self):
        """Integration test for the UsersAPI.load_custom_data method."""
        user_id = None  # Change me!!
        ns = None  # Change me!!

        r = self.client.load_custom_data(ns, user_id)

    def test_delete_custom_data(self):
        """Integration test for the UsersAPI.delete_custom_data method."""
        user_id = None  # Change me!!
        ns = None  # Change me!!

        r = self.client.delete_custom_data(ns, user_id)

    def test_list_course_nicknames(self):
        """Integration test for the UsersAPI.list_course_nicknames method."""

        r = self.client.list_course_nicknames()

    def test_get_course_nickname(self):
        """Integration test for the UsersAPI.get_course_nickname method."""
        course_id = None  # Change me!!

        r = self.client.get_course_nickname(course_id)

    def test_set_course_nickname(self):
        """Integration test for the UsersAPI.set_course_nickname method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_course_nickname(self):
        """Integration test for the UsersAPI.remove_course_nickname method."""
        course_id = None  # Change me!!

        r = self.client.remove_course_nickname(course_id)

    def test_clear_course_nicknames(self):
        """Integration test for the UsersAPI.clear_course_nicknames method."""

        r = self.client.clear_course_nicknames()

