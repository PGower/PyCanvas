"""UserObservees API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class UserObserveesAPI(BaseCanvasAPI):
    """UserObservees API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for UserObserveesAPI."""
        super(UserObserveesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.UserObserveesAPI")

    def list_observees(self, user_id, include=None):
        """
        List observees.

        List the users that the given user is observing.
        
        *Note:* all users are allowed to list their own observees. Administrators can list
        other users' observees.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # OPTIONAL - include
        """- "avatar_url": Optionally include avatar_url."""
        if include is not None:
            self._validate_enum(include, ["avatar_url"])
            params["include"] = include

        self.logger.debug("GET /api/v1/users/{user_id}/observees with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observees".format(**path), data=data, params=params, all_pages=True)

    def add_observee_with_credentials(self, user_id, access_token=None, observee_password=None, observee_unique_id=None):
        """
        Add an observee with credentials.

        Register the given user to observe another user, given the observee's credentials.
        
        *Note:* all users are allowed to add their own observees, given the observee's
        credentials or access token are provided. Administrators can add observees given credentials, access token or
        the {api:UserObserveesController#update observee's id}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # OPTIONAL - observee[unique_id]
        """The login id for the user to observe.  Required if access_token is omitted."""
        if observee_unique_id is not None:
            data["observee[unique_id]"] = observee_unique_id
        # OPTIONAL - observee[password]
        """The password for the user to observe. Required if access_token is omitted."""
        if observee_password is not None:
            data["observee[password]"] = observee_password
        # OPTIONAL - access_token
        """The access token for the user to observe.  Required if <tt>observee[unique_id]</tt> or <tt>observee[password]</tt> are omitted."""
        if access_token is not None:
            data["access_token"] = access_token

        self.logger.debug("POST /api/v1/users/{user_id}/observees with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/observees".format(**path), data=data, params=params, single_item=True)

    def show_observee(self, user_id, observee_id):
        """
        Show an observee.

        Gets information about an observed user.
        
        *Note:* all users are allowed to view their own observees.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - PATH - observee_id
        """ID"""
        path["observee_id"] = observee_id

        self.logger.debug("GET /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

    def add_observee(self, user_id, observee_id):
        """
        Add an observee.

        Registers a user as being observed by the given user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - PATH - observee_id
        """ID"""
        path["observee_id"] = observee_id

        self.logger.debug("PUT /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

    def remove_observee(self, user_id, observee_id):
        """
        Remove an observee.

        Unregisters a user as being observed by the given user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - PATH - observee_id
        """ID"""
        path["observee_id"] = observee_id

        self.logger.debug("DELETE /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

