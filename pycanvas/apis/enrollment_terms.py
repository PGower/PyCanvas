"""EnrollmentTerms API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class EnrollmentTermsAPI(BaseCanvasAPI):
    """EnrollmentTerms API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for EnrollmentTermsAPI."""
        super(EnrollmentTermsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.EnrollmentTermsAPI")

    def create_enrollment_term(self, account_id, enrollment_term_end_at=None, enrollment_term_name=None, enrollment_term_sis_term_id=None, enrollment_term_start_at=None):
        """
        Create enrollment term.

        Create a new enrollment term for the specified account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # OPTIONAL - enrollment_term[name] - The name of the term.
        if enrollment_term_name is not None:
            data["enrollment_term[name]"] = enrollment_term_name
        # OPTIONAL - enrollment_term[start_at] - The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        if enrollment_term_start_at is not None:
            data["enrollment_term[start_at]"] = enrollment_term_start_at
        # OPTIONAL - enrollment_term[end_at] - The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        if enrollment_term_end_at is not None:
            data["enrollment_term[end_at]"] = enrollment_term_end_at
        # OPTIONAL - enrollment_term[sis_term_id] - The unique SIS identifier for the term.
        if enrollment_term_sis_term_id is not None:
            data["enrollment_term[sis_term_id]"] = enrollment_term_sis_term_id

        self.logger.debug("POST /api/v1/accounts/{account_id}/terms with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/terms".format(**path), data=data, params=params, single_item=True)

    def update_enrollment_term(self, id, account_id, enrollment_term_end_at=None, enrollment_term_name=None, enrollment_term_sis_term_id=None, enrollment_term_start_at=None):
        """
        Update enrollment term.

        Update an existing enrollment term for the specified account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - enrollment_term[name] - The name of the term.
        if enrollment_term_name is not None:
            data["enrollment_term[name]"] = enrollment_term_name
        # OPTIONAL - enrollment_term[start_at] - The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        if enrollment_term_start_at is not None:
            data["enrollment_term[start_at]"] = enrollment_term_start_at
        # OPTIONAL - enrollment_term[end_at] - The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        if enrollment_term_end_at is not None:
            data["enrollment_term[end_at]"] = enrollment_term_end_at
        # OPTIONAL - enrollment_term[sis_term_id] - The unique SIS identifier for the term.
        if enrollment_term_sis_term_id is not None:
            data["enrollment_term[sis_term_id]"] = enrollment_term_sis_term_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/terms/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/terms/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_enrollment_term(self, id, account_id):
        """
        Delete enrollment term.

        Delete the specified enrollment term.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/terms/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/terms/{id}".format(**path), data=data, params=params, single_item=True)

    def list_enrollment_terms(self, account_id, workflow_state=None):
        """
        List enrollment terms.

        Return all of the terms in the account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # OPTIONAL - workflow_state - no description
        if workflow_state is not None:
            params["workflow_state"] = workflow_state

        self.logger.debug("GET /api/v1/accounts/{account_id}/terms with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/terms".format(**path), data=data, params=params, all_pages=True)


class Enrollmentterm(BaseModel):
    """Enrollmentterm Model."""

    def __init__(self, start_at=None, name=None, workflow_state=None, sis_term_id=None, end_at=None, id=None):
        """Init method for Enrollmentterm class."""
        self._start_at = start_at
        self._name = name
        self._workflow_state = workflow_state
        self._sis_term_id = sis_term_id
        self._end_at = end_at
        self._id = id

        self.logger = logging.getLogger('pycanvas.Enrollmentterm')

    @property
    def start_at(self):
        """The datetime of the start of the term."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def name(self):
        """The name of the term."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def workflow_state(self):
        """The state of the term. Can be 'active' or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def sis_term_id(self):
        """The SIS id of the term. Only included if the user has permission to view SIS information."""
        return self._sis_term_id

    @sis_term_id.setter
    def sis_term_id(self, value):
        """Setter for sis_term_id property."""
        self.logger.warn("Setting values on sis_term_id will NOT update the remote Canvas instance.")
        self._sis_term_id = value

    @property
    def end_at(self):
        """The datetime of the end of the term."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def id(self):
        """The unique identifier for the enrollment term."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

