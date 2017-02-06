"""AuthenticationsLog API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AuthenticationsLogAPI(BaseCanvasAPI):
    """AuthenticationsLog API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AuthenticationsLogAPI."""
        super(AuthenticationsLogAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AuthenticationsLogAPI")

    def query_by_login(self, login_id, end_time=None, start_time=None):
        """
        Query by login.

        List authentication events for a given login.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - login_id
        """ID"""
        path["login_id"] = login_id

        # OPTIONAL - start_time
        """The beginning of the time range from which you want events."""
        if start_time is not None:
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """The end of the time range from which you want events."""
        if end_time is not None:
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/audit/authentication/logins/{login_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/audit/authentication/logins/{login_id}".format(**path), data=data, params=params, no_data=True)

    def query_by_account(self, account_id, end_time=None, start_time=None):
        """
        Query by account.

        List authentication events for a given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - start_time
        """The beginning of the time range from which you want events."""
        if start_time is not None:
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """The end of the time range from which you want events."""
        if end_time is not None:
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/audit/authentication/accounts/{account_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/audit/authentication/accounts/{account_id}".format(**path), data=data, params=params, no_data=True)

    def query_by_user(self, user_id, end_time=None, start_time=None):
        """
        Query by user.

        List authentication events for a given user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - start_time
        """The beginning of the time range from which you want events."""
        if start_time is not None:
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """The end of the time range from which you want events."""
        if end_time is not None:
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/audit/authentication/users/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/audit/authentication/users/{user_id}".format(**path), data=data, params=params, no_data=True)


class Authenticationevent(BaseModel):
    """Authenticationevent Model."""

    def __init__(self, pseudonym_id=None, created_at=None, user_id=None, event_type=None, account_id=None):
        """Init method for Authenticationevent class."""
        self._pseudonym_id = pseudonym_id
        self._created_at = created_at
        self._user_id = user_id
        self._event_type = event_type
        self._account_id = account_id

        self.logger = logging.getLogger('pycanvas.Authenticationevent')

    @property
    def pseudonym_id(self):
        """ID of the pseudonym (login) associated with the event."""
        return self._pseudonym_id

    @pseudonym_id.setter
    def pseudonym_id(self, value):
        """Setter for pseudonym_id property."""
        self.logger.warn("Setting values on pseudonym_id will NOT update the remote Canvas instance.")
        self._pseudonym_id = value

    @property
    def created_at(self):
        """timestamp of the event."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def user_id(self):
        """ID of the user associated with the event will match the user_id in the associated pseudonym."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def event_type(self):
        """authentication event type ('login' or 'logout')."""
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """Setter for event_type property."""
        self.logger.warn("Setting values on event_type will NOT update the remote Canvas instance.")
        self._event_type = value

    @property
    def account_id(self):
        """ID of the account associated with the event. will match the account_id in the associated pseudonym."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn("Setting values on account_id will NOT update the remote Canvas instance.")
        self._account_id = value

