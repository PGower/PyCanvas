"""GroupCategories API Tests for Version 1.0.

This is a testing template for the generated GroupCategoriesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.group_categories import GroupCategoriesAPI
from pycanvas.apis.group_categories import Groupcategory


class TestGroupCategoriesAPI(unittest.TestCase):
    """Tests for the GroupCategoriesAPI."""

    def setUp(self):
        self.client = GroupCategoriesAPI(secrets.instance_address, secrets.access_token)

    def test_list_group_categories_for_context_accounts(self):
        """Integration test for the GroupCategoriesAPI.list_group_categories_for_context_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_group_categories_for_context_accounts(account_id)

    def test_list_group_categories_for_context_courses(self):
        """Integration test for the GroupCategoriesAPI.list_group_categories_for_context_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_group_categories_for_context_courses(course_id)

    def test_get_single_group_category(self):
        """Integration test for the GroupCategoriesAPI.get_single_group_category method."""
        group_category_id = None  # Change me!!

        r = self.client.get_single_group_category(group_category_id)

    def test_create_group_category_accounts(self):
        """Integration test for the GroupCategoriesAPI.create_group_category_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_group_category_courses(self):
        """Integration test for the GroupCategoriesAPI.create_group_category_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_group_category(self):
        """Integration test for the GroupCategoriesAPI.update_group_category method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_group_category(self):
        """Integration test for the GroupCategoriesAPI.delete_group_category method."""
        group_category_id = None  # Change me!!

        r = self.client.delete_group_category(group_category_id)

    def test_list_groups_in_group_category(self):
        """Integration test for the GroupCategoriesAPI.list_groups_in_group_category method."""
        group_category_id = None  # Change me!!

        r = self.client.list_groups_in_group_category(group_category_id)

    def test_list_users_in_group_category(self):
        """Integration test for the GroupCategoriesAPI.list_users_in_group_category method."""
        group_category_id = None  # Change me!!

        r = self.client.list_users_in_group_category(group_category_id, search_term=None, unassigned=None)

    def test_assign_unassigned_members(self):
        """Integration test for the GroupCategoriesAPI.assign_unassigned_members method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

