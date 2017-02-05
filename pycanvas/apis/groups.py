"""Groups API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class GroupsAPI(BaseCanvasAPI):
    """Groups API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GroupsAPI."""
        super(GroupsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.GroupsAPI")

    def list_your_groups(self, context_type=None):
        """
        List your groups.

        Returns a list of active groups for the current user.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - context_type - Only include groups that are in this type of context.
        if context_type is not None:
            self._validate_enum(context_type, ["Account", "Course"])
            params["context_type"] = context_type

        self.logger.debug("GET /api/v1/users/self/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/self/groups".format(**path), data=data, params=params, all_pages=True)

    def list_groups_available_in_context_accounts(self, account_id, only_own_groups=None):
        """
        List the groups available in a context.

        Returns the list of active groups in the given context that are visible to user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # OPTIONAL - only_own_groups - Will only include groups that the user belongs to if this is set
        if only_own_groups is not None:
            params["only_own_groups"] = only_own_groups

        self.logger.debug("GET /api/v1/accounts/{account_id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/groups".format(**path), data=data, params=params, all_pages=True)

    def list_groups_available_in_context_courses(self, course_id, only_own_groups=None):
        """
        List the groups available in a context.

        Returns the list of active groups in the given context that are visible to user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - only_own_groups - Will only include groups that the user belongs to if this is set
        if only_own_groups is not None:
            params["only_own_groups"] = only_own_groups

        self.logger.debug("GET /api/v1/courses/{course_id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/groups".format(**path), data=data, params=params, all_pages=True)

    def get_single_group(self, group_id, include=None):
        """
        Get a single group.

        Returns the data for a single group, or a 401 if the caller doesn't have
        the rights to see it.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - include - - "permissions": Include permissions the current user has for the group.
        if include is not None:
            self._validate_enum(include, ["permissions"])
            params["include"] = include

        self.logger.debug("GET /api/v1/groups/{group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}".format(**path), data=data, params=params, single_item=True)

    def create_group_groups(self, description=None, is_public=None, join_level=None, name=None, storage_quota_mb=None):
        """
        Create a group.

        Creates a new group. Groups created using the "/api/v1/groups/"
        endpoint will be community groups.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - name - The name of the group
        if name is not None:
            data["name"] = name
        # OPTIONAL - description - A description of the group
        if description is not None:
            data["description"] = description
        # OPTIONAL - is_public - whether the group is public (applies only to community groups)
        if is_public is not None:
            data["is_public"] = is_public
        # OPTIONAL - join_level - no description
        if join_level is not None:
            self._validate_enum(join_level, ["parent_context_auto_join", "parent_context_request", "invitation_only"])
            data["join_level"] = join_level
        # OPTIONAL - storage_quota_mb - The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission.
        if storage_quota_mb is not None:
            data["storage_quota_mb"] = storage_quota_mb

        self.logger.debug("POST /api/v1/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups".format(**path), data=data, params=params, single_item=True)

    def create_group_group_categories(self, group_category_id, description=None, is_public=None, join_level=None, name=None, storage_quota_mb=None):
        """
        Create a group.

        Creates a new group. Groups created using the "/api/v1/groups/"
        endpoint will be community groups.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_category_id - ID
        path["group_category_id"] = group_category_id
        # OPTIONAL - name - The name of the group
        if name is not None:
            data["name"] = name
        # OPTIONAL - description - A description of the group
        if description is not None:
            data["description"] = description
        # OPTIONAL - is_public - whether the group is public (applies only to community groups)
        if is_public is not None:
            data["is_public"] = is_public
        # OPTIONAL - join_level - no description
        if join_level is not None:
            self._validate_enum(join_level, ["parent_context_auto_join", "parent_context_request", "invitation_only"])
            data["join_level"] = join_level
        # OPTIONAL - storage_quota_mb - The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission.
        if storage_quota_mb is not None:
            data["storage_quota_mb"] = storage_quota_mb

        self.logger.debug("POST /api/v1/group_categories/{group_category_id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/group_categories/{group_category_id}/groups".format(**path), data=data, params=params, single_item=True)

    def edit_group(self, group_id, avatar_id=None, description=None, is_public=None, join_level=None, members=None, name=None, storage_quota_mb=None):
        """
        Edit a group.

        Modifies an existing group.  Note that to set an avatar image for the
        group, you must first upload the image file to the group, and the use the
        id in the response as the argument to this function.  See the
        {file:file_uploads.html File Upload Documentation} for details on the file
        upload workflow.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - name - The name of the group
        if name is not None:
            data["name"] = name
        # OPTIONAL - description - A description of the group
        if description is not None:
            data["description"] = description
        # OPTIONAL - is_public - Whether the group is public (applies only to community groups). Currently you cannot set a group back to private once it has been made public.
        if is_public is not None:
            data["is_public"] = is_public
        # OPTIONAL - join_level - no description
        if join_level is not None:
            self._validate_enum(join_level, ["parent_context_auto_join", "parent_context_request", "invitation_only"])
            data["join_level"] = join_level
        # OPTIONAL - avatar_id - The id of the attachment previously uploaded to the group that you would like to use as the avatar image for this group.
        if avatar_id is not None:
            data["avatar_id"] = avatar_id
        # OPTIONAL - storage_quota_mb - The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission.
        if storage_quota_mb is not None:
            data["storage_quota_mb"] = storage_quota_mb
        # OPTIONAL - members - An array of user ids for users you would like in the group. Users not in the group will be sent invitations. Existing group members who aren't in the list will be removed from the group.
        if members is not None:
            data["members"] = members

        self.logger.debug("PUT /api/v1/groups/{group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}".format(**path), data=data, params=params, single_item=True)

    def delete_group(self, group_id):
        """
        Delete a group.

        Deletes a group and removes all members.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("DELETE /api/v1/groups/{group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}".format(**path), data=data, params=params, single_item=True)

    def invite_others_to_group(self, group_id, invitees):
        """
        Invite others to a group.

        Sends an invitation to all supplied email addresses which will allow the
        receivers to join the group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - invitees - An array of email addresses to be sent invitations.
        data["invitees"] = invitees

        self.logger.debug("POST /api/v1/groups/{group_id}/invite with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/invite".format(**path), data=data, params=params, no_data=True)

    def list_group_s_users(self, group_id, include=None, search_term=None):
        """
        List group's users.

        Returns a list of users in the group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - search_term - The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - include - - "avatar_url": Include users' avatar_urls.
        if include is not None:
            self._validate_enum(include, ["avatar_url"])
            params["include"] = include

        self.logger.debug("GET /api/v1/groups/{group_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/users".format(**path), data=data, params=params, all_pages=True)

    def upload_file(self, group_id):
        """
        Upload a file.

        Upload a file to the group.
        
        This API endpoint is the first step in uploading a file to a group.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.
        
        Only those with the "Manage Files" permission on a group can upload files
        to the group. By default, this is anybody participating in the
        group, or any admin over the group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("POST /api/v1/groups/{group_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/files".format(**path), data=data, params=params, no_data=True)

    def preview_processed_html(self, group_id, html=None):
        """
        Preview processed html.

        Preview html content processed for this group
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - html - The html content to process
        if html is not None:
            data["html"] = html

        self.logger.debug("POST /api/v1/groups/{group_id}/preview_html with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/preview_html".format(**path), data=data, params=params, no_data=True)

    def group_activity_stream(self, group_id):
        """
        Group activity stream.

        Returns the current user's group-specific activity stream, paginated.
        
        For full documentation, see the API documentation for the user activity
        stream, in the user api.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/activity_stream with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/activity_stream".format(**path), data=data, params=params, no_data=True)

    def group_activity_stream_summary(self, group_id):
        """
        Group activity stream summary.

        Returns a summary of the current user's group-specific activity stream.
        
        For full documentation, see the API documentation for the user activity
        stream summary, in the user api.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/activity_stream/summary with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/activity_stream/summary".format(**path), data=data, params=params, no_data=True)

    def list_group_memberships(self, group_id, filter_states=None):
        """
        List group memberships.

        List the members of a group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - filter_states - Only list memberships with the given workflow_states. By default it will return all memberships.
        if filter_states is not None:
            self._validate_enum(filter_states, ["accepted", "invited", "requested"])
            params["filter_states"] = filter_states

        self.logger.debug("GET /api/v1/groups/{group_id}/memberships with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/memberships".format(**path), data=data, params=params, all_pages=True)

    def create_membership(self, group_id, user_id=None):
        """
        Create a membership.

        Join, or request to join, a group, depending on the join_level of the
        group.  If the membership or join request already exists, then it is simply
        returned
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - user_id - no description
        if user_id is not None:
            data["user_id"] = user_id

        self.logger.debug("POST /api/v1/groups/{group_id}/memberships with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/memberships".format(**path), data=data, params=params, single_item=True)

    def update_membership_memberships(self, group_id, membership_id, moderator=None, workflow_state=None):
        """
        Update a membership.

        Accept a membership request, or add/remove moderator rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - membership_id - ID
        path["membership_id"] = membership_id
        # OPTIONAL - workflow_state - Currently, the only allowed value is "accepted"
        if workflow_state is not None:
            self._validate_enum(workflow_state, ["accepted"])
            data["workflow_state"] = workflow_state
        # OPTIONAL - moderator - no description
        if moderator is not None:
            data["moderator"] = moderator

        self.logger.debug("PUT /api/v1/groups/{group_id}/memberships/{membership_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/memberships/{membership_id}".format(**path), data=data, params=params, single_item=True)

    def update_membership_users(self, user_id, group_id, moderator=None, workflow_state=None):
        """
        Update a membership.

        Accept a membership request, or add/remove moderator rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # OPTIONAL - workflow_state - Currently, the only allowed value is "accepted"
        if workflow_state is not None:
            self._validate_enum(workflow_state, ["accepted"])
            data["workflow_state"] = workflow_state
        # OPTIONAL - moderator - no description
        if moderator is not None:
            data["moderator"] = moderator

        self.logger.debug("PUT /api/v1/groups/{group_id}/users/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/users/{user_id}".format(**path), data=data, params=params, single_item=True)

    def leave_group_memberships(self, group_id, membership_id):
        """
        Leave a group.

        Leave a group if you are allowed to leave (some groups, such as sets of
        course groups created by teachers, cannot be left). You may also use 'self'
        in place of a membership_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - membership_id - ID
        path["membership_id"] = membership_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/memberships/{membership_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/memberships/{membership_id}".format(**path), data=data, params=params, no_data=True)

    def leave_group_users(self, user_id, group_id):
        """
        Leave a group.

        Leave a group if you are allowed to leave (some groups, such as sets of
        course groups created by teachers, cannot be left). You may also use 'self'
        in place of a membership_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("DELETE /api/v1/groups/{group_id}/users/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/users/{user_id}".format(**path), data=data, params=params, no_data=True)


class Group(BaseModel):
    """Group Model."""

    def __init__(self, members_count=None, description=None, context_type=None, storage_quota_mb=None, join_level=None, followed_by_user=None, group_category_id=None, sis_import_id=None, avatar_url=None, role=None, sis_group_id=None, course_id=None, is_public=None, permissions=None, id=None, name=None):
        """Init method for Group class."""
        self._members_count = members_count
        self._description = description
        self._context_type = context_type
        self._storage_quota_mb = storage_quota_mb
        self._join_level = join_level
        self._followed_by_user = followed_by_user
        self._group_category_id = group_category_id
        self._sis_import_id = sis_import_id
        self._avatar_url = avatar_url
        self._role = role
        self._sis_group_id = sis_group_id
        self._course_id = course_id
        self._is_public = is_public
        self._permissions = permissions
        self._id = id
        self._name = name

        self.logger = logging.getLogger('pycanvas.Group')

    @property
    def members_count(self):
        """The number of members currently in the group."""
        return self._members_count

    @members_count.setter
    def members_count(self, value):
        """Setter for members_count property."""
        self.logger.warn("Setting values on members_count will NOT update the remote Canvas instance.")
        self._members_count = value

    @property
    def description(self):
        """A description of the group. This is plain text."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def context_type(self):
        """The course or account that the group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'account', the course_id field would be replaced by an account_id field."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def storage_quota_mb(self):
        """the storage quota for the group, in megabytes."""
        return self._storage_quota_mb

    @storage_quota_mb.setter
    def storage_quota_mb(self, value):
        """Setter for storage_quota_mb property."""
        self.logger.warn("Setting values on storage_quota_mb will NOT update the remote Canvas instance.")
        self._storage_quota_mb = value

    @property
    def join_level(self):
        """How people are allowed to join the group.  For all groups except for community groups, the user must share the group's parent course or account.  For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are 'parent_context_auto_join', 'parent_context_request', and 'invitation_only'.  For class groups, where students are divided up and should only be part of one group of the category, this value will always be 'invitation_only', and is not relevant. * If 'parent_context_auto_join', anyone can join and will be automatically accepted. * If 'parent_context_request', anyone  can request to join, which must be approved by a group moderator. * If 'invitation_only', only those how have received an invitation my join the group, by accepting that invitation."""
        return self._join_level

    @join_level.setter
    def join_level(self, value):
        """Setter for join_level property."""
        self.logger.warn("Setting values on join_level will NOT update the remote Canvas instance.")
        self._join_level = value

    @property
    def followed_by_user(self):
        """Whether or not the current user is following this group."""
        return self._followed_by_user

    @followed_by_user.setter
    def followed_by_user(self, value):
        """Setter for followed_by_user property."""
        self.logger.warn("Setting values on followed_by_user will NOT update the remote Canvas instance.")
        self._followed_by_user = value

    @property
    def group_category_id(self):
        """The ID of the group's category."""
        return self._group_category_id

    @group_category_id.setter
    def group_category_id(self, value):
        """Setter for group_category_id property."""
        self.logger.warn("Setting values on group_category_id will NOT update the remote Canvas instance.")
        self._group_category_id = value

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
    def avatar_url(self):
        """The url of the group's avatar."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn("Setting values on avatar_url will NOT update the remote Canvas instance.")
        self._avatar_url = value

    @property
    def role(self):
        """Certain types of groups have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account groups have a role of null."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def sis_group_id(self):
        """The SIS ID of the group. Only included if the user has permission to view SIS information."""
        return self._sis_group_id

    @sis_group_id.setter
    def sis_group_id(self, value):
        """Setter for sis_group_id property."""
        self.logger.warn("Setting values on sis_group_id will NOT update the remote Canvas instance.")
        self._sis_group_id = value

    @property
    def course_id(self):
        """course_id."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def is_public(self):
        """Whether or not the group is public.  Currently only community groups can be made public.  Also, once a group has been set to public, it cannot be changed back to private."""
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        """Setter for is_public property."""
        self.logger.warn("Setting values on is_public will NOT update the remote Canvas instance.")
        self._is_public = value

    @property
    def permissions(self):
        """optional: the permissions the user has for the group. returned only for a single group and include[]=permissions."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

    @property
    def id(self):
        """The ID of the group."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """The display name of the group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Groupmembership(BaseModel):
    """Groupmembership Model."""

    def __init__(self, user_id=None, workflow_state=None, moderator=None, sis_import_id=None, just_created=None, group_id=None, id=None):
        """Init method for Groupmembership class."""
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._moderator = moderator
        self._sis_import_id = sis_import_id
        self._just_created = just_created
        self._group_id = group_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.Groupmembership')

    @property
    def user_id(self):
        """The id of the user object to which the membership belongs."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def moderator(self):
        """Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate)."""
        return self._moderator

    @moderator.setter
    def moderator(self, value):
        """Setter for moderator property."""
        self.logger.warn("Setting values on moderator will NOT update the remote Canvas instance.")
        self._moderator = value

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
    def just_created(self):
        """optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member."""
        return self._just_created

    @just_created.setter
    def just_created(self, value):
        """Setter for just_created property."""
        self.logger.warn("Setting values on just_created will NOT update the remote Canvas instance.")
        self._just_created = value

    @property
    def group_id(self):
        """The id of the group object to which the membership belongs."""
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        """Setter for group_id property."""
        self.logger.warn("Setting values on group_id will NOT update the remote Canvas instance.")
        self._group_id = value

    @property
    def id(self):
        """The id of the membership object."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

