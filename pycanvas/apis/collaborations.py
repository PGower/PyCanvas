"""Collaborations API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CollaborationsAPI(BaseCanvasAPI):
    """Collaborations API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CollaborationsAPI."""
        super(CollaborationsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CollaborationsAPI")

    def list_members_of_collaboration(self, id):
        """
        List members of a collaboration.

        List the collaborators of a given collaboration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/collaborations/{id}/members with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/collaborations/{id}/members".format(**path), data=data, params=params, all_pages=True)


class Collaborator(BaseModel):
    """Collaborator Model."""

    def __init__(self, id, type=None, name=None):
        """Init method for Collaborator class."""
        self._type = type
        self._id = id
        self._name = name

        self.logger = logging.getLogger('pycanvas.Collaborator')

    @property
    def type(self):
        """The type of collaborator (e.g. 'user' or 'group')."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """The unique user or group identifier for the collaborator."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """The name of the collaborator."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

