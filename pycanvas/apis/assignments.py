"""Assignments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class AssignmentsAPI(BaseCanvasAPI):
    """Assignments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AssignmentsAPI."""
        super(AssignmentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.AssignmentsAPI")

    def delete_assignment(self, id, course_id):
        """
        Delete an assignment.

        Delete the given assignment.
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

        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def list_assignments(self, course_id, assignment_ids=None, bucket=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None, search_term=None):
        """
        List assignments.

        Returns the list of assignments for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - include
        """Associations to include with the assignment. The "assignment_visibility" option
        requires that the Differentiated Assignments course feature be turned on. If
        "observed_users" is passed, submissions for observed users will also be included as an array."""
        if include is not None:
            self._validate_enum(include, ["submission", "assignment_visibility", "all_dates", "overrides", "observed_users"])
            params["include"] = include

        # OPTIONAL - search_term
        """The partial title of the assignments to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - override_assignment_dates
        """Apply assignment overrides for each assignment, defaults to true."""
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates

        # OPTIONAL - needs_grading_count_by_section
        """Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false"""
        if needs_grading_count_by_section is not None:
            params["needs_grading_count_by_section"] = needs_grading_count_by_section

        # OPTIONAL - bucket
        """If included, only return certain assignments depending on due date and submission status."""
        if bucket is not None:
            self._validate_enum(bucket, ["past", "overdue", "undated", "ungraded", "unsubmitted", "upcoming", "future"])
            params["bucket"] = bucket

        # OPTIONAL - assignment_ids
        """if set, return only assignments specified"""
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments".format(**path), data=data, params=params, all_pages=True)

    def list_assignments_for_user(self, user_id, course_id):
        """
        List assignments for user.

        Returns the list of assignments for the specified user if the current user has rights to view.
        See {api:AssignmentsApiController#index List assignments} for valid arguments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/users/{user_id}/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/courses/{course_id}/assignments".format(**path), data=data, params=params, no_data=True)

    def get_single_assignment(self, id, course_id, all_dates=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None):
        """
        Get a single assignment.

        Returns the assignment with the given id.
         "observed_users" is passed, submissions for observed users will also be included.
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

        # OPTIONAL - include
        """Associations to include with the assignment. The "assignment_visibility" option
        requires that the Differentiated Assignments course feature be turned on. If"""
        if include is not None:
            self._validate_enum(include, ["submission", "assignment_visibility", "overrides", "observed_users"])
            params["include"] = include

        # OPTIONAL - override_assignment_dates
        """Apply assignment overrides to the assignment, defaults to true."""
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates

        # OPTIONAL - needs_grading_count_by_section
        """Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false"""
        if needs_grading_count_by_section is not None:
            params["needs_grading_count_by_section"] = needs_grading_count_by_section

        # OPTIONAL - all_dates
        """All dates associated with the assignment, if applicable"""
        if all_dates is not None:
            params["all_dates"] = all_dates

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def create_assignment(self, course_id, assignment_name, assignment_allowed_extensions=None, assignment_assignment_group_id=None, assignment_assignment_overrides=None, assignment_automatic_peer_reviews=None, assignment_description=None, assignment_due_at=None, assignment_external_tool_tag_attributes=None, assignment_grade_group_students_individually=None, assignment_grading_standard_id=None, assignment_grading_type=None, assignment_group_category_id=None, assignment_integration_data=None, assignment_integration_id=None, assignment_lock_at=None, assignment_muted=None, assignment_notify_of_update=None, assignment_omit_from_final_grade=None, assignment_only_visible_to_overrides=None, assignment_peer_reviews=None, assignment_points_possible=None, assignment_position=None, assignment_published=None, assignment_submission_types=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_unlock_at=None, assignment_vericite_enabled=None):
        """
        Create an assignment.

        Create a new assignment for this course. The assignment is created in the
        active state.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - assignment[name]
        """The assignment name."""
        data["assignment[name]"] = assignment_name

        # OPTIONAL - assignment[position]
        """The position of this assignment in the group when displaying
        assignment lists."""
        if assignment_position is not None:
            data["assignment[position]"] = assignment_position

        # OPTIONAL - assignment[submission_types]
        """List of supported submission types for the assignment.
        Unless the assignment is allowing online submissions, the array should
        only have one element.
        
        If not allowing online submissions, your options are:
          "online_quiz"
          "none"
          "on_paper"
          "online_quiz"
          "discussion_topic"
          "external_tool"
        
        If you are allowing online submissions, you can have one or many
        allowed submission types:
        
          "online_upload"
          "online_text_entry"
          "online_url"
          "media_recording" (Only valid when the Kaltura plugin is enabled)"""
        if assignment_submission_types is not None:
            self._validate_enum(assignment_submission_types, ["online_quiz", "none", "on_paper", "online_quiz", "discussion_topic", "external_tool", "online_upload", "online_text_entry", "online_url", "media_recording"])
            data["assignment[submission_types]"] = assignment_submission_types

        # OPTIONAL - assignment[allowed_extensions]
        """Allowed extensions if submission_types includes "online_upload"
        
        Example:
          allowed_extensions: ["docx","ppt"]"""
        if assignment_allowed_extensions is not None:
            data["assignment[allowed_extensions]"] = assignment_allowed_extensions

        # OPTIONAL - assignment[turnitin_enabled]
        """Only applies when the Turnitin plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles Turnitin submissions for the assignment.
        Will be ignored if Turnitin is not available for the course."""
        if assignment_turnitin_enabled is not None:
            data["assignment[turnitin_enabled]"] = assignment_turnitin_enabled

        # OPTIONAL - assignment[vericite_enabled]
        """Only applies when the VeriCite plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles VeriCite submissions for the assignment.
        Will be ignored if VeriCite is not available for the course."""
        if assignment_vericite_enabled is not None:
            data["assignment[vericite_enabled]"] = assignment_vericite_enabled

        # OPTIONAL - assignment[turnitin_settings]
        """Settings to send along to turnitin. See Assignment object definition for
        format."""
        if assignment_turnitin_settings is not None:
            data["assignment[turnitin_settings]"] = assignment_turnitin_settings

        # OPTIONAL - assignment[integration_data]
        """Data related to third party integrations, JSON string required."""
        if assignment_integration_data is not None:
            data["assignment[integration_data]"] = assignment_integration_data

        # OPTIONAL - assignment[integration_id]
        """Unique ID from third party integrations"""
        if assignment_integration_id is not None:
            data["assignment[integration_id]"] = assignment_integration_id

        # OPTIONAL - assignment[peer_reviews]
        """If submission_types does not include external_tool,discussion_topic,
        online_quiz, or on_paper, determines whether or not peer reviews
        will be turned on for the assignment."""
        if assignment_peer_reviews is not None:
            data["assignment[peer_reviews]"] = assignment_peer_reviews

        # OPTIONAL - assignment[automatic_peer_reviews]
        """Whether peer reviews will be assigned automatically by Canvas or if
        teachers must manually assign peer reviews. Does not apply if peer reviews
        are not enabled."""
        if assignment_automatic_peer_reviews is not None:
            data["assignment[automatic_peer_reviews]"] = assignment_automatic_peer_reviews

        # OPTIONAL - assignment[notify_of_update]
        """If true, Canvas will send a notification to students in the class
        notifying them that the content has changed."""
        if assignment_notify_of_update is not None:
            data["assignment[notify_of_update]"] = assignment_notify_of_update

        # OPTIONAL - assignment[group_category_id]
        """If present, the assignment will become a group assignment assigned
        to the group."""
        if assignment_group_category_id is not None:
            data["assignment[group_category_id]"] = assignment_group_category_id

        # OPTIONAL - assignment[grade_group_students_individually]
        """If this is a group assignment, teachers have the options to grade
        students individually. If false, Canvas will apply the assignment's
        score to each member of the group. If true, the teacher can manually
        assign scores to each member of the group."""
        if assignment_grade_group_students_individually is not None:
            data["assignment[grade_group_students_individually]"] = assignment_grade_group_students_individually

        # OPTIONAL - assignment[external_tool_tag_attributes]
        """Hash of external tool parameters if submission_types is ["external_tool"].
        See Assignment object definition for format."""
        if assignment_external_tool_tag_attributes is not None:
            data["assignment[external_tool_tag_attributes]"] = assignment_external_tool_tag_attributes

        # OPTIONAL - assignment[points_possible]
        """The maximum points possible on the assignment."""
        if assignment_points_possible is not None:
            data["assignment[points_possible]"] = assignment_points_possible

        # OPTIONAL - assignment[grading_type]
        """The strategy used for grading the assignment.
        The assignment defaults to "points" if this field is omitted."""
        if assignment_grading_type is not None:
            self._validate_enum(assignment_grading_type, ["pass_fail", "percent", "letter_grade", "gpa_scale", "points"])
            data["assignment[grading_type]"] = assignment_grading_type

        # OPTIONAL - assignment[due_at]
        """The day/time the assignment is due.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_due_at is not None:
            data["assignment[due_at]"] = assignment_due_at

        # OPTIONAL - assignment[lock_at]
        """The day/time the assignment is locked after.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_lock_at is not None:
            data["assignment[lock_at]"] = assignment_lock_at

        # OPTIONAL - assignment[unlock_at]
        """The day/time the assignment is unlocked.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_unlock_at is not None:
            data["assignment[unlock_at]"] = assignment_unlock_at

        # OPTIONAL - assignment[description]
        """The assignment's description, supports HTML."""
        if assignment_description is not None:
            data["assignment[description]"] = assignment_description

        # OPTIONAL - assignment[assignment_group_id]
        """The assignment group id to put the assignment in.
        Defaults to the top assignment group in the course."""
        if assignment_assignment_group_id is not None:
            data["assignment[assignment_group_id]"] = assignment_assignment_group_id

        # OPTIONAL - assignment[muted]
        """Whether this assignment is muted.
        A muted assignment does not send change notifications
        and hides grades from students.
        Defaults to false."""
        if assignment_muted is not None:
            data["assignment[muted]"] = assignment_muted

        # OPTIONAL - assignment[assignment_overrides]
        """List of overrides for the assignment.
        NOTE: The assignment overrides feature is in beta."""
        if assignment_assignment_overrides is not None:
            data["assignment[assignment_overrides]"] = assignment_assignment_overrides

        # OPTIONAL - assignment[only_visible_to_overrides]
        """Whether this assignment is only visible to overrides
        (Only useful if 'differentiated assignments' account setting is on)"""
        if assignment_only_visible_to_overrides is not None:
            data["assignment[only_visible_to_overrides]"] = assignment_only_visible_to_overrides

        # OPTIONAL - assignment[published]
        """Whether this assignment is published.
        (Only useful if 'draft state' account setting is on)
        Unpublished assignments are not visible to students."""
        if assignment_published is not None:
            data["assignment[published]"] = assignment_published

        # OPTIONAL - assignment[grading_standard_id]
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'."""
        if assignment_grading_standard_id is not None:
            data["assignment[grading_standard_id]"] = assignment_grading_standard_id

        # OPTIONAL - assignment[omit_from_final_grade]
        """Whether this assignment is counted towards a student's final grade."""
        if assignment_omit_from_final_grade is not None:
            data["assignment[omit_from_final_grade]"] = assignment_omit_from_final_grade

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments".format(**path), data=data, params=params, single_item=True)

    def edit_assignment(self, id, course_id, assignment_allowed_extensions=None, assignment_assignment_group_id=None, assignment_assignment_overrides=None, assignment_automatic_peer_reviews=None, assignment_description=None, assignment_due_at=None, assignment_external_tool_tag_attributes=None, assignment_grade_group_students_individually=None, assignment_grading_standard_id=None, assignment_grading_type=None, assignment_group_category_id=None, assignment_integration_data=None, assignment_integration_id=None, assignment_lock_at=None, assignment_muted=None, assignment_name=None, assignment_notify_of_update=None, assignment_omit_from_final_grade=None, assignment_only_visible_to_overrides=None, assignment_peer_reviews=None, assignment_points_possible=None, assignment_position=None, assignment_published=None, assignment_submission_types=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_unlock_at=None, assignment_vericite_enabled=None):
        """
        Edit an assignment.

        Modify an existing assignment.
        
        If the assignment [assignment_overrides] key is absent, any existing
        overrides are kept as is. If the assignment [assignment_overrides] key is
        present, existing overrides are updated or deleted (and new ones created,
        as necessary) to match the provided list.
        
        NOTE: The assignment overrides feature is in beta.
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

        # OPTIONAL - assignment[name]
        """The assignment name."""
        if assignment_name is not None:
            data["assignment[name]"] = assignment_name

        # OPTIONAL - assignment[position]
        """The position of this assignment in the group when displaying
        assignment lists."""
        if assignment_position is not None:
            data["assignment[position]"] = assignment_position

        # OPTIONAL - assignment[submission_types]
        """List of supported submission types for the assignment.
        Unless the assignment is allowing online submissions, the array should
        only have one element.
        
        If not allowing online submissions, your options are:
          "online_quiz"
          "none"
          "on_paper"
          "online_quiz"
          "discussion_topic"
          "external_tool"
        
        If you are allowing online submissions, you can have one or many
        allowed submission types:
        
          "online_upload"
          "online_text_entry"
          "online_url"
          "media_recording" (Only valid when the Kaltura plugin is enabled)"""
        if assignment_submission_types is not None:
            self._validate_enum(assignment_submission_types, ["online_quiz", "none", "on_paper", "online_quiz", "discussion_topic", "external_tool", "online_upload", "online_text_entry", "online_url", "media_recording"])
            data["assignment[submission_types]"] = assignment_submission_types

        # OPTIONAL - assignment[allowed_extensions]
        """Allowed extensions if submission_types includes "online_upload"
        
        Example:
          allowed_extensions: ["docx","ppt"]"""
        if assignment_allowed_extensions is not None:
            data["assignment[allowed_extensions]"] = assignment_allowed_extensions

        # OPTIONAL - assignment[turnitin_enabled]
        """Only applies when the Turnitin plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles Turnitin submissions for the assignment.
        Will be ignored if Turnitin is not available for the course."""
        if assignment_turnitin_enabled is not None:
            data["assignment[turnitin_enabled]"] = assignment_turnitin_enabled

        # OPTIONAL - assignment[vericite_enabled]
        """Only applies when the VeriCite plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles VeriCite submissions for the assignment.
        Will be ignored if VeriCite is not available for the course."""
        if assignment_vericite_enabled is not None:
            data["assignment[vericite_enabled]"] = assignment_vericite_enabled

        # OPTIONAL - assignment[turnitin_settings]
        """Settings to send along to turnitin. See Assignment object definition for
        format."""
        if assignment_turnitin_settings is not None:
            data["assignment[turnitin_settings]"] = assignment_turnitin_settings

        # OPTIONAL - assignment[integration_data]
        """Data related to third party integrations, JSON string required."""
        if assignment_integration_data is not None:
            data["assignment[integration_data]"] = assignment_integration_data

        # OPTIONAL - assignment[integration_id]
        """Unique ID from third party integrations"""
        if assignment_integration_id is not None:
            data["assignment[integration_id]"] = assignment_integration_id

        # OPTIONAL - assignment[peer_reviews]
        """If submission_types does not include external_tool,discussion_topic,
        online_quiz, or on_paper, determines whether or not peer reviews
        will be turned on for the assignment."""
        if assignment_peer_reviews is not None:
            data["assignment[peer_reviews]"] = assignment_peer_reviews

        # OPTIONAL - assignment[automatic_peer_reviews]
        """Whether peer reviews will be assigned automatically by Canvas or if
        teachers must manually assign peer reviews. Does not apply if peer reviews
        are not enabled."""
        if assignment_automatic_peer_reviews is not None:
            data["assignment[automatic_peer_reviews]"] = assignment_automatic_peer_reviews

        # OPTIONAL - assignment[notify_of_update]
        """If true, Canvas will send a notification to students in the class
        notifying them that the content has changed."""
        if assignment_notify_of_update is not None:
            data["assignment[notify_of_update]"] = assignment_notify_of_update

        # OPTIONAL - assignment[group_category_id]
        """If present, the assignment will become a group assignment assigned
        to the group."""
        if assignment_group_category_id is not None:
            data["assignment[group_category_id]"] = assignment_group_category_id

        # OPTIONAL - assignment[grade_group_students_individually]
        """If this is a group assignment, teachers have the options to grade
        students individually. If false, Canvas will apply the assignment's
        score to each member of the group. If true, the teacher can manually
        assign scores to each member of the group."""
        if assignment_grade_group_students_individually is not None:
            data["assignment[grade_group_students_individually]"] = assignment_grade_group_students_individually

        # OPTIONAL - assignment[external_tool_tag_attributes]
        """Hash of external tool parameters if submission_types is ["external_tool"].
        See Assignment object definition for format."""
        if assignment_external_tool_tag_attributes is not None:
            data["assignment[external_tool_tag_attributes]"] = assignment_external_tool_tag_attributes

        # OPTIONAL - assignment[points_possible]
        """The maximum points possible on the assignment."""
        if assignment_points_possible is not None:
            data["assignment[points_possible]"] = assignment_points_possible

        # OPTIONAL - assignment[grading_type]
        """The strategy used for grading the assignment.
        The assignment defaults to "points" if this field is omitted."""
        if assignment_grading_type is not None:
            self._validate_enum(assignment_grading_type, ["pass_fail", "percent", "letter_grade", "gpa_scale", "points"])
            data["assignment[grading_type]"] = assignment_grading_type

        # OPTIONAL - assignment[due_at]
        """The day/time the assignment is due.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_due_at is not None:
            data["assignment[due_at]"] = assignment_due_at

        # OPTIONAL - assignment[lock_at]
        """The day/time the assignment is locked after.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_lock_at is not None:
            data["assignment[lock_at]"] = assignment_lock_at

        # OPTIONAL - assignment[unlock_at]
        """The day/time the assignment is unlocked.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z."""
        if assignment_unlock_at is not None:
            data["assignment[unlock_at]"] = assignment_unlock_at

        # OPTIONAL - assignment[description]
        """The assignment's description, supports HTML."""
        if assignment_description is not None:
            data["assignment[description]"] = assignment_description

        # OPTIONAL - assignment[assignment_group_id]
        """The assignment group id to put the assignment in.
        Defaults to the top assignment group in the course."""
        if assignment_assignment_group_id is not None:
            data["assignment[assignment_group_id]"] = assignment_assignment_group_id

        # OPTIONAL - assignment[muted]
        """Whether this assignment is muted.
        A muted assignment does not send change notifications
        and hides grades from students.
        Defaults to false."""
        if assignment_muted is not None:
            data["assignment[muted]"] = assignment_muted

        # OPTIONAL - assignment[assignment_overrides]
        """List of overrides for the assignment.
        NOTE: The assignment overrides feature is in beta."""
        if assignment_assignment_overrides is not None:
            data["assignment[assignment_overrides]"] = assignment_assignment_overrides

        # OPTIONAL - assignment[only_visible_to_overrides]
        """Whether this assignment is only visible to overrides
        (Only useful if 'differentiated assignments' account setting is on)"""
        if assignment_only_visible_to_overrides is not None:
            data["assignment[only_visible_to_overrides]"] = assignment_only_visible_to_overrides

        # OPTIONAL - assignment[published]
        """Whether this assignment is published.
        (Only useful if 'draft state' account setting is on)
        Unpublished assignments are not visible to students."""
        if assignment_published is not None:
            data["assignment[published]"] = assignment_published

        # OPTIONAL - assignment[grading_standard_id]
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'."""
        if assignment_grading_standard_id is not None:
            data["assignment[grading_standard_id]"] = assignment_grading_standard_id

        # OPTIONAL - assignment[omit_from_final_grade]
        """Whether this assignment is counted towards a student's final grade."""
        if assignment_omit_from_final_grade is not None:
            data["assignment[omit_from_final_grade]"] = assignment_omit_from_final_grade

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def list_assignment_overrides(self, course_id, assignment_id):
        """
        List assignment overrides.

        Returns the list of overrides for this assignment that target
        sections/groups/students visible to the current user.
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

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides".format(**path), data=data, params=params, all_pages=True)

    def get_single_assignment_override(self, id, course_id, assignment_id):
        """
        Get a single assignment override.

        Returns details of the the override with the given id.
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

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def redirect_to_assignment_override_for_group(self, group_id, assignment_id):
        """
        Redirect to the assignment override for a group.

        Responds with a redirect to the override for the given group, if any
        (404 otherwise).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        self.logger.debug("GET /api/v1/groups/{group_id}/assignments/{assignment_id}/override with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/assignments/{assignment_id}/override".format(**path), data=data, params=params, no_data=True)

    def redirect_to_assignment_override_for_section(self, assignment_id, course_section_id):
        """
        Redirect to the assignment override for a section.

        Responds with a redirect to the override for the given section, if any
        (404 otherwise).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_section_id
        """ID"""
        path["course_section_id"] = course_section_id

        # REQUIRED - PATH - assignment_id
        """ID"""
        path["assignment_id"] = assignment_id

        self.logger.debug("GET /api/v1/sections/{course_section_id}/assignments/{assignment_id}/override with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{course_section_id}/assignments/{assignment_id}/override".format(**path), data=data, params=params, no_data=True)

    def create_assignment_override(self, course_id, assignment_id, assignment_override_course_section_id=None, assignment_override_due_at=None, assignment_override_group_id=None, assignment_override_lock_at=None, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_unlock_at=None):
        """
        Create an assignment override.

        One of student_ids, group_id, or course_section_id must be present. At most
        one should be present; if multiple are present only the most specific
        (student_ids first, then group_id, then course_section_id) is used and any
        others are ignored.
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

        # OPTIONAL - assignment_override[student_ids]
        """The IDs of
        the override's target students. If present, the IDs must each identify a
        user with an active student enrollment in the course that is not already
        targetted by a different adhoc override."""
        if assignment_override_student_ids is not None:
            data["assignment_override[student_ids]"] = assignment_override_student_ids

        # OPTIONAL - assignment_override[title]
        """The title of the adhoc
        assignment override. Required if student_ids is present, ignored
        otherwise (the title is set to the name of the targetted group or section
        instead)."""
        if assignment_override_title is not None:
            data["assignment_override[title]"] = assignment_override_title

        # OPTIONAL - assignment_override[group_id]
        """The ID of the
        override's target group. If present, the following conditions must be met
        for the override to be successful:
        
        1. the assignment MUST be a group assignment (a group_category_id is assigned to it)
        2. the ID must identify an active group in the group set the assignment is in
        3. the ID must not be targetted by a different override
        
        See {Appendix: Group assignments} for more info."""
        if assignment_override_group_id is not None:
            data["assignment_override[group_id]"] = assignment_override_group_id

        # OPTIONAL - assignment_override[course_section_id]
        """The ID
        of the override's target section. If present, must identify an active
        section of the assignment's course not already targetted by a different
        override."""
        if assignment_override_course_section_id is not None:
            data["assignment_override[course_section_id]"] = assignment_override_course_section_id

        # OPTIONAL - assignment_override[due_at]
        """The day/time
        the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
        2014-10-21T18:48:00Z. If absent, this override will not affect due date.
        May be present but null to indicate the override removes any previous due
        date."""
        if assignment_override_due_at is not None:
            data["assignment_override[due_at]"] = assignment_override_due_at

        # OPTIONAL - assignment_override[unlock_at]
        """The day/time
        the overridden assignment becomes unlocked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the unlock date. May be present but null to indicate the override
        removes any previous unlock date."""
        if assignment_override_unlock_at is not None:
            data["assignment_override[unlock_at]"] = assignment_override_unlock_at

        # OPTIONAL - assignment_override[lock_at]
        """The day/time
        the overridden assignment becomes locked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the lock date. May be present but null to indicate the override
        removes any previous lock date."""
        if assignment_override_lock_at is not None:
            data["assignment_override[lock_at]"] = assignment_override_lock_at

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides".format(**path), data=data, params=params, single_item=True)

    def update_assignment_override(self, id, course_id, assignment_id, assignment_override_due_at=None, assignment_override_lock_at=None, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_unlock_at=None):
        """
        Update an assignment override.

        All current overridden values must be supplied if they are to be retained;
        e.g. if due_at was overridden, but this PUT omits a value for due_at,
        due_at will no longer be overridden. If the override is adhoc and
        student_ids is not supplied, the target override set is unchanged. Target
        override sets cannot be changed for group or section overrides.
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

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - assignment_override[student_ids]
        """The IDs of the
        override's target students. If present, the IDs must each identify a
        user with an active student enrollment in the course that is not already
        targetted by a different adhoc override. Ignored unless the override
        being updated is adhoc."""
        if assignment_override_student_ids is not None:
            data["assignment_override[student_ids]"] = assignment_override_student_ids

        # OPTIONAL - assignment_override[title]
        """The title of an adhoc
        assignment override. Ignored unless the override being updated is adhoc."""
        if assignment_override_title is not None:
            data["assignment_override[title]"] = assignment_override_title

        # OPTIONAL - assignment_override[due_at]
        """The day/time
        the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
        2014-10-21T18:48:00Z. If absent, this override will not affect due date.
        May be present but null to indicate the override removes any previous due
        date."""
        if assignment_override_due_at is not None:
            data["assignment_override[due_at]"] = assignment_override_due_at

        # OPTIONAL - assignment_override[unlock_at]
        """The day/time
        the overridden assignment becomes unlocked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the unlock date. May be present but null to indicate the override
        removes any previous unlock date."""
        if assignment_override_unlock_at is not None:
            data["assignment_override[unlock_at]"] = assignment_override_unlock_at

        # OPTIONAL - assignment_override[lock_at]
        """The day/time
        the overridden assignment becomes locked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the lock date. May be present but null to indicate the override
        removes any previous lock date."""
        if assignment_override_lock_at is not None:
            data["assignment_override[lock_at]"] = assignment_override_lock_at

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_assignment_override(self, id, course_id, assignment_id):
        """
        Delete an assignment override.

        Deletes an override and returns its former details.
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

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def batch_retrieve_overrides_in_course(self, course_id, assignment_overrides_id, assignment_overrides_assignment_id):
        """
        Batch retrieve overrides in a course.

        Returns a list of specified overrides in this course, providing
        they target sections/groups/students visible to the current user.
        Returns null elements in the list for requests that were not found.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - assignment_overrides[id]
        """Ids of overrides to retrieve"""
        params["assignment_overrides[id]"] = assignment_overrides_id

        # REQUIRED - assignment_overrides[assignment_id]
        """Ids of assignments for each override"""
        params["assignment_overrides[assignment_id]"] = assignment_overrides_assignment_id

        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)

    def batch_create_overrides_in_course(self, course_id, assignment_overrides):
        """
        Batch create overrides in a course.

        Creates the specified overrides for each assignment.  Handles creation in a
        transaction, so all records are created or none are.
        
        One of student_ids, group_id, or course_section_id must be present. At most
        one should be present; if multiple are present only the most specific
        (student_ids first, then group_id, then course_section_id) is used and any
        others are ignored.
        
        Errors are reported in an errors attribute, an array of errors corresponding
        to inputs.  Global errors will be reported as a single element errors array
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - assignment_overrides
        """Attributes for the new assignment overrides.
        See {api:AssignmentOverridesController#create Create an assignment override} for available
        attributes"""
        data["assignment_overrides"] = assignment_overrides

        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)

    def batch_update_overrides_in_course(self, course_id, assignment_overrides):
        """
        Batch update overrides in a course.

        Updates a list of specified overrides for each assignment.  Handles overrides
        in a transaction, so either all updates are applied or none.
        See {api:AssignmentOverridesController#update Update an assignment override} for
        available attributes.
        
        All current overridden values must be supplied if they are to be retained;
        e.g. if due_at was overridden, but this PUT omits a value for due_at,
        due_at will no longer be overridden. If the override is adhoc and
        student_ids is not supplied, the target override set is unchanged. Target
        override sets cannot be changed for group or section overrides.
        
        Errors are reported in an errors attribute, an array of errors corresponding
        to inputs.  Global errors will be reported as a single element errors array
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - assignment_overrides
        """Attributes for the updated overrides."""
        data["assignment_overrides"] = assignment_overrides

        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)


class Turnitinsettings(BaseModel):
    """Turnitinsettings Model."""

    def __init__(self, originality_report_visibility=None, s_paper_check=None, journal_check=None, exclude_small_matches_type=None, exclude_quoted=None, internet_check=None, exclude_small_matches_value=None, exclude_biblio=None):
        """Init method for Turnitinsettings class."""
        self._originality_report_visibility = originality_report_visibility
        self._s_paper_check = s_paper_check
        self._journal_check = journal_check
        self._exclude_small_matches_type = exclude_small_matches_type
        self._exclude_quoted = exclude_quoted
        self._internet_check = internet_check
        self._exclude_small_matches_value = exclude_small_matches_value
        self._exclude_biblio = exclude_biblio

        self.logger = logging.getLogger('pycanvas.Turnitinsettings')

    @property
    def originality_report_visibility(self):
        """originality_report_visibility."""
        return self._originality_report_visibility

    @originality_report_visibility.setter
    def originality_report_visibility(self, value):
        """Setter for originality_report_visibility property."""
        self.logger.warn("Setting values on originality_report_visibility will NOT update the remote Canvas instance.")
        self._originality_report_visibility = value

    @property
    def s_paper_check(self):
        """s_paper_check."""
        return self._s_paper_check

    @s_paper_check.setter
    def s_paper_check(self, value):
        """Setter for s_paper_check property."""
        self.logger.warn("Setting values on s_paper_check will NOT update the remote Canvas instance.")
        self._s_paper_check = value

    @property
    def journal_check(self):
        """journal_check."""
        return self._journal_check

    @journal_check.setter
    def journal_check(self, value):
        """Setter for journal_check property."""
        self.logger.warn("Setting values on journal_check will NOT update the remote Canvas instance.")
        self._journal_check = value

    @property
    def exclude_small_matches_type(self):
        """exclude_small_matches_type."""
        return self._exclude_small_matches_type

    @exclude_small_matches_type.setter
    def exclude_small_matches_type(self, value):
        """Setter for exclude_small_matches_type property."""
        self.logger.warn("Setting values on exclude_small_matches_type will NOT update the remote Canvas instance.")
        self._exclude_small_matches_type = value

    @property
    def exclude_quoted(self):
        """exclude_quoted."""
        return self._exclude_quoted

    @exclude_quoted.setter
    def exclude_quoted(self, value):
        """Setter for exclude_quoted property."""
        self.logger.warn("Setting values on exclude_quoted will NOT update the remote Canvas instance.")
        self._exclude_quoted = value

    @property
    def internet_check(self):
        """internet_check."""
        return self._internet_check

    @internet_check.setter
    def internet_check(self, value):
        """Setter for internet_check property."""
        self.logger.warn("Setting values on internet_check will NOT update the remote Canvas instance.")
        self._internet_check = value

    @property
    def exclude_small_matches_value(self):
        """exclude_small_matches_value."""
        return self._exclude_small_matches_value

    @exclude_small_matches_value.setter
    def exclude_small_matches_value(self, value):
        """Setter for exclude_small_matches_value property."""
        self.logger.warn("Setting values on exclude_small_matches_value will NOT update the remote Canvas instance.")
        self._exclude_small_matches_value = value

    @property
    def exclude_biblio(self):
        """exclude_biblio."""
        return self._exclude_biblio

    @exclude_biblio.setter
    def exclude_biblio(self, value):
        """Setter for exclude_biblio property."""
        self.logger.warn("Setting values on exclude_biblio will NOT update the remote Canvas instance.")
        self._exclude_biblio = value


class Assignmentoverride(BaseModel):
    """Assignmentoverride Model.
    NOTE: The Assignment Override feature is in beta! This API is not finalized and there could be breaking changes before its final release."""

    def __init__(self, unlock_at=None, title=None, assignment_id=None, lock_at=None, course_section_id=None, all_day=None, student_ids=None, all_day_date=None, due_at=None, group_id=None, id=None):
        """Init method for Assignmentoverride class."""
        self._unlock_at = unlock_at
        self._title = title
        self._assignment_id = assignment_id
        self._lock_at = lock_at
        self._course_section_id = course_section_id
        self._all_day = all_day
        self._student_ids = student_ids
        self._all_day_date = all_day_date
        self._due_at = due_at
        self._group_id = group_id
        self._id = id

        self.logger = logging.getLogger('pycanvas.Assignmentoverride')

    @property
    def unlock_at(self):
        """the overridden unlock at (present if unlock_at is overridden)."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def title(self):
        """the title of the override."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def assignment_id(self):
        """the ID of the assignment the override applies to."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def lock_at(self):
        """the overridden lock at, if any (present if lock_at is overridden)."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def course_section_id(self):
        """the ID of the overrides's target section (present if the override targets a section)."""
        return self._course_section_id

    @course_section_id.setter
    def course_section_id(self, value):
        """Setter for course_section_id property."""
        self.logger.warn("Setting values on course_section_id will NOT update the remote Canvas instance.")
        self._course_section_id = value

    @property
    def all_day(self):
        """the overridden all day flag (present if due_at is overridden)."""
        return self._all_day

    @all_day.setter
    def all_day(self, value):
        """Setter for all_day property."""
        self.logger.warn("Setting values on all_day will NOT update the remote Canvas instance.")
        self._all_day = value

    @property
    def student_ids(self):
        """the IDs of the override's target students (present if the override targets an ad-hoc set of students)."""
        return self._student_ids

    @student_ids.setter
    def student_ids(self, value):
        """Setter for student_ids property."""
        self.logger.warn("Setting values on student_ids will NOT update the remote Canvas instance.")
        self._student_ids = value

    @property
    def all_day_date(self):
        """the overridden all day date (present if due_at is overridden)."""
        return self._all_day_date

    @all_day_date.setter
    def all_day_date(self, value):
        """Setter for all_day_date property."""
        self.logger.warn("Setting values on all_day_date will NOT update the remote Canvas instance.")
        self._all_day_date = value

    @property
    def due_at(self):
        """the overridden due at (present if due_at is overridden)."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def group_id(self):
        """the ID of the override's target group (present if the override targets a group and the assignment is a group assignment)."""
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        """Setter for group_id property."""
        self.logger.warn("Setting values on group_id will NOT update the remote Canvas instance.")
        self._group_id = value

    @property
    def id(self):
        """the ID of the assignment override."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Externaltooltagattributes(BaseModel):
    """Externaltooltagattributes Model."""

    def __init__(self, url=None, new_tab=None, resource_link_id=None):
        """Init method for Externaltooltagattributes class."""
        self._url = url
        self._new_tab = new_tab
        self._resource_link_id = resource_link_id

        self.logger = logging.getLogger('pycanvas.Externaltooltagattributes')

    @property
    def url(self):
        """URL to the external tool."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def new_tab(self):
        """Whether or not there is a new tab for the external tool."""
        return self._new_tab

    @new_tab.setter
    def new_tab(self, value):
        """Setter for new_tab property."""
        self.logger.warn("Setting values on new_tab will NOT update the remote Canvas instance.")
        self._new_tab = value

    @property
    def resource_link_id(self):
        """the identifier for this tool_tag."""
        return self._resource_link_id

    @resource_link_id.setter
    def resource_link_id(self, value):
        """Setter for resource_link_id property."""
        self.logger.warn("Setting values on resource_link_id will NOT update the remote Canvas instance.")
        self._resource_link_id = value


class Assignment(BaseModel):
    """Assignment Model."""

    def __init__(self, use_rubric_for_grading=None, has_overrides=None, lock_info=None, frozen_attributes=None, points_possible=None, assignment_visibility=None, updated_at=None, turnitin_enabled=None, rubric=None, omit_from_final_grade=None, course_id=None, needs_grading_count_by_section=None, id=None, locked_for_user=None, muted=None, grading_type=None, rubric_settings=None, anonymous_submissions=None, peer_reviews=None, discussion_topic=None, intra_group_peer_reviews=None, quiz_id=None, freeze_on_copy=None, all_dates=None, integration_data=None, description=None, peer_review_count=None, grade_group_students_individually=None, grading_standard_id=None, external_tool_tag_attributes=None, html_url=None, turnitin_settings=None, group_category_id=None, lock_explanation=None, needs_grading_count=None, vericite_enabled=None, peer_reviews_assign_at=None, name=None, integration_id=None, frozen=None, only_visible_to_overrides=None, unlock_at=None, submission=None, due_at=None, created_at=None, post_to_sis=None, lock_at=None, assignment_group_id=None, allowed_extensions=None, automatic_peer_reviews=None, published=None, position=None, submission_types=None, submissions_download_url=None, overrides=None, unpublishable=None):
        """Init method for Assignment class."""
        self._use_rubric_for_grading = use_rubric_for_grading
        self._has_overrides = has_overrides
        self._lock_info = lock_info
        self._frozen_attributes = frozen_attributes
        self._points_possible = points_possible
        self._assignment_visibility = assignment_visibility
        self._updated_at = updated_at
        self._turnitin_enabled = turnitin_enabled
        self._rubric = rubric
        self._omit_from_final_grade = omit_from_final_grade
        self._course_id = course_id
        self._needs_grading_count_by_section = needs_grading_count_by_section
        self._id = id
        self._locked_for_user = locked_for_user
        self._muted = muted
        self._grading_type = grading_type
        self._rubric_settings = rubric_settings
        self._anonymous_submissions = anonymous_submissions
        self._peer_reviews = peer_reviews
        self._discussion_topic = discussion_topic
        self._intra_group_peer_reviews = intra_group_peer_reviews
        self._quiz_id = quiz_id
        self._freeze_on_copy = freeze_on_copy
        self._all_dates = all_dates
        self._integration_data = integration_data
        self._description = description
        self._peer_review_count = peer_review_count
        self._grade_group_students_individually = grade_group_students_individually
        self._grading_standard_id = grading_standard_id
        self._external_tool_tag_attributes = external_tool_tag_attributes
        self._html_url = html_url
        self._turnitin_settings = turnitin_settings
        self._group_category_id = group_category_id
        self._lock_explanation = lock_explanation
        self._needs_grading_count = needs_grading_count
        self._vericite_enabled = vericite_enabled
        self._peer_reviews_assign_at = peer_reviews_assign_at
        self._name = name
        self._integration_id = integration_id
        self._frozen = frozen
        self._only_visible_to_overrides = only_visible_to_overrides
        self._unlock_at = unlock_at
        self._submission = submission
        self._due_at = due_at
        self._created_at = created_at
        self._post_to_sis = post_to_sis
        self._lock_at = lock_at
        self._assignment_group_id = assignment_group_id
        self._allowed_extensions = allowed_extensions
        self._automatic_peer_reviews = automatic_peer_reviews
        self._published = published
        self._position = position
        self._submission_types = submission_types
        self._submissions_download_url = submissions_download_url
        self._overrides = overrides
        self._unpublishable = unpublishable

        self.logger = logging.getLogger('pycanvas.Assignment')

    @property
    def use_rubric_for_grading(self):
        """(Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric."""
        return self._use_rubric_for_grading

    @use_rubric_for_grading.setter
    def use_rubric_for_grading(self, value):
        """Setter for use_rubric_for_grading property."""
        self.logger.warn("Setting values on use_rubric_for_grading will NOT update the remote Canvas instance.")
        self._use_rubric_for_grading = value

    @property
    def has_overrides(self):
        """whether this assignment has overrides."""
        return self._has_overrides

    @has_overrides.setter
    def has_overrides(self, value):
        """Setter for has_overrides property."""
        self.logger.warn("Setting values on has_overrides will NOT update the remote Canvas instance.")
        self._has_overrides = value

    @property
    def lock_info(self):
        """(Optional) Information for the user about the lock. Present when locked_for_user is true."""
        return self._lock_info

    @lock_info.setter
    def lock_info(self, value):
        """Setter for lock_info property."""
        self.logger.warn("Setting values on lock_info will NOT update the remote Canvas instance.")
        self._lock_info = value

    @property
    def frozen_attributes(self):
        """(Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._frozen_attributes

    @frozen_attributes.setter
    def frozen_attributes(self, value):
        """Setter for frozen_attributes property."""
        self.logger.warn("Setting values on frozen_attributes will NOT update the remote Canvas instance.")
        self._frozen_attributes = value

    @property
    def points_possible(self):
        """the maximum points possible for the assignment."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def assignment_visibility(self):
        """(Optional) If 'assignment_visibility' is included in the 'include' parameter, includes an array of student IDs who can see this assignment."""
        return self._assignment_visibility

    @assignment_visibility.setter
    def assignment_visibility(self, value):
        """Setter for assignment_visibility property."""
        self.logger.warn("Setting values on assignment_visibility will NOT update the remote Canvas instance.")
        self._assignment_visibility = value

    @property
    def updated_at(self):
        """The time at which this assignment was last modified in any way."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def turnitin_enabled(self):
        """Boolean flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available."""
        return self._turnitin_enabled

    @turnitin_enabled.setter
    def turnitin_enabled(self, value):
        """Setter for turnitin_enabled property."""
        self.logger.warn("Setting values on turnitin_enabled will NOT update the remote Canvas instance.")
        self._turnitin_enabled = value

    @property
    def rubric(self):
        """(Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric."""
        return self._rubric

    @rubric.setter
    def rubric(self, value):
        """Setter for rubric property."""
        self.logger.warn("Setting values on rubric will NOT update the remote Canvas instance.")
        self._rubric = value

    @property
    def omit_from_final_grade(self):
        """(Optional) If true, the assignment will be ommitted from the student's final grade."""
        return self._omit_from_final_grade

    @omit_from_final_grade.setter
    def omit_from_final_grade(self, value):
        """Setter for omit_from_final_grade property."""
        self.logger.warn("Setting values on omit_from_final_grade will NOT update the remote Canvas instance.")
        self._omit_from_final_grade = value

    @property
    def course_id(self):
        """the ID of the course the assignment belongs to."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def needs_grading_count_by_section(self):
        """if the requesting user has grading rights and the 'needs_grading_count_by_section' flag is specified, the number of submissions that need grading split out by section. NOTE: This key is NOT present unless you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER NOTE: it's possible to be enrolled in multiple sections, and if a student is setup that way they will show an assignment that needs grading in multiple sections (effectively the count will be duplicated between sections)."""
        return self._needs_grading_count_by_section

    @needs_grading_count_by_section.setter
    def needs_grading_count_by_section(self, value):
        """Setter for needs_grading_count_by_section property."""
        self.logger.warn("Setting values on needs_grading_count_by_section will NOT update the remote Canvas instance.")
        self._needs_grading_count_by_section = value

    @property
    def id(self):
        """the ID of the assignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

    @property
    def muted(self):
        """whether the assignment is muted."""
        return self._muted

    @muted.setter
    def muted(self, value):
        """Setter for muted property."""
        self.logger.warn("Setting values on muted will NOT update the remote Canvas instance.")
        self._muted = value

    @property
    def grading_type(self):
        """The type of grading the assignment receives; one of 'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'."""
        return self._grading_type

    @grading_type.setter
    def grading_type(self, value):
        """Setter for grading_type property."""
        self.logger.warn("Setting values on grading_type will NOT update the remote Canvas instance.")
        self._grading_type = value

    @property
    def rubric_settings(self):
        """(Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric."""
        return self._rubric_settings

    @rubric_settings.setter
    def rubric_settings(self, value):
        """Setter for rubric_settings property."""
        self.logger.warn("Setting values on rubric_settings will NOT update the remote Canvas instance.")
        self._rubric_settings = value

    @property
    def anonymous_submissions(self):
        """(Optional) whether anonymous submissions are accepted (applies only to quiz assignments)."""
        return self._anonymous_submissions

    @anonymous_submissions.setter
    def anonymous_submissions(self, value):
        """Setter for anonymous_submissions property."""
        self.logger.warn("Setting values on anonymous_submissions will NOT update the remote Canvas instance.")
        self._anonymous_submissions = value

    @property
    def peer_reviews(self):
        """Boolean indicating if peer reviews are required for this assignment."""
        return self._peer_reviews

    @peer_reviews.setter
    def peer_reviews(self, value):
        """Setter for peer_reviews property."""
        self.logger.warn("Setting values on peer_reviews will NOT update the remote Canvas instance.")
        self._peer_reviews = value

    @property
    def discussion_topic(self):
        """(Optional) the DiscussionTopic associated with the assignment, if applicable."""
        return self._discussion_topic

    @discussion_topic.setter
    def discussion_topic(self, value):
        """Setter for discussion_topic property."""
        self.logger.warn("Setting values on discussion_topic will NOT update the remote Canvas instance.")
        self._discussion_topic = value

    @property
    def intra_group_peer_reviews(self):
        """Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work."""
        return self._intra_group_peer_reviews

    @intra_group_peer_reviews.setter
    def intra_group_peer_reviews(self, value):
        """Setter for intra_group_peer_reviews property."""
        self.logger.warn("Setting values on intra_group_peer_reviews will NOT update the remote Canvas instance.")
        self._intra_group_peer_reviews = value

    @property
    def quiz_id(self):
        """(Optional) id of the associated quiz (applies only when submission_types is ['online_quiz'])."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def freeze_on_copy(self):
        """(Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._freeze_on_copy

    @freeze_on_copy.setter
    def freeze_on_copy(self, value):
        """Setter for freeze_on_copy property."""
        self.logger.warn("Setting values on freeze_on_copy will NOT update the remote Canvas instance.")
        self._freeze_on_copy = value

    @property
    def all_dates(self):
        """(Optional) all dates associated with the assignment, if applicable."""
        return self._all_dates

    @all_dates.setter
    def all_dates(self, value):
        """Setter for all_dates property."""
        self.logger.warn("Setting values on all_dates will NOT update the remote Canvas instance.")
        self._all_dates = value

    @property
    def integration_data(self):
        """(optional, Third Party integration data for assignment)."""
        return self._integration_data

    @integration_data.setter
    def integration_data(self, value):
        """Setter for integration_data property."""
        self.logger.warn("Setting values on integration_data will NOT update the remote Canvas instance.")
        self._integration_data = value

    @property
    def description(self):
        """the assignment description, in an HTML fragment."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def peer_review_count(self):
        """Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true."""
        return self._peer_review_count

    @peer_review_count.setter
    def peer_review_count(self, value):
        """Setter for peer_review_count property."""
        self.logger.warn("Setting values on peer_review_count will NOT update the remote Canvas instance.")
        self._peer_review_count = value

    @property
    def grade_group_students_individually(self):
        """If this is a group assignment, boolean flag indicating whether or not students will be graded individually."""
        return self._grade_group_students_individually

    @grade_group_students_individually.setter
    def grade_group_students_individually(self, value):
        """Setter for grade_group_students_individually property."""
        self.logger.warn("Setting values on grade_group_students_individually will NOT update the remote Canvas instance.")
        self._grade_group_students_individually = value

    @property
    def grading_standard_id(self):
        """The id of the grading standard being applied to this assignment. Valid if grading_type is 'letter_grade' or 'gpa_scale'."""
        return self._grading_standard_id

    @grading_standard_id.setter
    def grading_standard_id(self, value):
        """Setter for grading_standard_id property."""
        self.logger.warn("Setting values on grading_standard_id will NOT update the remote Canvas instance.")
        self._grading_standard_id = value

    @property
    def external_tool_tag_attributes(self):
        """(Optional) assignment's settings for external tools if submission_types include 'external_tool'. Only url and new_tab are included (new_tab defaults to false).  Use the 'External Tools' API if you need more information about an external tool."""
        return self._external_tool_tag_attributes

    @external_tool_tag_attributes.setter
    def external_tool_tag_attributes(self, value):
        """Setter for external_tool_tag_attributes property."""
        self.logger.warn("Setting values on external_tool_tag_attributes will NOT update the remote Canvas instance.")
        self._external_tool_tag_attributes = value

    @property
    def html_url(self):
        """the URL to the assignment's web page."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def turnitin_settings(self):
        """Settings to pass along to turnitin to control what kinds of matches should be considered. originality_report_visibility can be 'immediate', 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can be null, 'percent', 'words' exclude_small_matches_value: - if type is null, this will be null also - if type is 'percent', this will be a number between 0 and 100 representing match size to exclude as a percentage of the document size. - if type is 'words', this will be number > 0 representing how many words a match must contain for it to be considered NOTE: This flag will not appear unless your account has the Turnitin plugin available."""
        return self._turnitin_settings

    @turnitin_settings.setter
    def turnitin_settings(self, value):
        """Setter for turnitin_settings property."""
        self.logger.warn("Setting values on turnitin_settings will NOT update the remote Canvas instance.")
        self._turnitin_settings = value

    @property
    def group_category_id(self):
        """The ID of the assignment's group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment."""
        return self._group_category_id

    @group_category_id.setter
    def group_category_id(self, value):
        """Setter for group_category_id property."""
        self.logger.warn("Setting values on group_category_id will NOT update the remote Canvas instance.")
        self._group_category_id = value

    @property
    def lock_explanation(self):
        """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def needs_grading_count(self):
        """if the requesting user has grading rights, the number of submissions that need grading."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn("Setting values on needs_grading_count will NOT update the remote Canvas instance.")
        self._needs_grading_count = value

    @property
    def vericite_enabled(self):
        """Boolean flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available."""
        return self._vericite_enabled

    @vericite_enabled.setter
    def vericite_enabled(self, value):
        """Setter for vericite_enabled property."""
        self.logger.warn("Setting values on vericite_enabled will NOT update the remote Canvas instance.")
        self._vericite_enabled = value

    @property
    def peer_reviews_assign_at(self):
        """String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment's due date, the assignment's due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true."""
        return self._peer_reviews_assign_at

    @peer_reviews_assign_at.setter
    def peer_reviews_assign_at(self, value):
        """Setter for peer_reviews_assign_at property."""
        self.logger.warn("Setting values on peer_reviews_assign_at will NOT update the remote Canvas instance.")
        self._peer_reviews_assign_at = value

    @property
    def name(self):
        """the name of the assignment."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def integration_id(self):
        """(optional, Third Party unique identifier for Assignment)."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def frozen(self):
        """(Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._frozen

    @frozen.setter
    def frozen(self, value):
        """Setter for frozen property."""
        self.logger.warn("Setting values on frozen will NOT update the remote Canvas instance.")
        self._frozen = value

    @property
    def only_visible_to_overrides(self):
        """Whether the assignment is only visible to overrides."""
        return self._only_visible_to_overrides

    @only_visible_to_overrides.setter
    def only_visible_to_overrides(self, value):
        """Setter for only_visible_to_overrides property."""
        self.logger.warn("Setting values on only_visible_to_overrides will NOT update the remote Canvas instance.")
        self._only_visible_to_overrides = value

    @property
    def unlock_at(self):
        """the unlock date (assignment is unlocked after this date) returns null if not present NOTE: If this assignment has assignment overrides, this field will be the unlock date as it applies to the user requesting information from the API."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def submission(self):
        """(Optional) If 'submission' is included in the 'include' parameter, includes a Submission object that represents the current user's (user who is requesting information from the api) current submission for the assignment. See the Submissions API for an example response. If the user does not have a submission, this key will be absent."""
        return self._submission

    @submission.setter
    def submission(self, value):
        """Setter for submission property."""
        self.logger.warn("Setting values on submission will NOT update the remote Canvas instance.")
        self._submission = value

    @property
    def due_at(self):
        """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def created_at(self):
        """The time at which this assignment was originally created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def post_to_sis(self):
        """(optional, present if Post Grades to SIS feature is enabled)."""
        return self._post_to_sis

    @post_to_sis.setter
    def post_to_sis(self, value):
        """Setter for post_to_sis property."""
        self.logger.warn("Setting values on post_to_sis will NOT update the remote Canvas instance.")
        self._post_to_sis = value

    @property
    def lock_at(self):
        """the lock date (assignment is locked after this date). returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the lock date as it applies to the user requesting information from the API."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def assignment_group_id(self):
        """the ID of the assignment's group."""
        return self._assignment_group_id

    @assignment_group_id.setter
    def assignment_group_id(self, value):
        """Setter for assignment_group_id property."""
        self.logger.warn("Setting values on assignment_group_id will NOT update the remote Canvas instance.")
        self._assignment_group_id = value

    @property
    def allowed_extensions(self):
        """Allowed file extensions, which take effect if submission_types includes 'online_upload'."""
        return self._allowed_extensions

    @allowed_extensions.setter
    def allowed_extensions(self, value):
        """Setter for allowed_extensions property."""
        self.logger.warn("Setting values on allowed_extensions will NOT update the remote Canvas instance.")
        self._allowed_extensions = value

    @property
    def automatic_peer_reviews(self):
        """Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews."""
        return self._automatic_peer_reviews

    @automatic_peer_reviews.setter
    def automatic_peer_reviews(self, value):
        """Setter for automatic_peer_reviews property."""
        self.logger.warn("Setting values on automatic_peer_reviews will NOT update the remote Canvas instance.")
        self._automatic_peer_reviews = value

    @property
    def published(self):
        """Whether the assignment is published."""
        return self._published

    @published.setter
    def published(self, value):
        """Setter for published property."""
        self.logger.warn("Setting values on published will NOT update the remote Canvas instance.")
        self._published = value

    @property
    def position(self):
        """the sorting order of the assignment in the group."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def submission_types(self):
        """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload' 'media_recording'."""
        return self._submission_types

    @submission_types.setter
    def submission_types(self, value):
        """Setter for submission_types property."""
        self.logger.warn("Setting values on submission_types will NOT update the remote Canvas instance.")
        self._submission_types = value

    @property
    def submissions_download_url(self):
        """the URL to download all submissions as a zip."""
        return self._submissions_download_url

    @submissions_download_url.setter
    def submissions_download_url(self, value):
        """Setter for submissions_download_url property."""
        self.logger.warn("Setting values on submissions_download_url will NOT update the remote Canvas instance.")
        self._submissions_download_url = value

    @property
    def overrides(self):
        """(Optional) If 'overrides' is included in the 'include' parameter, includes an array of assignment override objects."""
        return self._overrides

    @overrides.setter
    def overrides(self, value):
        """Setter for overrides property."""
        self.logger.warn("Setting values on overrides will NOT update the remote Canvas instance.")
        self._overrides = value

    @property
    def unpublishable(self):
        """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the assignment."""
        return self._unpublishable

    @unpublishable.setter
    def unpublishable(self, value):
        """Setter for unpublishable property."""
        self.logger.warn("Setting values on unpublishable will NOT update the remote Canvas instance.")
        self._unpublishable = value


class Needsgradingcount(BaseModel):
    """Needsgradingcount Model.
    Used by Assignment model"""

    def __init__(self, needs_grading_count=None, section_id=None):
        """Init method for Needsgradingcount class."""
        self._needs_grading_count = needs_grading_count
        self._section_id = section_id

        self.logger = logging.getLogger('pycanvas.Needsgradingcount')

    @property
    def needs_grading_count(self):
        """Number of submissions that need grading."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn("Setting values on needs_grading_count will NOT update the remote Canvas instance.")
        self._needs_grading_count = value

    @property
    def section_id(self):
        """The section ID."""
        return self._section_id

    @section_id.setter
    def section_id(self, value):
        """Setter for section_id property."""
        self.logger.warn("Setting values on section_id will NOT update the remote Canvas instance.")
        self._section_id = value


class Rubriccriteria(BaseModel):
    """Rubriccriteria Model."""

    def __init__(self, vendor_guid=None, description=None, ratings=None, id=None, points=None, outcome_id=None, long_description=None):
        """Init method for Rubriccriteria class."""
        self._vendor_guid = vendor_guid
        self._description = description
        self._ratings = ratings
        self._id = id
        self._points = points
        self._outcome_id = outcome_id
        self._long_description = long_description

        self.logger = logging.getLogger('pycanvas.Rubriccriteria')

    @property
    def vendor_guid(self):
        """(Optional) The 3rd party vendor's GUID for the outcome this criteria references, if any."""
        return self._vendor_guid

    @vendor_guid.setter
    def vendor_guid(self, value):
        """Setter for vendor_guid property."""
        self.logger.warn("Setting values on vendor_guid will NOT update the remote Canvas instance.")
        self._vendor_guid = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def ratings(self):
        """ratings."""
        return self._ratings

    @ratings.setter
    def ratings(self, value):
        """Setter for ratings property."""
        self.logger.warn("Setting values on ratings will NOT update the remote Canvas instance.")
        self._ratings = value

    @property
    def id(self):
        """The id of rubric criteria."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def outcome_id(self):
        """(Optional) The id of the learning outcome this criteria uses, if any."""
        return self._outcome_id

    @outcome_id.setter
    def outcome_id(self, value):
        """Setter for outcome_id property."""
        self.logger.warn("Setting values on outcome_id will NOT update the remote Canvas instance.")
        self._outcome_id = value

    @property
    def long_description(self):
        """long_description."""
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        """Setter for long_description property."""
        self.logger.warn("Setting values on long_description will NOT update the remote Canvas instance.")
        self._long_description = value


class Assignmentdate(BaseModel):
    """Assignmentdate Model.
    Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field."""

    def __init__(self, unlock_at=None, title=None, due_at=None, lock_at=None, base=None, id=None):
        """Init method for Assignmentdate class."""
        self._unlock_at = unlock_at
        self._title = title
        self._due_at = due_at
        self._lock_at = lock_at
        self._base = base
        self._id = id

        self.logger = logging.getLogger('pycanvas.Assignmentdate')

    @property
    def unlock_at(self):
        """unlock_at."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def due_at(self):
        """due_at."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def lock_at(self):
        """lock_at."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def base(self):
        """(Optional, present if 'id' is missing) whether this date represents the assignment's or quiz's default due date."""
        return self._base

    @base.setter
    def base(self, value):
        """Setter for base property."""
        self.logger.warn("Setting values on base will NOT update the remote Canvas instance.")
        self._base = value

    @property
    def id(self):
        """(Optional, missing if 'base' is present) id of the assignment override this date represents."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Rubricrating(BaseModel):
    """Rubricrating Model."""

    def __init__(self, points=None, id=None, description=None):
        """Init method for Rubricrating class."""
        self._points = points
        self._id = id
        self._description = description

        self.logger = logging.getLogger('pycanvas.Rubricrating')

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value


class Lockinfo(BaseModel):
    """Lockinfo Model."""

    def __init__(self, lock_at=None, context_module=None, asset_string=None, unlock_at=None, manually_locked=None):
        """Init method for Lockinfo class."""
        self._lock_at = lock_at
        self._context_module = context_module
        self._asset_string = asset_string
        self._unlock_at = unlock_at
        self._manually_locked = manually_locked

        self.logger = logging.getLogger('pycanvas.Lockinfo')

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def context_module(self):
        """(Optional) Context module causing the lock."""
        return self._context_module

    @context_module.setter
    def context_module(self, value):
        """Setter for context_module property."""
        self.logger.warn("Setting values on context_module will NOT update the remote Canvas instance.")
        self._context_module = value

    @property
    def asset_string(self):
        """Asset string for the object causing the lock."""
        return self._asset_string

    @asset_string.setter
    def asset_string(self, value):
        """Setter for asset_string property."""
        self.logger.warn("Setting values on asset_string will NOT update the remote Canvas instance.")
        self._asset_string = value

    @property
    def unlock_at(self):
        """(Optional) Time at which this was/will be unlocked."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def manually_locked(self):
        """manually_locked."""
        return self._manually_locked

    @manually_locked.setter
    def manually_locked(self, value):
        """Setter for manually_locked property."""
        self.logger.warn("Setting values on manually_locked will NOT update the remote Canvas instance.")
        self._manually_locked = value

