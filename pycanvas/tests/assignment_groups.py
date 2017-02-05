"""AssignmentGroups API Tests for Version 1.0.

This is a testing template for the generated AssignmentGroupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.assignment_groups import AssignmentGroupsAPI
from pycanvas.apis.assignment_groups import Gradingrules
from pycanvas.apis.assignment_groups import Assignmentgroup


class TestAssignmentGroupsAPI(unittest.TestCase):
    """Tests for the AssignmentGroupsAPI."""

    def setUp(self):
        self.client = AssignmentGroupsAPI(secrets.instance_address, secrets.access_token)

    def test_list_assignment_groups(self):
        """Integration test for the AssignmentGroupsAPI.list_assignment_groups method."""
        course_id = None  # Change me!!

        r = self.client.list_assignment_groups(course_id, exclude_assignment_submission_types=None, grading_period_id=None, include=None, override_assignment_dates=None, scope_assignments_to_student=None)

    def test_get_assignment_group(self):
        """Integration test for the AssignmentGroupsAPI.get_assignment_group method."""
        course_id = None  # Change me!!
        assignment_group_id = None  # Change me!!

        r = self.client.get_assignment_group(course_id, assignment_group_id, grading_period_id=None, include=None, override_assignment_dates=None)

    def test_create_assignment_group(self):
        """Integration test for the AssignmentGroupsAPI.create_assignment_group method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_assignment_group(self):
        """Integration test for the AssignmentGroupsAPI.edit_assignment_group method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_destroy_assignment_group(self):
        """Integration test for the AssignmentGroupsAPI.destroy_assignment_group method."""
        course_id = None  # Change me!!
        assignment_group_id = None  # Change me!!

        r = self.client.destroy_assignment_group(course_id, assignment_group_id, move_assignments_to=None)

