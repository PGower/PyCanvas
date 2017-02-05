"""CalendarEvents API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CalendarEventsAPI(BaseCanvasAPI):
    """CalendarEvents API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CalendarEventsAPI."""
        super(CalendarEventsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CalendarEventsAPI")

    def list_calendar_events(self, all_events=None, context_codes=None, end_date=None, excludes=None, start_date=None, type=None, undated=None):
        """
        List calendar events.

        Retrieve the list of calendar events or assignments for the current user
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - type
        """Defaults to "event""""
        if type is not None:
            self._validate_enum(type, ["event", "assignment"])
            params["type"] = type
        # OPTIONAL - start_date
        """Only return events since the start_date (inclusive).
        Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ."""
        if start_date is not None:
            params["start_date"] = start_date
        # OPTIONAL - end_date
        """Only return events before the end_date (inclusive).
        Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        If end_date is the same as start_date, then only events on that day are
        returned."""
        if end_date is not None:
            params["end_date"] = end_date
        # OPTIONAL - undated
        """Defaults to false (dated events only).
        If true, only return undated events and ignore start_date and end_date."""
        if undated is not None:
            params["undated"] = undated
        # OPTIONAL - all_events
        """Defaults to false (uses start_date, end_date, and undated criteria).
        If true, all events are returned, ignoring start_date, end_date, and undated criteria."""
        if all_events is not None:
            params["all_events"] = all_events
        # OPTIONAL - context_codes
        """List of context codes of courses/groups/users whose events you want to see.
        If not specified, defaults to the current user (i.e personal calendar,
        no course/group events). Limited to 10 context codes, additional ones are
        ignored. The format of this field is the context type, followed by an
        underscore, followed by the context id. For example: course_42"""
        if context_codes is not None:
            params["context_codes"] = context_codes
        # OPTIONAL - excludes
        """Array of attributes to exclude. Possible values are "description", "child_events" and "assignment""""
        if excludes is not None:
            params["excludes"] = excludes

        self.logger.debug("GET /api/v1/calendar_events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/calendar_events".format(**path), data=data, params=params, all_pages=True)

    def list_calendar_events_for_user(self, user_id, all_events=None, context_codes=None, end_date=None, excludes=None, start_date=None, type=None, undated=None):
        """
        List calendar events for a user.

        Retrieve the list of calendar events or assignments for the specified user.
        To view calendar events for a user other than yourself,
        you must either be an observer of that user or an administrator.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # OPTIONAL - type
        """Defaults to "event""""
        if type is not None:
            self._validate_enum(type, ["event", "assignment"])
            params["type"] = type
        # OPTIONAL - start_date
        """Only return events since the start_date (inclusive).
        Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ."""
        if start_date is not None:
            params["start_date"] = start_date
        # OPTIONAL - end_date
        """Only return events before the end_date (inclusive).
        Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        If end_date is the same as start_date, then only events on that day are
        returned."""
        if end_date is not None:
            params["end_date"] = end_date
        # OPTIONAL - undated
        """Defaults to false (dated events only).
        If true, only return undated events and ignore start_date and end_date."""
        if undated is not None:
            params["undated"] = undated
        # OPTIONAL - all_events
        """Defaults to false (uses start_date, end_date, and undated criteria).
        If true, all events are returned, ignoring start_date, end_date, and undated criteria."""
        if all_events is not None:
            params["all_events"] = all_events
        # OPTIONAL - context_codes
        """List of context codes of courses/groups/users whose events you want to see.
        If not specified, defaults to the current user (i.e personal calendar,
        no course/group events). Limited to 10 context codes, additional ones are
        ignored. The format of this field is the context type, followed by an
        underscore, followed by the context id. For example: course_42"""
        if context_codes is not None:
            params["context_codes"] = context_codes
        # OPTIONAL - excludes
        """Array of attributes to exclude. Possible values are "description", "child_events" and "assignment""""
        if excludes is not None:
            params["excludes"] = excludes

        self.logger.debug("GET /api/v1/users/{user_id}/calendar_events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/calendar_events".format(**path), data=data, params=params, all_pages=True)

    def create_calendar_event(self, calendar_event_context_code, calendar_event_child_event_data_X_context_code=None, calendar_event_child_event_data_X_end_at=None, calendar_event_child_event_data_X_start_at=None, calendar_event_description=None, calendar_event_duplicate_append_iterator=None, calendar_event_duplicate_count=None, calendar_event_duplicate_frequency=None, calendar_event_duplicate_interval=None, calendar_event_end_at=None, calendar_event_location_address=None, calendar_event_location_name=None, calendar_event_start_at=None, calendar_event_time_zone_edited=None, calendar_event_title=None):
        """
        Create a calendar event.

        Create and return a new calendar event
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - calendar_event[context_code]
        """Context code of the course/group/user whose calendar this event should be
        added to."""
        data["calendar_event[context_code]"] = calendar_event_context_code
        # OPTIONAL - calendar_event[title]
        """Short title for the calendar event."""
        if calendar_event_title is not None:
            data["calendar_event[title]"] = calendar_event_title
        # OPTIONAL - calendar_event[description]
        """Longer HTML description of the event."""
        if calendar_event_description is not None:
            data["calendar_event[description]"] = calendar_event_description
        # OPTIONAL - calendar_event[start_at]
        """Start date/time of the event."""
        if calendar_event_start_at is not None:
            data["calendar_event[start_at]"] = calendar_event_start_at
        # OPTIONAL - calendar_event[end_at]
        """End date/time of the event."""
        if calendar_event_end_at is not None:
            data["calendar_event[end_at]"] = calendar_event_end_at
        # OPTIONAL - calendar_event[location_name]
        """Location name of the event."""
        if calendar_event_location_name is not None:
            data["calendar_event[location_name]"] = calendar_event_location_name
        # OPTIONAL - calendar_event[location_address]
        """Location address"""
        if calendar_event_location_address is not None:
            data["calendar_event[location_address]"] = calendar_event_location_address
        # OPTIONAL - calendar_event[time_zone_edited]
        """Time zone of the user editing the event. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        if calendar_event_time_zone_edited is not None:
            data["calendar_event[time_zone_edited]"] = calendar_event_time_zone_edited
        # OPTIONAL - calendar_event[child_event_data][X][start_at]
        """Section-level start time(s) if this is a course event. X can be any
        identifier, provided that it is consistent across the start_at, end_at
        and context_code"""
        if calendar_event_child_event_data_X_start_at is not None:
            data["calendar_event[child_event_data][X][start_at]"] = calendar_event_child_event_data_X_start_at
        # OPTIONAL - calendar_event[child_event_data][X][end_at]
        """Section-level end time(s) if this is a course event."""
        if calendar_event_child_event_data_X_end_at is not None:
            data["calendar_event[child_event_data][X][end_at]"] = calendar_event_child_event_data_X_end_at
        # OPTIONAL - calendar_event[child_event_data][X][context_code]
        """Context code(s) corresponding to the section-level start and end time(s)."""
        if calendar_event_child_event_data_X_context_code is not None:
            data["calendar_event[child_event_data][X][context_code]"] = calendar_event_child_event_data_X_context_code
        # OPTIONAL - calendar_event[duplicate][count]
        """Number of times to copy/duplicate the event."""
        if calendar_event_duplicate_count is not None:
            data["calendar_event[duplicate][count]"] = calendar_event_duplicate_count
        # OPTIONAL - calendar_event[duplicate][interval]
        """Defaults to 1 if duplicate `count` is set.  The interval between the duplicated events."""
        if calendar_event_duplicate_interval is not None:
            data["calendar_event[duplicate][interval]"] = calendar_event_duplicate_interval
        # OPTIONAL - calendar_event[duplicate][frequency]
        """Defaults to "weekly".  The frequency at which to duplicate the event"""
        if calendar_event_duplicate_frequency is not None:
            self._validate_enum(calendar_event_duplicate_frequency, ["daily", "weekly", "monthly"])
            data["calendar_event[duplicate][frequency]"] = calendar_event_duplicate_frequency
        # OPTIONAL - calendar_event[duplicate][append_iterator]
        """Defaults to false.  If set to `true`, an increasing counter number will be appended to the event title
        when the event is duplicated.  (e.g. Event 1, Event 2, Event 3, etc)"""
        if calendar_event_duplicate_append_iterator is not None:
            data["calendar_event[duplicate][append_iterator]"] = calendar_event_duplicate_append_iterator

        self.logger.debug("POST /api/v1/calendar_events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/calendar_events".format(**path), data=data, params=params, no_data=True)

    def get_single_calendar_event_or_assignment(self, id):
        """
        Get a single calendar event or assignment.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/calendar_events/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/calendar_events/{id}".format(**path), data=data, params=params, single_item=True)

    def reserve_time_slot(self, id, cancel_existing=None, comments=None, participant_id=None):
        """
        Reserve a time slot.

        Reserves a particular time slot and return the new reservation
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - participant_id
        """User or group id for whom you are making the reservation (depends on the
        participant type). Defaults to the current user (or user's candidate group)."""
        if participant_id is not None:
            data["participant_id"] = participant_id
        # OPTIONAL - comments
        """Comments to associate with this reservation"""
        if comments is not None:
            data["comments"] = comments
        # OPTIONAL - cancel_existing
        """Defaults to false. If true, cancel any previous reservation(s) for this
        participant and appointment group."""
        if cancel_existing is not None:
            data["cancel_existing"] = cancel_existing

        self.logger.debug("POST /api/v1/calendar_events/{id}/reservations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/calendar_events/{id}/reservations".format(**path), data=data, params=params, no_data=True)

    def reserve_time_slot_participant_id(self, id, participant_id, cancel_existing=None, comments=None):
        """
        Reserve a time slot.

        Reserves a particular time slot and return the new reservation
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # REQUIRED - PATH - participant_id
        """User or group id for whom you are making the reservation (depends on the
        participant type). Defaults to the current user (or user's candidate group)."""
        path["participant_id"] = participant_id
        # OPTIONAL - comments
        """Comments to associate with this reservation"""
        if comments is not None:
            data["comments"] = comments
        # OPTIONAL - cancel_existing
        """Defaults to false. If true, cancel any previous reservation(s) for this
        participant and appointment group."""
        if cancel_existing is not None:
            data["cancel_existing"] = cancel_existing

        self.logger.debug("POST /api/v1/calendar_events/{id}/reservations/{participant_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/calendar_events/{id}/reservations/{participant_id}".format(**path), data=data, params=params, no_data=True)

    def update_calendar_event(self, id, calendar_event_child_event_data_X_context_code=None, calendar_event_child_event_data_X_end_at=None, calendar_event_child_event_data_X_start_at=None, calendar_event_context_code=None, calendar_event_description=None, calendar_event_end_at=None, calendar_event_location_address=None, calendar_event_location_name=None, calendar_event_start_at=None, calendar_event_time_zone_edited=None, calendar_event_title=None):
        """
        Update a calendar event.

        Update and return a calendar event
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - calendar_event[context_code]
        """Context code of the course/group/user to move this event to.
        Scheduler appointments and events with section-specific times cannot be moved between calendars."""
        if calendar_event_context_code is not None:
            data["calendar_event[context_code]"] = calendar_event_context_code
        # OPTIONAL - calendar_event[title]
        """Short title for the calendar event."""
        if calendar_event_title is not None:
            data["calendar_event[title]"] = calendar_event_title
        # OPTIONAL - calendar_event[description]
        """Longer HTML description of the event."""
        if calendar_event_description is not None:
            data["calendar_event[description]"] = calendar_event_description
        # OPTIONAL - calendar_event[start_at]
        """Start date/time of the event."""
        if calendar_event_start_at is not None:
            data["calendar_event[start_at]"] = calendar_event_start_at
        # OPTIONAL - calendar_event[end_at]
        """End date/time of the event."""
        if calendar_event_end_at is not None:
            data["calendar_event[end_at]"] = calendar_event_end_at
        # OPTIONAL - calendar_event[location_name]
        """Location name of the event."""
        if calendar_event_location_name is not None:
            data["calendar_event[location_name]"] = calendar_event_location_name
        # OPTIONAL - calendar_event[location_address]
        """Location address"""
        if calendar_event_location_address is not None:
            data["calendar_event[location_address]"] = calendar_event_location_address
        # OPTIONAL - calendar_event[time_zone_edited]
        """Time zone of the user editing the event. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        if calendar_event_time_zone_edited is not None:
            data["calendar_event[time_zone_edited]"] = calendar_event_time_zone_edited
        # OPTIONAL - calendar_event[child_event_data][X][start_at]
        """Section-level start time(s) if this is a course event. X can be any
        identifier, provided that it is consistent across the start_at, end_at
        and context_code"""
        if calendar_event_child_event_data_X_start_at is not None:
            data["calendar_event[child_event_data][X][start_at]"] = calendar_event_child_event_data_X_start_at
        # OPTIONAL - calendar_event[child_event_data][X][end_at]
        """Section-level end time(s) if this is a course event."""
        if calendar_event_child_event_data_X_end_at is not None:
            data["calendar_event[child_event_data][X][end_at]"] = calendar_event_child_event_data_X_end_at
        # OPTIONAL - calendar_event[child_event_data][X][context_code]
        """Context code(s) corresponding to the section-level start and end time(s)."""
        if calendar_event_child_event_data_X_context_code is not None:
            data["calendar_event[child_event_data][X][context_code]"] = calendar_event_child_event_data_X_context_code

        self.logger.debug("PUT /api/v1/calendar_events/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/calendar_events/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_calendar_event(self, id, cancel_reason=None):
        """
        Delete a calendar event.

        Delete an event from the calendar and return the deleted event
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - cancel_reason
        """Reason for deleting/canceling the event."""
        if cancel_reason is not None:
            params["cancel_reason"] = cancel_reason

        self.logger.debug("DELETE /api/v1/calendar_events/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/calendar_events/{id}".format(**path), data=data, params=params, no_data=True)

    def set_course_timetable(self, course_id, timetables_course_section_id=None, timetables_course_section_id_end_time=None, timetables_course_section_id_location_name=None, timetables_course_section_id_start_time=None, timetables_course_section_id_weekdays=None):
        """
        Set a course timetable.

        Creates and updates "timetable" events for a course.
        Can automaticaly generate a series of calendar events based on simple schedules
        (e.g. "Monday and Wednesday at 2:00pm" )
        
        Existing timetable events for the course and course sections
        will be updated if they still are part of the timetable.
        Otherwise, they will be deleted.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # OPTIONAL - timetables[course_section_id]
        """An array of timetable objects for the course section specified by course_section_id.
        If course_section_id is set to "all", events will be created for the entire course."""
        if timetables_course_section_id is not None:
            data["timetables[course_section_id]"] = timetables_course_section_id
        # OPTIONAL - timetables[course_section_id][weekdays]
        """A comma-separated list of abbreviated weekdays
        (Mon-Monday, Tue-Tuesday, Wed-Wednesday, Thu-Thursday, Fri-Friday, Sat-Saturday, Sun-Sunday)"""
        if timetables_course_section_id_weekdays is not None:
            data["timetables[course_section_id][weekdays]"] = timetables_course_section_id_weekdays
        # OPTIONAL - timetables[course_section_id][start_time]
        """Time to start each event at (e.g. "9:00 am")"""
        if timetables_course_section_id_start_time is not None:
            data["timetables[course_section_id][start_time]"] = timetables_course_section_id_start_time
        # OPTIONAL - timetables[course_section_id][end_time]
        """Time to end each event at (e.g. "9:00 am")"""
        if timetables_course_section_id_end_time is not None:
            data["timetables[course_section_id][end_time]"] = timetables_course_section_id_end_time
        # OPTIONAL - timetables[course_section_id][location_name]
        """A location name to set for each event"""
        if timetables_course_section_id_location_name is not None:
            data["timetables[course_section_id][location_name]"] = timetables_course_section_id_location_name

        self.logger.debug("POST /api/v1/courses/{course_id}/calendar_events/timetable with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/calendar_events/timetable".format(**path), data=data, params=params, no_data=True)

    def get_course_timetable(self, course_id):
        """
        Get course timetable.

        Returns the last timetable set by the
        {api:CalendarEventsApiController#set_course_timetable Set a course timetable} endpoint
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/calendar_events/timetable with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/calendar_events/timetable".format(**path), data=data, params=params, no_data=True)

    def create_or_update_events_directly_for_course_timetable(self, course_id, course_section_id=None, events=None, events_code=None, events_end_at=None, events_location_name=None, events_start_at=None):
        """
        Create or update events directly for a course timetable.

        Creates and updates "timetable" events for a course or course section.
        Similar to {api:CalendarEventsApiController#set_course_timetable setting a course timetable},
        but instead of generating a list of events based on a timetable schedule,
        this endpoint expects a complete list of events.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # OPTIONAL - course_section_id
        """Events will be created for the course section specified by course_section_id.
        If not present, events will be created for the entire course."""
        if course_section_id is not None:
            data["course_section_id"] = course_section_id
        # OPTIONAL - events
        """An array of event objects to use."""
        if events is not None:
            data["events"] = events
        # OPTIONAL - events[start_at]
        """Start time for the event"""
        if events_start_at is not None:
            data["events[start_at]"] = events_start_at
        # OPTIONAL - events[end_at]
        """End time for the event"""
        if events_end_at is not None:
            data["events[end_at]"] = events_end_at
        # OPTIONAL - events[location_name]
        """Location name for the event"""
        if events_location_name is not None:
            data["events[location_name]"] = events_location_name
        # OPTIONAL - events[code]
        """A unique identifier that can be used to update the event at a later time
        If one is not specified, an identifier will be generated based on the start and end times"""
        if events_code is not None:
            data["events[code]"] = events_code

        self.logger.debug("POST /api/v1/courses/{course_id}/calendar_events/timetable_events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/calendar_events/timetable_events".format(**path), data=data, params=params, no_data=True)


class Calendarevent(BaseModel):
    """Calendarevent Model."""

    def __init__(self, reserved=None, updated_at=None, group=None, child_events_count=None, available_slots=None, id=None, reserve_url=None, location_name=None, title=None, end_at=None, appointment_group_id=None, context_code=None, hidden=None, start_at=None, description=None, child_events=None, workflow_state=None, effective_context_code=None, html_url=None, all_day_date=None, user=None, participants_per_appointment=None, parent_event_id=None, created_at=None, all_day=None, url=None, location_address=None, own_reservation=None, appointment_group_url=None, all_context_codes=None):
        """Init method for Calendarevent class."""
        self._reserved = reserved
        self._updated_at = updated_at
        self._group = group
        self._child_events_count = child_events_count
        self._available_slots = available_slots
        self._id = id
        self._reserve_url = reserve_url
        self._location_name = location_name
        self._title = title
        self._end_at = end_at
        self._appointment_group_id = appointment_group_id
        self._context_code = context_code
        self._hidden = hidden
        self._start_at = start_at
        self._description = description
        self._child_events = child_events
        self._workflow_state = workflow_state
        self._effective_context_code = effective_context_code
        self._html_url = html_url
        self._all_day_date = all_day_date
        self._user = user
        self._participants_per_appointment = participants_per_appointment
        self._parent_event_id = parent_event_id
        self._created_at = created_at
        self._all_day = all_day
        self._url = url
        self._location_address = location_address
        self._own_reservation = own_reservation
        self._appointment_group_url = appointment_group_url
        self._all_context_codes = all_context_codes

        self.logger = logging.getLogger('pycanvas.Calendarevent')

    @property
    def reserved(self):
        """If the event is a time slot, a boolean indicating whether the user has already made a reservation for it."""
        return self._reserved

    @reserved.setter
    def reserved(self, value):
        """Setter for reserved property."""
        self.logger.warn("Setting values on reserved will NOT update the remote Canvas instance.")
        self._reserved = value

    @property
    def updated_at(self):
        """When the calendar event was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def group(self):
        """If the event is a group-level reservation, this will contain the group participant JSON (refer to the Groups API)."""
        return self._group

    @group.setter
    def group(self, value):
        """Setter for group property."""
        self.logger.warn("Setting values on group will NOT update the remote Canvas instance.")
        self._group = value

    @property
    def child_events_count(self):
        """The number of child_events. See child_events (and parent_event_id)."""
        return self._child_events_count

    @child_events_count.setter
    def child_events_count(self, value):
        """Setter for child_events_count property."""
        self.logger.warn("Setting values on child_events_count will NOT update the remote Canvas instance.")
        self._child_events_count = value

    @property
    def available_slots(self):
        """If the event is a time slot and it has a participant limit, an integer indicating how many slots are available."""
        return self._available_slots

    @available_slots.setter
    def available_slots(self, value):
        """Setter for available_slots property."""
        self.logger.warn("Setting values on available_slots will NOT update the remote Canvas instance.")
        self._available_slots = value

    @property
    def id(self):
        """The ID of the calendar event."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def reserve_url(self):
        """If the event is a time slot, the API URL for reserving it."""
        return self._reserve_url

    @reserve_url.setter
    def reserve_url(self, value):
        """Setter for reserve_url property."""
        self.logger.warn("Setting values on reserve_url will NOT update the remote Canvas instance.")
        self._reserve_url = value

    @property
    def location_name(self):
        """The location name of the event."""
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        """Setter for location_name property."""
        self.logger.warn("Setting values on location_name will NOT update the remote Canvas instance.")
        self._location_name = value

    @property
    def title(self):
        """The title of the calendar event."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def end_at(self):
        """The end timestamp of the event."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def appointment_group_id(self):
        """Various Appointment-Group-related fields.These fields are only pertinent to time slots (appointments) and reservations of those time slots. See the Appointment Groups API. The id of the appointment group."""
        return self._appointment_group_id

    @appointment_group_id.setter
    def appointment_group_id(self, value):
        """Setter for appointment_group_id property."""
        self.logger.warn("Setting values on appointment_group_id will NOT update the remote Canvas instance.")
        self._appointment_group_id = value

    @property
    def context_code(self):
        """the context code of the calendar this event belongs to (course, user or group)."""
        return self._context_code

    @context_code.setter
    def context_code(self, value):
        """Setter for context_code property."""
        self.logger.warn("Setting values on context_code will NOT update the remote Canvas instance.")
        self._context_code = value

    @property
    def hidden(self):
        """Whether this event should be displayed on the calendar. Only true for course-level events with section-level child events."""
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Setter for hidden property."""
        self.logger.warn("Setting values on hidden will NOT update the remote Canvas instance.")
        self._hidden = value

    @property
    def start_at(self):
        """The start timestamp of the event."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def description(self):
        """The HTML description of the event."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def child_events(self):
        """Included by default, but may be excluded (see include[] option). If this is a time slot (see the Appointment Groups API) this will be a list of any reservations. If this is a course-level event, this will be a list of section-level events (if any)."""
        return self._child_events

    @child_events.setter
    def child_events(self, value):
        """Setter for child_events property."""
        self.logger.warn("Setting values on child_events will NOT update the remote Canvas instance.")
        self._child_events = value

    @property
    def workflow_state(self):
        """Current state of the event ('active', 'locked' or 'deleted') 'locked' indicates that start_at/end_at cannot be changed (though the event could be deleted). Normally only reservations or time slots with reservations are locked (see the Appointment Groups API)."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def effective_context_code(self):
        """if specified, it indicates which calendar this event should be displayed on. for example, a section-level event would have the course's context code here, while the section's context code would be returned above)."""
        return self._effective_context_code

    @effective_context_code.setter
    def effective_context_code(self, value):
        """Setter for effective_context_code property."""
        self.logger.warn("Setting values on effective_context_code will NOT update the remote Canvas instance.")
        self._effective_context_code = value

    @property
    def html_url(self):
        """URL for a user to view this event."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def all_day_date(self):
        """The date of this event."""
        return self._all_day_date

    @all_day_date.setter
    def all_day_date(self, value):
        """Setter for all_day_date property."""
        self.logger.warn("Setting values on all_day_date will NOT update the remote Canvas instance.")
        self._all_day_date = value

    @property
    def user(self):
        """If the event is a user-level reservation, this will contain the user participant JSON (refer to the Users API)."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def participants_per_appointment(self):
        """If the event is a time slot, this is the participant limit."""
        return self._participants_per_appointment

    @participants_per_appointment.setter
    def participants_per_appointment(self, value):
        """Setter for participants_per_appointment property."""
        self.logger.warn("Setting values on participants_per_appointment will NOT update the remote Canvas instance.")
        self._participants_per_appointment = value

    @property
    def parent_event_id(self):
        """Normally null. If this is a reservation (see the Appointment Groups API), the id will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event."""
        return self._parent_event_id

    @parent_event_id.setter
    def parent_event_id(self, value):
        """Setter for parent_event_id property."""
        self.logger.warn("Setting values on parent_event_id will NOT update the remote Canvas instance.")
        self._parent_event_id = value

    @property
    def created_at(self):
        """When the calendar event was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def all_day(self):
        """Boolean indicating whether this is an all-day event (midnight to midnight)."""
        return self._all_day

    @all_day.setter
    def all_day(self, value):
        """Setter for all_day property."""
        self.logger.warn("Setting values on all_day will NOT update the remote Canvas instance.")
        self._all_day = value

    @property
    def url(self):
        """URL for this calendar event (to update, delete, etc.)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def location_address(self):
        """The address where the event is taking place."""
        return self._location_address

    @location_address.setter
    def location_address(self, value):
        """Setter for location_address property."""
        self.logger.warn("Setting values on location_address will NOT update the remote Canvas instance.")
        self._location_address = value

    @property
    def own_reservation(self):
        """If the event is a reservation, this a boolean indicating whether it is the current user's reservation, or someone else's."""
        return self._own_reservation

    @own_reservation.setter
    def own_reservation(self, value):
        """Setter for own_reservation property."""
        self.logger.warn("Setting values on own_reservation will NOT update the remote Canvas instance.")
        self._own_reservation = value

    @property
    def appointment_group_url(self):
        """The API URL of the appointment group."""
        return self._appointment_group_url

    @appointment_group_url.setter
    def appointment_group_url(self, value):
        """Setter for appointment_group_url property."""
        self.logger.warn("Setting values on appointment_group_url will NOT update the remote Canvas instance.")
        self._appointment_group_url = value

    @property
    def all_context_codes(self):
        """a comma-separated list of all calendar contexts this event is part of."""
        return self._all_context_codes

    @all_context_codes.setter
    def all_context_codes(self, value):
        """Setter for all_context_codes property."""
        self.logger.warn("Setting values on all_context_codes will NOT update the remote Canvas instance.")
        self._all_context_codes = value


class Assignmentevent(BaseModel):
    """Assignmentevent Model."""

    def __init__(self, start_at=None, description=None, title=None, url=None, assignment=None, created_at=None, workflow_state=None, html_url=None, end_at=None, updated_at=None, all_day_date=None, context_code=None, assignment_overrides=None, id=None, all_day=None):
        """Init method for Assignmentevent class."""
        self._start_at = start_at
        self._description = description
        self._title = title
        self._url = url
        self._assignment = assignment
        self._created_at = created_at
        self._workflow_state = workflow_state
        self._html_url = html_url
        self._end_at = end_at
        self._updated_at = updated_at
        self._all_day_date = all_day_date
        self._context_code = context_code
        self._assignment_overrides = assignment_overrides
        self._id = id
        self._all_day = all_day

        self.logger = logging.getLogger('pycanvas.Assignmentevent')

    @property
    def start_at(self):
        """The due_at timestamp of the assignment."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def description(self):
        """The HTML description of the assignment."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def title(self):
        """The title of the assignment."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """URL for this assignment (note that updating/deleting should be done via the Assignments API)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def assignment(self):
        """The full assignment JSON data (See the Assignments API)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value):
        """Setter for assignment property."""
        self.logger.warn("Setting values on assignment will NOT update the remote Canvas instance.")
        self._assignment = value

    @property
    def created_at(self):
        """When the assignment was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def workflow_state(self):
        """Current state of the assignment ('published' or 'deleted')."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def html_url(self):
        """URL for a user to view this assignment."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def end_at(self):
        """The due_at timestamp of the assignment."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def updated_at(self):
        """When the assignment was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def all_day_date(self):
        """The due date of this assignment."""
        return self._all_day_date

    @all_day_date.setter
    def all_day_date(self, value):
        """Setter for all_day_date property."""
        self.logger.warn("Setting values on all_day_date will NOT update the remote Canvas instance.")
        self._all_day_date = value

    @property
    def context_code(self):
        """the context code of the (course) calendar this assignment belongs to."""
        return self._context_code

    @context_code.setter
    def context_code(self, value):
        """Setter for context_code property."""
        self.logger.warn("Setting values on context_code will NOT update the remote Canvas instance.")
        self._context_code = value

    @property
    def assignment_overrides(self):
        """The list of AssignmentOverrides that apply to this event (See the Assignments API). This information is useful for determining which students or sections this assignment-due event applies to."""
        return self._assignment_overrides

    @assignment_overrides.setter
    def assignment_overrides(self, value):
        """Setter for assignment_overrides property."""
        self.logger.warn("Setting values on assignment_overrides will NOT update the remote Canvas instance.")
        self._assignment_overrides = value

    @property
    def id(self):
        """A synthetic ID for the assignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def all_day(self):
        """Boolean indicating whether this is an all-day event (e.g. assignment due at midnight)."""
        return self._all_day

    @all_day.setter
    def all_day(self, value):
        """Setter for all_day property."""
        self.logger.warn("Setting values on all_day will NOT update the remote Canvas instance.")
        self._all_day = value

