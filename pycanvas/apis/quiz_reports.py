"""QuizReports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizReportsAPI(BaseCanvasAPI):
    """QuizReports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizReportsAPI."""
        super(QuizReportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizReportsAPI")

    def retrieve_all_quiz_reports(self, quiz_id, course_id, includes_all_versions=None):
        """
        Retrieve all quiz reports.

        Returns a list of all available reports.
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

        # OPTIONAL - includes_all_versions
        """Whether to retrieve reports that consider all the submissions or only
        the most recent. Defaults to false, ignored for item_analysis reports."""
        if includes_all_versions is not None:
            params["includes_all_versions"] = includes_all_versions

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports".format(**path), data=data, params=params, all_pages=True)

    def create_quiz_report(self, quiz_id, course_id, quiz_report_report_type, include=None, quiz_report_includes_all_versions=None):
        """
        Create a quiz report.

        Create and return a new report for this quiz. If a previously
        generated report matches the arguments and is still current (i.e.
        there have been no new submissions), it will be returned.
        
        *Responses*
        
        * <code>400 Bad Request</code> if the specified report type is invalid
        * <code>409 Conflict</code> if a quiz report of the specified type is already being
          generated
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

        # REQUIRED - quiz_report[report_type]
        """The type of report to be generated."""
        self._validate_enum(quiz_report_report_type, ["student_analysis", "item_analysis"])
        data["quiz_report[report_type]"] = quiz_report_report_type

        # OPTIONAL - quiz_report[includes_all_versions]
        """Whether the report should consider all submissions or only the most
        recent. Defaults to false, ignored for item_analysis."""
        if quiz_report_includes_all_versions is not None:
            data["quiz_report[includes_all_versions]"] = quiz_report_includes_all_versions

        # OPTIONAL - include
        """Whether the output should include documents for the file and/or progress
        objects associated with this report. (Note: JSON-API only)"""
        if include is not None:
            self._validate_enum(include, ["file", "progress"])
            data["include"] = include

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports".format(**path), data=data, params=params, single_item=True)

    def get_quiz_report(self, id, quiz_id, course_id, include=None):
        """
        Get a quiz report.

        Returns the data for a single quiz report.
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

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Whether the output should include documents for the file and/or progress
        objects associated with this report. (Note: JSON-API only)"""
        if include is not None:
            self._validate_enum(include, ["file", "progress"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}".format(**path), data=data, params=params, single_item=True)

    def abort_generation_of_report_or_remove_previously_generated_one(self, id, quiz_id, course_id):
        """
        Abort the generation of a report, or remove a previously generated one.

        This API allows you to cancel a previous request you issued for a report to
        be generated. Or in the case of an already generated report, you'd like to
        remove it, perhaps to generate it another time with an updated version that
        provides new features.
        
        You must check the report's generation status before attempting to use this
        interface. See the "workflow_state" property of the QuizReport's Progress
        object for more information. Only when the progress reports itself in a
        "queued" state can the generation be aborted.
        
        *Responses*
        
        - <code>204 No Content</code> if your request was accepted
        - <code>422 Unprocessable Entity</code> if the report is not being generated
          or can not be aborted at this stage
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

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}".format(**path), data=data, params=params, no_data=True)


class Quizreport(BaseModel):
    """Quizreport Model."""

    def __init__(self, file=None, progress_url=None, report_type=None, readable_type=None, url=None, created_at=None, updated_at=None, generatable=None, anonymous=None, progress=None, quiz_id=None, includes_all_versions=None, id=None):
        """Init method for Quizreport class."""
        self._file = file
        self._progress_url = progress_url
        self._report_type = report_type
        self._readable_type = readable_type
        self._url = url
        self._created_at = created_at
        self._updated_at = updated_at
        self._generatable = generatable
        self._anonymous = anonymous
        self._progress = progress
        self._quiz_id = quiz_id
        self._includes_all_versions = includes_all_versions
        self._id = id

        self.logger = logging.getLogger('pycanvas.Quizreport')

    @property
    def file(self):
        """if the report has finished generating, a File object that represents it. refer to the Files API for more information about the format."""
        return self._file

    @file.setter
    def file(self, value):
        """Setter for file property."""
        self.logger.warn("Setting values on file will NOT update the remote Canvas instance.")
        self._file = value

    @property
    def progress_url(self):
        """if the report has not yet finished generating, a URL where information about its progress can be retrieved. refer to the Progress API for more information (Note: not available in JSON-API format)."""
        return self._progress_url

    @progress_url.setter
    def progress_url(self, value):
        """Setter for progress_url property."""
        self.logger.warn("Setting values on progress_url will NOT update the remote Canvas instance.")
        self._progress_url = value

    @property
    def report_type(self):
        """which type of report this is possible values: 'student_analysis', 'item_analysis'."""
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        """Setter for report_type property."""
        self.logger.warn("Setting values on report_type will NOT update the remote Canvas instance.")
        self._report_type = value

    @property
    def readable_type(self):
        """a human-readable (and localized) version of the report_type."""
        return self._readable_type

    @readable_type.setter
    def readable_type(self, value):
        """Setter for readable_type property."""
        self.logger.warn("Setting values on readable_type will NOT update the remote Canvas instance.")
        self._readable_type = value

    @property
    def url(self):
        """the API endpoint for this report."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """when the report was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """when the report was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def generatable(self):
        """boolean indicating whether the report can be generated, which is true unless the quiz is a survey one."""
        return self._generatable

    @generatable.setter
    def generatable(self, value):
        """Setter for generatable property."""
        self.logger.warn("Setting values on generatable will NOT update the remote Canvas instance.")
        self._generatable = value

    @property
    def anonymous(self):
        """boolean indicating whether the report is for an anonymous survey. if true, no student names will be included in the csv."""
        return self._anonymous

    @anonymous.setter
    def anonymous(self, value):
        """Setter for anonymous property."""
        self.logger.warn("Setting values on anonymous will NOT update the remote Canvas instance.")
        self._anonymous = value

    @property
    def progress(self):
        """if the report is being generated, a Progress object that represents the operation. Refer to the Progress API for more information about the format. (Note: available only in JSON-API format)."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn("Setting values on progress will NOT update the remote Canvas instance.")
        self._progress = value

    @property
    def quiz_id(self):
        """the ID of the quiz."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def includes_all_versions(self):
        """boolean indicating whether the report represents all submissions or only the most recent ones for each student."""
        return self._includes_all_versions

    @includes_all_versions.setter
    def includes_all_versions(self, value):
        """Setter for includes_all_versions property."""
        self.logger.warn("Setting values on includes_all_versions will NOT update the remote Canvas instance.")
        self._includes_all_versions = value

    @property
    def id(self):
        """the ID of the quiz report."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

