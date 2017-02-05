"""Logins API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class LoginsAPI(BaseCanvasAPI):
    """Logins API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for LoginsAPI."""
        super(LoginsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.LoginsAPI")

    def list_user_logins_accounts(self, account_id):
        """
        List user logins.

        Given a user ID, return that user's logins for the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/logins with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/logins".format(**path), data=data, params=params, no_data=True)

    def list_user_logins_users(self, user_id):
        """
        List user logins.

        Given a user ID, return that user's logins for the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/logins with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/logins".format(**path), data=data, params=params, no_data=True)

    def create_user_login(self, user_id, account_id, login_unique_id, login_password=None, login_sis_user_id=None):
        """
        Create a user login.

        Create a new login for an existing user in the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - user[id] - The ID of the user to create the login for.
        data["user[id]"] = user_id
        # REQUIRED - login[unique_id] - The unique ID for the new login.
        data["login[unique_id]"] = login_unique_id
        # OPTIONAL - login[password] - The new login's password.
        if login_password is not None:
            data["login[password]"] = login_password
        # OPTIONAL - login[sis_user_id] - SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        if login_sis_user_id is not None:
            data["login[sis_user_id]"] = login_sis_user_id

        self.logger.debug("POST /api/v1/accounts/{account_id}/logins with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/logins".format(**path), data=data, params=params, no_data=True)

    def edit_user_login(self, id, account_id, login_password=None, login_sis_user_id=None, login_unique_id=None):
        """
        Edit a user login.

        Update an existing login for a user in the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - login[unique_id] - The new unique ID for the login.
        if login_unique_id is not None:
            data["login[unique_id]"] = login_unique_id
        # OPTIONAL - login[password] - The new password for the login. Can only be set by an admin user if admins are allowed to change passwords for the account.
        if login_password is not None:
            data["login[password]"] = login_password
        # OPTIONAL - login[sis_user_id] - SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.
        if login_sis_user_id is not None:
            data["login[sis_user_id]"] = login_sis_user_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/logins/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/logins/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_user_login(self, id, user_id):
        """
        Delete a user login.

        Delete an existing login.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/users/{user_id}/logins/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/logins/{id}".format(**path), data=data, params=params, no_data=True)

