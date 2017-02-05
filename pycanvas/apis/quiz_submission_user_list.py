"""QuizSubmissionUserList API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizSubmissionUserListAPI(BaseCanvasAPI):
    """QuizSubmissionUserList API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionUserListAPI."""
        super(QuizSubmissionUserListAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionUserListAPI")

    def send_message_to_unsubmitted_or_submitted_users_for_quiz(self, id, course_id, conversations=None):
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
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - conversations
        """- Body and recipients to send the message to."""
        if conversations is not None:
            data["conversations"] = conversations

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{id}/submission_users/message with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{id}/submission_users/message".format(**path), data=data, params=params, no_data=True)


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

