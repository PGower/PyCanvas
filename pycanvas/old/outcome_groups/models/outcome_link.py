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


class OutcomeLink(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, context_id=None, context_type=None, outcome_group=None, outcome=None):
        """
        OutcomeLink - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'context_id': 'int',
            'context_type': 'str',
            'outcome_group': 'OutcomeGroup',
            'outcome': 'Outcome'
        }

        self.attribute_map = {
            'url': 'url',
            'context_id': 'context_id',
            'context_type': 'context_type',
            'outcome_group': 'outcome_group',
            'outcome': 'outcome'
        }

        self._url = url
        self._context_id = context_id
        self._context_type = context_type
        self._outcome_group = outcome_group
        self._outcome = outcome

    @property
    def url(self):
        """
        Gets the url of this OutcomeLink.
        the URL for fetching/updating the outcome link. should be treated as opaque

        :return: The url of this OutcomeLink.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OutcomeLink.
        the URL for fetching/updating the outcome link. should be treated as opaque

        :param url: The url of this OutcomeLink.
        :type: str
        """

        self._url = url

    @property
    def context_id(self):
        """
        Gets the context_id of this OutcomeLink.
        the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups.

        :return: The context_id of this OutcomeLink.
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this OutcomeLink.
        the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups.

        :param context_id: The context_id of this OutcomeLink.
        :type: int
        """

        self._context_id = context_id

    @property
    def context_type(self):
        """
        Gets the context_type of this OutcomeLink.


        :return: The context_type of this OutcomeLink.
        :rtype: str
        """
        return self._context_type

    @context_type.setter
    def context_type(self, context_type):
        """
        Sets the context_type of this OutcomeLink.


        :param context_type: The context_type of this OutcomeLink.
        :type: str
        """

        self._context_type = context_type

    @property
    def outcome_group(self):
        """
        Gets the outcome_group of this OutcomeLink.
        an abbreviated OutcomeGroup object representing the group containing the outcome link.

        :return: The outcome_group of this OutcomeLink.
        :rtype: OutcomeGroup
        """
        return self._outcome_group

    @outcome_group.setter
    def outcome_group(self, outcome_group):
        """
        Sets the outcome_group of this OutcomeLink.
        an abbreviated OutcomeGroup object representing the group containing the outcome link.

        :param outcome_group: The outcome_group of this OutcomeLink.
        :type: OutcomeGroup
        """

        self._outcome_group = outcome_group

    @property
    def outcome(self):
        """
        Gets the outcome of this OutcomeLink.
        an abbreviated Outcome object representing the outcome linked into the containing outcome group.

        :return: The outcome of this OutcomeLink.
        :rtype: Outcome
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """
        Sets the outcome of this OutcomeLink.
        an abbreviated Outcome object representing the outcome linked into the containing outcome group.

        :param outcome: The outcome of this OutcomeLink.
        :type: Outcome
        """

        self._outcome = outcome

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