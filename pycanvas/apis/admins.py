"""Admins API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AdminsAPI(BaseCanvasAPI):
    """Admins API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AdminsAPI."""
        super(AdminsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AdminsAPI")

    def make_account_admin(self, user_id, account_id, role=None, role_id=None, send_confirmation=None):
        """
        Make an account admin.

        Flag an existing user as an admin within the account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - user_id
        """The id of the user to promote."""
        data["user_id"] = user_id
        # OPTIONAL - role
        """(deprecated)
        The user's admin relationship with the account will be created with the
        given role. Defaults to 'AccountAdmin'."""
        if role is not None:
            data["role"] = role
        # OPTIONAL - role_id
        """The user's admin relationship with the account will be created with the
        given role. Defaults to the built-in role for 'AccountAdmin'."""
        if role_id is not None:
            data["role_id"] = role_id
        # OPTIONAL - send_confirmation
        """Send a notification email to
        the new admin if true. Default is true."""
        if send_confirmation is not None:
            data["send_confirmation"] = send_confirmation

        self.logger.debug("POST /api/v1/accounts/{account_id}/admins with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/admins".format(**path), data=data, params=params, single_item=True)

    def remove_account_admin(self, user_id, account_id, role=None, role_id=None):
        """
        Remove account admin.

        Remove the rights associated with an account admin role from a user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # OPTIONAL - role
        """(Deprecated)
        Account role to remove from the user. Defaults to 'AccountAdmin'. Any
        other account role must be specified explicitly."""
        if role is not None:
            params["role"] = role
        # OPTIONAL - role_id
        """The user's admin relationship with the account will be created with the
        given role. Defaults to the built-in role for 'AccountAdmin'."""
        if role_id is not None:
            params["role_id"] = role_id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/admins/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/admins/{user_id}".format(**path), data=data, params=params, single_item=True)

    def list_account_admins(self, account_id, user_id=None):
        """
        List account admins.

        List the admins in the account
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # OPTIONAL - user_id
        """Scope the results to those with user IDs equal to any of the IDs specified here."""
        if user_id is not None:
            params["user_id"] = user_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/admins with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/admins".format(**path), data=data, params=params, all_pages=True)


class Admin(BaseModel):
    """Admin Model."""

    def __init__(self, id, status=None, role=None, user=None):
        """Init method for Admin class."""
        self._status = status
        self._role = role
        self._id = id
        self._user = user

        self.logger = logging.getLogger('pycanvas.Admin')

    @property
    def status(self):
        """The status of the account role/user assignment."""
        return self._status

    @status.setter
    def status(self, value):
        """Setter for status property."""
        self.logger.warn("Setting values on status will NOT update the remote Canvas instance.")
        self._status = value

    @property
    def role(self):
        """The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def id(self):
        """The unique identifier for the account role/user assignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def user(self):
        """The user the role is assigned to. See the Users API for details."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

