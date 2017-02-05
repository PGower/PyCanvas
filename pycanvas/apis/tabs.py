"""Tabs API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class TabsAPI(BaseCanvasAPI):
    """Tabs API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for TabsAPI."""
        super(TabsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.TabsAPI")

    def list_available_tabs_for_course_or_group_courses(self, course_id, include=None):
        """
        List available tabs for a course or group.

        Returns a list of navigation tabs available in the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - include - Optionally include external tool tabs in the returned list of tabs (Only has effect for courses, not groups)
        if include is not None:
            self._validate_enum(include, ["external"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/tabs with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/tabs".format(**path), data=data, params=params, no_data=True)

    def list_available_tabs_for_course_or_group_groups(self, group_id, include=None):
        """
        List available tabs for a course or group.

        Returns a list of navigation tabs available in the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - include - Optionally include external tool tabs in the returned list of tabs (Only has effect for courses, not groups)
        if include is not None:
            self._validate_enum(include, ["external"])
            params["include"] = include

        self.logger.debug("GET /api/v1/groups/{group_id}/tabs with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/tabs".format(**path), data=data, params=params, no_data=True)

    def update_tab_for_course(self, tab_id, course_id, hidden=None, position=None):
        """
        Update a tab for a course.

        Home and Settings tabs are not manageable, and can't be hidden or moved
        
        Returns a tab object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - tab_id - ID
        path["tab_id"] = tab_id
        # OPTIONAL - position - The new position of the tab, 1-based
        if position is not None:
            data["position"] = position
        # OPTIONAL - hidden - no description
        if hidden is not None:
            data["hidden"] = hidden

        self.logger.debug("PUT /api/v1/courses/{course_id}/tabs/{tab_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/tabs/{tab_id}".format(**path), data=data, params=params, single_item=True)


class Tab(BaseModel):
    """Tab Model."""

    def __init__(self, html_url=None, visibility=None, label=None, position=None, hidden=None, type=None, id=None):
        """Init method for Tab class."""
        self._html_url = html_url
        self._visibility = visibility
        self._label = label
        self._position = position
        self._hidden = hidden
        self._type = type
        self._id = id

        self.logger = logging.getLogger('pycanvas.Tab')

    @property
    def html_url(self):
        """html_url."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def visibility(self):
        """possible values are: public, members, admins, and none."""
        return self._visibility

    @visibility.setter
    def visibility(self, value):
        """Setter for visibility property."""
        self.logger.warn("Setting values on visibility will NOT update the remote Canvas instance.")
        self._visibility = value

    @property
    def label(self):
        """label."""
        return self._label

    @label.setter
    def label(self, value):
        """Setter for label property."""
        self.logger.warn("Setting values on label will NOT update the remote Canvas instance.")
        self._label = value

    @property
    def position(self):
        """1 based."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def hidden(self):
        """only included if true."""
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Setter for hidden property."""
        self.logger.warn("Setting values on hidden will NOT update the remote Canvas instance.")
        self._hidden = value

    @property
    def type(self):
        """type."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

