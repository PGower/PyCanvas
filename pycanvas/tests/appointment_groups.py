"""AppointmentGroups API Tests for Version 1.0.

This is a testing template for the generated AppointmentGroupsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.appointment_groups import AppointmentGroupsAPI
from pycanvas.apis.appointment_groups import Appointmentgroup
from pycanvas.apis.appointment_groups import Appointment


class TestAppointmentGroupsAPI(unittest.TestCase):
    """Tests for the AppointmentGroupsAPI."""

    def setUp(self):
        self.client = AppointmentGroupsAPI(secrets.instance_address, secrets.access_token)

    def test_list_appointment_groups(self):
        """Integration test for the AppointmentGroupsAPI.list_appointment_groups method."""

        r = self.client.list_appointment_groups(context_codes=None, include=None, include_past_appointments=None, scope=None)

    def test_create_appointment_group(self):
        """Integration test for the AppointmentGroupsAPI.create_appointment_group method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_single_appointment_group(self):
        """Integration test for the AppointmentGroupsAPI.get_single_appointment_group method."""
        id = None  # Change me!!

        r = self.client.get_single_appointment_group(id, include=None)

    def test_update_appointment_group(self):
        """Integration test for the AppointmentGroupsAPI.update_appointment_group method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_appointment_group(self):
        """Integration test for the AppointmentGroupsAPI.delete_appointment_group method."""
        id = None  # Change me!!

        r = self.client.delete_appointment_group(id, cancel_reason=None)

    def test_list_user_participants(self):
        """Integration test for the AppointmentGroupsAPI.list_user_participants method."""
        id = None  # Change me!!

        r = self.client.list_user_participants(id, registration_status=None)

    def test_list_student_group_participants(self):
        """Integration test for the AppointmentGroupsAPI.list_student_group_participants method."""
        id = None  # Change me!!

        r = self.client.list_student_group_participants(id, registration_status=None)

