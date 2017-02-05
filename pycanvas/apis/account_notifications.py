"""AccountNotifications API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from base import BaseCanvasAPI
from base import BaseModel


class AccountNotificationsAPI(BaseCanvasAPI):
    """AccountNotifications API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountNotificationsAPI."""
        super(AccountNotificationsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AccountNotificationsAPI")

    def index_of_active_global_notification_for_user(self, user_id, account_id):
        """
        Index of active global notification for the user.

        Returns a list of all global notifications in the account for this user
        Any notifications that have been closed by the user will not be returned
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/users/{user_id}/account_notifications with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/users/{user_id}/account_notifications".format(**path), params=payload, all_pages=True)

    def close_notification_for_user(self, id, user_id, account_id):
        """
        Close notification for user.

        If the user no long wants to see this notification it can be excused with this call
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/users/{user_id}/account_notifications/{id} with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/users/{user_id}/account_notifications/{id}".format(**path), params=payload, single_item=True)

    def create_global_notification(self, account_id, account_notification_end_at, account_notification_subject, account_notification_message, account_notification_start_at, account_notification_icon=None, account_notification_roles=None):
        """
        Create a global notification.

        Create and return a new global notification for an account.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - account_notification[subject] - The subject of the notification.
        payload["account_notification[subject]"] = account_notification_subject
        # REQUIRED - account_notification[message] - The message body of the notification.
        payload["account_notification[message]"] = account_notification_message
        # REQUIRED - account_notification[start_at] - The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z
        payload["account_notification[start_at]"] = account_notification_start_at
        # REQUIRED - account_notification[end_at] - The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z
        payload["account_notification[end_at]"] = account_notification_end_at
        # OPTIONAL - account_notification[icon] - The icon to display with the notification. Note: Defaults to warning.
        if account_notification_icon is not None:
            self._validate_enum(account_notification_icon, ["warning", "information", "question", "error", "calendar"])
        if account_notification_icon is not None:
            payload["account_notification[icon]"] = account_notification_icon
        # OPTIONAL - account_notification_roles - The role(s) to send global notification to. Note: ommitting this field will send to everyone Example: account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"]
        if account_notification_roles is not None:
            payload["account_notification_roles"] = account_notification_roles

        self.logger.debug("POST /api/v1/accounts/{account_id}/account_notifications with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/account_notifications".format(**path), data=payload, no_data=True)


class Accountnotification(BaseModel):
    """Accountnotification Model."""

    def __init__(self, role_ids=None, start_at=None, roles=None, end_at=None, message=None, subject=None, icon=None):
        """Init method for Accountnotification class."""
        self._role_ids = role_ids
        self._start_at = start_at
        self._roles = roles
        self._end_at = end_at
        self._message = message
        self._subject = subject
        self._icon = icon

        self.logger = logging.getLogger('pycanvas.Accountnotification')

    @property
    def role_ids(self):
        """The roles to send the notification to.  If roles is not passed it defaults to all roles."""
        return self._role_ids

    @role_ids.setter
    def role_ids(self, value):
        """Setter for role_ids property."""
        self.logger.warn("Setting values on role_ids will NOT update the remote Canvas instance.")
        self._role_ids = value

    @property
    def start_at(self):
        """When to send out the notification."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def roles(self):
        """(Deprecated) The roles to send the notification to.  If roles is not passed it defaults to all roles."""
        return self._roles

    @roles.setter
    def roles(self, value):
        """Setter for roles property."""
        self.logger.warn("Setting values on roles will NOT update the remote Canvas instance.")
        self._roles = value

    @property
    def end_at(self):
        """When to expire the notification."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def message(self):
        """The message to be sent in the notification."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn("Setting values on message will NOT update the remote Canvas instance.")
        self._message = value

    @property
    def subject(self):
        """The subject of the notifications."""
        return self._subject

    @subject.setter
    def subject(self, value):
        """Setter for subject property."""
        self.logger.warn("Setting values on subject will NOT update the remote Canvas instance.")
        self._subject = value

    @property
    def icon(self):
        """The icon to display with the message.  Defaults to warning."""
        return self._icon

    @icon.setter
    def icon(self, value):
        """Setter for icon property."""
        self.logger.warn("Setting values on icon will NOT update the remote Canvas instance.")
        self._icon = value

