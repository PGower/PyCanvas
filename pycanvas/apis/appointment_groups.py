"""AppointmentGroups API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AppointmentGroupsAPI(BaseCanvasAPI):
    """AppointmentGroups API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AppointmentGroupsAPI."""
        super(AppointmentGroupsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AppointmentGroupsAPI")

    def list_appointment_groups(self, context_codes=None, include=None, include_past_appointments=None, scope=None):
        """
        List appointment groups.

        Retrieve the list of appointment groups that can be reserved or managed by
        the current user.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - scope
        """Defaults to "reservable""""
        if scope is not None:
            self._validate_enum(scope, ["reservable", "manageable"])
            params["scope"] = scope

        # OPTIONAL - context_codes
        """Array of context codes used to limit returned results."""
        if context_codes is not None:
            params["context_codes"] = context_codes

        # OPTIONAL - include_past_appointments
        """Defaults to false. If true, includes past appointment groups"""
        if include_past_appointments is not None:
            params["include_past_appointments"] = include_past_appointments

        # OPTIONAL - include
        """Array of additional information to include.
        
        "appointments":: calendar event time slots for this appointment group
        "child_events":: reservations of those time slots
        "participant_count":: number of reservations
        "reserved_times":: the event id, start time and end time of reservations
                           the current user has made)
        "all_context_codes":: all context codes associated with this appointment group"""
        if include is not None:
            self._validate_enum(include, ["appointments", "child_events", "participant_count", "reserved_times", "all_context_codes"])
            params["include"] = include

        self.logger.debug("GET /api/v1/appointment_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/appointment_groups".format(**path), data=data, params=params, no_data=True)

    def create_appointment_group(self, appointment_group_title, appointment_group_context_codes, appointment_group_description=None, appointment_group_location_address=None, appointment_group_location_name=None, appointment_group_max_appointments_per_participant=None, appointment_group_min_appointments_per_participant=None, appointment_group_new_appointments_X=None, appointment_group_participant_visibility=None, appointment_group_participants_per_appointment=None, appointment_group_publish=None, appointment_group_sub_context_codes=None):
        """
        Create an appointment group.

        Create and return a new appointment group. If new_appointments are
        specified, the response will return a new_appointments array (same format
        as appointments array, see "List appointment groups" action)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - appointment_group[context_codes]
        """Array of context codes (courses, e.g. course_1) this group should be
        linked to (1 or more). Users in the course(s) with appropriate permissions
        will be able to sign up for this appointment group."""
        data["appointment_group[context_codes]"] = appointment_group_context_codes

        # OPTIONAL - appointment_group[sub_context_codes]
        """Array of sub context codes (course sections or a single group category)
        this group should be linked to. Used to limit the appointment group to
        particular sections. If a group category is specified, students will sign
        up in groups and the participant_type will be "Group" instead of "User"."""
        if appointment_group_sub_context_codes is not None:
            data["appointment_group[sub_context_codes]"] = appointment_group_sub_context_codes

        # REQUIRED - appointment_group[title]
        """Short title for the appointment group."""
        data["appointment_group[title]"] = appointment_group_title

        # OPTIONAL - appointment_group[description]
        """Longer text description of the appointment group."""
        if appointment_group_description is not None:
            data["appointment_group[description]"] = appointment_group_description

        # OPTIONAL - appointment_group[location_name]
        """Location name of the appointment group."""
        if appointment_group_location_name is not None:
            data["appointment_group[location_name]"] = appointment_group_location_name

        # OPTIONAL - appointment_group[location_address]
        """Location address."""
        if appointment_group_location_address is not None:
            data["appointment_group[location_address]"] = appointment_group_location_address

        # OPTIONAL - appointment_group[publish]
        """Indicates whether this appointment group should be published (i.e. made
        available for signup). Once published, an appointment group cannot be
        unpublished. Defaults to false."""
        if appointment_group_publish is not None:
            data["appointment_group[publish]"] = appointment_group_publish

        # OPTIONAL - appointment_group[participants_per_appointment]
        """Maximum number of participants that may register for each time slot.
        Defaults to null (no limit)."""
        if appointment_group_participants_per_appointment is not None:
            data["appointment_group[participants_per_appointment]"] = appointment_group_participants_per_appointment

        # OPTIONAL - appointment_group[min_appointments_per_participant]
        """Minimum number of time slots a user must register for. If not set, users
        do not need to sign up for any time slots."""
        if appointment_group_min_appointments_per_participant is not None:
            data["appointment_group[min_appointments_per_participant]"] = appointment_group_min_appointments_per_participant

        # OPTIONAL - appointment_group[max_appointments_per_participant]
        """Maximum number of time slots a user may register for."""
        if appointment_group_max_appointments_per_participant is not None:
            data["appointment_group[max_appointments_per_participant]"] = appointment_group_max_appointments_per_participant

        # OPTIONAL - appointment_group[new_appointments][X]
        """Nested array of start time/end time pairs indicating time slots for this
        appointment group. Refer to the example request."""
        if appointment_group_new_appointments_X is not None:
            data["appointment_group[new_appointments][X]"] = appointment_group_new_appointments_X

        # OPTIONAL - appointment_group[participant_visibility]
        """"private":: participants cannot see who has signed up for a particular
                    time slot
        "protected":: participants can see who has signed up.  Defaults to
                      "private"."""
        if appointment_group_participant_visibility is not None:
            self._validate_enum(appointment_group_participant_visibility, ["private", "protected"])
            data["appointment_group[participant_visibility]"] = appointment_group_participant_visibility

        self.logger.debug("POST /api/v1/appointment_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/appointment_groups".format(**path), data=data, params=params, no_data=True)

    def get_single_appointment_group(self, id, include=None):
        """
        Get a single appointment group.

        Returns information for a single appointment group
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Array of additional information to include. See include[] argument of
        "List appointment groups" action.
        
        "child_events":: reservations of time slots time slots
        "appointments":: will always be returned
        "all_context_codes":: all context codes associated with this appointment group"""
        if include is not None:
            self._validate_enum(include, ["child_events", "appointments", "all_context_codes"])
            params["include"] = include

        self.logger.debug("GET /api/v1/appointment_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/appointment_groups/{id}".format(**path), data=data, params=params, no_data=True)

    def update_appointment_group(self, id, appointment_group_context_codes, appointment_group_description=None, appointment_group_location_address=None, appointment_group_location_name=None, appointment_group_max_appointments_per_participant=None, appointment_group_min_appointments_per_participant=None, appointment_group_new_appointments_X=None, appointment_group_participant_visibility=None, appointment_group_participants_per_appointment=None, appointment_group_publish=None, appointment_group_sub_context_codes=None, appointment_group_title=None):
        """
        Update an appointment group.

        Update and return an appointment group. If new_appointments are specified,
        the response will return a new_appointments array (same format as
        appointments array, see "List appointment groups" action).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - appointment_group[context_codes]
        """Array of context codes (courses, e.g. course_1) this group should be
        linked to (1 or more). Users in the course(s) with appropriate permissions
        will be able to sign up for this appointment group."""
        data["appointment_group[context_codes]"] = appointment_group_context_codes

        # OPTIONAL - appointment_group[sub_context_codes]
        """Array of sub context codes (course sections or a single group category)
        this group should be linked to. Used to limit the appointment group to
        particular sections. If a group category is specified, students will sign
        up in groups and the participant_type will be "Group" instead of "User"."""
        if appointment_group_sub_context_codes is not None:
            data["appointment_group[sub_context_codes]"] = appointment_group_sub_context_codes

        # OPTIONAL - appointment_group[title]
        """Short title for the appointment group."""
        if appointment_group_title is not None:
            data["appointment_group[title]"] = appointment_group_title

        # OPTIONAL - appointment_group[description]
        """Longer text description of the appointment group."""
        if appointment_group_description is not None:
            data["appointment_group[description]"] = appointment_group_description

        # OPTIONAL - appointment_group[location_name]
        """Location name of the appointment group."""
        if appointment_group_location_name is not None:
            data["appointment_group[location_name]"] = appointment_group_location_name

        # OPTIONAL - appointment_group[location_address]
        """Location address."""
        if appointment_group_location_address is not None:
            data["appointment_group[location_address]"] = appointment_group_location_address

        # OPTIONAL - appointment_group[publish]
        """Indicates whether this appointment group should be published (i.e. made
        available for signup). Once published, an appointment group cannot be
        unpublished. Defaults to false."""
        if appointment_group_publish is not None:
            data["appointment_group[publish]"] = appointment_group_publish

        # OPTIONAL - appointment_group[participants_per_appointment]
        """Maximum number of participants that may register for each time slot.
        Defaults to null (no limit)."""
        if appointment_group_participants_per_appointment is not None:
            data["appointment_group[participants_per_appointment]"] = appointment_group_participants_per_appointment

        # OPTIONAL - appointment_group[min_appointments_per_participant]
        """Minimum number of time slots a user must register for. If not set, users
        do not need to sign up for any time slots."""
        if appointment_group_min_appointments_per_participant is not None:
            data["appointment_group[min_appointments_per_participant]"] = appointment_group_min_appointments_per_participant

        # OPTIONAL - appointment_group[max_appointments_per_participant]
        """Maximum number of time slots a user may register for."""
        if appointment_group_max_appointments_per_participant is not None:
            data["appointment_group[max_appointments_per_participant]"] = appointment_group_max_appointments_per_participant

        # OPTIONAL - appointment_group[new_appointments][X]
        """Nested array of start time/end time pairs indicating time slots for this
        appointment group. Refer to the example request."""
        if appointment_group_new_appointments_X is not None:
            data["appointment_group[new_appointments][X]"] = appointment_group_new_appointments_X

        # OPTIONAL - appointment_group[participant_visibility]
        """"private":: participants cannot see who has signed up for a particular
                    time slot
        "protected":: participants can see who has signed up. Defaults to "private"."""
        if appointment_group_participant_visibility is not None:
            self._validate_enum(appointment_group_participant_visibility, ["private", "protected"])
            data["appointment_group[participant_visibility]"] = appointment_group_participant_visibility

        self.logger.debug("PUT /api/v1/appointment_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/appointment_groups/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_appointment_group(self, id, cancel_reason=None):
        """
        Delete an appointment group.

        Delete an appointment group (and associated time slots and reservations)
        and return the deleted group
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - cancel_reason
        """Reason for deleting/canceling the appointment group."""
        if cancel_reason is not None:
            params["cancel_reason"] = cancel_reason

        self.logger.debug("DELETE /api/v1/appointment_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/appointment_groups/{id}".format(**path), data=data, params=params, no_data=True)

    def list_user_participants(self, id, registration_status=None):
        """
        List user participants.

        List users that are (or may be) participating in this appointment group.
        Refer to the Users API for the response fields. Returns no results for
        appointment groups with the "Group" participant_type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - registration_status
        """Limits results to the a given participation status, defaults to "all""""
        if registration_status is not None:
            self._validate_enum(registration_status, ["all", "registered", "registered"])
            params["registration_status"] = registration_status

        self.logger.debug("GET /api/v1/appointment_groups/{id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/appointment_groups/{id}/users".format(**path), data=data, params=params, no_data=True)

    def list_student_group_participants(self, id, registration_status=None):
        """
        List student group participants.

        List student groups that are (or may be) participating in this appointment
        group. Refer to the Groups API for the response fields. Returns no results
        for appointment groups with the "User" participant_type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - registration_status
        """Limits results to the a given participation status, defaults to "all""""
        if registration_status is not None:
            self._validate_enum(registration_status, ["all", "registered", "registered"])
            params["registration_status"] = registration_status

        self.logger.debug("GET /api/v1/appointment_groups/{id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/appointment_groups/{id}/groups".format(**path), data=data, params=params, no_data=True)

    def get_next_appointment(self, appointment_group_ids=None):
        """
        Get next appointment.

        Return the next appointment available to sign up for. The appointment
        is returned in a one-element array. If no future appointments are
        available, an empty array is returned.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - appointment_group_ids
        """List of ids of appointment groups to search."""
        if appointment_group_ids is not None:
            params["appointment_group_ids"] = appointment_group_ids

        self.logger.debug("GET /api/v1/appointment_groups/next_appointment with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/appointment_groups/next_appointment".format(**path), data=data, params=params, all_pages=True)


class Appointmentgroup(BaseModel):
    """Appointmentgroup Model."""

    def __init__(self, participant_visibility=None, updated_at=None, context_codes=None, participant_type=None, end_at=None, id=None, participants_per_appointment=None, title=None, new_appointments=None, min_appointments_per_participant=None, appointments_count=None, start_at=None, description=None, participant_count=None, workflow_state=None, html_url=None, location_address=None, appointments=None, reserved_times=None, location_name=None, max_appointments_per_participant=None, url=None, created_at=None, sub_context_codes=None, requiring_action=None):
        """Init method for Appointmentgroup class."""
        self._participant_visibility = participant_visibility
        self._updated_at = updated_at
        self._context_codes = context_codes
        self._participant_type = participant_type
        self._end_at = end_at
        self._id = id
        self._participants_per_appointment = participants_per_appointment
        self._title = title
        self._new_appointments = new_appointments
        self._min_appointments_per_participant = min_appointments_per_participant
        self._appointments_count = appointments_count
        self._start_at = start_at
        self._description = description
        self._participant_count = participant_count
        self._workflow_state = workflow_state
        self._html_url = html_url
        self._location_address = location_address
        self._appointments = appointments
        self._reserved_times = reserved_times
        self._location_name = location_name
        self._max_appointments_per_participant = max_appointments_per_participant
        self._url = url
        self._created_at = created_at
        self._sub_context_codes = sub_context_codes
        self._requiring_action = requiring_action

        self.logger = logging.getLogger('pycanvas.Appointmentgroup')

    @property
    def participant_visibility(self):
        """'private' means participants cannot see who has signed up for a particular time slot, 'protected' means that they can."""
        return self._participant_visibility

    @participant_visibility.setter
    def participant_visibility(self, value):
        """Setter for participant_visibility property."""
        self.logger.warn("Setting values on participant_visibility will NOT update the remote Canvas instance.")
        self._participant_visibility = value

    @property
    def updated_at(self):
        """When the appointment group was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def context_codes(self):
        """The context codes (i.e. courses) this appointment group belongs to. Only people in these courses will be eligible to sign up."""
        return self._context_codes

    @context_codes.setter
    def context_codes(self, value):
        """Setter for context_codes property."""
        self.logger.warn("Setting values on context_codes will NOT update the remote Canvas instance.")
        self._context_codes = value

    @property
    def participant_type(self):
        """Indicates how participants sign up for the appointment group, either as individuals ('User') or in student groups ('Group'). Related to sub_context_codes (i.e. 'Group' signups always have a single group category)."""
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        """Setter for participant_type property."""
        self.logger.warn("Setting values on participant_type will NOT update the remote Canvas instance.")
        self._participant_type = value

    @property
    def end_at(self):
        """The end of the last time slot in the appointment group."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def id(self):
        """The ID of the appointment group."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def participants_per_appointment(self):
        """Maximum number of participants that may register for each time slot, or null if no limit."""
        return self._participants_per_appointment

    @participants_per_appointment.setter
    def participants_per_appointment(self, value):
        """Setter for participants_per_appointment property."""
        self.logger.warn("Setting values on participants_per_appointment will NOT update the remote Canvas instance.")
        self._participants_per_appointment = value

    @property
    def title(self):
        """The title of the appointment group."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def new_appointments(self):
        """Newly created time slots (same format as appointments above). Only returned in Create/Update responses where new time slots have been added."""
        return self._new_appointments

    @new_appointments.setter
    def new_appointments(self, value):
        """Setter for new_appointments property."""
        self.logger.warn("Setting values on new_appointments will NOT update the remote Canvas instance.")
        self._new_appointments = value

    @property
    def min_appointments_per_participant(self):
        """Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots."""
        return self._min_appointments_per_participant

    @min_appointments_per_participant.setter
    def min_appointments_per_participant(self, value):
        """Setter for min_appointments_per_participant property."""
        self.logger.warn("Setting values on min_appointments_per_participant will NOT update the remote Canvas instance.")
        self._min_appointments_per_participant = value

    @property
    def appointments_count(self):
        """Number of time slots in this appointment group."""
        return self._appointments_count

    @appointments_count.setter
    def appointments_count(self, value):
        """Setter for appointments_count property."""
        self.logger.warn("Setting values on appointments_count will NOT update the remote Canvas instance.")
        self._appointments_count = value

    @property
    def start_at(self):
        """The start of the first time slot in the appointment group."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def description(self):
        """The text description of the appointment group."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def participant_count(self):
        """The number of participant who have reserved slots (see include[] argument)."""
        return self._participant_count

    @participant_count.setter
    def participant_count(self, value):
        """Setter for participant_count property."""
        self.logger.warn("Setting values on participant_count will NOT update the remote Canvas instance.")
        self._participant_count = value

    @property
    def workflow_state(self):
        """Current state of the appointment group ('pending', 'active' or 'deleted'). 'pending' indicates that it has not been published yet and is invisible to participants."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def html_url(self):
        """URL for a user to view this appointment group."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def location_address(self):
        """The address of the appointment group's location."""
        return self._location_address

    @location_address.setter
    def location_address(self, value):
        """Setter for location_address property."""
        self.logger.warn("Setting values on location_address will NOT update the remote Canvas instance.")
        self._location_address = value

    @property
    def appointments(self):
        """Calendar Events representing the time slots (see include[] argument) Refer to the Calendar Events API for more information."""
        return self._appointments

    @appointments.setter
    def appointments(self, value):
        """Setter for appointments property."""
        self.logger.warn("Setting values on appointments will NOT update the remote Canvas instance.")
        self._appointments = value

    @property
    def reserved_times(self):
        """The start and end times of slots reserved by the current user as well as the id of the calendar event for the reservation (see include[] argument)."""
        return self._reserved_times

    @reserved_times.setter
    def reserved_times(self, value):
        """Setter for reserved_times property."""
        self.logger.warn("Setting values on reserved_times will NOT update the remote Canvas instance.")
        self._reserved_times = value

    @property
    def location_name(self):
        """The location name of the appointment group."""
        return self._location_name

    @location_name.setter
    def location_name(self, value):
        """Setter for location_name property."""
        self.logger.warn("Setting values on location_name will NOT update the remote Canvas instance.")
        self._location_name = value

    @property
    def max_appointments_per_participant(self):
        """Maximum number of time slots a user may register for, or null if no limit."""
        return self._max_appointments_per_participant

    @max_appointments_per_participant.setter
    def max_appointments_per_participant(self, value):
        """Setter for max_appointments_per_participant property."""
        self.logger.warn("Setting values on max_appointments_per_participant will NOT update the remote Canvas instance.")
        self._max_appointments_per_participant = value

    @property
    def url(self):
        """URL for this appointment group (to update, delete, etc.)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """When the appointment group was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def sub_context_codes(self):
        """The sub-context codes (i.e. course sections and group categories) this appointment group is restricted to."""
        return self._sub_context_codes

    @sub_context_codes.setter
    def sub_context_codes(self, value):
        """Setter for sub_context_codes property."""
        self.logger.warn("Setting values on sub_context_codes will NOT update the remote Canvas instance.")
        self._sub_context_codes = value

    @property
    def requiring_action(self):
        """Boolean indicating whether the current user needs to sign up for this appointment group (i.e. it's reservable and the min_appointments_per_participant limit has not been met by this user)."""
        return self._requiring_action

    @requiring_action.setter
    def requiring_action(self, value):
        """Setter for requiring_action property."""
        self.logger.warn("Setting values on requiring_action will NOT update the remote Canvas instance.")
        self._requiring_action = value


class Appointment(BaseModel):
    """Appointment Model.
    Date and time for an appointment"""

    def __init__(self, start_at=None, id=None, end_at=None):
        """Init method for Appointment class."""
        self._start_at = start_at
        self._id = id
        self._end_at = end_at

        self.logger = logging.getLogger('pycanvas.Appointment')

    @property
    def start_at(self):
        """Start time for the appointment."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def id(self):
        """The appointment identifier."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def end_at(self):
        """End time for the appointment."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

