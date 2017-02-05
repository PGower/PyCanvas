"""PollSessions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class PollSessionsAPI(BaseCanvasAPI):
    """PollSessions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PollSessionsAPI."""
        super(PollSessionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.PollSessionsAPI")

    def list_poll_sessions_for_poll(self, poll_id):
        """
        List poll sessions for a poll.

        Returns the list of PollSessions in this poll.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_sessions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_sessions".format(**path), data=data, params=params, no_data=True)

    def get_results_for_single_poll_session(self, id, poll_id):
        """
        Get the results for a single poll session.

        Returns the poll session with the given id
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_sessions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_sessions/{id}".format(**path), data=data, params=params, no_data=True)

    def create_single_poll_session(self, poll_id, poll_sessions_course_id, poll_sessions_course_section_id=None, poll_sessions_has_public_results=None):
        """
        Create a single poll session.

        Create a new poll session for this poll
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - poll_sessions[course_id]
        """The id of the course this session is associated with."""
        data["poll_sessions[course_id]"] = poll_sessions_course_id
        # OPTIONAL - poll_sessions[course_section_id]
        """The id of the course section this session is associated with."""
        if poll_sessions_course_section_id is not None:
            data["poll_sessions[course_section_id]"] = poll_sessions_course_section_id
        # OPTIONAL - poll_sessions[has_public_results]
        """Whether or not results are viewable by students."""
        if poll_sessions_has_public_results is not None:
            data["poll_sessions[has_public_results]"] = poll_sessions_has_public_results

        self.logger.debug("POST /api/v1/polls/{poll_id}/poll_sessions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/polls/{poll_id}/poll_sessions".format(**path), data=data, params=params, no_data=True)

    def update_single_poll_session(self, id, poll_id, poll_sessions_course_id=None, poll_sessions_course_section_id=None, poll_sessions_has_public_results=None):
        """
        Update a single poll session.

        Update an existing poll session for this poll
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - poll_sessions[course_id]
        """The id of the course this session is associated with."""
        if poll_sessions_course_id is not None:
            data["poll_sessions[course_id]"] = poll_sessions_course_id
        # OPTIONAL - poll_sessions[course_section_id]
        """The id of the course section this session is associated with."""
        if poll_sessions_course_section_id is not None:
            data["poll_sessions[course_section_id]"] = poll_sessions_course_section_id
        # OPTIONAL - poll_sessions[has_public_results]
        """Whether or not results are viewable by students."""
        if poll_sessions_has_public_results is not None:
            data["poll_sessions[has_public_results]"] = poll_sessions_has_public_results

        self.logger.debug("PUT /api/v1/polls/{poll_id}/poll_sessions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/polls/{poll_id}/poll_sessions/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_poll_session(self, id, poll_id):
        """
        Delete a poll session.

        <b>204 No Content</b> response code is returned if the deletion was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/polls/{poll_id}/poll_sessions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/polls/{poll_id}/poll_sessions/{id}".format(**path), data=data, params=params, no_data=True)

    def open_poll_session(self, id, poll_id):
        """
        Open a poll session.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_sessions/{id}/open with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_sessions/{id}/open".format(**path), data=data, params=params, no_data=True)

    def close_opened_poll_session(self, id, poll_id):
        """
        Close an opened poll session.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_sessions/{id}/close with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_sessions/{id}/close".format(**path), data=data, params=params, no_data=True)

    def list_opened_poll_sessions(self):
        """
        List opened poll sessions.

        Lists all opened poll sessions available to the current user.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/poll_sessions/opened with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/poll_sessions/opened".format(**path), data=data, params=params, no_data=True)

    def list_closed_poll_sessions(self):
        """
        List closed poll sessions.

        Lists all closed poll sessions available to the current user.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/poll_sessions/closed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/poll_sessions/closed".format(**path), data=data, params=params, no_data=True)


class Pollsession(BaseModel):
    """Pollsession Model."""

    def __init__(self, id, poll_id, course_id, poll_submissions=None, created_at=None, course_section_id=None, has_public_results=None, results=None, is_published=None):
        """Init method for Pollsession class."""
        self._poll_submissions = poll_submissions
        self._created_at = created_at
        self._course_section_id = course_section_id
        self._has_public_results = has_public_results
        self._poll_id = poll_id
        self._results = results
        self._course_id = course_id
        self._id = id
        self._is_published = is_published

        self.logger = logging.getLogger('pycanvas.Pollsession')

    @property
    def poll_submissions(self):
        """If the poll session has public results, this will return an array of all submissions, viewable by both students and teachers. If the results are not public, for students it will return their submission only."""
        return self._poll_submissions

    @poll_submissions.setter
    def poll_submissions(self, value):
        """Setter for poll_submissions property."""
        self.logger.warn("Setting values on poll_submissions will NOT update the remote Canvas instance.")
        self._poll_submissions = value

    @property
    def created_at(self):
        """The time at which the poll session was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def course_section_id(self):
        """The id of the Course Section this poll session is associated with."""
        return self._course_section_id

    @course_section_id.setter
    def course_section_id(self, value):
        """Setter for course_section_id property."""
        self.logger.warn("Setting values on course_section_id will NOT update the remote Canvas instance.")
        self._course_section_id = value

    @property
    def has_public_results(self):
        """Specifies whether the results are viewable by students."""
        return self._has_public_results

    @has_public_results.setter
    def has_public_results(self, value):
        """Setter for has_public_results property."""
        self.logger.warn("Setting values on has_public_results will NOT update the remote Canvas instance.")
        self._has_public_results = value

    @property
    def poll_id(self):
        """The id of the Poll this poll session is associated with."""
        return self._poll_id

    @poll_id.setter
    def poll_id(self, value):
        """Setter for poll_id property."""
        self.logger.warn("Setting values on poll_id will NOT update the remote Canvas instance.")
        self._poll_id = value

    @property
    def results(self):
        """The results of the submissions of the poll. Each key is the poll choice id, and the value is the count of submissions."""
        return self._results

    @results.setter
    def results(self, value):
        """Setter for results property."""
        self.logger.warn("Setting values on results will NOT update the remote Canvas instance.")
        self._results = value

    @property
    def course_id(self):
        """The id of the Course this poll session is associated with."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def id(self):
        """The unique identifier for the poll session."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def is_published(self):
        """Specifies whether or not this poll session has been published for students to participate in."""
        return self._is_published

    @is_published.setter
    def is_published(self, value):
        """Setter for is_published property."""
        self.logger.warn("Setting values on is_published will NOT update the remote Canvas instance.")
        self._is_published = value

