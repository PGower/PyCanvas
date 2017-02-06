"""Outcomes API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class OutcomesAPI(BaseCanvasAPI):
    """Outcomes API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OutcomesAPI."""
        super(OutcomesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.OutcomesAPI")

    def show_outcome(self, id):
        """
        Show an outcome.

        Returns the details of the outcome with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/outcomes/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/outcomes/{id}".format(**path), data=data, params=params, single_item=True)

    def update_outcome(self, id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Update an outcome.

        Modify an existing outcome. Fields not provided are left as is;
        unrecognized fields are ignored.
        
        If any new ratings are provided, the combination of all new ratings
        provided completely replace any existing embedded rubric criterion; it is
        not possible to tweak the ratings of the embedded rubric criterion.
        
        A new embedded rubric criterion's mastery_points default to the maximum
        points in the highest rating if not specified in the mastery_points
        parameter. Any new ratings lacking a description are given a default of "No
        description". Any new ratings lacking a point value are given a default of
        0.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - title
        """The new outcome title."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The new outcome description."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The new mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a new rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a new rating level for the embedded rubric
        criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method."""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("PUT /api/v1/outcomes/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/outcomes/{id}".format(**path), data=data, params=params, single_item=True)


class Outcome(BaseModel):
    """Outcome Model."""

    def __init__(self, vendor_guid=None, can_edit=None, display_name=None, description=None, title=None, url=None, context_id=None, points_possible=None, can_unlink=None, context_type=None, ratings=None, calculation_int=None, calculation_method=None, assessed=None, id=None, mastery_points=None):
        """Init method for Outcome class."""
        self._vendor_guid = vendor_guid
        self._can_edit = can_edit
        self._display_name = display_name
        self._description = description
        self._title = title
        self._url = url
        self._context_id = context_id
        self._points_possible = points_possible
        self._can_unlink = can_unlink
        self._context_type = context_type
        self._ratings = ratings
        self._calculation_int = calculation_int
        self._calculation_method = calculation_method
        self._assessed = assessed
        self._id = id
        self._mastery_points = mastery_points

        self.logger = logging.getLogger('pycanvas.Outcome')

    @property
    def vendor_guid(self):
        """A custom GUID for the learning standard."""
        return self._vendor_guid

    @vendor_guid.setter
    def vendor_guid(self, value):
        """Setter for vendor_guid property."""
        self.logger.warn("Setting values on vendor_guid will NOT update the remote Canvas instance.")
        self._vendor_guid = value

    @property
    def can_edit(self):
        """whether the current user can update the outcome."""
        return self._can_edit

    @can_edit.setter
    def can_edit(self, value):
        """Setter for can_edit property."""
        self.logger.warn("Setting values on can_edit will NOT update the remote Canvas instance.")
        self._can_edit = value

    @property
    def display_name(self):
        """Optional friendly name for reporting."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def description(self):
        """description of the outcome. omitted in the abbreviated form."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def title(self):
        """title of the outcome."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """the URL for fetching/updating the outcome. should be treated as opaque."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def context_id(self):
        """the context owning the outcome. may be null for global outcomes."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def points_possible(self):
        """maximum points possible. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def can_unlink(self):
        """whether the outcome can be unlinked."""
        return self._can_unlink

    @can_unlink.setter
    def can_unlink(self, value):
        """Setter for can_unlink property."""
        self.logger.warn("Setting values on can_unlink will NOT update the remote Canvas instance.")
        self._can_unlink = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def ratings(self):
        """possible ratings for this outcome. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form."""
        return self._ratings

    @ratings.setter
    def ratings(self, value):
        """Setter for ratings property."""
        self.logger.warn("Setting values on ratings will NOT update the remote Canvas instance.")
        self._ratings = value

    @property
    def calculation_int(self):
        """this defines the variable value used by the calculation_method. included only if calculation_method uses it."""
        return self._calculation_int

    @calculation_int.setter
    def calculation_int(self, value):
        """Setter for calculation_int property."""
        self.logger.warn("Setting values on calculation_int will NOT update the remote Canvas instance.")
        self._calculation_int = value

    @property
    def calculation_method(self):
        """the method used to calculate a students score."""
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, value):
        """Setter for calculation_method property."""
        self.logger.warn("Setting values on calculation_method will NOT update the remote Canvas instance.")
        self._calculation_method = value

    @property
    def assessed(self):
        """whether this outcome has been used to assess a student."""
        return self._assessed

    @assessed.setter
    def assessed(self, value):
        """Setter for assessed property."""
        self.logger.warn("Setting values on assessed will NOT update the remote Canvas instance.")
        self._assessed = value

    @property
    def id(self):
        """the ID of the outcome."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def mastery_points(self):
        """points necessary to demonstrate mastery outcomes. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form."""
        return self._mastery_points

    @mastery_points.setter
    def mastery_points(self, value):
        """Setter for mastery_points property."""
        self.logger.warn("Setting values on mastery_points will NOT update the remote Canvas instance.")
        self._mastery_points = value

