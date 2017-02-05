"""GradingStandards API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class GradingStandardsAPI(BaseCanvasAPI):
    """GradingStandards API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GradingStandardsAPI."""
        super(GradingStandardsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.GradingStandardsAPI")

    def create_new_grading_standard_accounts(self, title, account_id, grading_scheme_entry_name, grading_scheme_entry_value):
        """
        Create a new grading standard.

        Create a new grading standard
        
        If grading_scheme_entry arguments are omitted, then a default grading scheme
        will be set. The default scheme is as follows:
             "A" : 94,
             "A-" : 90,
             "B+" : 87,
             "B" : 84,
             "B-" : 80,
             "C+" : 77,
             "C" : 74,
             "C-" : 70,
             "D+" : 67,
             "D" : 64,
             "D-" : 61,
             "F" : 0,
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - title - The title for the Grading Standard.
        data["title"] = title
        # REQUIRED - grading_scheme_entry[name] - The name for an entry value within a GradingStandard that describes the range of the value e.g. A-
        data["grading_scheme_entry[name]"] = grading_scheme_entry_name
        # REQUIRED - grading_scheme_entry[value] - The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93
        data["grading_scheme_entry[value]"] = grading_scheme_entry_value

        self.logger.debug("POST /api/v1/accounts/{account_id}/grading_standards with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/grading_standards".format(**path), data=data, params=params, single_item=True)

    def create_new_grading_standard_courses(self, title, course_id, grading_scheme_entry_name, grading_scheme_entry_value):
        """
        Create a new grading standard.

        Create a new grading standard
        
        If grading_scheme_entry arguments are omitted, then a default grading scheme
        will be set. The default scheme is as follows:
             "A" : 94,
             "A-" : 90,
             "B+" : 87,
             "B" : 84,
             "B-" : 80,
             "C+" : 77,
             "C" : 74,
             "C-" : 70,
             "D+" : 67,
             "D" : 64,
             "D-" : 61,
             "F" : 0,
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - title - The title for the Grading Standard.
        data["title"] = title
        # REQUIRED - grading_scheme_entry[name] - The name for an entry value within a GradingStandard that describes the range of the value e.g. A-
        data["grading_scheme_entry[name]"] = grading_scheme_entry_name
        # REQUIRED - grading_scheme_entry[value] - The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93
        data["grading_scheme_entry[value]"] = grading_scheme_entry_value

        self.logger.debug("POST /api/v1/courses/{course_id}/grading_standards with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/grading_standards".format(**path), data=data, params=params, single_item=True)


class Gradingstandard(BaseModel):
    """Gradingstandard Model."""

    def __init__(self, context_type=None, context_id=None, grading_scheme=None, id=None, title=None):
        """Init method for Gradingstandard class."""
        self._context_type = context_type
        self._context_id = context_id
        self._grading_scheme = grading_scheme
        self._id = id
        self._title = title

        self.logger = logging.getLogger('pycanvas.Gradingstandard')

    @property
    def context_type(self):
        """the context this standard is associated with, either 'Account' or 'Course'."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """the id for the context either the Account or Course id."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def grading_scheme(self):
        """A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value."""
        return self._grading_scheme

    @grading_scheme.setter
    def grading_scheme(self, value):
        """Setter for grading_scheme property."""
        self.logger.warn("Setting values on grading_scheme will NOT update the remote Canvas instance.")
        self._grading_scheme = value

    @property
    def id(self):
        """the id of the grading standard."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def title(self):
        """the title of the grading standard."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value


class Gradingschemeentry(BaseModel):
    """Gradingschemeentry Model."""

    def __init__(self, name=None, value=None):
        """Init method for Gradingschemeentry class."""
        self._name = name
        self._value = value

        self.logger = logging.getLogger('pycanvas.Gradingschemeentry')

    @property
    def name(self):
        """The name for an entry value within a GradingStandard that describes the range of the value."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def value(self):
        """The value for the name of the entry within a GradingStandard.  The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0."""
        return self._value

    @value.setter
    def value(self, value):
        """Setter for value property."""
        self.logger.warn("Setting values on value will NOT update the remote Canvas instance.")
        self._value = value

