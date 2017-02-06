"""AssignmentGroups API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AssignmentGroupsAPI(BaseCanvasAPI):
    """AssignmentGroups API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AssignmentGroupsAPI."""
        super(AssignmentGroupsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AssignmentGroupsAPI")

    def list_assignment_groups(self, course_id, exclude_assignment_submission_types=None, grading_period_id=None, include=None, override_assignment_dates=None, scope_assignments_to_student=None):
        """
        List assignment groups.

        Returns the list of assignment groups for the current context. The returned
        groups are sorted by their position field.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - include
        """Associations to include with the group. "discussion_topic", "all_dates"
        "assignment_visibility" & "submission" are only valid are only valid if "assignments" is also included.
        The "assignment_visibility" option additionally requires that the Differentiated Assignments course feature be turned on."""
        if include is not None:
            self._validate_enum(include, ["assignments", "discussion_topic", "all_dates", "assignment_visibility", "overrides", "submission"])
            params["include"] = include

        # OPTIONAL - exclude_assignment_submission_types
        """If "assignments" are included, those with the specified submission types
        will be excluded from the assignment groups."""
        if exclude_assignment_submission_types is not None:
            self._validate_enum(exclude_assignment_submission_types, ["online_quiz", "discussion_topic", "wiki_page", "external_tool"])
            params["exclude_assignment_submission_types"] = exclude_assignment_submission_types

        # OPTIONAL - override_assignment_dates
        """Apply assignment overrides for each assignment, defaults to true."""
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates

        # OPTIONAL - grading_period_id
        """The id of the grading period in which assignment groups are being requested
        (Requires the Multiple Grading Periods feature turned on.)"""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - scope_assignments_to_student
        """If true, all assignments returned will apply to the current user in the
        specified grading period. If assignments apply to other students in the
        specified grading period, but not the current user, they will not be
        returned. (Requires the grading_period_id argument and the Multiple Grading
        Periods feature turned on. In addition, the current user must be a student.)"""
        if scope_assignments_to_student is not None:
            params["scope_assignments_to_student"] = scope_assignments_to_student

        self.logger.debug("GET /api/v1/courses/{course_id}/assignment_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignment_groups".format(**path), data=data, params=params, all_pages=True)

    def get_assignment_group(self, course_id, assignment_group_id, grading_period_id=None, include=None, override_assignment_dates=None):
        """
        Get an Assignment Group.

        Returns the assignment group with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_group_id
        """ID"""
        path["assignment_group_id"] = assignment_group_id

        # OPTIONAL - include
        """Associations to include with the group. "discussion_topic" and "assignment_visibility" and "submission"
        are only valid if "assignments" is also included. The "assignment_visibility" option additionally
        requires that the Differentiated Assignments course feature be turned on."""
        if include is not None:
            self._validate_enum(include, ["assignments", "discussion_topic", "assignment_visibility", "submission"])
            params["include"] = include

        # OPTIONAL - override_assignment_dates
        """Apply assignment overrides for each assignment, defaults to true."""
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates

        # OPTIONAL - grading_period_id
        """The id of the grading period in which assignment groups are being requested
        (Requires the Multiple Grading Periods account feature turned on)"""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        self.logger.debug("GET /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}".format(**path), data=data, params=params, single_item=True)

    def create_assignment_group(self, course_id, group_weight=None, integration_data=None, name=None, position=None, rules=None, sis_source_id=None):
        """
        Create an Assignment Group.

        Create a new assignment group for this course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - name
        """The assignment group's name"""
        if name is not None:
            data["name"] = name

        # OPTIONAL - position
        """The position of this assignment group in relation to the other assignment groups"""
        if position is not None:
            data["position"] = position

        # OPTIONAL - group_weight
        """The percent of the total grade that this assignment group represents"""
        if group_weight is not None:
            data["group_weight"] = group_weight

        # OPTIONAL - sis_source_id
        """The sis source id of the Assignment Group"""
        if sis_source_id is not None:
            data["sis_source_id"] = sis_source_id

        # OPTIONAL - integration_data
        """The integration data of the Assignment Group"""
        if integration_data is not None:
            data["integration_data"] = integration_data

        # OPTIONAL - rules
        """The grading rules that are applied within this assignment group
        See the Assignment Group object definition for format"""
        if rules is not None:
            data["rules"] = rules

        self.logger.debug("POST /api/v1/courses/{course_id}/assignment_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignment_groups".format(**path), data=data, params=params, single_item=True)

    def edit_assignment_group(self, course_id, assignment_group_id):
        """
        Edit an Assignment Group.

        Modify an existing Assignment Group.
        Accepts the same parameters as Assignment Group creation
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_group_id
        """ID"""
        path["assignment_group_id"] = assignment_group_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}".format(**path), data=data, params=params, single_item=True)

    def destroy_assignment_group(self, course_id, assignment_group_id, move_assignments_to=None):
        """
        Destroy an Assignment Group.

        Deletes the assignment group with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_group_id
        """ID"""
        path["assignment_group_id"] = assignment_group_id

        # OPTIONAL - move_assignments_to
        """The ID of an active Assignment Group to which the assignments that are
        currently assigned to the destroyed Assignment Group will be assigned.
        NOTE: If this argument is not provided, any assignments in this Assignment
        Group will be deleted."""
        if move_assignments_to is not None:
            params["move_assignments_to"] = move_assignments_to

        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}".format(**path), data=data, params=params, single_item=True)


class Gradingrules(BaseModel):
    """Gradingrules Model."""

    def __init__(self, never_drop=None, drop_highest=None, drop_lowest=None):
        """Init method for Gradingrules class."""
        self._never_drop = never_drop
        self._drop_highest = drop_highest
        self._drop_lowest = drop_lowest

        self.logger = logging.getLogger('pycanvas.Gradingrules')

    @property
    def never_drop(self):
        """Assignment IDs that should never be dropped."""
        return self._never_drop

    @never_drop.setter
    def never_drop(self, value):
        """Setter for never_drop property."""
        self.logger.warn("Setting values on never_drop will NOT update the remote Canvas instance.")
        self._never_drop = value

    @property
    def drop_highest(self):
        """Number of highest scores to be dropped for each user."""
        return self._drop_highest

    @drop_highest.setter
    def drop_highest(self, value):
        """Setter for drop_highest property."""
        self.logger.warn("Setting values on drop_highest will NOT update the remote Canvas instance.")
        self._drop_highest = value

    @property
    def drop_lowest(self):
        """Number of lowest scores to be dropped for each user."""
        return self._drop_lowest

    @drop_lowest.setter
    def drop_lowest(self, value):
        """Setter for drop_lowest property."""
        self.logger.warn("Setting values on drop_lowest will NOT update the remote Canvas instance.")
        self._drop_lowest = value


class Assignmentgroup(BaseModel):
    """Assignmentgroup Model."""

    def __init__(self, group_weight=None, name=None, rules=None, assignments=None, sis_source_id=None, integration_data=None, position=None, id=None):
        """Init method for Assignmentgroup class."""
        self._group_weight = group_weight
        self._name = name
        self._rules = rules
        self._assignments = assignments
        self._sis_source_id = sis_source_id
        self._integration_data = integration_data
        self._position = position
        self._id = id

        self.logger = logging.getLogger('pycanvas.Assignmentgroup')

    @property
    def group_weight(self):
        """the weight of the Assignment Group."""
        return self._group_weight

    @group_weight.setter
    def group_weight(self, value):
        """Setter for group_weight property."""
        self.logger.warn("Setting values on group_weight will NOT update the remote Canvas instance.")
        self._group_weight = value

    @property
    def name(self):
        """the name of the Assignment Group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def rules(self):
        """the grading rules that this Assignment Group has."""
        return self._rules

    @rules.setter
    def rules(self, value):
        """Setter for rules property."""
        self.logger.warn("Setting values on rules will NOT update the remote Canvas instance.")
        self._rules = value

    @property
    def assignments(self):
        """the assignments in this Assignment Group (see the Assignment API for a detailed list of fields)."""
        return self._assignments

    @assignments.setter
    def assignments(self, value):
        """Setter for assignments property."""
        self.logger.warn("Setting values on assignments will NOT update the remote Canvas instance.")
        self._assignments = value

    @property
    def sis_source_id(self):
        """the sis source id of the Assignment Group."""
        return self._sis_source_id

    @sis_source_id.setter
    def sis_source_id(self, value):
        """Setter for sis_source_id property."""
        self.logger.warn("Setting values on sis_source_id will NOT update the remote Canvas instance.")
        self._sis_source_id = value

    @property
    def integration_data(self):
        """the integration data of the Assignment Group."""
        return self._integration_data

    @integration_data.setter
    def integration_data(self, value):
        """Setter for integration_data property."""
        self.logger.warn("Setting values on integration_data will NOT update the remote Canvas instance.")
        self._integration_data = value

    @property
    def position(self):
        """the position of the Assignment Group."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def id(self):
        """the id of the Assignment Group."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

