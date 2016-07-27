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

from ...base_model import BaseModel
from pprint import pformat
from six import iteritems
import re


class OutcomeGroup(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, url=None, parent_outcome_group=None, context_id=None, context_type=None, title=None, description=None, vendor_guid=None, subgroups_url=None, outcomes_url=None, import_url=None, can_edit=None):
        """
        OutcomeGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'url': 'str',
            'parent_outcome_group': 'OutcomeGroup',
            'context_id': 'int',
            'context_type': 'str',
            'title': 'str',
            'description': 'str',
            'vendor_guid': 'str',
            'subgroups_url': 'str',
            'outcomes_url': 'str',
            'import_url': 'str',
            'can_edit': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'url': 'url',
            'parent_outcome_group': 'parent_outcome_group',
            'context_id': 'context_id',
            'context_type': 'context_type',
            'title': 'title',
            'description': 'description',
            'vendor_guid': 'vendor_guid',
            'subgroups_url': 'subgroups_url',
            'outcomes_url': 'outcomes_url',
            'import_url': 'import_url',
            'can_edit': 'can_edit'
        }

        self._id = id
        self._url = url
        self._parent_outcome_group = parent_outcome_group
        self._context_id = context_id
        self._context_type = context_type
        self._title = title
        self._description = description
        self._vendor_guid = vendor_guid
        self._subgroups_url = subgroups_url
        self._outcomes_url = outcomes_url
        self._import_url = import_url
        self._can_edit = can_edit

    @property
    def id(self):
        """
        Gets the id of this OutcomeGroup.
        the ID of the outcome group

        :return: The id of this OutcomeGroup.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OutcomeGroup.
        the ID of the outcome group

        :param id: The id of this OutcomeGroup.
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this OutcomeGroup.
        the URL for fetching/updating the outcome group. should be treated as opaque

        :return: The url of this OutcomeGroup.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OutcomeGroup.
        the URL for fetching/updating the outcome group. should be treated as opaque

        :param url: The url of this OutcomeGroup.
        :type: str
        """

        self._url = url

    @property
    def parent_outcome_group(self):
        """
        Gets the parent_outcome_group of this OutcomeGroup.
        an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form.

        :return: The parent_outcome_group of this OutcomeGroup.
        :rtype: OutcomeGroup
        """
        return self._parent_outcome_group

    @parent_outcome_group.setter
    def parent_outcome_group(self, parent_outcome_group):
        """
        Sets the parent_outcome_group of this OutcomeGroup.
        an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form.

        :param parent_outcome_group: The parent_outcome_group of this OutcomeGroup.
        :type: OutcomeGroup
        """

        self._parent_outcome_group = parent_outcome_group

    @property
    def context_id(self):
        """
        Gets the context_id of this OutcomeGroup.
        the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form.

        :return: The context_id of this OutcomeGroup.
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this OutcomeGroup.
        the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form.

        :param context_id: The context_id of this OutcomeGroup.
        :type: int
        """

        self._context_id = context_id

    @property
    def context_type(self):
        """
        Gets the context_type of this OutcomeGroup.


        :return: The context_type of this OutcomeGroup.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this OutcomeGroup.


        :param context_type: The context_type of this OutcomeGroup.
        :type: str
        """

        self._context_type = context_type

    @property
    def title(self):
        """
        Gets the title of this OutcomeGroup.
        title of the outcome group

        :return: The title of this OutcomeGroup.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OutcomeGroup.
        title of the outcome group

        :param title: The title of this OutcomeGroup.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this OutcomeGroup.
        description of the outcome group. omitted in the abbreviated form.

        :return: The description of this OutcomeGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OutcomeGroup.
        description of the outcome group. omitted in the abbreviated form.

        :param description: The description of this OutcomeGroup.
        :type: str
        """

        self._description = description

    @property
    def vendor_guid(self):
        """
        Gets the vendor_guid of this OutcomeGroup.
        A custom GUID for the learning standard.

        :return: The vendor_guid of this OutcomeGroup.
        :rtype: str
        """
        return self._vendor_guid

    @vendor_guid.setter
    def vendor_guid(self, vendor_guid):
        """
        Sets the vendor_guid of this OutcomeGroup.
        A custom GUID for the learning standard.

        :param vendor_guid: The vendor_guid of this OutcomeGroup.
        :type: str
        """

        self._vendor_guid = vendor_guid

    @property
    def subgroups_url(self):
        """
        Gets the subgroups_url of this OutcomeGroup.
        the URL for listing/creating subgroups under the outcome group. should be treated as opaque

        :return: The subgroups_url of this OutcomeGroup.
        :rtype: str
        """
        return self._subgroups_url

    @subgroups_url.setter
    def subgroups_url(self, subgroups_url):
        """
        Sets the subgroups_url of this OutcomeGroup.
        the URL for listing/creating subgroups under the outcome group. should be treated as opaque

        :param subgroups_url: The subgroups_url of this OutcomeGroup.
        :type: str
        """

        self._subgroups_url = subgroups_url

    @property
    def outcomes_url(self):
        """
        Gets the outcomes_url of this OutcomeGroup.
        the URL for listing/creating outcome links under the outcome group. should be treated as opaque

        :return: The outcomes_url of this OutcomeGroup.
        :rtype: str
        """
        return self._outcomes_url

    @outcomes_url.setter
    def outcomes_url(self, outcomes_url):
        """
        Sets the outcomes_url of this OutcomeGroup.
        the URL for listing/creating outcome links under the outcome group. should be treated as opaque

        :param outcomes_url: The outcomes_url of this OutcomeGroup.
        :type: str
        """

        self._outcomes_url = outcomes_url

    @property
    def import_url(self):
        """
        Gets the import_url of this OutcomeGroup.
        the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form.

        :return: The import_url of this OutcomeGroup.
        :rtype: str
        """
        return self._import_url

    @import_url.setter
    def import_url(self, import_url):
        """
        Sets the import_url of this OutcomeGroup.
        the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form.

        :param import_url: The import_url of this OutcomeGroup.
        :type: str
        """

        self._import_url = import_url

    @property
    def can_edit(self):
        """
        Gets the can_edit of this OutcomeGroup.
        whether the current user can update the outcome group

        :return: The can_edit of this OutcomeGroup.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """
        Sets the can_edit of this OutcomeGroup.
        whether the current user can update the outcome group

        :param can_edit: The can_edit of this OutcomeGroup.
        :type: bool
        """

        self._can_edit = can_edit

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other