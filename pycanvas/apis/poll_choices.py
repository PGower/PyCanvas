"""PollChoices API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class PollChoicesAPI(BaseCanvasAPI):
    """PollChoices API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PollChoicesAPI."""
        super(PollChoicesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.PollChoicesAPI")

    def list_poll_choices_in_poll(self, poll_id):
        """
        List poll choices in a poll.

        Returns the list of PollChoices in this poll.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_choices with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_choices".format(**path), data=data, params=params, no_data=True)

    def get_single_poll_choice(self, id, poll_id):
        """
        Get a single poll choice.

        Returns the poll choice with the given id
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

        self.logger.debug("GET /api/v1/polls/{poll_id}/poll_choices/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/polls/{poll_id}/poll_choices/{id}".format(**path), data=data, params=params, no_data=True)

    def create_single_poll_choice(self, poll_id, poll_choices_text, poll_choices_is_correct=None, poll_choices_position=None):
        """
        Create a single poll choice.

        Create a new poll choice for this poll
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - poll_id
        """ID"""
        path["poll_id"] = poll_id
        # REQUIRED - poll_choices[text]
        """The descriptive text of the poll choice."""
        data["poll_choices[text]"] = poll_choices_text
        # OPTIONAL - poll_choices[is_correct]
        """Whether this poll choice is considered correct or not. Defaults to false."""
        if poll_choices_is_correct is not None:
            data["poll_choices[is_correct]"] = poll_choices_is_correct
        # OPTIONAL - poll_choices[position]
        """The order this poll choice should be returned in the context it's sibling poll choices."""
        if poll_choices_position is not None:
            data["poll_choices[position]"] = poll_choices_position

        self.logger.debug("POST /api/v1/polls/{poll_id}/poll_choices with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/polls/{poll_id}/poll_choices".format(**path), data=data, params=params, no_data=True)

    def update_single_poll_choice(self, id, poll_id, poll_choices_text, poll_choices_is_correct=None, poll_choices_position=None):
        """
        Update a single poll choice.

        Update an existing poll choice for this poll
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
        # REQUIRED - poll_choices[text]
        """The descriptive text of the poll choice."""
        data["poll_choices[text]"] = poll_choices_text
        # OPTIONAL - poll_choices[is_correct]
        """Whether this poll choice is considered correct or not.  Defaults to false."""
        if poll_choices_is_correct is not None:
            data["poll_choices[is_correct]"] = poll_choices_is_correct
        # OPTIONAL - poll_choices[position]
        """The order this poll choice should be returned in the context it's sibling poll choices."""
        if poll_choices_position is not None:
            data["poll_choices[position]"] = poll_choices_position

        self.logger.debug("PUT /api/v1/polls/{poll_id}/poll_choices/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/polls/{poll_id}/poll_choices/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_poll_choice(self, id, poll_id):
        """
        Delete a poll choice.

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

        self.logger.debug("DELETE /api/v1/polls/{poll_id}/poll_choices/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/polls/{poll_id}/poll_choices/{id}".format(**path), data=data, params=params, no_data=True)


class Pollchoice(BaseModel):
    """Pollchoice Model."""

    def __init__(self, id, poll_id, text, is_correct=None, position=None):
        """Init method for Pollchoice class."""
        self._is_correct = is_correct
        self._position = position
        self._id = id
        self._poll_id = poll_id
        self._text = text

        self.logger = logging.getLogger('pycanvas.Pollchoice')

    @property
    def is_correct(self):
        """Specifies whether or not this poll choice is a 'correct' choice."""
        return self._is_correct

    @is_correct.setter
    def is_correct(self, value):
        """Setter for is_correct property."""
        self.logger.warn("Setting values on is_correct will NOT update the remote Canvas instance.")
        self._is_correct = value

    @property
    def position(self):
        """The order of the poll choice in relation to it's sibling poll choices."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def id(self):
        """The unique identifier for the poll choice."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def poll_id(self):
        """The id of the poll this poll choice belongs to."""
        return self._poll_id

    @poll_id.setter
    def poll_id(self, value):
        """Setter for poll_id property."""
        self.logger.warn("Setting values on poll_id will NOT update the remote Canvas instance.")
        self._poll_id = value

    @property
    def text(self):
        """The text of the poll choice."""
        return self._text

    @text.setter
    def text(self, value):
        """Setter for text property."""
        self.logger.warn("Setting values on text will NOT update the remote Canvas instance.")
        self._text = value

