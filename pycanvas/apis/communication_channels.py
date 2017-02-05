"""CommunicationChannels API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CommunicationChannelsAPI(BaseCanvasAPI):
    """CommunicationChannels API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CommunicationChannelsAPI."""
        super(CommunicationChannelsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CommunicationChannelsAPI")

    def list_user_communication_channels(self, user_id):
        """
        List user communication channels.

        Returns a list of communication channels for the specified user, sorted by
        position.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/communication_channels with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/communication_channels".format(**path), data=data, params=params, all_pages=True)

    def create_communication_channel(self, user_id, communication_channel_type, communication_channel_address, communication_channel_token=None, skip_confirmation=None):
        """
        Create a communication channel.

        Creates a new communication channel for the specified user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - communication_channel[address]
        """An email address or SMS number. Not required for "push" type channels."""
        data["communication_channel[address]"] = communication_channel_address
        # REQUIRED - communication_channel[type]
        """The type of communication channel.
        
        In order to enable push notification support, the server must be
        properly configured (via sns.yml) to communicate with Amazon
        Simple Notification Services, and the developer key used to create
        the access token from this request must have an SNS ARN configured on
        it."""
        self._validate_enum(communication_channel_type, ["email", "sms", "push"])
        data["communication_channel[type]"] = communication_channel_type
        # OPTIONAL - communication_channel[token]
        """A registration id, device token, or equivalent token given to an app when
        registering with a push notification provider. Only valid for "push" type channels."""
        if communication_channel_token is not None:
            data["communication_channel[token]"] = communication_channel_token
        # OPTIONAL - skip_confirmation
        """Only valid for site admins and account admins making requests; If true, the channel is
        automatically validated and no confirmation email or SMS is sent.
        Otherwise, the user must respond to a confirmation message to confirm the
        channel."""
        if skip_confirmation is not None:
            data["skip_confirmation"] = skip_confirmation

        self.logger.debug("POST /api/v1/users/{user_id}/communication_channels with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/communication_channels".format(**path), data=data, params=params, single_item=True)

    def delete_communication_channel_id(self, id, user_id):
        """
        Delete a communication channel.

        Delete an existing communication channel.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/users/{user_id}/communication_channels/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/communication_channels/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_communication_channel_type(self, type, user_id, address):
        """
        Delete a communication channel.

        Delete an existing communication channel.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id
        # REQUIRED - PATH - type
        """ID"""
        path["type"] = type
        # REQUIRED - PATH - address
        """ID"""
        path["address"] = address

        self.logger.debug("DELETE /api/v1/users/{user_id}/communication_channels/{type}/{address} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/communication_channels/{type}/{address}".format(**path), data=data, params=params, single_item=True)


class Communicationchannel(BaseModel):
    """Communicationchannel Model."""

    def __init__(self, user_id=None, workflow_state=None, address=None, position=None, type=None, id=None):
        """Init method for Communicationchannel class."""
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._address = address
        self._position = position
        self._type = type
        self._id = id

        self.logger = logging.getLogger('pycanvas.Communicationchannel')

    @property
    def user_id(self):
        """The ID of the user that owns this communication channel."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """The current state of the communication channel. Possible values are: 'unconfirmed' or 'active'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def address(self):
        """The address, or path, of the communication channel."""
        return self._address

    @address.setter
    def address(self, value):
        """Setter for address property."""
        self.logger.warn("Setting values on address will NOT update the remote Canvas instance.")
        self._address = value

    @property
    def position(self):
        """The position of this communication channel relative to the user's other channels when they are ordered."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def type(self):
        """The type of communcation channel being described. Possible values are: 'email', 'push', 'sms', 'twitter' or 'yo'. This field determines the type of value seen in 'address'."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """The ID of the communication channel."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

