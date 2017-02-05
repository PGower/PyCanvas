"""QuizSubmissionEvents API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizSubmissionEventsAPI(BaseCanvasAPI):
    """QuizSubmissionEvents API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionEventsAPI."""
        super(QuizSubmissionEventsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionEventsAPI")

    def submit_captured_events(self, id, quiz_id, course_id, quiz_submission_events):
        """
        Submit captured events.

        Store a set of events which were captured during a quiz taking session.
        
        On success, the response will be 204 No Content with an empty body.
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
        # REQUIRED - quiz_submission_events
        """The submission events to be recorded"""
        data["quiz_submission_events"] = quiz_submission_events

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events".format(**path), data=data, params=params, no_data=True)

    def retrieve_captured_events(self, id, quiz_id, course_id, attempt=None):
        """
        Retrieve captured events.

        Retrieve the set of events captured during a specific submission attempt.
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
        # OPTIONAL - attempt
        """The specific submission attempt to look up the events for. If unspecified,
        the latest attempt will be used."""
        if attempt is not None:
            params["attempt"] = attempt

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events".format(**path), data=data, params=params, no_data=True)


class Quizsubmissionevent(BaseModel):
    """Quizsubmissionevent Model.
    An event passed from the Quiz Submission take page"""

    def __init__(self, created_at=None, event_type=None, event_data=None):
        """Init method for Quizsubmissionevent class."""
        self._created_at = created_at
        self._event_type = event_type
        self._event_data = event_data

        self.logger = logging.getLogger('pycanvas.Quizsubmissionevent')

    @property
    def created_at(self):
        """a timestamp record of creation time."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def event_type(self):
        """the type of event being sent."""
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """Setter for event_type property."""
        self.logger.warn("Setting values on event_type will NOT update the remote Canvas instance.")
        self._event_type = value

    @property
    def event_data(self):
        """custom contextual data for the specific event type."""
        return self._event_data

    @event_data.setter
    def event_data(self, value):
        """Setter for event_data property."""
        self.logger.warn("Setting values on event_data will NOT update the remote Canvas instance.")
        self._event_data = value

