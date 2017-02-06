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

    def list_collaborations_courses(self, course_id):
        """
        List collaborations.

        List collaborations the current user has access to in the context of the course
        provided in the url. NOTE: this only returns ExternalToolCollaboration type
        collaborations.
        
          curl https://<canvas>/api/v1/courses/1/collaborations/
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/collaborations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/collaborations".format(**path), data=data, params=params, all_pages=True)

    def list_collaborations_groups(self, group_id):
        """
        List collaborations.

        List collaborations the current user has access to in the context of the course
        provided in the url. NOTE: this only returns ExternalToolCollaboration type
        collaborations.
        
          curl https://<canvas>/api/v1/courses/1/collaborations/
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/collaborations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/collaborations".format(**path), data=data, params=params, all_pages=True)

    def list_members_of_collaboration(self, id, include=None):
        """
        List members of a collaboration.

        List the collaborators of a given collaboration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """- "collaborator_lti_id": Optional information to include with each member.
          Represents an identifier to be used for the member in an LTI context.
        - "avatar_image_url": Optional information to include with each member.
          The url for the avatar of a collaborator with type 'user'."""
        if include is not None:
            self._validate_enum(include, ["collaborator_lti_id", "avatar_image_url"])
            params["include"] = include

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


class Collaboration(BaseModel):
    """Collaboration Model."""

    def __init__(self, user_id=None, description=None, title=None, context_type=None, context_id=None, created_at=None, updated_at=None, url=None, user_name=None, collaboration_type=None, update_url=None, type=None, id=None, document_id=None):
        """Init method for Collaboration class."""
        self._user_id = user_id
        self._description = description
        self._title = title
        self._context_type = context_type
        self._context_id = context_id
        self._created_at = created_at
        self._updated_at = updated_at
        self._url = url
        self._user_name = user_name
        self._collaboration_type = collaboration_type
        self._update_url = update_url
        self._type = type
        self._id = id
        self._document_id = document_id

        self.logger = logging.getLogger('pycanvas.Collaboration')

    @property
    def user_id(self):
        """The canvas id of the user who created the collaboration."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def context_type(self):
        """The canvas type of the course or group to which the collaboration belongs."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """The canvas id of the course or group to which the collaboration belongs."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def created_at(self):
        """The timestamp when the collaboration was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """The timestamp when the collaboration was last modified."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def url(self):
        """The LTI launch url to view collaboration."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def user_name(self):
        """The name of the user who owns the collaboration."""
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """Setter for user_name property."""
        self.logger.warn("Setting values on user_name will NOT update the remote Canvas instance.")
        self._user_name = value

    @property
    def collaboration_type(self):
        """A name for the type of collaboration."""
        return self._collaboration_type

    @collaboration_type.setter
    def collaboration_type(self, value):
        """Setter for collaboration_type property."""
        self.logger.warn("Setting values on collaboration_type will NOT update the remote Canvas instance.")
        self._collaboration_type = value

    @property
    def update_url(self):
        """The LTI launch url to edit the collaboration."""
        return self._update_url

    @update_url.setter
    def update_url(self, value):
        """Setter for update_url property."""
        self.logger.warn("Setting values on update_url will NOT update the remote Canvas instance.")
        self._update_url = value

    @property
    def type(self):
        """Another representation of the collaboration type."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """The unique identifier for the collaboration."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def document_id(self):
        """The collaboration document identifier for the collaboration provider."""
        return self._document_id

    @document_id.setter
    def document_id(self, value):
        """Setter for document_id property."""
        self.logger.warn("Setting values on document_id will NOT update the remote Canvas instance.")
        self._document_id = value

