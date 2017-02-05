"""PollSubmissions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class PollSubmissionsAPI(BaseCanvasAPI):
    """PollSubmissions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PollSubmissionsAPI."""
        super(PollSubmissionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.PollSubmissionsAPI")

    def get_single_poll_submission(self, id, poll_id, poll_session_id):
        """
        Get a single poll submission.

        Returns the poll submission with the given id
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - poll_session_id
        """ID"""
        path["poll_session_id"] = poll_session_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id}".format(**path), data=data, params=params, no_data=True)

    def create_single_poll_submission(self, poll_id, poll_session_id, poll_submissions_poll_choice_id):
        """
        Create a single poll submission.

        Create a new poll submission for this poll session
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - PATH - poll_session_id
        """ID"""
        path["poll_session_id"] = poll_session_id
        # REQUIRED - poll_submissions[poll_choice_id]
        """The chosen poll choice for this submission."""
        data["poll_submissions[poll_choice_id]"] = poll_submissions_poll_choice_id

        self.logger.debug("POST /api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions".format(**path), data=data, params=params, no_data=True)


class Pollsubmission(BaseModel):
    """Pollsubmission Model."""

    def __init__(self, id, poll_choice, created_at=None, user_id=None, poll_choice_id=None):
        """Init method for Pollsubmission class."""
        self._created_at = created_at
        self._user_id = user_id
        self._id = id
        self._poll_choice_id = poll_choice_id

        self.logger = logging.getLogger('pycanvas.Pollsubmission')

    @property
    def created_at(self):
        """The date and time the poll submission was submitted."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def user_id(self):
        """the unique identifier of the user who submitted this poll submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def id(self):
        """The unique identifier for the poll submission."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def poll_choice_id(self):
        """The unique identifier of the poll choice chosen for this submission."""
        return self._poll_choice_id

    @poll_choice_id.setter
    def poll_choice_id(self, value):
        """Setter for poll_choice_id property."""
        self.logger.warn("Setting values on poll_choice_id will NOT update the remote Canvas instance.")
        self._poll_choice_id = value

