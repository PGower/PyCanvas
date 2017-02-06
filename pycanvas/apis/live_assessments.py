"""LiveAssessments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class LiveAssessmentsAPI(BaseCanvasAPI):
    """LiveAssessments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for LiveAssessmentsAPI."""
        super(LiveAssessmentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.LiveAssessmentsAPI")

    def create_live_assessment_results(self, course_id, assessment_id):
        """
        Create live assessment results.

        Creates live assessment results and adds them to a live assessment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assessment_id
        """ID"""
        path["assessment_id"] = assessment_id

        self.logger.debug("POST /api/v1/courses/{course_id}/live_assessments/{assessment_id}/results with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/live_assessments/{assessment_id}/results".format(**path), data=data, params=params, no_data=True)

    def list_live_assessment_results(self, course_id, assessment_id, user_id=None):
        """
        List live assessment results.

        Returns a list of live assessment results
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assessment_id
        """ID"""
        path["assessment_id"] = assessment_id

        # OPTIONAL - user_id
        """If set, restrict results to those for this user"""
        if user_id is not None:
            params["user_id"] = user_id

        self.logger.debug("GET /api/v1/courses/{course_id}/live_assessments/{assessment_id}/results with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/live_assessments/{assessment_id}/results".format(**path), data=data, params=params, no_data=True)

    def create_or_find_live_assessment(self, course_id):
        """
        Create or find a live assessment.

        Creates or finds an existing live assessment with the given key and aligns it with
        the linked outcome
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("POST /api/v1/courses/{course_id}/live_assessments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/live_assessments".format(**path), data=data, params=params, no_data=True)

    def list_live_assessments(self, course_id):
        """
        List live assessments.

        Returns a list of live assessments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/live_assessments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/live_assessments".format(**path), data=data, params=params, no_data=True)


class Assessment(BaseModel):
    """Assessment Model.
    A simple assessment that collects pass/fail results for a student"""

    def __init__(self, id=None, key=None, title=None):
        """Init method for Assessment class."""
        self._id = id
        self._key = key
        self._title = title

        self.logger = logging.getLogger('pycanvas.Assessment')

    @property
    def id(self):
        """A unique identifier for this live assessment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def key(self):
        """A client specified unique identifier for the assessment."""
        return self._key

    @key.setter
    def key(self, value):
        """Setter for key property."""
        self.logger.warn("Setting values on key will NOT update the remote Canvas instance.")
        self._key = value

    @property
    def title(self):
        """A human readable title for the assessment."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value


class Result(BaseModel):
    """Result Model.
    A pass/fail results for a student"""

    def __init__(self, assessed_at=None, links=None, id=None, passed=None):
        """Init method for Result class."""
        self._assessed_at = assessed_at
        self._links = links
        self._id = id
        self._passed = passed

        self.logger = logging.getLogger('pycanvas.Result')

    @property
    def assessed_at(self):
        """When this result was recorded."""
        return self._assessed_at

    @assessed_at.setter
    def assessed_at(self, value):
        """Setter for assessed_at property."""
        self.logger.warn("Setting values on assessed_at will NOT update the remote Canvas instance.")
        self._assessed_at = value

    @property
    def links(self):
        """Unique identifiers of objects associated with this result."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def id(self):
        """A unique identifier for this result."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def passed(self):
        """Whether the user passed or not."""
        return self._passed

    @passed.setter
    def passed(self, value):
        """Setter for passed property."""
        self.logger.warn("Setting values on passed will NOT update the remote Canvas instance.")
        self._passed = value


class Resultlinks(BaseModel):
    """Resultlinks Model.
    Unique identifiers of objects associated with a result"""

    def __init__(self, assessment=None, user=None, assessor=None):
        """Init method for Resultlinks class."""
        self._assessment = assessment
        self._user = user
        self._assessor = assessor

        self.logger = logging.getLogger('pycanvas.Resultlinks')

    @property
    def assessment(self):
        """A unique identifier for the assessment that this result is for."""
        return self._assessment

    @assessment.setter
    def assessment(self, value):
        """Setter for assessment property."""
        self.logger.warn("Setting values on assessment will NOT update the remote Canvas instance.")
        self._assessment = value

    @property
    def user(self):
        """A unique identifier for the user to whom this result applies."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def assessor(self):
        """A unique identifier for the user who created this result."""
        return self._assessor

    @assessor.setter
    def assessor(self, value):
        """Setter for assessor property."""
        self.logger.warn("Setting values on assessor will NOT update the remote Canvas instance.")
        self._assessor = value

