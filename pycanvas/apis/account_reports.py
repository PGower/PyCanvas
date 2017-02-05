"""AccountReports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AccountReportsAPI(BaseCanvasAPI):
    """AccountReports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountReportsAPI."""
        super(AccountReportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AccountReportsAPI")

    def list_available_reports(self, account_id):
        """
        List Available Reports.

        Returns the list of reports for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/reports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/reports".format(**path), data=data, params=params, no_data=True)

    def start_report(self, report, account_id, _parameters=None):
        """
        Start a Report.

        Generates a report instance for the account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - PATH - report
        """ID"""
        path["report"] = report
        # OPTIONAL - [parameters]
        """The parameters will vary for each report"""
        if _parameters is not None:
            data["[parameters]"] = _parameters

        self.logger.debug("POST /api/v1/accounts/{account_id}/reports/{report} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/reports/{report}".format(**path), data=data, params=params, single_item=True)

    def index_of_reports(self, report, account_id):
        """
        Index of Reports.

        Shows all reports that have been run for the account of a specific type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - PATH - report
        """ID"""
        path["report"] = report

        self.logger.debug("GET /api/v1/accounts/{account_id}/reports/{report} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/reports/{report}".format(**path), data=data, params=params, all_pages=True)

    def status_of_report(self, id, report, account_id):
        """
        Status of a Report.

        Returns the status of a report.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - PATH - report
        """ID"""
        path["report"] = report
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/reports/{report}/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/reports/{report}/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_report(self, id, report, account_id):
        """
        Delete a Report.

        Deletes a generated report instance.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id
        # REQUIRED - PATH - report
        """ID"""
        path["report"] = report
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/reports/{report}/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/reports/{report}/{id}".format(**path), data=data, params=params, single_item=True)


class Report(BaseModel):
    """Report Model."""

    def __init__(self, status=None, parameters=None, file_url=None, report=None, progress=None, id=None):
        """Init method for Report class."""
        self._status = status
        self._parameters = parameters
        self._file_url = file_url
        self._report = report
        self._progress = progress
        self._id = id

        self.logger = logging.getLogger('pycanvas.Report')

    @property
    def status(self):
        """The status of the report."""
        return self._status

    @status.setter
    def status(self, value):
        """Setter for status property."""
        self.logger.warn("Setting values on status will NOT update the remote Canvas instance.")
        self._status = value

    @property
    def parameters(self):
        """The report parameters."""
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        """Setter for parameters property."""
        self.logger.warn("Setting values on parameters will NOT update the remote Canvas instance.")
        self._parameters = value

    @property
    def file_url(self):
        """The url to the report download."""
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        """Setter for file_url property."""
        self.logger.warn("Setting values on file_url will NOT update the remote Canvas instance.")
        self._file_url = value

    @property
    def report(self):
        """The type of report."""
        return self._report

    @report.setter
    def report(self, value):
        """Setter for report property."""
        self.logger.warn("Setting values on report will NOT update the remote Canvas instance.")
        self._report = value

    @property
    def progress(self):
        """The progress of the report."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn("Setting values on progress will NOT update the remote Canvas instance.")
        self._progress = value

    @property
    def id(self):
        """The unique identifier for the report."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Reportparameters(BaseModel):
    """Reportparameters Model.
    The parameters returned will vary for each report."""

    def __init__(self, include_enrollment_state=None, sis_terms_csv=None, terms=None, users=None, enrollments=None, enrollment_term_id=None, include_deleted=None, courses=None, sis_accounts_csv=None, accounts=None, groups=None, course_id=None, start_at=None, enrollment_state=None, end_at=None, sections=None, order=None, xlist=None):
        """Init method for Reportparameters class."""
        self._include_enrollment_state = include_enrollment_state
        self._sis_terms_csv = sis_terms_csv
        self._terms = terms
        self._users = users
        self._enrollments = enrollments
        self._enrollment_term_id = enrollment_term_id
        self._include_deleted = include_deleted
        self._courses = courses
        self._sis_accounts_csv = sis_accounts_csv
        self._accounts = accounts
        self._groups = groups
        self._course_id = course_id
        self._start_at = start_at
        self._enrollment_state = enrollment_state
        self._end_at = end_at
        self._sections = sections
        self._order = order
        self._xlist = xlist

        self.logger = logging.getLogger('pycanvas.Reportparameters')

    @property
    def include_enrollment_state(self):
        """Include enrollment state. Defaults to false."""
        return self._include_enrollment_state

    @include_enrollment_state.setter
    def include_enrollment_state(self, value):
        """Setter for include_enrollment_state property."""
        self.logger.warn("Setting values on include_enrollment_state will NOT update the remote Canvas instance.")
        self._include_enrollment_state = value

    @property
    def sis_terms_csv(self):
        """sis_terms_csv."""
        return self._sis_terms_csv

    @sis_terms_csv.setter
    def sis_terms_csv(self, value):
        """Setter for sis_terms_csv property."""
        self.logger.warn("Setting values on sis_terms_csv will NOT update the remote Canvas instance.")
        self._sis_terms_csv = value

    @property
    def terms(self):
        """Get the data for terms."""
        return self._terms

    @terms.setter
    def terms(self, value):
        """Setter for terms property."""
        self.logger.warn("Setting values on terms will NOT update the remote Canvas instance.")
        self._terms = value

    @property
    def users(self):
        """Get the data for users."""
        return self._users

    @users.setter
    def users(self, value):
        """Setter for users property."""
        self.logger.warn("Setting values on users will NOT update the remote Canvas instance.")
        self._users = value

    @property
    def enrollments(self):
        """Get the data for enrollments."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn("Setting values on enrollments will NOT update the remote Canvas instance.")
        self._enrollments = value

    @property
    def enrollment_term_id(self):
        """The canvas id of the term to get grades from."""
        return self._enrollment_term_id

    @enrollment_term_id.setter
    def enrollment_term_id(self, value):
        """Setter for enrollment_term_id property."""
        self.logger.warn("Setting values on enrollment_term_id will NOT update the remote Canvas instance.")
        self._enrollment_term_id = value

    @property
    def include_deleted(self):
        """Include deleted objects."""
        return self._include_deleted

    @include_deleted.setter
    def include_deleted(self, value):
        """Setter for include_deleted property."""
        self.logger.warn("Setting values on include_deleted will NOT update the remote Canvas instance.")
        self._include_deleted = value

    @property
    def courses(self):
        """Get the data for courses."""
        return self._courses

    @courses.setter
    def courses(self, value):
        """Setter for courses property."""
        self.logger.warn("Setting values on courses will NOT update the remote Canvas instance.")
        self._courses = value

    @property
    def sis_accounts_csv(self):
        """sis_accounts_csv."""
        return self._sis_accounts_csv

    @sis_accounts_csv.setter
    def sis_accounts_csv(self, value):
        """Setter for sis_accounts_csv property."""
        self.logger.warn("Setting values on sis_accounts_csv will NOT update the remote Canvas instance.")
        self._sis_accounts_csv = value

    @property
    def accounts(self):
        """Get the data for accounts."""
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        """Setter for accounts property."""
        self.logger.warn("Setting values on accounts will NOT update the remote Canvas instance.")
        self._accounts = value

    @property
    def groups(self):
        """Get the data for groups."""
        return self._groups

    @groups.setter
    def groups(self, value):
        """Setter for groups property."""
        self.logger.warn("Setting values on groups will NOT update the remote Canvas instance.")
        self._groups = value

    @property
    def course_id(self):
        """The course to report on."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def start_at(self):
        """The beginning date for submissions. Max time range is 2 weeks."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def enrollment_state(self):
        """Include enrollment state. Defaults to 'all' Options: ['active'| 'invited'| 'creation_pending'| 'deleted'| 'rejected'| 'completed'| 'inactive'| 'all']."""
        return self._enrollment_state

    @enrollment_state.setter
    def enrollment_state(self, value):
        """Setter for enrollment_state property."""
        self.logger.warn("Setting values on enrollment_state will NOT update the remote Canvas instance.")
        self._enrollment_state = value

    @property
    def end_at(self):
        """The end date for submissions. Max time range is 2 weeks."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def sections(self):
        """Get the data for sections."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections property."""
        self.logger.warn("Setting values on sections will NOT update the remote Canvas instance.")
        self._sections = value

    @property
    def order(self):
        """The sort order for the csv, Options: 'users', 'courses', 'outcomes'."""
        return self._order

    @order.setter
    def order(self, value):
        """Setter for order property."""
        self.logger.warn("Setting values on order will NOT update the remote Canvas instance.")
        self._order = value

    @property
    def xlist(self):
        """Get the data for cross-listed courses."""
        return self._xlist

    @xlist.setter
    def xlist(self, value):
        """Setter for xlist property."""
        self.logger.warn("Setting values on xlist will NOT update the remote Canvas instance.")
        self._xlist = value

