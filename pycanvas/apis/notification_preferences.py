"""NotificationPreferences API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class NotificationPreferencesAPI(BaseCanvasAPI):
    """NotificationPreferences API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for NotificationPreferencesAPI."""
        super(NotificationPreferencesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.NotificationPreferencesAPI")

    def list_preferences_communication_channel_id(self, user_id, communication_channel_id):
        """
        List preferences.

        Fetch all preferences for the given communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences".format(**path), data=data, params=params, all_pages=True)

    def list_preferences_type(self, type, user_id, address):
        """
        List preferences.

        Fetch all preferences for the given communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - type
        """ID"""
        path["type"] = type

        # REQUIRED - PATH - address
        """ID"""
        path["address"] = address

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences".format(**path), data=data, params=params, all_pages=True)

    def list_of_preference_categories(self, user_id, communication_channel_id):
        """
        List of preference categories.

        Fetch all notification preference categories for the given communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories".format(**path), data=data, params=params, all_pages=True)

    def get_preference_communication_channel_id(self, user_id, notification, communication_channel_id):
        """
        Get a preference.

        Fetch the preference for the given notification for the given communicaiton channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        # REQUIRED - PATH - notification
        """ID"""
        path["notification"] = notification

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification}".format(**path), data=data, params=params, single_item=True)

    def get_preference_type(self, type, user_id, address, notification):
        """
        Get a preference.

        Fetch the preference for the given notification for the given communicaiton channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - type
        """ID"""
        path["type"] = type

        # REQUIRED - PATH - address
        """ID"""
        path["address"] = address

        # REQUIRED - PATH - notification
        """ID"""
        path["notification"] = notification

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification}".format(**path), data=data, params=params, single_item=True)

    def update_preference_communication_channel_id(self, notification, communication_channel_id, notification_preferences_frequency):
        """
        Update a preference.

        Change the preference for a single notification for a single communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        # REQUIRED - PATH - notification
        """ID"""
        path["notification"] = notification

        # REQUIRED - notification_preferences[frequency]
        """The desired frequency for this notification"""
        data["notification_preferences[frequency]"] = notification_preferences_frequency

        self.logger.debug("PUT /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification}".format(**path), data=data, params=params, no_data=True)

    def update_preference_type(self, type, address, notification, notification_preferences_frequency):
        """
        Update a preference.

        Change the preference for a single notification for a single communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - type
        """ID"""
        path["type"] = type

        # REQUIRED - PATH - address
        """ID"""
        path["address"] = address

        # REQUIRED - PATH - notification
        """ID"""
        path["notification"] = notification

        # REQUIRED - notification_preferences[frequency]
        """The desired frequency for this notification"""
        data["notification_preferences[frequency]"] = notification_preferences_frequency

        self.logger.debug("PUT /api/v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification}".format(**path), data=data, params=params, no_data=True)

    def update_preferences_by_category(self, category, communication_channel_id, notification_preferences_frequency):
        """
        Update preferences by category.

        Change the preferences for multiple notifications based on the category for a single communication channel
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        # REQUIRED - PATH - category
        """The name of the category. Must be parameterized (e.g. The category "Course Content" should be "course_content")"""
        path["category"] = category

        # REQUIRED - notification_preferences[frequency]
        """The desired frequency for each notification in the category"""
        data["notification_preferences[frequency]"] = notification_preferences_frequency

        self.logger.debug("PUT /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category}".format(**path), data=data, params=params, no_data=True)

    def update_multiple_preferences_communication_channel_id(self, communication_channel_id, notification_preferences_<X>_frequency):
        """
        Update multiple preferences.

        Change the preferences for multiple notifications for a single communication channel at once
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - communication_channel_id
        """ID"""
        path["communication_channel_id"] = communication_channel_id

        # REQUIRED - notification_preferences[<X>][frequency]
        """The desired frequency for <X> notification"""
        data["notification_preferences[<X>][frequency]"] = notification_preferences_<X>_frequency

        self.logger.debug("PUT /api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences".format(**path), data=data, params=params, no_data=True)

    def update_multiple_preferences_type(self, type, address, notification_preferences_<X>_frequency):
        """
        Update multiple preferences.

        Change the preferences for multiple notifications for a single communication channel at once
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - type
        """ID"""
        path["type"] = type

        # REQUIRED - PATH - address
        """ID"""
        path["address"] = address

        # REQUIRED - notification_preferences[<X>][frequency]
        """The desired frequency for <X> notification"""
        data["notification_preferences[<X>][frequency]"] = notification_preferences_<X>_frequency

        self.logger.debug("PUT /api/v1/users/self/communication_channels/{type}/{address}/notification_preferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/self/communication_channels/{type}/{address}/notification_preferences".format(**path), data=data, params=params, no_data=True)


class Notificationpreference(BaseModel):
    """Notificationpreference Model."""

    def __init__(self, category=None, notification=None, href=None, frequency=None):
        """Init method for Notificationpreference class."""
        self._category = category
        self._notification = notification
        self._href = href
        self._frequency = frequency

        self.logger = logging.getLogger('pycanvas.Notificationpreference')

    @property
    def category(self):
        """The category of that notification."""
        return self._category

    @category.setter
    def category(self, value):
        """Setter for category property."""
        self.logger.warn("Setting values on category will NOT update the remote Canvas instance.")
        self._category = value

    @property
    def notification(self):
        """The notification this preference belongs to."""
        return self._notification

    @notification.setter
    def notification(self, value):
        """Setter for notification property."""
        self.logger.warn("Setting values on notification will NOT update the remote Canvas instance.")
        self._notification = value

    @property
    def href(self):
        """href."""
        return self._href

    @href.setter
    def href(self, value):
        """Setter for href property."""
        self.logger.warn("Setting values on href will NOT update the remote Canvas instance.")
        self._href = value

    @property
    def frequency(self):
        """How often to send notifications to this communication channel for the given notification. Possible values are 'immediately', 'daily', 'weekly', and 'never'."""
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        """Setter for frequency property."""
        self.logger.warn("Setting values on frequency will NOT update the remote Canvas instance.")
        self._frequency = value

