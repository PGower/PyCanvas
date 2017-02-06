"""CommMessages API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CommMessagesAPI(BaseCanvasAPI):
    """CommMessages API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CommMessagesAPI."""
        super(CommMessagesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CommMessagesAPI")

    def list_of_commmessages_for_user(self, user_id, end_time=None, start_time=None):
        """
        List of CommMessages for a user.

        Retrieve messages sent to a user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - user_id
        """The user id for whom you want to retrieve CommMessages"""
        params["user_id"] = user_id

        # OPTIONAL - start_time
        """The beginning of the time range you want to retrieve message from."""
        if start_time is not None:
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """The end of the time range you want to retrieve messages for."""
        if end_time is not None:
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/comm_messages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/comm_messages".format(**path), data=data, params=params, all_pages=True)


class Commmessage(BaseModel):
    """Commmessage Model."""

    def __init__(self, body=None, from=None, sent_at=None, workflow_state=None, created_at=None, to=None, reply_to=None, html_body=None, id=None, subject=None):
        """Init method for Commmessage class."""
        self._body = body
        self._from = from
        self._sent_at = sent_at
        self._workflow_state = workflow_state
        self._created_at = created_at
        self._to = to
        self._reply_to = reply_to
        self._html_body = html_body
        self._id = id
        self._subject = subject

        self.logger = logging.getLogger('pycanvas.Commmessage')

    @property
    def body(self):
        """The plain text body of the message."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def from(self):
        """The address that was put in the 'from' field of the message."""
        return self._from

    @from.setter
    def from(self, value):
        """Setter for from property."""
        self.logger.warn("Setting values on from will NOT update the remote Canvas instance.")
        self._from = value

    @property
    def sent_at(self):
        """The date and time this message was sent."""
        return self._sent_at

    @sent_at.setter
    def sent_at(self, value):
        """Setter for sent_at property."""
        self.logger.warn("Setting values on sent_at will NOT update the remote Canvas instance.")
        self._sent_at = value

    @property
    def workflow_state(self):
        """The workflow state of the message. One of 'created', 'staged', 'sending', 'sent', 'bounced', 'dashboard', 'cancelled', or 'closed'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def created_at(self):
        """The date and time this message was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def to(self):
        """The address the message was sent to:."""
        return self._to

    @to.setter
    def to(self, value):
        """Setter for to property."""
        self.logger.warn("Setting values on to will NOT update the remote Canvas instance.")
        self._to = value

    @property
    def reply_to(self):
        """The reply_to header of the message."""
        return self._reply_to

    @reply_to.setter
    def reply_to(self, value):
        """Setter for reply_to property."""
        self.logger.warn("Setting values on reply_to will NOT update the remote Canvas instance.")
        self._reply_to = value

    @property
    def html_body(self):
        """The HTML body of the message."""
        return self._html_body

    @html_body.setter
    def html_body(self, value):
        """Setter for html_body property."""
        self.logger.warn("Setting values on html_body will NOT update the remote Canvas instance.")
        self._html_body = value

    @property
    def id(self):
        """The ID of the CommMessage."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def subject(self):
        """The message subject."""
        return self._subject

    @subject.setter
    def subject(self, value):
        """Setter for subject property."""
        self.logger.warn("Setting values on subject will NOT update the remote Canvas instance.")
        self._subject = value

