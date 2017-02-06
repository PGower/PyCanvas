"""GroupCategories API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class GroupCategoriesAPI(BaseCanvasAPI):
    """GroupCategories API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GroupCategoriesAPI."""
        super(GroupCategoriesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.GroupCategoriesAPI")

    def list_group_categories_for_context_accounts(self, account_id):
        """
        List group categories for a context.

        Returns a list of group categories in a context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/group_categories with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/group_categories".format(**path), data=data, params=params, all_pages=True)

    def list_group_categories_for_context_courses(self, course_id):
        """
        List group categories for a context.

        Returns a list of group categories in a context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/group_categories with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/group_categories".format(**path), data=data, params=params, all_pages=True)

    def get_single_group_category(self, group_category_id):
        """
        Get a single group category.

        Returns the data for a single group category, or a 401 if the caller doesn't have
        the rights to see it.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        self.logger.debug("GET /api/v1/group_categories/{group_category_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/group_categories/{group_category_id}".format(**path), data=data, params=params, single_item=True)

    def create_group_category_accounts(self, name, account_id, auto_leader=None, create_group_count=None, group_limit=None, self_signup=None, split_group_count=None):
        """
        Create a Group Category.

        Create a new group category
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - name
        """Name of the group category"""
        data["name"] = name

        # OPTIONAL - self_signup
        """Allow students to sign up for a group themselves (Course Only).
        valid values are:
        "enabled":: allows students to self sign up for any group in course
        "restricted":: allows students to self sign up only for groups in the
                       same section null disallows self sign up"""
        if self_signup is not None:
            self._validate_enum(self_signup, ["enabled", "restricted"])
            data["self_signup"] = self_signup

        # OPTIONAL - auto_leader
        """Assigns group leaders automatically when generating and allocating students to groups
        Valid values are:
        "first":: the first student to be allocated to a group is the leader
        "random":: a random student from all members is chosen as the leader"""
        if auto_leader is not None:
            self._validate_enum(auto_leader, ["first", "random"])
            data["auto_leader"] = auto_leader

        # OPTIONAL - group_limit
        """Limit the maximum number of users in each group (Course Only). Requires
        self signup."""
        if group_limit is not None:
            data["group_limit"] = group_limit

        # OPTIONAL - create_group_count
        """Create this number of groups (Course Only)."""
        if create_group_count is not None:
            data["create_group_count"] = create_group_count

        # OPTIONAL - split_group_count
        """(Deprecated)
        Create this number of groups, and evenly distribute students
        among them. not allowed with "enable_self_signup". because
        the group assignment happens synchronously, it's recommended
        that you instead use the assign_unassigned_members endpoint.
        (Course Only)"""
        if split_group_count is not None:
            data["split_group_count"] = split_group_count

        self.logger.debug("POST /api/v1/accounts/{account_id}/group_categories with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/group_categories".format(**path), data=data, params=params, single_item=True)

    def create_group_category_courses(self, name, course_id, auto_leader=None, create_group_count=None, group_limit=None, self_signup=None, split_group_count=None):
        """
        Create a Group Category.

        Create a new group category
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - name
        """Name of the group category"""
        data["name"] = name

        # OPTIONAL - self_signup
        """Allow students to sign up for a group themselves (Course Only).
        valid values are:
        "enabled":: allows students to self sign up for any group in course
        "restricted":: allows students to self sign up only for groups in the
                       same section null disallows self sign up"""
        if self_signup is not None:
            self._validate_enum(self_signup, ["enabled", "restricted"])
            data["self_signup"] = self_signup

        # OPTIONAL - auto_leader
        """Assigns group leaders automatically when generating and allocating students to groups
        Valid values are:
        "first":: the first student to be allocated to a group is the leader
        "random":: a random student from all members is chosen as the leader"""
        if auto_leader is not None:
            self._validate_enum(auto_leader, ["first", "random"])
            data["auto_leader"] = auto_leader

        # OPTIONAL - group_limit
        """Limit the maximum number of users in each group (Course Only). Requires
        self signup."""
        if group_limit is not None:
            data["group_limit"] = group_limit

        # OPTIONAL - create_group_count
        """Create this number of groups (Course Only)."""
        if create_group_count is not None:
            data["create_group_count"] = create_group_count

        # OPTIONAL - split_group_count
        """(Deprecated)
        Create this number of groups, and evenly distribute students
        among them. not allowed with "enable_self_signup". because
        the group assignment happens synchronously, it's recommended
        that you instead use the assign_unassigned_members endpoint.
        (Course Only)"""
        if split_group_count is not None:
            data["split_group_count"] = split_group_count

        self.logger.debug("POST /api/v1/courses/{course_id}/group_categories with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/group_categories".format(**path), data=data, params=params, single_item=True)

    def update_group_category(self, group_category_id, auto_leader=None, create_group_count=None, group_limit=None, name=None, self_signup=None, split_group_count=None):
        """
        Update a Group Category.

        Modifies an existing group category.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        # OPTIONAL - name
        """Name of the group category"""
        if name is not None:
            data["name"] = name

        # OPTIONAL - self_signup
        """Allow students to sign up for a group themselves (Course Only).
        Valid values are:
        "enabled":: allows students to self sign up for any group in course
        "restricted":: allows students to self sign up only for groups in the
                       same section null disallows self sign up"""
        if self_signup is not None:
            self._validate_enum(self_signup, ["enabled", "restricted"])
            data["self_signup"] = self_signup

        # OPTIONAL - auto_leader
        """Assigns group leaders automatically when generating and allocating students to groups
        Valid values are:
        "first":: the first student to be allocated to a group is the leader
        "random":: a random student from all members is chosen as the leader"""
        if auto_leader is not None:
            self._validate_enum(auto_leader, ["first", "random"])
            data["auto_leader"] = auto_leader

        # OPTIONAL - group_limit
        """Limit the maximum number of users in each group (Course Only). Requires
        self signup."""
        if group_limit is not None:
            data["group_limit"] = group_limit

        # OPTIONAL - create_group_count
        """Create this number of groups (Course Only)."""
        if create_group_count is not None:
            data["create_group_count"] = create_group_count

        # OPTIONAL - split_group_count
        """(Deprecated)
        Create this number of groups, and evenly distribute students
        among them. not allowed with "enable_self_signup". because
        the group assignment happens synchronously, it's recommended
        that you instead use the assign_unassigned_members endpoint.
        (Course Only)"""
        if split_group_count is not None:
            data["split_group_count"] = split_group_count

        self.logger.debug("PUT /api/v1/group_categories/{group_category_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/group_categories/{group_category_id}".format(**path), data=data, params=params, single_item=True)

    def delete_group_category(self, group_category_id):
        """
        Delete a Group Category.

        Deletes a group category and all groups under it. Protected group
        categories can not be deleted, i.e. "communities" and "student_organized".
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        self.logger.debug("DELETE /api/v1/group_categories/{group_category_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/group_categories/{group_category_id}".format(**path), data=data, params=params, no_data=True)

    def list_groups_in_group_category(self, group_category_id):
        """
        List groups in group category.

        Returns a list of groups in a group category
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        self.logger.debug("GET /api/v1/group_categories/{group_category_id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/group_categories/{group_category_id}/groups".format(**path), data=data, params=params, all_pages=True)

    def list_users_in_group_category(self, group_category_id, search_term=None, unassigned=None):
        """
        List users in group category.

        Returns a list of users in the group category.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        # OPTIONAL - search_term
        """The partial name or full ID of the users to match and return in the results
        list. Must be at least 3 characters."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - unassigned
        """Set this value to true if you wish only to search unassigned users in the
        group category."""
        if unassigned is not None:
            params["unassigned"] = unassigned

        self.logger.debug("GET /api/v1/group_categories/{group_category_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/group_categories/{group_category_id}/users".format(**path), data=data, params=params, all_pages=True)

    def assign_unassigned_members(self, group_category_id, sync=None):
        """
        Assign unassigned members.

        Assign all unassigned members as evenly as possible among the existing
        student groups.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id
        """ID"""
        path["group_category_id"] = group_category_id

        # OPTIONAL - sync
        """The assigning is done asynchronously by default. If you would like to
        override this and have the assigning done synchronously, set this value
        to true."""
        if sync is not None:
            data["sync"] = sync

        self.logger.debug("POST /api/v1/group_categories/{group_category_id}/assign_unassigned_members with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/group_categories/{group_category_id}/assign_unassigned_members".format(**path), data=data, params=params, single_item=True)


class Groupcategory(BaseModel):
    """Groupcategory Model."""

    def __init__(self, name=None, self_signup=None, auto_leader=None, context_type=None, role=None, group_limit=None, progress=None, id=None, account_id=None):
        """Init method for Groupcategory class."""
        self._name = name
        self._self_signup = self_signup
        self._auto_leader = auto_leader
        self._context_type = context_type
        self._role = role
        self._group_limit = group_limit
        self._progress = progress
        self._id = id
        self._account_id = account_id

        self.logger = logging.getLogger('pycanvas.Groupcategory')

    @property
    def name(self):
        """The display name of the group category."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def self_signup(self):
        """If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include 'restricted', 'enabled', and null 'enabled' allows students to assign themselves to a group 'restricted' restricts them to only joining a group in their section null disallows students from joining groups."""
        return self._self_signup

    @self_signup.setter
    def self_signup(self, value):
        """Setter for self_signup property."""
        self.logger.warn("Setting values on self_signup will NOT update the remote Canvas instance.")
        self._self_signup = value

    @property
    def auto_leader(self):
        """Gives instructors the ability to automatically have group leaders assigned.  Values include 'random', 'first', and null; 'random' picks a student from the group at random as the leader, 'first' sets the first student to be assigned to the group as the leader."""
        return self._auto_leader

    @auto_leader.setter
    def auto_leader(self, value):
        """Setter for auto_leader property."""
        self.logger.warn("Setting values on auto_leader will NOT update the remote Canvas instance.")
        self._auto_leader = value

    @property
    def context_type(self):
        """The course or account that the category group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'Course', the course_id field would be replaced by an course_id field."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def role(self):
        """Certain types of group categories have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account group categories have a role of null."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def group_limit(self):
        """If self-signup is enabled, group_limit can be set to cap the number of users in each group. If null, there is no limit."""
        return self._group_limit

    @group_limit.setter
    def group_limit(self, value):
        """Setter for group_limit property."""
        self.logger.warn("Setting values on group_limit will NOT update the remote Canvas instance.")
        self._group_limit = value

    @property
    def progress(self):
        """If the group category has not yet finished a randomly student assignment request, a progress object will be attached, which will contain information related to the progress of the assignment request. Refer to the Progress API for more information."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn("Setting values on progress will NOT update the remote Canvas instance.")
        self._progress = value

    @property
    def id(self):
        """The ID of the group category."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def account_id(self):
        """account_id."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn("Setting values on account_id will NOT update the remote Canvas instance.")
        self._account_id = value

