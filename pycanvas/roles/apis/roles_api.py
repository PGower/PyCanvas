# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ...base_api import BaseApi
from ...configuration import Configuration
from ..api_client import ApiClient


class RolesApi(BaseApi):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    # OPERATIONID: activate_role
    def activate_role(self, account_id, id, role_id, **kwargs):
        """
        Activate a role
        Re-activates an inactive role (allowing it to be assigned to new users)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.activate_role_with_http_info(account_id, id, role_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :param int role_id: The unique identifier for the role (required)
        :param Object role: The name for the role
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id', 'role_id', 'role']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `activate_role`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `activate_role`")
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params) or (params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `activate_role`")

        resource_path = '/v1/accounts/{account_id}/roles/{id}/activate'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'role_id' in params:
            form_params.append(('role_id', params['role_id']))
        if 'role' in params:
            form_params.append(('role', params['role']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Role',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: create_new_role
    def create_new_role(self, account_id, label, **kwargs):
        """
        Create a new role
        Create a new course-level or account-level role.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_new_role_with_http_info(account_id, label, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str label: Label for the role. (required)
        :param str role: Deprecated alias for label.
        :param str base_role_type: Specifies the role type that will be used as a base for the permissions granted to this role. Defaults to 'AccountMembership' if absent
        :param bool permissions_x_explicit: no description
        :param bool permissions_x_enabled: If explicit is 1 and enabled is 1, permission <X> will be explicitly granted to this role. If explicit is 1 and enabled has any other value (typically 0), permission <X> will be explicitly denied to this role. If explicit is any other value (typically 0) or absent, or if enabled is absent, the value for permission <X> will be inherited from upstream. Ignored if permission <X> is locked upstream (in an ancestor account). May occur multiple times with unique values for <X>. Recognized permission names for <X> are: [For Account-Level Roles Only] become_user -- Become other users manage_account_memberships -- Add/remove other admins for the account manage_account_settings -- Manage account-level settings manage_alerts -- Manage global alerts manage_courses -- Manage ( add / edit / delete ) courses manage_developer_keys -- Manage developer keys manage_global_outcomes -- Manage learning outcomes manage_jobs -- Manage background jobs manage_role_overrides -- Manage permissions manage_storage_quotas -- Set storage quotas for courses, groups, and users manage_sis -- Import and manage SIS data manage_site_settings -- Manage site-wide and plugin settings manage_user_logins -- Modify login details for users read_course_content -- View course content read_course_list -- View the list of courses read_messages -- View notifications sent to users site_admin -- Use the Site Admin section and admin all other accounts view_error_reports -- View error reports view_statistics -- View statistics manage_feature_flags -- Enable or disable features at an account level [For both Account-Level and Course-Level roles] Note: Applicable enrollment types for course-level roles are given in brackets: S = student, T = teacher, A = TA, D = designer, O = observer. Lower-case letters indicate permissions that are off by default. A missing letter indicates the permission cannot be enabled for the role or any derived custom roles. change_course_state -- [ TaD ] Change course state comment_on_others_submissions -- [sTAD ] View all students' submissions and make comments on them create_collaborations -- [STADo] Create student collaborations create_conferences -- [STADo] Create web conferences manage_admin_users -- [ Tad ] Add/remove other teachers, course designers or TAs to the course manage_assignments -- [ TADo] Manage (add / edit / delete) assignments and quizzes manage_calendar -- [sTADo] Add, edit and delete events on the course calendar manage_content -- [ TADo] Manage all other course content manage_files -- [ TADo] Manage (add / edit / delete) course files manage_grades -- [ TA ] Edit grades manage_groups -- [ TAD ] Manage (create / edit / delete) groups manage_interaction_alerts -- [ Ta ] Manage alerts manage_outcomes -- [sTaDo] Manage learning outcomes manage_sections -- [ TaD ] Manage (create / edit / delete) course sections manage_students -- [ TAD ] Add/remove students for the course manage_user_notes -- [ TA ] Manage faculty journal entries manage_rubrics -- [ TAD ] Edit assessing rubrics manage_wiki -- [ TADo] Manage wiki (add / edit / delete pages) read_forum -- [STADO] View discussions moderate_forum -- [sTADo] Moderate discussions (delete/edit others' posts, lock topics) post_to_forum -- [STADo] Post to discussions read_question_banks -- [ TADo] View and link to question banks read_reports -- [ TAD ] View usage reports for the course read_roster -- [STADo] See the list of users read_sis -- [sTa ] Read SIS data send_messages -- [STADo] Send messages to individual course members send_messages_all -- [sTADo] Send messages to the entire class view_all_grades -- [ TAd ] View all grades view_group_pages -- [sTADo] View the group pages of all student groups Some of these permissions are applicable only for roles on the site admin account, on a root account, or for course-level roles with a particular base role type; if a specified permission is inapplicable, it will be ignored. Additional permissions may exist based on installed plugins.
        :param bool permissions_x_locked: If the value is 1, permission <X> will be locked downstream (new roles in subaccounts cannot override the setting). For any other value, permission <X> is left unlocked. Ignored if permission <X> is already locked upstream. May occur multiple times with unique values for <X>.
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'label', 'role', 'base_role_type', 'permissions_x_explicit', 'permissions_x_enabled', 'permissions_x_locked']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_new_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_new_role`")
        # verify the required parameter 'label' is set
        if ('label' not in params) or (params['label'] is None):
            raise ValueError("Missing the required parameter `label` when calling `create_new_role`")

        resource_path = '/v1/accounts/{account_id}/roles'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'label' in params:
            form_params.append(('label', params['label']))
        if 'role' in params:
            form_params.append(('role', params['role']))
        if 'base_role_type' in params:
            form_params.append(('base_role_type', params['base_role_type']))
        if 'permissions_x_explicit' in params:
            form_params.append(('permissions[&lt;X&gt;][explicit]', params['permissions_x_explicit']))
        if 'permissions_x_enabled' in params:
            form_params.append(('permissions[&lt;X&gt;][enabled]', params['permissions_x_enabled']))
        if 'permissions_x_locked' in params:
            form_params.append(('permissions[&lt;X&gt;][locked]', params['permissions_x_locked']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Role',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: deactivate_role
    def deactivate_role(self, account_id, id, role_id, **kwargs):
        """
        Deactivate a role
        Deactivates a custom role.  This hides it in the user interface and prevents it from being assigned to new users.  Existing users assigned to the role will continue to function with the same permissions they had previously. Built-in roles cannot be deactivated.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.deactivate_role_with_http_info(account_id, id, role_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :param int role_id: The unique identifier for the role (required)
        :param str role: The name for the role
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id', 'role_id', 'role']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deactivate_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `deactivate_role`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `deactivate_role`")
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params) or (params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `deactivate_role`")

        resource_path = '/v1/accounts/{account_id}/roles/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'role_id' in params:
            query_params['role_id'] = params['role_id']
        if 'role' in params:
            query_params['role'] = params['role']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Role',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: get_single_role
    def get_single_role(self, id, account_id, role_id, **kwargs):
        """
        Get a single role
        Retrieve information about a single role

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_single_role_with_http_info(id, account_id, role_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param str account_id: The id of the account containing the role (required)
        :param int role_id: The unique identifier for the role (required)
        :param str role: The name for the role
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'account_id', 'role_id', 'role']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_single_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_single_role`")
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_single_role`")
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params) or (params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `get_single_role`")

        resource_path = '/v1/accounts/{account_id}/roles/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'role_id' in params:
            query_params['role_id'] = params['role_id']
        if 'role' in params:
            query_params['role'] = params['role']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Role',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_roles
    def list_roles(self, account_id, **kwargs):
        """
        List roles
        List the roles available to an account.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_roles_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The id of the account to retrieve roles for. (required)
        :param list[str] state: Filter by role state. If this argument is omitted, only 'active' roles are returned.
        :param bool show_inherited: If this argument is true, all roles inherited from parent accounts will be included.
        :return: list[Role]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'state', 'show_inherited']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_roles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_roles`")

        resource_path = '/v1/accounts/{account_id}/roles'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = {}
        if 'state' in params:
            query_params['state'] = params['state']
        if 'show_inherited' in params:
            query_params['show_inherited'] = params['show_inherited']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Role]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: update_role
    def update_role(self, account_id, id, **kwargs):
        """
        Update a role
        Update permissions for an existing role.  Recognized roles are: * TeacherEnrollment * StudentEnrollment * TaEnrollment * ObserverEnrollment * DesignerEnrollment * AccountAdmin * Any previously created custom role

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_role_with_http_info(account_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: ID (required)
        :param str id: ID (required)
        :param str label: The label for the role. Can only change the label of a custom role that belongs directly to the account.
        :param bool permissions_x_explicit: no description
        :param bool permissions_x_enabled: These arguments are described in the documentation for the {api:RoleOverridesController#add_role add_role method}.
        :return: Role
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'id', 'label', 'permissions_x_explicit', 'permissions_x_enabled']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_role`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_role`")

        resource_path = '/v1/accounts/{account_id}/roles/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'label' in params:
            form_params.append(('label', params['label']))
        if 'permissions_x_explicit' in params:
            form_params.append(('permissions[&lt;X&gt;][explicit]', params['permissions_x_explicit']))
        if 'permissions_x_enabled' in params:
            form_params.append(('permissions[&lt;X&gt;][enabled]', params['permissions_x_enabled']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Role',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))