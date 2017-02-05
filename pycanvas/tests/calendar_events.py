"""CalendarEvents API Tests for Version 1.0.

This is a testing template for the generated CalendarEventsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.calendar_events import CalendarEventsAPI
from pycanvas.apis.calendar_events import Calendarevent
from pycanvas.apis.calendar_events import Assignmentevent


class TestCalendarEventsAPI(unittest.TestCase):
    """Tests for the CalendarEventsAPI."""

    def setUp(self):
        self.client = CalendarEventsAPI(secrets.instance_address, secrets.access_token)

    def test_list_calendar_events(self):
        """Integration test for the CalendarEventsAPI.list_calendar_events method."""

        r = self.client.list_calendar_events(all_events=None, context_codes=None, end_date=None, excludes=None, start_date=None, type=None, undated=None)

    def test_list_calendar_events_for_user(self):
        """Integration test for the CalendarEventsAPI.list_calendar_events_for_user method."""
        user_id = None  # Change me!!

        r = self.client.list_calendar_events_for_user(user_id, all_events=None, context_codes=None, end_date=None, excludes=None, start_date=None, type=None, undated=None)

    def test_create_calendar_event(self):
        """Integration test for the CalendarEventsAPI.create_calendar_event method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_single_calendar_event_or_assignment(self):
        """Integration test for the CalendarEventsAPI.get_single_calendar_event_or_assignment method."""
        id = None  # Change me!!

        r = self.client.get_single_calendar_event_or_assignment(id)

    def test_reserve_time_slot(self):
        """Integration test for the CalendarEventsAPI.reserve_time_slot method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_reserve_time_slot_participant_id(self):
        """Integration test for the CalendarEventsAPI.reserve_time_slot_participant_id method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_calendar_event(self):
        """Integration test for the CalendarEventsAPI.update_calendar_event method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_calendar_event(self):
        """Integration test for the CalendarEventsAPI.delete_calendar_event method."""
        id = None  # Change me!!

        r = self.client.delete_calendar_event(id, cancel_reason=None)

    def test_set_course_timetable(self):
        """Integration test for the CalendarEventsAPI.set_course_timetable method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_course_timetable(self):
        """Integration test for the CalendarEventsAPI.get_course_timetable method."""
        course_id = None  # Change me!!

        r = self.client.get_course_timetable(course_id)

    def test_create_or_update_events_directly_for_course_timetable(self):
        """Integration test for the CalendarEventsAPI.create_or_update_events_directly_for_course_timetable method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

