"""ExternalTools API Tests for Version 1.0.

This is a testing template for the generated ExternalToolsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.external_tools import ExternalToolsAPI


class TestExternalToolsAPI(unittest.TestCase):
    """Tests for the ExternalToolsAPI."""

    def setUp(self):
        self.client = ExternalToolsAPI(secrets.instance_address, secrets.access_token)

    def test_list_external_tools_courses(self):
        """Integration test for the ExternalToolsAPI.list_external_tools_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_external_tools_courses(course_id, search_term=None, selectable=None)

    def test_list_external_tools_accounts(self):
        """Integration test for the ExternalToolsAPI.list_external_tools_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_external_tools_accounts(account_id, search_term=None, selectable=None)

    def test_get_sessionless_launch_url_for_external_tool_courses(self):
        """Integration test for the ExternalToolsAPI.get_sessionless_launch_url_for_external_tool_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_sessionless_launch_url_for_external_tool_courses(course_id, assignment_id=None, id=None, launch_type=None, url=None)

    def test_get_sessionless_launch_url_for_external_tool_accounts(self):
        """Integration test for the ExternalToolsAPI.get_sessionless_launch_url_for_external_tool_accounts method."""
        account_id = None  # Change me!!

        r = self.client.get_sessionless_launch_url_for_external_tool_accounts(account_id, assignment_id=None, id=None, launch_type=None, url=None)

    def test_get_single_external_tool_courses(self):
        """Integration test for the ExternalToolsAPI.get_single_external_tool_courses method."""
        course_id = None  # Change me!!
        external_tool_id = None  # Change me!!

        r = self.client.get_single_external_tool_courses(course_id, external_tool_id)

    def test_get_single_external_tool_accounts(self):
        """Integration test for the ExternalToolsAPI.get_single_external_tool_accounts method."""
        account_id = None  # Change me!!
        external_tool_id = None  # Change me!!

        r = self.client.get_single_external_tool_accounts(account_id, external_tool_id)

    def test_create_external_tool_courses(self):
        """Integration test for the ExternalToolsAPI.create_external_tool_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_external_tool_accounts(self):
        """Integration test for the ExternalToolsAPI.create_external_tool_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_external_tool_courses(self):
        """Integration test for the ExternalToolsAPI.edit_external_tool_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_external_tool_accounts(self):
        """Integration test for the ExternalToolsAPI.edit_external_tool_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_external_tool_courses(self):
        """Integration test for the ExternalToolsAPI.delete_external_tool_courses method."""
        course_id = None  # Change me!!
        external_tool_id = None  # Change me!!

        r = self.client.delete_external_tool_courses(course_id, external_tool_id)

    def test_delete_external_tool_accounts(self):
        """Integration test for the ExternalToolsAPI.delete_external_tool_accounts method."""
        account_id = None  # Change me!!
        external_tool_id = None  # Change me!!

        r = self.client.delete_external_tool_accounts(account_id, external_tool_id)

