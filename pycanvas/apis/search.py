"""Search API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class SearchAPI(BaseCanvasAPI):
    """Search API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SearchAPI."""
        super(SearchAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.SearchAPI")

    def find_recipients_conversations(self, context=None, exclude=None, from_conversation_id=None, permissions=None, search=None, type=None, user_id=None):
        """
        Find recipients.

        Find valid recipients (users, courses and groups) that the current user
        can send messages to. The /api/v1/search/recipients path is the preferred
        endpoint, /api/v1/conversations/find_recipients is deprecated.
        
        Pagination is supported.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - search
        """Search terms used for matching users/courses/groups (e.g. "bob smith"). If
        multiple terms are given (separated via whitespace), only results matching
        all terms will be returned."""
        if search is not None:
            params["search"] = search
        # OPTIONAL - context
        """Limit the search to a particular course/group (e.g. "course_3" or "group_4")."""
        if context is not None:
            params["context"] = context
        # OPTIONAL - exclude
        """Array of ids to exclude from the search. These may be user ids or
        course/group ids prefixed with "course_" or "group_" respectively,
        e.g. exclude[]=1&exclude[]=2&exclude[]=course_3"""
        if exclude is not None:
            params["exclude"] = exclude
        # OPTIONAL - type
        """Limit the search just to users or contexts (groups/courses)."""
        if type is not None:
            self._validate_enum(type, ["user", "context"])
            params["type"] = type
        # OPTIONAL - user_id
        """Search for a specific user id. This ignores the other above parameters,
        and will never return more than one result."""
        if user_id is not None:
            params["user_id"] = user_id
        # OPTIONAL - from_conversation_id
        """When searching by user_id, only users that could be normally messaged by
        this user will be returned. This parameter allows you to specify a
        conversation that will be referenced for a shared context -- if both the
        current user and the searched user are in the conversation, the user will
        be returned. This is used to start new side conversations."""
        if from_conversation_id is not None:
            params["from_conversation_id"] = from_conversation_id
        # OPTIONAL - permissions
        """Array of permission strings to be checked for each matched context (e.g.
        "send_messages"). This argument determines which permissions may be
        returned in the response; it won't prevent contexts from being returned if
        they don't grant the permission(s)."""
        if permissions is not None:
            params["permissions"] = permissions

        self.logger.debug("GET /api/v1/conversations/find_recipients with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conversations/find_recipients".format(**path), data=data, params=params, no_data=True)

    def find_recipients_search(self, context=None, exclude=None, from_conversation_id=None, permissions=None, search=None, type=None, user_id=None):
        """
        Find recipients.

        Find valid recipients (users, courses and groups) that the current user
        can send messages to. The /api/v1/search/recipients path is the preferred
        endpoint, /api/v1/conversations/find_recipients is deprecated.
        
        Pagination is supported.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - search
        """Search terms used for matching users/courses/groups (e.g. "bob smith"). If
        multiple terms are given (separated via whitespace), only results matching
        all terms will be returned."""
        if search is not None:
            params["search"] = search
        # OPTIONAL - context
        """Limit the search to a particular course/group (e.g. "course_3" or "group_4")."""
        if context is not None:
            params["context"] = context
        # OPTIONAL - exclude
        """Array of ids to exclude from the search. These may be user ids or
        course/group ids prefixed with "course_" or "group_" respectively,
        e.g. exclude[]=1&exclude[]=2&exclude[]=course_3"""
        if exclude is not None:
            params["exclude"] = exclude
        # OPTIONAL - type
        """Limit the search just to users or contexts (groups/courses)."""
        if type is not None:
            self._validate_enum(type, ["user", "context"])
            params["type"] = type
        # OPTIONAL - user_id
        """Search for a specific user id. This ignores the other above parameters,
        and will never return more than one result."""
        if user_id is not None:
            params["user_id"] = user_id
        # OPTIONAL - from_conversation_id
        """When searching by user_id, only users that could be normally messaged by
        this user will be returned. This parameter allows you to specify a
        conversation that will be referenced for a shared context -- if both the
        current user and the searched user are in the conversation, the user will
        be returned. This is used to start new side conversations."""
        if from_conversation_id is not None:
            params["from_conversation_id"] = from_conversation_id
        # OPTIONAL - permissions
        """Array of permission strings to be checked for each matched context (e.g.
        "send_messages"). This argument determines which permissions may be
        returned in the response; it won't prevent contexts from being returned if
        they don't grant the permission(s)."""
        if permissions is not None:
            params["permissions"] = permissions

        self.logger.debug("GET /api/v1/search/recipients with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/search/recipients".format(**path), data=data, params=params, no_data=True)

    def list_all_courses(self, open_enrollment_only=None, public_only=None, search=None):
        """
        List all courses.

        List all courses visible in the public index
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - search
        """Search terms used for matching users/courses/groups (e.g. "bob smith"). If
        multiple terms are given (separated via whitespace), only results matching
        all terms will be returned."""
        if search is not None:
            params["search"] = search
        # OPTIONAL - public_only
        """Only return courses with public content. Defaults to false."""
        if public_only is not None:
            params["public_only"] = public_only
        # OPTIONAL - open_enrollment_only
        """Only return courses that allow self enrollment. Defaults to false."""
        if open_enrollment_only is not None:
            params["open_enrollment_only"] = open_enrollment_only

        self.logger.debug("GET /api/v1/search/all_courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/search/all_courses".format(**path), data=data, params=params, no_data=True)

