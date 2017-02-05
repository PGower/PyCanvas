"""QuizSubmissionUserList API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from base import BaseCanvasAPI
from base import BaseModel


class QuizSubmissionUserListAPI(BaseCanvasAPI):
    """QuizSubmissionUserList API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionUserListAPI."""
        super(QuizSubmissionUserListAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionUserListAPI")

    def send_message_to_unsubmitted_or_submitted_users_for_quiz(self, id, course_id):
        """
        Send a message to unsubmitted or submitted users for the quiz.

        {
          "body": {
            "type": "string",
            "description": "message body of the conversation to be created",
            "example": "Please take the quiz."
          },
          "recipients": {
            "type": "string",
            "description": "Who to send the message to. May be either 'submitted' or 'unsubmitted'",
            "example": "submitted"
          },
          "subject": {
            "type": "string",
            "description": "Subject of the new Conversation created",
            "example": "ATTN: Quiz 101 Students"
          }
        }
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{id}/submission_users/message with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{id}/submission_users/message".format(**path), data=payload, no_data=True)


class Jsonapipagination(BaseModel):
    """Jsonapipagination Model."""

    def __init__(self):
        """Init method for Jsonapipagination class."""

        self.logger = logging.getLogger('pycanvas.Jsonapipagination')


class Quizsubmissionuserlistmeta(BaseModel):
    """Quizsubmissionuserlistmeta Model."""

    def __init__(self):
        """Init method for Quizsubmissionuserlistmeta class."""

        self.logger = logging.getLogger('pycanvas.Quizsubmissionuserlistmeta')


class Quizsubmissionuserlist(BaseModel):
    """Quizsubmissionuserlist Model."""

    def __init__(self):
        """Init method for Quizsubmissionuserlist class."""

        self.logger = logging.getLogger('pycanvas.Quizsubmissionuserlist')

