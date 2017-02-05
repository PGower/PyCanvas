"""QuizExtensions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizExtensionsAPI(BaseCanvasAPI):
    """QuizExtensions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizExtensionsAPI."""
        super(QuizExtensionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizExtensionsAPI")

    def set_extensions_for_student_quiz_submissions(self, quiz_id, user_id, course_id, extend_from_end_at=None, extend_from_now=None, extra_attempts=None, extra_time=None, manually_unlocked=None):
        """
        Set extensions for student quiz submissions.

        <b>Responses</b>
        
        * <b>200 OK</b> if the request was successful
        * <b>403 Forbidden</b> if you are not allowed to extend quizzes for this course
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
        # REQUIRED - user_id
        """The ID of the user we want to add quiz extensions for."""
        data["user_id"] = user_id
        # OPTIONAL - extra_attempts
        """Number of times the student is allowed to re-take the quiz over the
        multiple-attempt limit. This is limited to 1000 attempts or less."""
        if extra_attempts is not None:
            data["extra_attempts"] = extra_attempts
        # OPTIONAL - extra_time
        """The number of extra minutes to allow for all attempts. This will
        add to the existing time limit on the submission. This is limited to
        10080 minutes (1 week)"""
        if extra_time is not None:
            data["extra_time"] = extra_time
        # OPTIONAL - manually_unlocked
        """Allow the student to take the quiz even if it's locked for
        everyone else."""
        if manually_unlocked is not None:
            data["manually_unlocked"] = manually_unlocked
        # OPTIONAL - extend_from_now
        """The number of minutes to extend the quiz from the current time. This is
        mutually exclusive to extend_from_end_at. This is limited to 1440
        minutes (24 hours)"""
        if extend_from_now is not None:
            data["extend_from_now"] = extend_from_now
        # OPTIONAL - extend_from_end_at
        """The number of minutes to extend the quiz beyond the quiz's current
        ending time. This is mutually exclusive to extend_from_now. This is
        limited to 1440 minutes (24 hours)"""
        if extend_from_end_at is not None:
            data["extend_from_end_at"] = extend_from_end_at

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/extensions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/extensions".format(**path), data=data, params=params, no_data=True)


class Quizextension(BaseModel):
    """Quizextension Model."""

    def __init__(self, quiz_id, user_id, end_at=None, manually_unlocked=None, extra_attempts=None, extra_time=None):
        """Init method for Quizextension class."""
        self._user_id = user_id
        self._end_at = end_at
        self._manually_unlocked = manually_unlocked
        self._extra_attempts = extra_attempts
        self._quiz_id = quiz_id
        self._extra_time = extra_time

        self.logger = logging.getLogger('pycanvas.Quizextension')

    @property
    def user_id(self):
        """The ID of the Student that needs the quiz extension."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def end_at(self):
        """The time at which the quiz submission will be overdue, and be flagged as a late submission."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def manually_unlocked(self):
        """The student can take the quiz even if it's locked for everyone else."""
        return self._manually_unlocked

    @manually_unlocked.setter
    def manually_unlocked(self, value):
        """Setter for manually_unlocked property."""
        self.logger.warn("Setting values on manually_unlocked will NOT update the remote Canvas instance.")
        self._manually_unlocked = value

    @property
    def extra_attempts(self):
        """Number of times the student is allowed to re-take the quiz over the multiple-attempt limit."""
        return self._extra_attempts

    @extra_attempts.setter
    def extra_attempts(self, value):
        """Setter for extra_attempts property."""
        self.logger.warn("Setting values on extra_attempts will NOT update the remote Canvas instance.")
        self._extra_attempts = value

    @property
    def quiz_id(self):
        """The ID of the Quiz the quiz extension belongs to."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def extra_time(self):
        """Amount of extra time allowed for the quiz submission, in minutes."""
        return self._extra_time

    @extra_time.setter
    def extra_time(self, value):
        """Setter for extra_time property."""
        self.logger.warn("Setting values on extra_time will NOT update the remote Canvas instance.")
        self._extra_time = value

