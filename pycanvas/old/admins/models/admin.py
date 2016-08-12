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


class Admin(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, role=None, user=None, status=None):
        """
        Admin - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'role': 'str',
            'user': 'User',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'role': 'role',
            'user': 'user',
            'status': 'status'
        }

        self._id = id
        self._role = role
        self._user = user
        self._status = status

    @property
    def id(self):
        """
        Gets the id of this Admin.
        The unique identifier for the account role/user assignment.

        :return: The id of this Admin.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Admin.
        The unique identifier for the account role/user assignment.

        :param id: The id of this Admin.
        :type: int
        """

        self._id = id

    @property
    def role(self):
        """
        Gets the role of this Admin.
        The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API.

        :return: The role of this Admin.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Admin.
        The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API.

        :param role: The role of this Admin.
        :type: str
        """

        self._role = role

    @property
    def user(self):
        """
        Gets the user of this Admin.
        The user the role is assigned to. See the Users API for details.

        :return: The user of this Admin.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Admin.
        The user the role is assigned to. See the Users API for details.

        :param user: The user of this Admin.
        :type: User
        """

        self._user = user

    @property
    def status(self):
        """
        Gets the status of this Admin.
        The status of the account role/user assignment.

        :return: The status of this Admin.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Admin.
        The status of the account role/user assignment.

        :param status: The status of this Admin.
        :type: str
        """

        self._status = status

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