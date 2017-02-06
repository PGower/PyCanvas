"""QuizIpFilters API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizIpFiltersAPI(BaseCanvasAPI):
    """QuizIpFilters API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizIpFiltersAPI."""
        super(QuizIpFiltersAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizIpFiltersAPI")

    def get_available_quiz_ip_filters(self, quiz_id, course_id):
        """
        Get available quiz IP filters.

        Get a list of available IP filters for this Quiz.
        
        <b>200 OK</b> response code is returned if the request was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - quiz_id
        """ID"""
        path["quiz_id"] = quiz_id

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters".format(**path), data=data, params=params, no_data=True)


class Quizipfilter(BaseModel):
    """Quizipfilter Model."""

    def __init__(self, name, account, filter):
        """Init method for Quizipfilter class."""
        self._filter = filter
        self._account = account
        self._name = name

        self.logger = logging.getLogger('pycanvas.Quizipfilter')

    @property
    def filter(self):
        """An IP address (or range mask) this filter embodies."""
        return self._filter

    @filter.setter
    def filter(self, value):
        """Setter for filter property."""
        self.logger.warn("Setting values on filter will NOT update the remote Canvas instance.")
        self._filter = value

    @property
    def account(self):
        """Name of the Account (or Quiz) the IP filter is defined in."""
        return self._account

    @account.setter
    def account(self, value):
        """Setter for account property."""
        self.logger.warn("Setting values on account will NOT update the remote Canvas instance.")
        self._account = value

    @property
    def name(self):
        """A unique name for the filter."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

