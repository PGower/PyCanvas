"""CustomGradebookColumns API Tests for Version 1.0.

This is a testing template for the generated CustomGradebookColumnsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.custom_gradebook_columns import CustomGradebookColumnsAPI
from pycanvas.apis.custom_gradebook_columns import Columndatum
from pycanvas.apis.custom_gradebook_columns import Customcolumn


class TestCustomGradebookColumnsAPI(unittest.TestCase):
    """Tests for the CustomGradebookColumnsAPI."""

    def setUp(self):
        self.client = CustomGradebookColumnsAPI(secrets.instance_address, secrets.access_token)

    def test_list_custom_gradebook_columns(self):
        """Integration test for the CustomGradebookColumnsAPI.list_custom_gradebook_columns method."""
        course_id = None  # Change me!!

        r = self.client.list_custom_gradebook_columns(course_id, include_hidden=None)

    def test_create_custom_gradebook_column(self):
        """Integration test for the CustomGradebookColumnsAPI.create_custom_gradebook_column method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_custom_gradebook_column(self):
        """Integration test for the CustomGradebookColumnsAPI.update_custom_gradebook_column method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_custom_gradebook_column(self):
        """Integration test for the CustomGradebookColumnsAPI.delete_custom_gradebook_column method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_custom_gradebook_column(id, course_id)

    def test_reorder_custom_columns(self):
        """Integration test for the CustomGradebookColumnsAPI.reorder_custom_columns method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_entries_for_column(self):
        """Integration test for the CustomGradebookColumnsAPI.list_entries_for_column method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_entries_for_column(id, course_id)

    def test_update_column_data(self):
        """Integration test for the CustomGradebookColumnsAPI.update_column_data method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

