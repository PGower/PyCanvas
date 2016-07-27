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


class AssignmentgroupsApi(BaseApi):
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

    # OPERATIONID: create_assignment_group
    def create_assignment_group(self, course_id, **kwargs):
        """
        Create an Assignment Group
        Create a new assignment group for this course.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_assignment_group_with_http_info(course_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str name: The assignment group's name
        :param int position: The position of this assignment group in relation to the other assignment groups
        :param Object group_weight: The percent of the total grade that this assignment group represents
        :param str rules: The grading rules that are applied within this assignment group See the Assignment Group object definition for format
        :return: AssignmentGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'name', 'position', 'group_weight', 'rules']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_assignment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `create_assignment_group`")

        resource_path = '/v1/courses/{course_id}/assignment_groups'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'position' in params:
            form_params.append(('position', params['position']))
        if 'group_weight' in params:
            form_params.append(('group_weight', params['group_weight']))
        if 'rules' in params:
            form_params.append(('rules', params['rules']))

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
                                            response_type='AssignmentGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: destroy_assignment_group
    def destroy_assignment_group(self, course_id, assignment_group_id, **kwargs):
        """
        Destroy an Assignment Group
        Deletes the assignment group with the given id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.destroy_assignment_group_with_http_info(course_id, assignment_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str assignment_group_id: ID (required)
        :param str move_assignment_to: The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted.
        :return: AssignmentGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'assignment_group_id', 'move_assignment_to']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_assignment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `destroy_assignment_group`")
        # verify the required parameter 'assignment_group_id' is set
        if ('assignment_group_id' not in params) or (params['assignment_group_id'] is None):
            raise ValueError("Missing the required parameter `assignment_group_id` when calling `destroy_assignment_group`")

        resource_path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'assignment_group_id' in params:
            path_params['assignment_group_id'] = params['assignment_group_id']

        query_params = {}
        if 'move_assignment_to' in params:
            query_params['move_assignment_to'] = params['move_assignment_to']
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
                                            response_type='AssignmentGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: edit_assignment_group
    def edit_assignment_group(self, course_id, assignment_group_id, **kwargs):
        """
        Edit an Assignment Group
        Modify an existing Assignment Group. Accepts the same parameters as Assignment Group creation

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.edit_assignment_group_with_http_info(course_id, assignment_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str assignment_group_id: ID (required)
        :return: AssignmentGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'assignment_group_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_assignment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `edit_assignment_group`")
        # verify the required parameter 'assignment_group_id' is set
        if ('assignment_group_id' not in params) or (params['assignment_group_id'] is None):
            raise ValueError("Missing the required parameter `assignment_group_id` when calling `edit_assignment_group`")

        resource_path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'assignment_group_id' in params:
            path_params['assignment_group_id'] = params['assignment_group_id']

        query_params = {}
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

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AssignmentGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: get_assignment_group
    def get_assignment_group(self, course_id, assignment_group_id, **kwargs):
        """
        Get an Assignment Group
        Returns the assignment group with the given id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_assignment_group_with_http_info(course_id, assignment_group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param str assignment_group_id: ID (required)
        :param list[str] include: Associations to include with the group. \"discussion_topic\" and \"assignment_visibility\" are only valid if \"assignments\" is also included. The \"assignment_visibility\" option additionally requires that the Differentiated Assignments course feature be turned on.
        :param bool override_assignment_dates: Apply assignment overrides for each assignment, defaults to true.
        :param int grading_period_id: The id of the grading period in which assignment groups are being requested (Requires the Multiple Grading Periods account feature turned on)
        :return: AssignmentGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'assignment_group_id', 'include', 'override_assignment_dates', 'grading_period_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assignment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_assignment_group`")
        # verify the required parameter 'assignment_group_id' is set
        if ('assignment_group_id' not in params) or (params['assignment_group_id'] is None):
            raise ValueError("Missing the required parameter `assignment_group_id` when calling `get_assignment_group`")

        resource_path = '/v1/courses/{course_id}/assignment_groups/{assignment_group_id}'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']
        if 'assignment_group_id' in params:
            path_params['assignment_group_id'] = params['assignment_group_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']
        if 'override_assignment_dates' in params:
            query_params['override_assignment_dates'] = params['override_assignment_dates']
        if 'grading_period_id' in params:
            query_params['grading_period_id'] = params['grading_period_id']
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
                                            response_type='AssignmentGroup',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_assignment_groups
    def list_assignment_groups(self, course_id, **kwargs):
        """
        List assignment groups
        Returns the list of assignment groups for the current context. The returned groups are sorted by their position field.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_assignment_groups_with_http_info(course_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str course_id: ID (required)
        :param list[str] include: Associations to include with the group. \"discussion_topic\", \"all_dates\" \"assignment_visibility\" are only valid are only valid if \"assignments\" is also included. The \"assignment_visibility\" option additionally requires that the Differentiated Assignments course feature be turned on.
        :param bool override_assignment_dates: Apply assignment overrides for each assignment, defaults to true.
        :param int grading_period_id: The id of the grading period in which assignment groups are being requested (Requires the Multiple Grading Periods account feature turned on)
        :return: list[AssignmentGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'include', 'override_assignment_dates', 'grading_period_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_assignment_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params) or (params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `list_assignment_groups`")

        resource_path = '/v1/courses/{course_id}/assignment_groups'.replace('{format}', 'json')
        path_params = {}
        if 'course_id' in params:
            path_params['course_id'] = params['course_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']
        if 'override_assignment_dates' in params:
            query_params['override_assignment_dates'] = params['override_assignment_dates']
        if 'grading_period_id' in params:
            query_params['grading_period_id'] = params['grading_period_id']
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
                                            response_type='list[AssignmentGroup]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))