"""OutcomeGroups API Tests for Version 1.0.

This is a testing template for the generated OutcomeGroupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.outcome_groups import OutcomeGroupsAPI
from pycanvas.apis.outcome_groups import Outcomegroup
from pycanvas.apis.outcome_groups import Outcomelink


class TestOutcomeGroupsAPI(unittest.TestCase):
    """Tests for the OutcomeGroupsAPI."""

    def setUp(self):
        self.client = OutcomeGroupsAPI(secrets.instance_address, secrets.access_token)

    def test_redirect_to_root_outcome_group_for_context_global(self):
        """Integration test for the OutcomeGroupsAPI.redirect_to_root_outcome_group_for_context_global method."""

        r = self.client.redirect_to_root_outcome_group_for_context_global()

    def test_redirect_to_root_outcome_group_for_context_accounts(self):
        """Integration test for the OutcomeGroupsAPI.redirect_to_root_outcome_group_for_context_accounts method."""
        account_id = None  # Change me!!

        r = self.client.redirect_to_root_outcome_group_for_context_accounts(account_id)

    def test_redirect_to_root_outcome_group_for_context_courses(self):
        """Integration test for the OutcomeGroupsAPI.redirect_to_root_outcome_group_for_context_courses method."""
        course_id = None  # Change me!!

        r = self.client.redirect_to_root_outcome_group_for_context_courses(course_id)

    def test_get_all_outcome_groups_for_context_accounts(self):
        """Integration test for the OutcomeGroupsAPI.get_all_outcome_groups_for_context_accounts method."""
        account_id = None  # Change me!!

        r = self.client.get_all_outcome_groups_for_context_accounts(account_id)

    def test_get_all_outcome_groups_for_context_courses(self):
        """Integration test for the OutcomeGroupsAPI.get_all_outcome_groups_for_context_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_all_outcome_groups_for_context_courses(course_id)

    def test_get_all_outcome_links_for_context_accounts(self):
        """Integration test for the OutcomeGroupsAPI.get_all_outcome_links_for_context_accounts method."""
        account_id = None  # Change me!!

        r = self.client.get_all_outcome_links_for_context_accounts(account_id, outcome_group_style=None, outcome_style=None)

    def test_get_all_outcome_links_for_context_courses(self):
        """Integration test for the OutcomeGroupsAPI.get_all_outcome_links_for_context_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_all_outcome_links_for_context_courses(course_id, outcome_group_style=None, outcome_style=None)

    def test_show_outcome_group_global(self):
        """Integration test for the OutcomeGroupsAPI.show_outcome_group_global method."""
        id = None  # Change me!!

        r = self.client.show_outcome_group_global(id)

    def test_show_outcome_group_accounts(self):
        """Integration test for the OutcomeGroupsAPI.show_outcome_group_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_outcome_group_accounts(id, account_id)

    def test_show_outcome_group_courses(self):
        """Integration test for the OutcomeGroupsAPI.show_outcome_group_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_outcome_group_courses(id, course_id)

    def test_update_outcome_group_global(self):
        """Integration test for the OutcomeGroupsAPI.update_outcome_group_global method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_outcome_group_accounts(self):
        """Integration test for the OutcomeGroupsAPI.update_outcome_group_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_outcome_group_courses(self):
        """Integration test for the OutcomeGroupsAPI.update_outcome_group_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_outcome_group_global(self):
        """Integration test for the OutcomeGroupsAPI.delete_outcome_group_global method."""
        id = None  # Change me!!

        r = self.client.delete_outcome_group_global(id)

    def test_delete_outcome_group_accounts(self):
        """Integration test for the OutcomeGroupsAPI.delete_outcome_group_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_outcome_group_accounts(id, account_id)

    def test_delete_outcome_group_courses(self):
        """Integration test for the OutcomeGroupsAPI.delete_outcome_group_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_outcome_group_courses(id, course_id)

    def test_list_linked_outcomes_global(self):
        """Integration test for the OutcomeGroupsAPI.list_linked_outcomes_global method."""
        id = None  # Change me!!

        r = self.client.list_linked_outcomes_global(id)

    def test_list_linked_outcomes_accounts(self):
        """Integration test for the OutcomeGroupsAPI.list_linked_outcomes_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_linked_outcomes_accounts(id, account_id)

    def test_list_linked_outcomes_courses(self):
        """Integration test for the OutcomeGroupsAPI.list_linked_outcomes_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_linked_outcomes_courses(id, course_id)

    def test_create_link_outcome_global(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_global method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_link_outcome_global_outcome_id(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_global_outcome_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_link_outcome_accounts(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_link_outcome_accounts_outcome_id(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_accounts_outcome_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_link_outcome_courses(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_link_outcome_courses_outcome_id(self):
        """Integration test for the OutcomeGroupsAPI.create_link_outcome_courses_outcome_id method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_unlink_outcome_global(self):
        """Integration test for the OutcomeGroupsAPI.unlink_outcome_global method."""
        id = None  # Change me!!
        outcome_id = None  # Change me!!

        r = self.client.unlink_outcome_global(id, outcome_id)

    def test_unlink_outcome_accounts(self):
        """Integration test for the OutcomeGroupsAPI.unlink_outcome_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!
        outcome_id = None  # Change me!!

        r = self.client.unlink_outcome_accounts(id, account_id, outcome_id)

    def test_unlink_outcome_courses(self):
        """Integration test for the OutcomeGroupsAPI.unlink_outcome_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!
        outcome_id = None  # Change me!!

        r = self.client.unlink_outcome_courses(id, course_id, outcome_id)

    def test_list_subgroups_global(self):
        """Integration test for the OutcomeGroupsAPI.list_subgroups_global method."""
        id = None  # Change me!!

        r = self.client.list_subgroups_global(id)

    def test_list_subgroups_accounts(self):
        """Integration test for the OutcomeGroupsAPI.list_subgroups_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_subgroups_accounts(id, account_id)

    def test_list_subgroups_courses(self):
        """Integration test for the OutcomeGroupsAPI.list_subgroups_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_subgroups_courses(id, course_id)

    def test_create_subgroup_global(self):
        """Integration test for the OutcomeGroupsAPI.create_subgroup_global method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_subgroup_accounts(self):
        """Integration test for the OutcomeGroupsAPI.create_subgroup_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_subgroup_courses(self):
        """Integration test for the OutcomeGroupsAPI.create_subgroup_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_import_outcome_group_global(self):
        """Integration test for the OutcomeGroupsAPI.import_outcome_group_global method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_import_outcome_group_accounts(self):
        """Integration test for the OutcomeGroupsAPI.import_outcome_group_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_import_outcome_group_courses(self):
        """Integration test for the OutcomeGroupsAPI.import_outcome_group_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

