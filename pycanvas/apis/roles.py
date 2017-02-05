"""Roles API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class RolesAPI(BaseCanvasAPI):
    """Roles API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for RolesAPI."""
        super(RolesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.RolesAPI")

    def list_roles(self, account_id, show_inherited=None, state=None):
        """
        List roles.

        List the roles available to an account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - The id of the account to retrieve roles for.
        path["account_id"] = account_id
        # OPTIONAL - state - Filter by role state. If this argument is omitted, only 'active' roles are returned.
        if state is not None:
            self._validate_enum(state, ["active", "inactive"])
            params["state"] = state
        # OPTIONAL - show_inherited - If this argument is true, all roles inherited from parent accounts will be included.
        if show_inherited is not None:
            params["show_inherited"] = show_inherited

        self.logger.debug("GET /api/v1/accounts/{account_id}/roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/roles".format(**path), data=data, params=params, all_pages=True)

    def get_single_role(self, id, role_id, account_id, role=None):
        """
        Get a single role.

        Retrieve information about a single role
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - PATH - account_id - The id of the account containing the role
        path["account_id"] = account_id
        # REQUIRED - role_id - The unique identifier for the role
        params["role_id"] = role_id
        # OPTIONAL - role - The name for the role
        if role is not None:
            params["role"] = role

        self.logger.debug("GET /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)

    def create_new_role(self, label, account_id, base_role_type=None, permissions_<X>_enabled=None, permissions_<X>_explicit=None, permissions_<X>_locked=None, role=None):
        """
        Create a new role.

        Create a new course-level or account-level role.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - label - Label for the role.
        data["label"] = label
        # OPTIONAL - role - Deprecated alias for label.
        if role is not None:
            data["role"] = role
        # OPTIONAL - base_role_type - Specifies the role type that will be used as a base for the permissions granted to this role. Defaults to 'AccountMembership' if absent
        if base_role_type is not None:
            self._validate_enum(base_role_type, ["AccountMembership", "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", "DesignerEnrollment"])
            data["base_role_type"] = base_role_type
        # OPTIONAL - permissions[<X>][explicit] - no description
        if permissions_<X>_explicit is not None:
            data["permissions[<X>][explicit]"] = permissions_<X>_explicit
        # OPTIONAL - permissions[<X>][enabled] - If explicit is 1 and enabled is 1, permission <X> will be explicitly granted to this role. If explicit is 1 and enabled has any other value (typically 0), permission <X> will be explicitly denied to this role. If explicit is any other value (typically 0) or absent, or if enabled is absent, the value for permission <X> will be inherited from upstream. Ignored if permission <X> is locked upstream (in an ancestor account). May occur multiple times with unique values for <X>. Recognized permission names for <X> are: [For Account-Level Roles Only] become_user -- Become other users manage_account_memberships -- Add/remove other admins for the account manage_account_settings -- Manage account-level settings manage_alerts -- Manage global alerts manage_courses -- Manage ( add / edit / delete ) courses manage_developer_keys -- Manage developer keys manage_global_outcomes -- Manage learning outcomes manage_jobs -- Manage background jobs manage_role_overrides -- Manage permissions manage_storage_quotas -- Set storage quotas for courses, groups, and users manage_sis -- Import and manage SIS data manage_site_settings -- Manage site-wide and plugin settings manage_user_logins -- Modify login details for users read_course_content -- View course content read_course_list -- View the list of courses read_messages -- View notifications sent to users site_admin -- Use the Site Admin section and admin all other accounts view_error_reports -- View error reports view_statistics -- View statistics manage_feature_flags -- Enable or disable features at an account level [For both Account-Level and Course-Level roles] Note: Applicable enrollment types for course-level roles are given in brackets: S = student, T = teacher, A = TA, D = designer, O = observer. Lower-case letters indicate permissions that are off by default. A missing letter indicates the permission cannot be enabled for the role or any derived custom roles. change_course_state -- [ TaD ] Change course state comment_on_others_submissions -- [sTAD ] View all students' submissions and make comments on them create_collaborations -- [STADo] Create student collaborations create_conferences -- [STADo] Create web conferences manage_admin_users -- [ Tad ] Add/remove other teachers, course designers or TAs to the course manage_assignments -- [ TADo] Manage (add / edit / delete) assignments and quizzes manage_calendar -- [sTADo] Add, edit and delete events on the course calendar manage_content -- [ TADo] Manage all other course content manage_files -- [ TADo] Manage (add / edit / delete) course files manage_grades -- [ TA ] Edit grades manage_groups -- [ TAD ] Manage (create / edit / delete) groups manage_interaction_alerts -- [ Ta ] Manage alerts manage_outcomes -- [sTaDo] Manage learning outcomes manage_sections -- [ TaD ] Manage (create / edit / delete) course sections manage_students -- [ TAD ] Add/remove students for the course manage_user_notes -- [ TA ] Manage faculty journal entries manage_rubrics -- [ TAD ] Edit assessing rubrics manage_wiki -- [ TADo] Manage wiki (add / edit / delete pages) read_forum -- [STADO] View discussions moderate_forum -- [sTADo] Moderate discussions (delete/edit others' posts, lock topics) post_to_forum -- [STADo] Post to discussions read_question_banks -- [ TADo] View and link to question banks read_reports -- [ TAD ] View usage reports for the course read_roster -- [STADo] See the list of users read_sis -- [sTa ] Read SIS data send_messages -- [STADo] Send messages to individual course members send_messages_all -- [sTADo] Send messages to the entire class view_all_grades -- [ TAd ] View all grades view_group_pages -- [sTADo] View the group pages of all student groups Some of these permissions are applicable only for roles on the site admin account, on a root account, or for course-level roles with a particular base role type; if a specified permission is inapplicable, it will be ignored. Additional permissions may exist based on installed plugins.
        if permissions_<X>_enabled is not None:
            data["permissions[<X>][enabled]"] = permissions_<X>_enabled
        # OPTIONAL - permissions[<X>][locked] - If the value is 1, permission <X> will be locked downstream (new roles in subaccounts cannot override the setting). For any other value, permission <X> is left unlocked. Ignored if permission <X> is already locked upstream. May occur multiple times with unique values for <X>.
        if permissions_<X>_locked is not None:
            data["permissions[<X>][locked]"] = permissions_<X>_locked

        self.logger.debug("POST /api/v1/accounts/{account_id}/roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/roles".format(**path), data=data, params=params, single_item=True)

    def deactivate_role(self, id, role_id, account_id, role=None):
        """
        Deactivate a role.

        Deactivates a custom role.  This hides it in the user interface and prevents it
        from being assigned to new users.  Existing users assigned to the role will
        continue to function with the same permissions they had previously.
        Built-in roles cannot be deactivated.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - role_id - The unique identifier for the role
        params["role_id"] = role_id
        # OPTIONAL - role - The name for the role
        if role is not None:
            params["role"] = role

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)

    def activate_role(self, id, role_id, account_id, role=None):
        """
        Activate a role.

        Re-activates an inactive role (allowing it to be assigned to new users)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - role_id - The unique identifier for the role
        data["role_id"] = role_id
        # OPTIONAL - role - The name for the role
        if role is not None:
            data["role"] = role

        self.logger.debug("POST /api/v1/accounts/{account_id}/roles/{id}/activate with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/roles/{id}/activate".format(**path), data=data, params=params, single_item=True)

    def update_role(self, id, account_id, label=None, permissions_<X>_enabled=None, permissions_<X>_explicit=None):
        """
        Update a role.

        Update permissions for an existing role.
        
        Recognized roles are:
        * TeacherEnrollment
        * StudentEnrollment
        * TaEnrollment
        * ObserverEnrollment
        * DesignerEnrollment
        * AccountAdmin
        * Any previously created custom role
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - label - The label for the role. Can only change the label of a custom role that belongs directly to the account.
        if label is not None:
            data["label"] = label
        # OPTIONAL - permissions[<X>][explicit] - no description
        if permissions_<X>_explicit is not None:
            data["permissions[<X>][explicit]"] = permissions_<X>_explicit
        # OPTIONAL - permissions[<X>][enabled] - These arguments are described in the documentation for the {api:RoleOverridesController#add_role add_role method}.
        if permissions_<X>_enabled is not None:
            data["permissions[<X>][enabled]"] = permissions_<X>_enabled

        self.logger.debug("PUT /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)


class Rolepermissions(BaseModel):
    """Rolepermissions Model."""

    def __init__(self, locked=None, readonly=None, prior_default=None, enabled=None, explicit=None):
        """Init method for Rolepermissions class."""
        self._locked = locked
        self._readonly = readonly
        self._prior_default = prior_default
        self._enabled = enabled
        self._explicit = explicit

        self.logger = logging.getLogger('pycanvas.Rolepermissions')

    @property
    def locked(self):
        """Whether the permission is locked by this role."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def readonly(self):
        """Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role)."""
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        """Setter for readonly property."""
        self.logger.warn("Setting values on readonly will NOT update the remote Canvas instance.")
        self._readonly = value

    @property
    def prior_default(self):
        """The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true."""
        return self._prior_default

    @prior_default.setter
    def prior_default(self, value):
        """Setter for prior_default property."""
        self.logger.warn("Setting values on prior_default will NOT update the remote Canvas instance.")
        self._prior_default = value

    @property
    def enabled(self):
        """Whether the role has the permission."""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """Setter for enabled property."""
        self.logger.warn("Setting values on enabled will NOT update the remote Canvas instance.")
        self._enabled = value

    @property
    def explicit(self):
        """Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role."""
        return self._explicit

    @explicit.setter
    def explicit(self, value):
        """Setter for explicit property."""
        self.logger.warn("Setting values on explicit will NOT update the remote Canvas instance.")
        self._explicit = value


class Role(BaseModel):
    """Role Model."""

    def __init__(self, account=None, workflow_state=None, base_role_type=None, role=None, label=None, permissions=None):
        """Init method for Role class."""
        self._account = account
        self._workflow_state = workflow_state
        self._base_role_type = base_role_type
        self._role = role
        self._label = label
        self._permissions = permissions

        self.logger = logging.getLogger('pycanvas.Role')

    @property
    def account(self):
        """JSON representation of the account the role is in."""
        return self._account

    @account.setter
    def account(self, value):
        """Setter for account property."""
        self.logger.warn("Setting values on account will NOT update the remote Canvas instance.")
        self._account = value

    @property
    def workflow_state(self):
        """The state of the role: 'active', 'inactive', or 'built_in'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def base_role_type(self):
        """The role type that is being used as a base for this role. For account-level roles, this is 'AccountMembership'. For course-level roles, it is an enrollment type."""
        return self._base_role_type

    @base_role_type.setter
    def base_role_type(self, value):
        """Setter for base_role_type property."""
        self.logger.warn("Setting values on base_role_type will NOT update the remote Canvas instance.")
        self._base_role_type = value

    @property
    def role(self):
        """The label of the role. (Deprecated alias for 'label')."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def label(self):
        """The label of the role."""
        return self._label

    @label.setter
    def label(self, value):
        """Setter for label property."""
        self.logger.warn("Setting values on label will NOT update the remote Canvas instance.")
        self._label = value

    @property
    def permissions(self):
        """A dictionary of permissions keyed by name (see permissions input parameter in the 'Create a role' API)."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

