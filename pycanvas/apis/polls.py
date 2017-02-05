"""Polls API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class PollsAPI(BaseCanvasAPI):
    """Polls API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PollsAPI."""
        super(PollsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.PollsAPI")

    def list_polls(self):
        """
        List polls.

        Returns the list of polls for the current user.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/polls with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls".format(**path), data=data, params=params, no_data=True)

    def get_single_poll(self, id):
        """
        Get a single poll.

        Returns the poll with the given id
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/polls/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{id}".format(**path), data=data, params=params, no_data=True)

    def create_single_poll(self, polls_question, polls_description=None):
        """
        Create a single poll.

        Create a new poll for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - polls[question]
        """The title of the poll."""
        data["polls[question]"] = polls_question
        # OPTIONAL - polls[description]
        """A brief description or instructions for the poll."""
        if polls_description is not None:
            data["polls[description]"] = polls_description

        self.logger.debug("POST /api/v1/polls with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/polls".format(**path), data=data, params=params, no_data=True)

    def update_single_poll(self, id, polls_question, polls_description=None):
        """
        Update a single poll.

        Update an existing poll belonging to the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # REQUIRED - polls[question]
        """The title of the poll."""
        data["polls[question]"] = polls_question
        # OPTIONAL - polls[description]
        """A brief description or instructions for the poll."""
        if polls_description is not None:
            data["polls[description]"] = polls_description

        self.logger.debug("PUT /api/v1/polls/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/polls/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_poll(self, id):
        """
        Delete a poll.

        <b>204 No Content</b> response code is returned if the deletion was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/polls/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/polls/{id}".format(**path), data=data, params=params, no_data=True)


class Poll(BaseModel):
    """Poll Model."""

    def __init__(self, id, question, user_id=None, description=None, total_results=None, created_at=None):
        """Init method for Poll class."""
        self._user_id = user_id
        self._description = description
        self._total_results = total_results
        self._created_at = created_at
        self._question = question
        self._id = id

        self.logger = logging.getLogger('pycanvas.Poll')

    @property
    def user_id(self):
        """The unique identifier for the user that created the poll."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def description(self):
        """A short description of the poll."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def total_results(self):
        """An aggregate of the results of all associated poll sessions, with the poll choice id as the key, and the aggregated submission count as the value."""
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        """Setter for total_results property."""
        self.logger.warn("Setting values on total_results will NOT update the remote Canvas instance.")
        self._total_results = value

    @property
    def created_at(self):
        """The time at which the poll was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def question(self):
        """The question/title of the poll."""
        return self._question

    @question.setter
    def question(self, value):
        """Setter for question property."""
        self.logger.warn("Setting values on question will NOT update the remote Canvas instance.")
        self._question = value

    @property
    def id(self):
        """The unique identifier for the poll."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

