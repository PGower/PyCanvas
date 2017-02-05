"""GradingPeriods API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class GradingPeriodsAPI(BaseCanvasAPI):
    """GradingPeriods API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GradingPeriodsAPI."""
        super(GradingPeriodsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.GradingPeriodsAPI")

    def list_grading_periods_courses(self, course_id):
        """
        List grading periods.

        Returns the list of grading periods for the current course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/grading_periods with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/grading_periods".format(**path), data=data, params=params, no_data=True)

    def list_grading_periods_accounts(self, account_id):
        """
        List grading periods.

        Returns the list of grading periods for the current course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/grading_periods with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/grading_periods".format(**path), data=data, params=params, no_data=True)

    def get_single_grading_period_courses(self, id, course_id):
        """
        Get a single grading period.

        Returns the grading period with the given id
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)

    def get_single_grading_period_accounts(self, id, account_id):
        """
        Get a single grading period.

        Returns the grading period with the given id
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)

    def create_single_grading_period_courses(self, course_id, grading_periods_end_date, grading_periods_start_date, grading_periods_weight=None):
        """
        Create a single grading period.

        Create a new grading period for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - grading_periods[start_date] - The date the grading period starts.
        data["grading_periods[start_date]"] = grading_periods_start_date
        # REQUIRED - grading_periods[end_date] - no description
        data["grading_periods[end_date]"] = grading_periods_end_date
        # OPTIONAL - grading_periods[weight] - The percentage weight of how much the period should count toward the course grade.
        if grading_periods_weight is not None:
            data["grading_periods[weight]"] = grading_periods_weight

        self.logger.debug("POST /api/v1/courses/{course_id}/grading_periods with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/grading_periods".format(**path), data=data, params=params, no_data=True)

    def create_single_grading_period_accounts(self, account_id, grading_periods_end_date, grading_periods_start_date, grading_periods_weight=None):
        """
        Create a single grading period.

        Create a new grading period for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - grading_periods[start_date] - The date the grading period starts.
        data["grading_periods[start_date]"] = grading_periods_start_date
        # REQUIRED - grading_periods[end_date] - no description
        data["grading_periods[end_date]"] = grading_periods_end_date
        # OPTIONAL - grading_periods[weight] - The percentage weight of how much the period should count toward the course grade.
        if grading_periods_weight is not None:
            data["grading_periods[weight]"] = grading_periods_weight

        self.logger.debug("POST /api/v1/accounts/{account_id}/grading_periods with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/grading_periods".format(**path), data=data, params=params, no_data=True)

    def update_single_grading_period_courses(self, id, course_id, grading_periods_end_date, grading_periods_start_date, grading_periods_weight=None):
        """
        Update a single grading period.

        Update an existing grading period.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - grading_periods[start_date] - The date the grading period starts.
        data["grading_periods[start_date]"] = grading_periods_start_date
        # REQUIRED - grading_periods[end_date] - no description
        data["grading_periods[end_date]"] = grading_periods_end_date
        # OPTIONAL - grading_periods[weight] - The percentage weight of how much the period should count toward the course grade.
        if grading_periods_weight is not None:
            data["grading_periods[weight]"] = grading_periods_weight

        self.logger.debug("PUT /api/v1/courses/{course_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)

    def update_single_grading_period_accounts(self, id, account_id, grading_periods_end_date, grading_periods_start_date, grading_periods_weight=None):
        """
        Update a single grading period.

        Update an existing grading period.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - grading_periods[start_date] - The date the grading period starts.
        data["grading_periods[start_date]"] = grading_periods_start_date
        # REQUIRED - grading_periods[end_date] - no description
        data["grading_periods[end_date]"] = grading_periods_end_date
        # OPTIONAL - grading_periods[weight] - The percentage weight of how much the period should count toward the course grade.
        if grading_periods_weight is not None:
            data["grading_periods[weight]"] = grading_periods_weight

        self.logger.debug("PUT /api/v1/accounts/{account_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_grading_period_courses(self, id, course_id):
        """
        Delete a grading period.

        <b>204 No Content</b> response code is returned if the deletion was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_grading_period_accounts(self, id, account_id):
        """
        Delete a grading period.

        <b>204 No Content</b> response code is returned if the deletion was successful.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/grading_periods/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/grading_periods/{id}".format(**path), data=data, params=params, no_data=True)


class Gradingperiod(BaseModel):
    """Gradingperiod Model."""

    def __init__(self, id, start_date, end_date, weight=None):
        """Init method for Gradingperiod class."""
        self._weight = weight
        self._id = id
        self._end_date = end_date
        self._start_date = start_date

        self.logger = logging.getLogger('pycanvas.Gradingperiod')

    @property
    def weight(self):
        """The weighted percentage on how much this particular period should count toward the total grade."""
        return self._weight

    @weight.setter
    def weight(self, value):
        """Setter for weight property."""
        self.logger.warn("Setting values on weight will NOT update the remote Canvas instance.")
        self._weight = value

    @property
    def id(self):
        """The unique identifier for the grading period."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def end_date(self):
        """The end date of the grading period."""
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        """Setter for end_date property."""
        self.logger.warn("Setting values on end_date will NOT update the remote Canvas instance.")
        self._end_date = value

    @property
    def start_date(self):
        """The start date of the grading period."""
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        """Setter for start_date property."""
        self.logger.warn("Setting values on start_date will NOT update the remote Canvas instance.")
        self._start_date = value

