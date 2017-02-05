"""Modules API Tests for Version 1.0.

This is a testing template for the generated ModulesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.modules import ModulesAPI
from pycanvas.apis.modules import Contentdetails
from pycanvas.apis.modules import Moduleitemsequenceasset
from pycanvas.apis.modules import Moduleitemcompletionrequirement
from pycanvas.apis.modules import Module
from pycanvas.apis.modules import Moduleitemsequence
from pycanvas.apis.modules import Completionrequirement
from pycanvas.apis.modules import Moduleitem
from pycanvas.apis.modules import Moduleitemsequencenode
from pycanvas.apis.modules import Moduleitemcontentdetails


class TestModulesAPI(unittest.TestCase):
    """Tests for the ModulesAPI."""

    def setUp(self):
        self.client = ModulesAPI(secrets.instance_address, secrets.access_token)

    def test_list_modules(self):
        """Integration test for the ModulesAPI.list_modules method."""
        course_id = None  # Change me!!

        r = self.client.list_modules(course_id, include=None, search_term=None, student_id=None)

    def test_show_module(self):
        """Integration test for the ModulesAPI.show_module method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_module(id, course_id, include=None, student_id=None)

    def test_create_module(self):
        """Integration test for the ModulesAPI.create_module method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_module(self):
        """Integration test for the ModulesAPI.update_module method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_module(self):
        """Integration test for the ModulesAPI.delete_module method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_module(id, course_id)

    def test_re_lock_module_progressions(self):
        """Integration test for the ModulesAPI.re_lock_module_progressions method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_module_items(self):
        """Integration test for the ModulesAPI.list_module_items method."""
        course_id = None  # Change me!!
        module_id = None  # Change me!!

        r = self.client.list_module_items(course_id, module_id, include=None, search_term=None, student_id=None)

    def test_show_module_item(self):
        """Integration test for the ModulesAPI.show_module_item method."""
        course_id = None  # Change me!!
        module_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_module_item(id, course_id, module_id, include=None, student_id=None)

    def test_create_module_item(self):
        """Integration test for the ModulesAPI.create_module_item method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_module_item(self):
        """Integration test for the ModulesAPI.update_module_item method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_select_mastery_path(self):
        """Integration test for the ModulesAPI.select_mastery_path method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_module_item(self):
        """Integration test for the ModulesAPI.delete_module_item method."""
        course_id = None  # Change me!!
        module_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_module_item(id, course_id, module_id)

    def test_mark_module_item_as_done_not_done(self):
        """Integration test for the ModulesAPI.mark_module_item_as_done_not_done method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_module_item_sequence(self):
        """Integration test for the ModulesAPI.get_module_item_sequence method."""
        course_id = None  # Change me!!

        r = self.client.get_module_item_sequence(course_id, asset_id=None, asset_type=None)

    def test_mark_module_item_read(self):
        """Integration test for the ModulesAPI.mark_module_item_read method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

