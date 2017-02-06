"""AnnouncementExternalFeeds API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AnnouncementExternalFeedsAPI(BaseCanvasAPI):
    """AnnouncementExternalFeeds API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AnnouncementExternalFeedsAPI."""
        super(AnnouncementExternalFeedsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AnnouncementExternalFeedsAPI")

    def list_external_feeds_courses(self, course_id):
        """
        List external feeds.

        Returns the list of External Feeds this course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/external_feeds with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/external_feeds".format(**path), data=data, params=params, all_pages=True)

    def list_external_feeds_groups(self, group_id):
        """
        List external feeds.

        Returns the list of External Feeds this course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/external_feeds with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/external_feeds".format(**path), data=data, params=params, all_pages=True)

    def create_external_feed_courses(self, url, course_id, header_match=None, verbosity=None):
        """
        Create an external feed.

        Create a new external feed for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - url
        """The url to the external rss or atom feed"""
        data["url"] = url

        # OPTIONAL - header_match
        """If given, only feed entries that contain this string in their title will be imported"""
        if header_match is not None:
            data["header_match"] = header_match

        # OPTIONAL - verbosity
        """Defaults to "full""""
        if verbosity is not None:
            self._validate_enum(verbosity, ["full", "truncate", "link_only"])
            data["verbosity"] = verbosity

        self.logger.debug("POST /api/v1/courses/{course_id}/external_feeds with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/external_feeds".format(**path), data=data, params=params, single_item=True)

    def create_external_feed_groups(self, url, group_id, header_match=None, verbosity=None):
        """
        Create an external feed.

        Create a new external feed for the course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - url
        """The url to the external rss or atom feed"""
        data["url"] = url

        # OPTIONAL - header_match
        """If given, only feed entries that contain this string in their title will be imported"""
        if header_match is not None:
            data["header_match"] = header_match

        # OPTIONAL - verbosity
        """Defaults to "full""""
        if verbosity is not None:
            self._validate_enum(verbosity, ["full", "truncate", "link_only"])
            data["verbosity"] = verbosity

        self.logger.debug("POST /api/v1/groups/{group_id}/external_feeds with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/external_feeds".format(**path), data=data, params=params, single_item=True)

    def delete_external_feed_courses(self, course_id, external_feed_id):
        """
        Delete an external feed.

        Deletes the external feed.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - external_feed_id
        """ID"""
        path["external_feed_id"] = external_feed_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/external_feeds/{external_feed_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/external_feeds/{external_feed_id}".format(**path), data=data, params=params, single_item=True)

    def delete_external_feed_groups(self, group_id, external_feed_id):
        """
        Delete an external feed.

        Deletes the external feed.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - external_feed_id
        """ID"""
        path["external_feed_id"] = external_feed_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/external_feeds/{external_feed_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/external_feeds/{external_feed_id}".format(**path), data=data, params=params, single_item=True)


class Externalfeed(BaseModel):
    """Externalfeed Model."""

    def __init__(self, display_name=None, url=None, created_at=None, id=None, header_match=None, verbosity=None):
        """Init method for Externalfeed class."""
        self._display_name = display_name
        self._url = url
        self._created_at = created_at
        self._id = id
        self._header_match = header_match
        self._verbosity = verbosity

        self.logger = logging.getLogger('pycanvas.Externalfeed')

    @property
    def display_name(self):
        """The title of the feed, pulled from the feed itself. If the feed hasn't yet been pulled, a temporary name will be synthesized based on the URL."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def url(self):
        """The HTTP/HTTPS URL to the feed."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """When this external feed was added to Canvas."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def id(self):
        """The ID of the feed."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def header_match(self):
        """If not null, only feed entries whose title contains this string will trigger new posts in Canvas."""
        return self._header_match

    @header_match.setter
    def header_match(self, value):
        """Setter for header_match property."""
        self.logger.warn("Setting values on header_match will NOT update the remote Canvas instance.")
        self._header_match = value

    @property
    def verbosity(self):
        """The verbosity setting determines how much of the feed's content is imported into Canvas as part of the posting. 'link_only' means that only the title and a link to the item. 'truncate' means that a summary of the first portion of the item body will be used. 'full' means that the full item body will be used."""
        return self._verbosity

    @verbosity.setter
    def verbosity(self, value):
        """Setter for verbosity property."""
        self.logger.warn("Setting values on verbosity will NOT update the remote Canvas instance.")
        self._verbosity = value

