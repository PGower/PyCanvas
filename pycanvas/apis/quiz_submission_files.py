"""QuizSubmissionFiles API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class QuizSubmissionFilesAPI(BaseCanvasAPI):
    """QuizSubmissionFiles API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionFilesAPI."""
        super(QuizSubmissionFilesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionFilesAPI")

    def upload_file(self, quiz_id, course_id, name=None, on_duplicate=None):
        """
        Upload a file.

        Associate a new quiz submission file
        
        This API endpoint is the first step in uploading a quiz submission file.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow as these parameters are interpreted as per the
        documentation there.
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

        # OPTIONAL - name
        """The name of the quiz submission file"""
        if name is not None:
            data["name"] = name

        # OPTIONAL - on_duplicate
        """How to handle duplicate names"""
        if on_duplicate is not None:
            data["on_duplicate"] = on_duplicate

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files".format(**path), data=data, params=params, no_data=True)

