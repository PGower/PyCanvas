"""QuizSubmissions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizSubmissionsAPI(BaseCanvasAPI):
    """QuizSubmissions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionsAPI."""
        super(QuizSubmissionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionsAPI")

    def get_all_quiz_submissions(self, quiz_id, course_id, include=None):
        """
        Get all quiz submissions.

        Get a list of all submissions for this quiz. Users who can view or manage
        grades for a course will have submissions from multiple users returned. A
        user who can only submit will have only their own submissions returned. When
        a user has an in-progress submission, only that submission is returned. When
        there isn't an in-progress quiz_submission, all completed submissions,
        including previous attempts, are returned.
        
        <b>200 OK</b> response code is returned if the request was successful.
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

        # OPTIONAL - include
        """Associations to include with the quiz submission."""
        if include is not None:
            self._validate_enum(include, ["submission", "quiz", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def get_quiz_submission(self, quiz_id, course_id, include=None):
        """
        Get the quiz submission.

        Get the submission for this quiz for the current user.
        
        <b>200 OK</b> response code is returned if the request was successful.
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

        # OPTIONAL - include
        """Associations to include with the quiz submission."""
        if include is not None:
            self._validate_enum(include, ["submission", "quiz", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/submission with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submission".format(**path), data=data, params=params, no_data=True)

    def get_single_quiz_submission(self, id, quiz_id, course_id, include=None):
        """
        Get a single quiz submission.

        Get a single quiz submission.
        
        <b>200 OK</b> response code is returned if the request was successful.
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
        """Associations to include with the quiz submission."""
        if include is not None:
            self._validate_enum(include, ["submission", "quiz", "user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}".format(**path), data=data, params=params, no_data=True)

    def create_quiz_submission_start_quiz_taking_session(self, quiz_id, course_id, access_code=None, preview=None):
        """
        Create the quiz submission (start a quiz-taking session).

        Start taking a Quiz by creating a QuizSubmission which you can use to answer
        questions and submit your answers.
        
        <b>Responses</b>
        
        * <b>200 OK</b> if the request was successful
        * <b>400 Bad Request</b> if the quiz is locked
        * <b>403 Forbidden</b> if an invalid access code is specified
        * <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
        * <b>409 Conflict</b> if a QuizSubmission already exists for this user and quiz
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

        # OPTIONAL - access_code
        """Access code for the Quiz, if any."""
        if access_code is not None:
            data["access_code"] = access_code

        # OPTIONAL - preview
        """Whether this should be a preview QuizSubmission and not count towards
        the user's course record. Teachers only."""
        if preview is not None:
            data["preview"] = preview

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def update_student_question_scores_and_comments(self, id, quiz_id, attempt, course_id, fudge_points=None, questions=None):
        """
        Update student question scores and comments.

        Update the amount of points a student has scored for questions they've
        answered, provide comments for the student about their answer(s), or simply
        fudge the total score by a specific amount of points.
        
        <b>Responses</b>
        
        * <b>200 OK</b> if the request was successful
        * <b>403 Forbidden</b> if you are not a teacher in this course
        * <b>400 Bad Request</b> if the attempt parameter is missing or invalid
        * <b>400 Bad Request</b> if the specified QS attempt is not yet complete
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

        # REQUIRED - attempt
        """The attempt number of the quiz submission that should be updated. This
        attempt MUST be already completed."""
        data["attempt"] = attempt

        # OPTIONAL - fudge_points
        """Amount of positive or negative points to fudge the total score by."""
        if fudge_points is not None:
            data["fudge_points"] = fudge_points

        # OPTIONAL - questions
        """A set of scores and comments for each question answered by the student.
        The keys are the question IDs, and the values are hashes of `score` and
        `comment` entries. See {Appendix: Manual Scoring} for more on this
        parameter."""
        if questions is not None:
            data["questions"] = questions

        self.logger.debug("PUT /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}".format(**path), data=data, params=params, no_data=True)

    def complete_quiz_submission_turn_it_in(self, id, quiz_id, attempt, course_id, validation_token, access_code=None):
        """
        Complete the quiz submission (turn it in).

        Complete the quiz submission by marking it as complete and grading it. When
        the quiz submission has been marked as complete, no further modifications
        will be allowed.
        
        <b>Responses</b>
        
        * <b>200 OK</b> if the request was successful
        * <b>403 Forbidden</b> if an invalid access code is specified
        * <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
        * <b>403 Forbidden</b> if an invalid token is specified
        * <b>400 Bad Request</b> if the QS is already complete
        * <b>400 Bad Request</b> if the attempt parameter is missing
        * <b>400 Bad Request</b> if the attempt parameter is not the latest attempt
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

        # REQUIRED - attempt
        """The attempt number of the quiz submission that should be completed. Note
        that this must be the latest attempt index, as earlier attempts can not
        be modified."""
        data["attempt"] = attempt

        # REQUIRED - validation_token
        """The unique validation token you received when this Quiz Submission was
        created."""
        data["validation_token"] = validation_token

        # OPTIONAL - access_code
        """Access code for the Quiz, if any."""
        if access_code is not None:
            data["access_code"] = access_code

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete".format(**path), data=data, params=params, no_data=True)

    def get_current_quiz_submission_times(self, id, quiz_id, course_id):
        """
        Get current quiz submission times.

        Get the current timing data for the quiz attempt, both the end_at timestamp
        and the time_left parameter.
        
        <b>Responses</b>
        
        * <b>200 OK</b> if the request was successful
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

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time".format(**path), data=data, params=params, no_data=True)


class Quizsubmission(BaseModel):
    """Quizsubmission Model."""

    def __init__(self, id, quiz_id, submission_id=None, user_id=None, kept_score=None, time_spent=None, workflow_state=None, finished_at=None, overdue_and_needs_submission=None, end_at=None, manually_unlocked=None, score_before_regrade=None, score=None, extra_attempts=None, fudge_points=None, attempt=None, started_at=None, extra_time=None, has_seen_results=None):
        """Init method for Quizsubmission class."""
        self._submission_id = submission_id
        self._user_id = user_id
        self._kept_score = kept_score
        self._time_spent = time_spent
        self._workflow_state = workflow_state
        self._finished_at = finished_at
        self._overdue_and_needs_submission = overdue_and_needs_submission
        self._end_at = end_at
        self._manually_unlocked = manually_unlocked
        self._score_before_regrade = score_before_regrade
        self._score = score
        self._extra_attempts = extra_attempts
        self._fudge_points = fudge_points
        self._attempt = attempt
        self._quiz_id = quiz_id
        self._started_at = started_at
        self._extra_time = extra_time
        self._id = id
        self._has_seen_results = has_seen_results

        self.logger = logging.getLogger('pycanvas.Quizsubmission')

    @property
    def submission_id(self):
        """The ID of the Submission the quiz submission represents."""
        return self._submission_id

    @submission_id.setter
    def submission_id(self, value):
        """Setter for submission_id property."""
        self.logger.warn("Setting values on submission_id will NOT update the remote Canvas instance.")
        self._submission_id = value

    @property
    def user_id(self):
        """The ID of the Student that made the quiz submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def kept_score(self):
        """For quizzes that allow multiple attempts, this is the score that will be used, which might be the score of the latest, or the highest, quiz submission."""
        return self._kept_score

    @kept_score.setter
    def kept_score(self, value):
        """Setter for kept_score property."""
        self.logger.warn("Setting values on kept_score will NOT update the remote Canvas instance.")
        self._kept_score = value

    @property
    def time_spent(self):
        """Amount of time spent, in seconds."""
        return self._time_spent

    @time_spent.setter
    def time_spent(self, value):
        """Setter for time_spent property."""
        self.logger.warn("Setting values on time_spent will NOT update the remote Canvas instance.")
        self._time_spent = value

    @property
    def workflow_state(self):
        """The current state of the quiz submission. Possible values: ['untaken'|'pending_review'|'complete'|'settings_only'|'preview']."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def finished_at(self):
        """The time at which the student submitted the quiz submission."""
        return self._finished_at

    @finished_at.setter
    def finished_at(self, value):
        """Setter for finished_at property."""
        self.logger.warn("Setting values on finished_at will NOT update the remote Canvas instance.")
        self._finished_at = value

    @property
    def overdue_and_needs_submission(self):
        """Indicates whether the quiz submission is overdue and needs submission."""
        return self._overdue_and_needs_submission

    @overdue_and_needs_submission.setter
    def overdue_and_needs_submission(self, value):
        """Setter for overdue_and_needs_submission property."""
        self.logger.warn("Setting values on overdue_and_needs_submission will NOT update the remote Canvas instance.")
        self._overdue_and_needs_submission = value

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
    def score_before_regrade(self):
        """The original score of the quiz submission prior to any re-grading."""
        return self._score_before_regrade

    @score_before_regrade.setter
    def score_before_regrade(self, value):
        """Setter for score_before_regrade property."""
        self.logger.warn("Setting values on score_before_regrade will NOT update the remote Canvas instance.")
        self._score_before_regrade = value

    @property
    def score(self):
        """The score of the quiz submission, if graded."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def extra_attempts(self):
        """Number of times the student was allowed to re-take the quiz over the multiple-attempt limit."""
        return self._extra_attempts

    @extra_attempts.setter
    def extra_attempts(self, value):
        """Setter for extra_attempts property."""
        self.logger.warn("Setting values on extra_attempts will NOT update the remote Canvas instance.")
        self._extra_attempts = value

    @property
    def fudge_points(self):
        """Number of points the quiz submission's score was fudged by."""
        return self._fudge_points

    @fudge_points.setter
    def fudge_points(self, value):
        """Setter for fudge_points property."""
        self.logger.warn("Setting values on fudge_points will NOT update the remote Canvas instance.")
        self._fudge_points = value

    @property
    def attempt(self):
        """For quizzes that allow multiple attempts, this field specifies the quiz submission attempt number."""
        return self._attempt

    @attempt.setter
    def attempt(self, value):
        """Setter for attempt property."""
        self.logger.warn("Setting values on attempt will NOT update the remote Canvas instance.")
        self._attempt = value

    @property
    def quiz_id(self):
        """The ID of the Quiz the quiz submission belongs to."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def started_at(self):
        """The time at which the student started the quiz submission."""
        return self._started_at

    @started_at.setter
    def started_at(self, value):
        """Setter for started_at property."""
        self.logger.warn("Setting values on started_at will NOT update the remote Canvas instance.")
        self._started_at = value

    @property
    def extra_time(self):
        """Amount of extra time allowed for the quiz submission, in minutes."""
        return self._extra_time

    @extra_time.setter
    def extra_time(self, value):
        """Setter for extra_time property."""
        self.logger.warn("Setting values on extra_time will NOT update the remote Canvas instance.")
        self._extra_time = value

    @property
    def id(self):
        """The ID of the quiz submission."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def has_seen_results(self):
        """Whether the student has viewed their results to the quiz."""
        return self._has_seen_results

    @has_seen_results.setter
    def has_seen_results(self, value):
        """Setter for has_seen_results property."""
        self.logger.warn("Setting values on has_seen_results will NOT update the remote Canvas instance.")
        self._has_seen_results = value

