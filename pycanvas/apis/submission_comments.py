"""SubmissionComments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI



class SubmissionCommentsAPI(BaseCanvasAPI):
    """SubmissionComments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SubmissionCommentsAPI."""
        super(SubmissionCommentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.SubmissionCommentsAPI")

    def upload_file(self, user_id, course_id, assignment_id):
        """
        Upload a file.

        Upload a file to attach to a submission comment
        
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then PUT the file_id to the
        submission API to attach it to a comment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id
        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files".format(**path), data=data, params=params, no_data=True)

