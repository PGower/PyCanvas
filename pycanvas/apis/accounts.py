"""Accounts API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AccountsAPI(BaseCanvasAPI):
    """Accounts API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountsAPI."""
        super(AccountsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AccountsAPI")

    def list_accounts(self, include=None):
        """
        List accounts.

        List accounts that the current user can view or manage.  Typically,
        students and even teachers will get an empty list in response, only
        account admins can view the accounts that they are in.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - include
        """Array of additional information to include.
        
        "lti_guid":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches
        "registration_settings":: returns info about the privacy policy and terms of use
        "services":: returns services and whether they are enabled (requires account management permissions)"""
        if include is not None:
            self._validate_enum(include, ["lti_guid", "registration_settings", "services"])
            params["include"] = include

        self.logger.debug("GET /api/v1/accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts".format(**path), data=data, params=params, all_pages=True)

    def list_accounts_for_course_admins(self):
        """
        List accounts for course admins.

        List accounts that the current user can view through their admin course enrollments.
        (Teacher, TA, or designer enrollments).
        Only returns "id", "name", "workflow_state", "root_account_id" and "parent_account_id"
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/course_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/course_accounts".format(**path), data=data, params=params, all_pages=True)

    def get_single_account(self, id):
        """
        Get a single account.

        Retrieve information on an individual account, given by id or sis
        sis_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{id}".format(**path), data=data, params=params, single_item=True)

    def get_sub_accounts_of_account(self, account_id, recursive=None):
        """
        Get the sub-accounts of an account.

        List accounts that are sub-accounts of the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # OPTIONAL - recursive
        """If true, the entire account tree underneath
        this account will be returned (though still paginated). If false, only
        direct sub-accounts of this account will be returned. Defaults to false."""
        if recursive is not None:
            params["recursive"] = recursive

        self.logger.debug("GET /api/v1/accounts/{account_id}/sub_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sub_accounts".format(**path), data=data, params=params, all_pages=True)

    def list_active_courses_in_account(self, account_id, by_subaccounts=None, by_teachers=None, completed=None, enrollment_term_id=None, enrollment_type=None, hide_enrollmentless_courses=None, include=None, published=None, search_term=None, state=None, with_enrollments=None):
        """
        List active courses in an account.

        Retrieve the list of courses in this account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # OPTIONAL - with_enrollments
        """If true, include only courses with at least one enrollment.  If false,
        include only courses with no enrollments.  If not present, do not filter
        on course enrollment status."""
        if with_enrollments is not None:
            params["with_enrollments"] = with_enrollments
        # OPTIONAL - enrollment_type
        """If set, only return courses that have at least one user enrolled in
        in the course with one of the specified enrollment types."""
        if enrollment_type is not None:
            self._validate_enum(enrollment_type, ["teacher", "student", "ta", "observer", "designer"])
            params["enrollment_type"] = enrollment_type
        # OPTIONAL - published
        """If true, include only published courses.  If false, exclude published
        courses.  If not present, do not filter on published status."""
        if published is not None:
            params["published"] = published
        # OPTIONAL - completed
        """If true, include only completed courses (these may be in state
        'completed', or their enrollment term may have ended).  If false, exclude
        completed courses.  If not present, do not filter on completed status."""
        if completed is not None:
            params["completed"] = completed
        # OPTIONAL - by_teachers
        """List of User IDs of teachers; if supplied, include only courses taught by
        one of the referenced users."""
        if by_teachers is not None:
            params["by_teachers"] = by_teachers
        # OPTIONAL - by_subaccounts
        """List of Account IDs; if supplied, include only courses associated with one
        of the referenced subaccounts."""
        if by_subaccounts is not None:
            params["by_subaccounts"] = by_subaccounts
        # OPTIONAL - hide_enrollmentless_courses
        """If present, only return courses that have at least one enrollment.
        Equivalent to 'with_enrollments=true'; retained for compatibility."""
        if hide_enrollmentless_courses is not None:
            params["hide_enrollmentless_courses"] = hide_enrollmentless_courses
        # OPTIONAL - state
        """If set, only return courses that are in the given state(s). By default,
        all states but "deleted" are returned."""
        if state is not None:
            self._validate_enum(state, ["created", "claimed", "available", "completed", "deleted", "all"])
            params["state"] = state
        # OPTIONAL - enrollment_term_id
        """If set, only includes courses from the specified term."""
        if enrollment_term_id is not None:
            params["enrollment_term_id"] = enrollment_term_id
        # OPTIONAL - search_term
        """The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters."""
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - include
        """- All explanations can be seen in the {api:CoursesController#index Course API index documentation}
        - "sections", "needs_grading_count" and "total_scores" are not valid options at the account level"""
        if include is not None:
            self._validate_enum(include, ["syllabus_body", "term", "course_progress", "storage_quota_used_mb", "total_students", "teachers"])
            params["include"] = include

        self.logger.debug("GET /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/courses".format(**path), data=data, params=params, all_pages=True)

    def update_account(self, id, account_default_group_storage_quota_mb=None, account_default_storage_quota_mb=None, account_default_time_zone=None, account_default_user_storage_quota_mb=None, account_name=None, account_services=None, account_settings_lock_all_announcements_locked=None, account_settings_lock_all_announcements_value=None, account_settings_restrict_student_future_listing_locked=None, account_settings_restrict_student_future_listing_value=None, account_settings_restrict_student_future_view_locked=None, account_settings_restrict_student_future_view_value=None, account_settings_restrict_student_past_view_locked=None, account_settings_restrict_student_past_view_value=None):
        """
        Update an account.

        Update an existing account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - account[name]
        """Updates the account name"""
        if account_name is not None:
            data["account[name]"] = account_name
        # OPTIONAL - account[default_time_zone]
        """The default time zone of the account. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        if account_default_time_zone is not None:
            data["account[default_time_zone]"] = account_default_time_zone
        # OPTIONAL - account[default_storage_quota_mb]
        """The default course storage quota to be used, if not otherwise specified."""
        if account_default_storage_quota_mb is not None:
            data["account[default_storage_quota_mb]"] = account_default_storage_quota_mb
        # OPTIONAL - account[default_user_storage_quota_mb]
        """The default user storage quota to be used, if not otherwise specified."""
        if account_default_user_storage_quota_mb is not None:
            data["account[default_user_storage_quota_mb]"] = account_default_user_storage_quota_mb
        # OPTIONAL - account[default_group_storage_quota_mb]
        """The default group storage quota to be used, if not otherwise specified."""
        if account_default_group_storage_quota_mb is not None:
            data["account[default_group_storage_quota_mb]"] = account_default_group_storage_quota_mb
        # OPTIONAL - account[settings][restrict_student_past_view][value]
        """Restrict students from viewing courses after end date"""
        if account_settings_restrict_student_past_view_value is not None:
            data["account[settings][restrict_student_past_view][value]"] = account_settings_restrict_student_past_view_value
        # OPTIONAL - account[settings][restrict_student_past_view][locked]
        """Lock this setting for sub-accounts and courses"""
        if account_settings_restrict_student_past_view_locked is not None:
            data["account[settings][restrict_student_past_view][locked]"] = account_settings_restrict_student_past_view_locked
        # OPTIONAL - account[settings][restrict_student_future_view][value]
        """Restrict students from viewing courses before start date"""
        if account_settings_restrict_student_future_view_value is not None:
            data["account[settings][restrict_student_future_view][value]"] = account_settings_restrict_student_future_view_value
        # OPTIONAL - account[settings][restrict_student_future_view][locked]
        """Lock this setting for sub-accounts and courses"""
        if account_settings_restrict_student_future_view_locked is not None:
            data["account[settings][restrict_student_future_view][locked]"] = account_settings_restrict_student_future_view_locked
        # OPTIONAL - account[settings][lock_all_announcements][value]
        """Disable comments on announcements"""
        if account_settings_lock_all_announcements_value is not None:
            data["account[settings][lock_all_announcements][value]"] = account_settings_lock_all_announcements_value
        # OPTIONAL - account[settings][lock_all_announcements][locked]
        """Lock this setting for sub-accounts and courses"""
        if account_settings_lock_all_announcements_locked is not None:
            data["account[settings][lock_all_announcements][locked]"] = account_settings_lock_all_announcements_locked
        # OPTIONAL - account[settings][restrict_student_future_listing][value]
        """Restrict students from viewing future enrollments in course list"""
        if account_settings_restrict_student_future_listing_value is not None:
            data["account[settings][restrict_student_future_listing][value]"] = account_settings_restrict_student_future_listing_value
        # OPTIONAL - account[settings][restrict_student_future_listing][locked]
        """Lock this setting for sub-accounts and courses"""
        if account_settings_restrict_student_future_listing_locked is not None:
            data["account[settings][restrict_student_future_listing][locked]"] = account_settings_restrict_student_future_listing_locked
        # OPTIONAL - account[services]
        """Give this a set of keys and boolean values to enable or disable services matching the keys"""
        if account_services is not None:
            data["account[services]"] = account_services

        self.logger.debug("PUT /api/v1/accounts/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_user_from_root_account(self, user_id, account_id):
        """
        Delete a user from the root account.

        Delete a user record from a Canvas root account. If a user is associated
        with multiple root accounts (in a multi-tenant instance of Canvas), this
        action will NOT remove them from the other accounts.
        
        WARNING: This API will allow a user to remove themselves from the account.
        If they do this, they won't be able to make API calls or log into Canvas at
        that account.
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

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/users/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/users/{user_id}".format(**path), data=data, params=params, single_item=True)

    def create_new_sub_account(self, account_id, account_name, account_default_group_storage_quota_mb=None, account_default_storage_quota_mb=None, account_default_user_storage_quota_mb=None, account_sis_account_id=None):
        """
        Create a new sub-account.

        Add a new sub-account to a given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - account[name]
        """The name of the new sub-account."""
        data["account[name]"] = account_name
        # OPTIONAL - account[sis_account_id]
        """The account's identifier in the Student Information System."""
        if account_sis_account_id is not None:
            data["account[sis_account_id]"] = account_sis_account_id
        # OPTIONAL - account[default_storage_quota_mb]
        """The default course storage quota to be used, if not otherwise specified."""
        if account_default_storage_quota_mb is not None:
            data["account[default_storage_quota_mb]"] = account_default_storage_quota_mb
        # OPTIONAL - account[default_user_storage_quota_mb]
        """The default user storage quota to be used, if not otherwise specified."""
        if account_default_user_storage_quota_mb is not None:
            data["account[default_user_storage_quota_mb]"] = account_default_user_storage_quota_mb
        # OPTIONAL - account[default_group_storage_quota_mb]
        """The default group storage quota to be used, if not otherwise specified."""
        if account_default_group_storage_quota_mb is not None:
            data["account[default_group_storage_quota_mb]"] = account_default_group_storage_quota_mb

        self.logger.debug("POST /api/v1/accounts/{account_id}/sub_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/sub_accounts".format(**path), data=data, params=params, single_item=True)


class Account(BaseModel):
    """Account Model."""

    def __init__(self, integration_id=None, default_time_zone=None, name=None, default_storage_quota_mb=None, sis_account_id=None, root_account_id=None, default_group_storage_quota_mb=None, id=None, sis_import_id=None, lti_guid=None, workflow_state=None, parent_account_id=None, default_user_storage_quota_mb=None):
        """Init method for Account class."""
        self._integration_id = integration_id
        self._default_time_zone = default_time_zone
        self._name = name
        self._default_storage_quota_mb = default_storage_quota_mb
        self._sis_account_id = sis_account_id
        self._root_account_id = root_account_id
        self._default_group_storage_quota_mb = default_group_storage_quota_mb
        self._id = id
        self._sis_import_id = sis_import_id
        self._lti_guid = lti_guid
        self._workflow_state = workflow_state
        self._parent_account_id = parent_account_id
        self._default_user_storage_quota_mb = default_user_storage_quota_mb

        self.logger = logging.getLogger('pycanvas.Account')

    @property
    def integration_id(self):
        """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def default_time_zone(self):
        """The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        return self._default_time_zone

    @default_time_zone.setter
    def default_time_zone(self, value):
        """Setter for default_time_zone property."""
        self.logger.warn("Setting values on default_time_zone will NOT update the remote Canvas instance.")
        self._default_time_zone = value

    @property
    def name(self):
        """The display name of the account."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def default_storage_quota_mb(self):
        """The storage quota for the account in megabytes, if not otherwise specified."""
        return self._default_storage_quota_mb

    @default_storage_quota_mb.setter
    def default_storage_quota_mb(self, value):
        """Setter for default_storage_quota_mb property."""
        self.logger.warn("Setting values on default_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_storage_quota_mb = value

    @property
    def sis_account_id(self):
        """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information."""
        return self._sis_account_id

    @sis_account_id.setter
    def sis_account_id(self, value):
        """Setter for sis_account_id property."""
        self.logger.warn("Setting values on sis_account_id will NOT update the remote Canvas instance.")
        self._sis_account_id = value

    @property
    def root_account_id(self):
        """The ID of the root account, or null if this is the root account."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

    @property
    def default_group_storage_quota_mb(self):
        """The storage quota for a group in the account in megabytes, if not otherwise specified."""
        return self._default_group_storage_quota_mb

    @default_group_storage_quota_mb.setter
    def default_group_storage_quota_mb(self, value):
        """Setter for default_group_storage_quota_mb property."""
        self.logger.warn("Setting values on default_group_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_group_storage_quota_mb = value

    @property
    def id(self):
        """the ID of the Account object."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def sis_import_id(self):
        """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def lti_guid(self):
        """The account's identifier that is sent as context_id in LTI launches."""
        return self._lti_guid

    @lti_guid.setter
    def lti_guid(self, value):
        """Setter for lti_guid property."""
        self.logger.warn("Setting values on lti_guid will NOT update the remote Canvas instance.")
        self._lti_guid = value

    @property
    def workflow_state(self):
        """The state of the account. Can be 'active' or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def parent_account_id(self):
        """The account's parent ID, or null if this is the root account."""
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, value):
        """Setter for parent_account_id property."""
        self.logger.warn("Setting values on parent_account_id will NOT update the remote Canvas instance.")
        self._parent_account_id = value

    @property
    def default_user_storage_quota_mb(self):
        """The storage quota for a user in the account in megabytes, if not otherwise specified."""
        return self._default_user_storage_quota_mb

    @default_user_storage_quota_mb.setter
    def default_user_storage_quota_mb(self, value):
        """Setter for default_user_storage_quota_mb property."""
        self.logger.warn("Setting values on default_user_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_user_storage_quota_mb = value

