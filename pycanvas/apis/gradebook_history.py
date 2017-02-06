"""GradebookHistory API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class GradebookHistoryAPI(BaseCanvasAPI):
    """GradebookHistory API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GradebookHistoryAPI."""
        super(GradebookHistoryAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.GradebookHistoryAPI")

    def days_in_gradebook_history_for_this_course(self, course_id):
        """
        Days in gradebook history for this course.

        Returns a map of dates to grader/assignment groups
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """The id of the contextual course for this API call"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/gradebook_history/days with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/gradebook_history/days".format(**path), data=data, params=params, all_pages=True)

    def details_for_given_date_in_gradebook_history_for_this_course(self, date, course_id):
        """
        Details for a given date in gradebook history for this course.

        Returns the graders who worked on this day, along with the assignments they worked on.
        More details can be obtained by selecting a grader and assignment and calling the
        'submissions' api endpoint for a given date.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """The id of the contextual course for this API call"""
        path["course_id"] = course_id

        # REQUIRED - PATH - date
        """The date for which you would like to see detailed information"""
        path["date"] = date

        self.logger.debug("GET /api/v1/courses/{course_id}/gradebook_history/{date} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/gradebook_history/{date}".format(**path), data=data, params=params, all_pages=True)

    def lists_submissions(self, date, course_id, grader_id, assignment_id):
        """
        Lists submissions.

        Gives a nested list of submission versions
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """The id of the contextual course for this API call"""
        path["course_id"] = course_id

        # REQUIRED - PATH - date
        """The date for which you would like to see submissions"""
        path["date"] = date

        # REQUIRED - PATH - grader_id
        """The ID of the grader for which you want to see submissions"""
        path["grader_id"] = grader_id

        # REQUIRED - PATH - assignment_id
        """The ID of the assignment for which you want to see submissions"""
        path["assignment_id"] = assignment_id

        self.logger.debug("GET /api/v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, all_pages=True)

    def list_uncollated_submission_versions(self, course_id, ascending=None, assignment_id=None, user_id=None):
        """
        List uncollated submission versions.

        Gives a paginated, uncollated list of submission versions for all matching
        submissions in the context. This SubmissionVersion objects will not include
        the +new_grade+ or +previous_grade+ keys, only the +grade+; same for
        +graded_at+ and +grader+.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """The id of the contextual course for this API call"""
        path["course_id"] = course_id

        # OPTIONAL - assignment_id
        """The ID of the assignment for which you want to see submissions. If
        absent, versions of submissions from any assignment in the course are
        included."""
        if assignment_id is not None:
            params["assignment_id"] = assignment_id

        # OPTIONAL - user_id
        """The ID of the user for which you want to see submissions. If absent,
        versions of submissions from any user in the course are included."""
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - ascending
        """Returns submission versions in ascending date order (oldest first). If
        absent, returns submission versions in descending date order (newest
        first)."""
        if ascending is not None:
            params["ascending"] = ascending

        self.logger.debug("GET /api/v1/courses/{course_id}/gradebook_history/feed with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/gradebook_history/feed".format(**path), data=data, params=params, all_pages=True)


class Submissionversion(BaseModel):
    """Submissionversion Model.
    A SubmissionVersion object contains all the fields that a Submission object does, plus additional fields prefixed with current_* new_* and previous_* described below."""

    def __init__(self, new_grade=None, previous_grader=None, grader=None, current_grade=None, id=None, user_id=None, previous_graded_at=None, assignment_name=None, score=None, grade_matches_current_submission=None, previous_grade=None, grader_id=None, user_name=None, body=None, current_graded_at=None, workflow_state=None, graded_at=None, new_grader=None, assignment_id=None, current_grader=None, new_graded_at=None, url=None, submission_type=None):
        """Init method for Submissionversion class."""
        self._new_grade = new_grade
        self._previous_grader = previous_grader
        self._grader = grader
        self._current_grade = current_grade
        self._id = id
        self._user_id = user_id
        self._previous_graded_at = previous_graded_at
        self._assignment_name = assignment_name
        self._score = score
        self._grade_matches_current_submission = grade_matches_current_submission
        self._previous_grade = previous_grade
        self._grader_id = grader_id
        self._user_name = user_name
        self._body = body
        self._current_graded_at = current_graded_at
        self._workflow_state = workflow_state
        self._graded_at = graded_at
        self._new_grader = new_grader
        self._assignment_id = assignment_id
        self._current_grader = current_grader
        self._new_graded_at = new_graded_at
        self._url = url
        self._submission_type = submission_type

        self.logger = logging.getLogger('pycanvas.Submissionversion')

    @property
    def new_grade(self):
        """the updated grade provided in this version of the submission."""
        return self._new_grade

    @new_grade.setter
    def new_grade(self, value):
        """Setter for new_grade property."""
        self.logger.warn("Setting values on new_grade will NOT update the remote Canvas instance.")
        self._new_grade = value

    @property
    def previous_grader(self):
        """the name of the grader who graded the version of this submission immediately preceding this one."""
        return self._previous_grader

    @previous_grader.setter
    def previous_grader(self, value):
        """Setter for previous_grader property."""
        self.logger.warn("Setting values on previous_grader will NOT update the remote Canvas instance.")
        self._previous_grader = value

    @property
    def grader(self):
        """the name of the user who graded this version of the submission."""
        return self._grader

    @grader.setter
    def grader(self, value):
        """Setter for grader property."""
        self.logger.warn("Setting values on grader will NOT update the remote Canvas instance.")
        self._grader = value

    @property
    def current_grade(self):
        """the most up to date grade for the current version of this submission."""
        return self._current_grade

    @current_grade.setter
    def current_grade(self, value):
        """Setter for current_grade property."""
        self.logger.warn("Setting values on current_grade will NOT update the remote Canvas instance.")
        self._current_grade = value

    @property
    def id(self):
        """the id of the submission of which this is a version."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def user_id(self):
        """the user ID of the student who created this submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def previous_graded_at(self):
        """the timestamp for the grading of the submission version immediately preceding this one."""
        return self._previous_graded_at

    @previous_graded_at.setter
    def previous_graded_at(self, value):
        """Setter for previous_graded_at property."""
        self.logger.warn("Setting values on previous_graded_at will NOT update the remote Canvas instance.")
        self._previous_graded_at = value

    @property
    def assignment_name(self):
        """the name of the assignment this submission is for."""
        return self._assignment_name

    @assignment_name.setter
    def assignment_name(self, value):
        """Setter for assignment_name property."""
        self.logger.warn("Setting values on assignment_name will NOT update the remote Canvas instance.")
        self._assignment_name = value

    @property
    def score(self):
        """the score for this version of the submission."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def grade_matches_current_submission(self):
        """boolean indicating whether the grade is equal to the current submission grade."""
        return self._grade_matches_current_submission

    @grade_matches_current_submission.setter
    def grade_matches_current_submission(self, value):
        """Setter for grade_matches_current_submission property."""
        self.logger.warn("Setting values on grade_matches_current_submission will NOT update the remote Canvas instance.")
        self._grade_matches_current_submission = value

    @property
    def previous_grade(self):
        """the grade for the submission version immediately preceding this one."""
        return self._previous_grade

    @previous_grade.setter
    def previous_grade(self, value):
        """Setter for previous_grade property."""
        self.logger.warn("Setting values on previous_grade will NOT update the remote Canvas instance.")
        self._previous_grade = value

    @property
    def grader_id(self):
        """the user id of the user who graded this version of the submission."""
        return self._grader_id

    @grader_id.setter
    def grader_id(self, value):
        """Setter for grader_id property."""
        self.logger.warn("Setting values on grader_id will NOT update the remote Canvas instance.")
        self._grader_id = value

    @property
    def user_name(self):
        """the name of the student who created this submission."""
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """Setter for user_name property."""
        self.logger.warn("Setting values on user_name will NOT update the remote Canvas instance.")
        self._user_name = value

    @property
    def body(self):
        """the body text of the submission."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def current_graded_at(self):
        """the latest time stamp for the grading of this submission."""
        return self._current_graded_at

    @current_graded_at.setter
    def current_graded_at(self, value):
        """Setter for current_graded_at property."""
        self.logger.warn("Setting values on current_graded_at will NOT update the remote Canvas instance.")
        self._current_graded_at = value

    @property
    def workflow_state(self):
        """the state of the submission at this version."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def graded_at(self):
        """time stamp for the grading of this version of the submission."""
        return self._graded_at

    @graded_at.setter
    def graded_at(self, value):
        """Setter for graded_at property."""
        self.logger.warn("Setting values on graded_at will NOT update the remote Canvas instance.")
        self._graded_at = value

    @property
    def new_grader(self):
        """alias for 'grader'."""
        return self._new_grader

    @new_grader.setter
    def new_grader(self, value):
        """Setter for new_grader property."""
        self.logger.warn("Setting values on new_grader will NOT update the remote Canvas instance.")
        self._new_grader = value

    @property
    def assignment_id(self):
        """the id of the assignment this submissions is for."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def current_grader(self):
        """the name of the most recent grader for this submission."""
        return self._current_grader

    @current_grader.setter
    def current_grader(self, value):
        """Setter for current_grader property."""
        self.logger.warn("Setting values on current_grader will NOT update the remote Canvas instance.")
        self._current_grader = value

    @property
    def new_graded_at(self):
        """the timestamp for the grading of this version of the submission (alias for graded_at)."""
        return self._new_graded_at

    @new_graded_at.setter
    def new_graded_at(self, value):
        """Setter for new_graded_at property."""
        self.logger.warn("Setting values on new_graded_at will NOT update the remote Canvas instance.")
        self._new_graded_at = value

    @property
    def url(self):
        """the url of the submission, if there is one."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def submission_type(self):
        """the type of submission."""
        return self._submission_type

    @submission_type.setter
    def submission_type(self, value):
        """Setter for submission_type property."""
        self.logger.warn("Setting values on submission_type will NOT update the remote Canvas instance.")
        self._submission_type = value


class Grader(BaseModel):
    """Grader Model."""

    def __init__(self, assignments=None, id=None, name=None):
        """Init method for Grader class."""
        self._assignments = assignments
        self._id = id
        self._name = name

        self.logger = logging.getLogger('pycanvas.Grader')

    @property
    def assignments(self):
        """the assignment groups for all submissions in this response that were graded by this user.  The details are not nested inside here, but the fact that an assignment is present here means that the grader did grade submissions for this assignment on the contextual date. You can use the id of a grader and of an assignment to make another API call to find all submissions for a grader/assignment combination on a given date."""
        return self._assignments

    @assignments.setter
    def assignments(self, value):
        """Setter for assignments property."""
        self.logger.warn("Setting values on assignments will NOT update the remote Canvas instance.")
        self._assignments = value

    @property
    def id(self):
        """the user_id of the user who graded the contained submissions."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """the name of the user who graded the contained submissions."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Day(BaseModel):
    """Day Model."""

    def __init__(self, date=None, graders=None):
        """Init method for Day class."""
        self._date = date
        self._graders = graders

        self.logger = logging.getLogger('pycanvas.Day')

    @property
    def date(self):
        """the date represented by this entry."""
        return self._date

    @date.setter
    def date(self, value):
        """Setter for date property."""
        self.logger.warn("Setting values on date will NOT update the remote Canvas instance.")
        self._date = value

    @property
    def graders(self):
        """an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for."""
        return self._graders

    @graders.setter
    def graders(self, value):
        """Setter for graders property."""
        self.logger.warn("Setting values on graders will NOT update the remote Canvas instance.")
        self._graders = value


class Submissionhistory(BaseModel):
    """Submissionhistory Model."""

    def __init__(self, submission_id=None, versions=None):
        """Init method for Submissionhistory class."""
        self._submission_id = submission_id
        self._versions = versions

        self.logger = logging.getLogger('pycanvas.Submissionhistory')

    @property
    def submission_id(self):
        """the id of the submission."""
        return self._submission_id

    @submission_id.setter
    def submission_id(self, value):
        """Setter for submission_id property."""
        self.logger.warn("Setting values on submission_id will NOT update the remote Canvas instance.")
        self._submission_id = value

    @property
    def versions(self):
        """an array of all the versions of this submission."""
        return self._versions

    @versions.setter
    def versions(self, value):
        """Setter for versions property."""
        self.logger.warn("Setting values on versions will NOT update the remote Canvas instance.")
        self._versions = value

