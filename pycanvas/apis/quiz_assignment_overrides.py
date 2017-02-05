"""QuizAssignmentOverrides API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizAssignmentOverridesAPI(BaseCanvasAPI):
    """QuizAssignmentOverrides API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizAssignmentOverridesAPI."""
        super(QuizAssignmentOverridesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizAssignmentOverridesAPI")

    def retrieve_assignment_overridden_dates_for_quizzes(self, course_id, quiz_assignment_overrides_0_quiz_ids=None):
        """
        Retrieve assignment-overridden dates for quizzes.

        Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
        based on the assignment overrides active for the current API user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - quiz_assignment_overrides[0][quiz_ids] - An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned.
        if quiz_assignment_overrides_0_quiz_ids is not None:
            params["quiz_assignment_overrides[0][quiz_ids]"] = quiz_assignment_overrides_0_quiz_ids

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/assignment_overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/assignment_overrides".format(**path), data=data, params=params, single_item=True)


class Quizassignmentoverride(BaseModel):
    """Quizassignmentoverride Model.
    Set of assignment-overridden dates for a quiz."""

    def __init__(self, unlock_at=None, title=None, due_at=None, lock_at=None, base=None, id=None):
        """Init method for Quizassignmentoverride class."""
        self._unlock_at = unlock_at
        self._title = title
        self._due_at = due_at
        self._lock_at = lock_at
        self._base = base
        self._id = id

        self.logger = logging.getLogger('pycanvas.Quizassignmentoverride')

    @property
    def unlock_at(self):
        """Date when the quiz becomes available for taking."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def title(self):
        """Title of the section this assignment override is for, if any."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def due_at(self):
        """The date after which any quiz submission is considered late."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def lock_at(self):
        """When the quiz will stop being available for taking. A value of null means it can always be taken."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def base(self):
        """If this property is present, it means that dates in this structure are not based on an assignment override, but are instead for all students."""
        return self._base

    @base.setter
    def base(self, value):
        """Setter for base property."""
        self.logger.warn("Setting values on base will NOT update the remote Canvas instance.")
        self._base = value

    @property
    def id(self):
        """ID of the assignment override, unless this is the base construct, in which case the 'id' field is omitted."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Quizassignmentoverridesetcontainer(BaseModel):
    """Quizassignmentoverridesetcontainer Model.
    Container for set of assignment-overridden dates for a quiz."""

    def __init__(self, quiz_assignment_overrides=None):
        """Init method for Quizassignmentoverridesetcontainer class."""
        self._quiz_assignment_overrides = quiz_assignment_overrides

        self.logger = logging.getLogger('pycanvas.Quizassignmentoverridesetcontainer')

    @property
    def quiz_assignment_overrides(self):
        """The QuizAssignmentOverrideSet."""
        return self._quiz_assignment_overrides

    @quiz_assignment_overrides.setter
    def quiz_assignment_overrides(self, value):
        """Setter for quiz_assignment_overrides property."""
        self.logger.warn("Setting values on quiz_assignment_overrides will NOT update the remote Canvas instance.")
        self._quiz_assignment_overrides = value


class Quizassignmentoverrideset(BaseModel):
    """Quizassignmentoverrideset Model.
    Set of assignment-overridden dates for a quiz."""

    def __init__(self, due_dates=None, quiz_id=None, all_dates=None):
        """Init method for Quizassignmentoverrideset class."""
        self._due_dates = due_dates
        self._quiz_id = quiz_id
        self._all_dates = all_dates

        self.logger = logging.getLogger('pycanvas.Quizassignmentoverrideset')

    @property
    def due_dates(self):
        """An array of quiz assignment overrides. For students, this array will always contain a single item which is the set of dates that apply to that student. For teachers and staff, it may contain more."""
        return self._due_dates

    @due_dates.setter
    def due_dates(self, value):
        """Setter for due_dates property."""
        self.logger.warn("Setting values on due_dates will NOT update the remote Canvas instance.")
        self._due_dates = value

    @property
    def quiz_id(self):
        """ID of the quiz those dates are for."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def all_dates(self):
        """An array of all assignment overrides active for the quiz. This is visible only to teachers and staff."""
        return self._all_dates

    @all_dates.setter
    def all_dates(self, value):
        """Setter for all_dates property."""
        self.logger.warn("Setting values on all_dates will NOT update the remote Canvas instance.")
        self._all_dates = value

