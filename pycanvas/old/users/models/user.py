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


class User(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, sortable_name=None, short_name=None, sis_user_id=None, sis_import_id=None, sis_login_id=None, login_id=None, avatar_url=None, enrollments=None, email=None, locale=None, last_login=None, time_zone=None, bio=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'sortable_name': 'str',
            'short_name': 'str',
            'sis_user_id': 'str',
            'sis_import_id': 'int',
            'sis_login_id': 'str',
            'login_id': 'str',
            'avatar_url': 'str',
            'enrollments': 'list[Enrollment]',
            'email': 'str',
            'locale': 'str',
            'last_login': 'datetime',
            'time_zone': 'str',
            'bio': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'sortable_name': 'sortable_name',
            'short_name': 'short_name',
            'sis_user_id': 'sis_user_id',
            'sis_import_id': 'sis_import_id',
            'sis_login_id': 'sis_login_id',
            'login_id': 'login_id',
            'avatar_url': 'avatar_url',
            'enrollments': 'enrollments',
            'email': 'email',
            'locale': 'locale',
            'last_login': 'last_login',
            'time_zone': 'time_zone',
            'bio': 'bio'
        }

        self._id = id
        self._name = name
        self._sortable_name = sortable_name
        self._short_name = short_name
        self._sis_user_id = sis_user_id
        self._sis_import_id = sis_import_id
        self._sis_login_id = sis_login_id
        self._login_id = login_id
        self._avatar_url = avatar_url
        self._enrollments = enrollments
        self._email = email
        self._locale = locale
        self._last_login = last_login
        self._time_zone = time_zone
        self._bio = bio

    @property
    def id(self):
        """
        Gets the id of this User.
        The ID of the user.

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        The ID of the user.

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this User.
        The name of the user.

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        The name of the user.

        :param name: The name of this User.
        :type: str
        """

        self._name = name

    @property
    def sortable_name(self):
        """
        Gets the sortable_name of this User.
        The name of the user that is should be used for sorting groups of users, such as in the gradebook.

        :return: The sortable_name of this User.
        :rtype: str
        """
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, sortable_name):
        """
        Sets the sortable_name of this User.
        The name of the user that is should be used for sorting groups of users, such as in the gradebook.

        :param sortable_name: The sortable_name of this User.
        :type: str
        """

        self._sortable_name = sortable_name

    @property
    def short_name(self):
        """
        Gets the short_name of this User.
        A short name the user has selected, for use in conversations or other less formal places through the site.

        :return: The short_name of this User.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this User.
        A short name the user has selected, for use in conversations or other less formal places through the site.

        :param short_name: The short_name of this User.
        :type: str
        """

        self._short_name = short_name

    @property
    def sis_user_id(self):
        """
        Gets the sis_user_id of this User.
        The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information.

        :return: The sis_user_id of this User.
        :rtype: str
        """
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, sis_user_id):
        """
        Sets the sis_user_id of this User.
        The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information.

        :param sis_user_id: The sis_user_id of this User.
        :type: str
        """

        self._sis_user_id = sis_user_id

    @property
    def sis_import_id(self):
        """
        Gets the sis_import_id of this User.
        The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information.

        :return: The sis_import_id of this User.
        :rtype: int
        """
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, sis_import_id):
        """
        Sets the sis_import_id of this User.
        The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information.

        :param sis_import_id: The sis_import_id of this User.
        :type: int
        """

        self._sis_import_id = sis_import_id

    @property
    def sis_login_id(self):
        """
        Gets the sis_login_id of this User.
        DEPRECATED: The SIS login ID associated with the user. Please use the sis_user_id or login_id. This field will be removed in a future version of the API.

        :return: The sis_login_id of this User.
        :rtype: str
        """
        return self._sis_login_id

    @sis_login_id.setter
    def sis_login_id(self, sis_login_id):
        """
        Sets the sis_login_id of this User.
        DEPRECATED: The SIS login ID associated with the user. Please use the sis_user_id or login_id. This field will be removed in a future version of the API.

        :param sis_login_id: The sis_login_id of this User.
        :type: str
        """

        self._sis_login_id = sis_login_id

    @property
    def login_id(self):
        """
        Gets the login_id of this User.
        The unique login id for the user.  This is what the user uses to log in to Canvas.

        :return: The login_id of this User.
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """
        Sets the login_id of this User.
        The unique login id for the user.  This is what the user uses to log in to Canvas.

        :param login_id: The login_id of this User.
        :type: str
        """

        self._login_id = login_id

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this User.
        If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar.

        :return: The avatar_url of this User.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this User.
        If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar.

        :param avatar_url: The avatar_url of this User.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def enrollments(self):
        """
        Gets the enrollments of this User.
        Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records.

        :return: The enrollments of this User.
        :rtype: list[Enrollment]
        """
        return self._enrollments

    @enrollments.setter
    def enrollments(self, enrollments):
        """
        Sets the enrollments of this User.
        Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records.

        :param enrollments: The enrollments of this User.
        :type: list[Enrollment]
        """

        self._enrollments = enrollments

    @property
    def email(self):
        """
        Gets the email of this User.
        Optional: This field can be requested with certain API calls, and will return the users primary email address.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        Optional: This field can be requested with certain API calls, and will return the users primary email address.

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def locale(self):
        """
        Gets the locale of this User.
        Optional: This field can be requested with certain API calls, and will return the users locale.

        :return: The locale of this User.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this User.
        Optional: This field can be requested with certain API calls, and will return the users locale.

        :param locale: The locale of this User.
        :type: str
        """

        self._locale = locale

    @property
    def last_login(self):
        """
        Gets the last_login of this User.
        Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas.

        :return: The last_login of this User.
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this User.
        Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas.

        :param last_login: The last_login of this User.
        :type: datetime
        """

        self._last_login = last_login

    @property
    def time_zone(self):
        """
        Gets the time_zone of this User.
        Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone.

        :return: The time_zone of this User.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this User.
        Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone.

        :param time_zone: The time_zone of this User.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def bio(self):
        """
        Gets the bio of this User.
        Optional: The user's bio.

        :return: The bio of this User.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """
        Sets the bio of this User.
        Optional: The user's bio.

        :param bio: The bio of this User.
        :type: str
        """

        self._bio = bio

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