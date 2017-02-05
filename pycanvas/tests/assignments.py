"""Assignments API Tests for Version 1.0.

This is a testing template for the generated AssignmentsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.assignments import AssignmentsAPI
from pycanvas.apis.assignments import Turnitinsettings
from pycanvas.apis.assignments import Assignmentoverride
from pycanvas.apis.assignments import Externaltooltagattributes
from pycanvas.apis.assignments import Assignment
from pycanvas.apis.assignments import Needsgradingcount
from pycanvas.apis.assignments import Rubriccriteria
from pycanvas.apis.assignments import Assignmentdate
from pycanvas.apis.assignments import Rubricrating
from pycanvas.apis.assignments import Lockinfo


class TestAssignmentsAPI(unittest.TestCase):
    """Tests for the AssignmentsAPI."""

    def setUp(self):
        self.client = AssignmentsAPI(secrets.instance_address, secrets.access_token)

    def test_delete_assignment(self):
        """Integration test for the AssignmentsAPI.delete_assignment method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_assignment(id, course_id)

    def test_list_assignments(self):
        """Integration test for the AssignmentsAPI.list_assignments method."""
        course_id = None  # Change me!!

        r = self.client.list_assignments(course_id, bucket=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None, search_term=None)

    def test_get_single_assignment(self):
        """Integration test for the AssignmentsAPI.get_single_assignment method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_assignment(id, course_id, all_dates=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None)

    def test_create_assignment(self):
        """Integration test for the AssignmentsAPI.create_assignment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_assignment(self):
        """Integration test for the AssignmentsAPI.edit_assignment method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_assignment_overrides(self):
        """Integration test for the AssignmentsAPI.list_assignment_overrides method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_assignment_overrides(course_id, assignment_id)

    def test_get_single_assignment_override(self):
        """Integration test for the AssignmentsAPI.get_single_assignment_override method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_assignment_override(id, course_id, assignment_id)

    def test_redirect_to_assignment_override_for_group(self):
        """Integration test for the AssignmentsAPI.redirect_to_assignment_override_for_group method."""
        group_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.redirect_to_assignment_override_for_group(group_id, assignment_id)

    def test_redirect_to_assignment_override_for_section(self):
        """Integration test for the AssignmentsAPI.redirect_to_assignment_override_for_section method."""
        course_section_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.redirect_to_assignment_override_for_section(assignment_id, course_section_id)

    def test_create_assignment_override(self):
        """Integration test for the AssignmentsAPI.create_assignment_override method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_assignment_override(self):
        """Integration test for the AssignmentsAPI.update_assignment_override method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_assignment_override(self):
        """Integration test for the AssignmentsAPI.delete_assignment_override method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_assignment_override(id, course_id, assignment_id)

