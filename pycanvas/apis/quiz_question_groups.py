"""QuizQuestionGroups API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class QuizQuestionGroupsAPI(BaseCanvasAPI):
    """QuizQuestionGroups API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizQuestionGroupsAPI."""
        super(QuizQuestionGroupsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizQuestionGroupsAPI")

    def get_single_quiz_group(self, id, quiz_id, course_id):
        """
        Get a single quiz group.

        Returns details of the quiz group with the given id.
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

        self.logger.debug("GET /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}".format(**path), data=data, params=params, single_item=True)

    def create_question_group(self, quiz_id, course_id, quiz_groups_assessment_question_bank_id=None, quiz_groups_name=None, quiz_groups_pick_count=None, quiz_groups_question_points=None):
        """
        Create a question group.

        Create a new question group for this quiz
        
        <b>201 Created</b> response code is returned if the creation was successful.
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
        # OPTIONAL - quiz_groups[name]
        """The name of the question group."""
        if quiz_groups_name is not None:
            data["quiz_groups[name]"] = quiz_groups_name
        # OPTIONAL - quiz_groups[pick_count]
        """The number of questions to randomly select for this group."""
        if quiz_groups_pick_count is not None:
            data["quiz_groups[pick_count]"] = quiz_groups_pick_count
        # OPTIONAL - quiz_groups[question_points]
        """The number of points to assign to each question in the group."""
        if quiz_groups_question_points is not None:
            data["quiz_groups[question_points]"] = quiz_groups_question_points
        # OPTIONAL - quiz_groups[assessment_question_bank_id]
        """The id of the assessment question bank to pull questions from."""
        if quiz_groups_assessment_question_bank_id is not None:
            data["quiz_groups[assessment_question_bank_id]"] = quiz_groups_assessment_question_bank_id

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups".format(**path), data=data, params=params, no_data=True)

    def update_question_group(self, id, quiz_id, course_id, quiz_groups_name=None, quiz_groups_pick_count=None, quiz_groups_question_points=None):
        """
        Update a question group.

        Update a question group
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
        # OPTIONAL - quiz_groups[name]
        """The name of the question group."""
        if quiz_groups_name is not None:
            data["quiz_groups[name]"] = quiz_groups_name
        # OPTIONAL - quiz_groups[pick_count]
        """The number of questions to randomly select for this group."""
        if quiz_groups_pick_count is not None:
            data["quiz_groups[pick_count]"] = quiz_groups_pick_count
        # OPTIONAL - quiz_groups[question_points]
        """The number of points to assign to each question in the group."""
        if quiz_groups_question_points is not None:
            data["quiz_groups[question_points]"] = quiz_groups_question_points

        self.logger.debug("PUT /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}".format(**path), data=data, params=params, no_data=True)

    def delete_question_group(self, id, quiz_id, course_id):
        """
        Delete a question group.

        Delete a question group
        
        <b>204 No Content<b> response code is returned if the deletion was successful.
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

        self.logger.debug("DELETE /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}".format(**path), data=data, params=params, no_data=True)

    def reorder_question_groups(self, id, quiz_id, order_id, course_id, order_type=None):
        """
        Reorder question groups.

        Change the order of the quiz questions within the group
        
        <b>204 No Content<b> response code is returned if the reorder was successful.
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
        # REQUIRED - order[id]
        """The associated item's unique identifier"""
        data["order[id]"] = order_id
        # OPTIONAL - order[type]
        """The type of item is always 'question' for a group"""
        if order_type is not None:
            self._validate_enum(order_type, ["question"])
            data["order[type]"] = order_type

        self.logger.debug("POST /api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder".format(**path), data=data, params=params, no_data=True)


class Quizgroup(BaseModel):
    """Quizgroup Model."""

    def __init__(self, id, quiz_id, name=None, question_points=None, position=None, pick_count=None, assessment_question_bank_id=None):
        """Init method for Quizgroup class."""
        self._name = name
        self._question_points = question_points
        self._id = id
        self._position = position
        self._pick_count = pick_count
        self._quiz_id = quiz_id
        self._assessment_question_bank_id = assessment_question_bank_id

        self.logger = logging.getLogger('pycanvas.Quizgroup')

    @property
    def name(self):
        """The name of the question group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def question_points(self):
        """The amount of points allotted to each question in the group."""
        return self._question_points

    @question_points.setter
    def question_points(self, value):
        """Setter for question_points property."""
        self.logger.warn("Setting values on question_points will NOT update the remote Canvas instance.")
        self._question_points = value

    @property
    def id(self):
        """The ID of the question group."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def position(self):
        """The order in which the question group will be retrieved and displayed."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def pick_count(self):
        """The number of questions to pick from the group to display to the student."""
        return self._pick_count

    @pick_count.setter
    def pick_count(self, value):
        """Setter for pick_count property."""
        self.logger.warn("Setting values on pick_count will NOT update the remote Canvas instance.")
        self._pick_count = value

    @property
    def quiz_id(self):
        """The ID of the Quiz the question group belongs to."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def assessment_question_bank_id(self):
        """The ID of the Assessment question bank to pull questions from."""
        return self._assessment_question_bank_id

    @assessment_question_bank_id.setter
    def assessment_question_bank_id(self, value):
        """Setter for assessment_question_bank_id property."""
        self.logger.warn("Setting values on assessment_question_bank_id will NOT update the remote Canvas instance.")
        self._assessment_question_bank_id = value

