"""Enrollments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class EnrollmentsAPI(BaseCanvasAPI):
    """Enrollments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for EnrollmentsAPI."""
        super(EnrollmentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.EnrollmentsAPI")

    def list_enrollments_courses(self, course_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None, user_id=None):
        """
        List enrollments.

        Depending on the URL given, return either (1) all of the enrollments in
        a course, (2) all of the enrollments in a section or (3) all of a user's
        enrollments. This includes student, teacher, TA, and observer enrollments.
        
        If a user has multiple enrollments in a context (e.g. as a teacher
        and a student or in multiple course sections), each enrollment will be
        listed separately.
        
        note: Currently, only an admin user can return other users' enrollments. A
        user can, however, return his/her own enrollments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - type
        """A list of enrollment types to return. Accepted values are
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment
        types are returned. This argument is ignored if `role` is given."""
        if type is not None:
            params["type"] = type

        # OPTIONAL - role
        """A list of enrollment roles to return. Accepted values include course-level
        roles created by the {api:RoleOverridesController#add_role Add Role API}
        as well as the base enrollment types accepted by the `type` argument above."""
        if role is not None:
            params["role"] = role

        # OPTIONAL - state
        """Filter by enrollment state. If omitted, 'active' and 'invited' enrollments
        are returned. When querying a user's enrollments (either via user_id
        argument or via user enrollments endpoint), the following additional
        synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded""""
        if state is not None:
            self._validate_enum(state, ["active", "invited", "creation_pending", "deleted", "rejected", "completed", "inactive"])
            params["state"] = state

        # OPTIONAL - include
        """Array of additional information to include on the enrollment or user records.
        "avatar_url" and "group_ids" will be returned on the user record."""
        if include is not None:
            self._validate_enum(include, ["avatar_url", "group_ids", "locked", "observed_users", "can_be_removed"])
            params["include"] = include

        # OPTIONAL - user_id
        """Filter by user_id (only valid for course or section enrollment
        queries). If set to the current user's id, this is a way to
        determine if the user has any enrollments in the course or section,
        independent of whether the user has permission to view other people
        on the roster."""
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - grading_period_id
        """Return grades for the given grading_period.  If this parameter is not
        specified, the returned grades will be for the whole course."""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - sis_account_id
        """Returns only enrollments for the specified SIS account ID(s). Does not
        look into subaccounts. May pass in array or string."""
        if sis_account_id is not None:
            params["sis_account_id"] = sis_account_id

        # OPTIONAL - sis_course_id
        """Returns only enrollments matching the specified SIS course ID(s).
        May pass in array or string."""
        if sis_course_id is not None:
            params["sis_course_id"] = sis_course_id

        # OPTIONAL - sis_section_id
        """Returns only section enrollments matching the specified SIS section ID(s).
        May pass in array or string."""
        if sis_section_id is not None:
            params["sis_section_id"] = sis_section_id

        # OPTIONAL - sis_user_id
        """Returns only enrollments for the specified SIS user ID(s). May pass in
        array or string."""
        if sis_user_id is not None:
            params["sis_user_id"] = sis_user_id

        self.logger.debug("GET /api/v1/courses/{course_id}/enrollments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/enrollments".format(**path), data=data, params=params, all_pages=True)

    def list_enrollments_sections(self, section_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None, user_id=None):
        """
        List enrollments.

        Depending on the URL given, return either (1) all of the enrollments in
        a course, (2) all of the enrollments in a section or (3) all of a user's
        enrollments. This includes student, teacher, TA, and observer enrollments.
        
        If a user has multiple enrollments in a context (e.g. as a teacher
        and a student or in multiple course sections), each enrollment will be
        listed separately.
        
        note: Currently, only an admin user can return other users' enrollments. A
        user can, however, return his/her own enrollments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # OPTIONAL - type
        """A list of enrollment types to return. Accepted values are
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment
        types are returned. This argument is ignored if `role` is given."""
        if type is not None:
            params["type"] = type

        # OPTIONAL - role
        """A list of enrollment roles to return. Accepted values include course-level
        roles created by the {api:RoleOverridesController#add_role Add Role API}
        as well as the base enrollment types accepted by the `type` argument above."""
        if role is not None:
            params["role"] = role

        # OPTIONAL - state
        """Filter by enrollment state. If omitted, 'active' and 'invited' enrollments
        are returned. When querying a user's enrollments (either via user_id
        argument or via user enrollments endpoint), the following additional
        synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded""""
        if state is not None:
            self._validate_enum(state, ["active", "invited", "creation_pending", "deleted", "rejected", "completed", "inactive"])
            params["state"] = state

        # OPTIONAL - include
        """Array of additional information to include on the enrollment or user records.
        "avatar_url" and "group_ids" will be returned on the user record."""
        if include is not None:
            self._validate_enum(include, ["avatar_url", "group_ids", "locked", "observed_users", "can_be_removed"])
            params["include"] = include

        # OPTIONAL - user_id
        """Filter by user_id (only valid for course or section enrollment
        queries). If set to the current user's id, this is a way to
        determine if the user has any enrollments in the course or section,
        independent of whether the user has permission to view other people
        on the roster."""
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - grading_period_id
        """Return grades for the given grading_period.  If this parameter is not
        specified, the returned grades will be for the whole course."""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - sis_account_id
        """Returns only enrollments for the specified SIS account ID(s). Does not
        look into subaccounts. May pass in array or string."""
        if sis_account_id is not None:
            params["sis_account_id"] = sis_account_id

        # OPTIONAL - sis_course_id
        """Returns only enrollments matching the specified SIS course ID(s).
        May pass in array or string."""
        if sis_course_id is not None:
            params["sis_course_id"] = sis_course_id

        # OPTIONAL - sis_section_id
        """Returns only section enrollments matching the specified SIS section ID(s).
        May pass in array or string."""
        if sis_section_id is not None:
            params["sis_section_id"] = sis_section_id

        # OPTIONAL - sis_user_id
        """Returns only enrollments for the specified SIS user ID(s). May pass in
        array or string."""
        if sis_user_id is not None:
            params["sis_user_id"] = sis_user_id

        self.logger.debug("GET /api/v1/sections/{section_id}/enrollments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/enrollments".format(**path), data=data, params=params, all_pages=True)

    def list_enrollments_users(self, user_id, grading_period_id=None, include=None, role=None, sis_account_id=None, sis_course_id=None, sis_section_id=None, sis_user_id=None, state=None, type=None):
        """
        List enrollments.

        Depending on the URL given, return either (1) all of the enrollments in
        a course, (2) all of the enrollments in a section or (3) all of a user's
        enrollments. This includes student, teacher, TA, and observer enrollments.
        
        If a user has multiple enrollments in a context (e.g. as a teacher
        and a student or in multiple course sections), each enrollment will be
        listed separately.
        
        note: Currently, only an admin user can return other users' enrollments. A
        user can, however, return his/her own enrollments.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - type
        """A list of enrollment types to return. Accepted values are
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment
        types are returned. This argument is ignored if `role` is given."""
        if type is not None:
            params["type"] = type

        # OPTIONAL - role
        """A list of enrollment roles to return. Accepted values include course-level
        roles created by the {api:RoleOverridesController#add_role Add Role API}
        as well as the base enrollment types accepted by the `type` argument above."""
        if role is not None:
            params["role"] = role

        # OPTIONAL - state
        """Filter by enrollment state. If omitted, 'active' and 'invited' enrollments
        are returned. When querying a user's enrollments (either via user_id
        argument or via user enrollments endpoint), the following additional
        synthetic states are supported: "current_and_invited"|"current_and_future"|"current_and_concluded""""
        if state is not None:
            self._validate_enum(state, ["active", "invited", "creation_pending", "deleted", "rejected", "completed", "inactive"])
            params["state"] = state

        # OPTIONAL - include
        """Array of additional information to include on the enrollment or user records.
        "avatar_url" and "group_ids" will be returned on the user record."""
        if include is not None:
            self._validate_enum(include, ["avatar_url", "group_ids", "locked", "observed_users", "can_be_removed"])
            params["include"] = include

        # REQUIRED - PATH - user_id
        """Filter by user_id (only valid for course or section enrollment
        queries). If set to the current user's id, this is a way to
        determine if the user has any enrollments in the course or section,
        independent of whether the user has permission to view other people
        on the roster."""
        path["user_id"] = user_id

        # OPTIONAL - grading_period_id
        """Return grades for the given grading_period.  If this parameter is not
        specified, the returned grades will be for the whole course."""
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id

        # OPTIONAL - sis_account_id
        """Returns only enrollments for the specified SIS account ID(s). Does not
        look into subaccounts. May pass in array or string."""
        if sis_account_id is not None:
            params["sis_account_id"] = sis_account_id

        # OPTIONAL - sis_course_id
        """Returns only enrollments matching the specified SIS course ID(s).
        May pass in array or string."""
        if sis_course_id is not None:
            params["sis_course_id"] = sis_course_id

        # OPTIONAL - sis_section_id
        """Returns only section enrollments matching the specified SIS section ID(s).
        May pass in array or string."""
        if sis_section_id is not None:
            params["sis_section_id"] = sis_section_id

        # OPTIONAL - sis_user_id
        """Returns only enrollments for the specified SIS user ID(s). May pass in
        array or string."""
        if sis_user_id is not None:
            params["sis_user_id"] = sis_user_id

        self.logger.debug("GET /api/v1/users/{user_id}/enrollments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/enrollments".format(**path), data=data, params=params, all_pages=True)

    def enrollment_by_id(self, id, account_id):
        """
        Enrollment by ID.

        Get an Enrollment object by Enrollment ID
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """The ID of the enrollment object"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/enrollments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/enrollments/{id}".format(**path), data=data, params=params, single_item=True)

    def enroll_user_courses(self, course_id, enrollment_type, enrollment_user_id, enrollment_associated_user_id=None, enrollment_course_section_id=None, enrollment_enrollment_state=None, enrollment_limit_privileges_to_course_section=None, enrollment_notify=None, enrollment_role=None, enrollment_role_id=None, enrollment_self_enrolled=None, enrollment_self_enrollment_code=None):
        """
        Enroll a user.

        Create a new user enrollment for a course or section.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - enrollment[user_id]
        """The ID of the user to be enrolled in the course."""
        data["enrollment[user_id]"] = enrollment_user_id

        # REQUIRED - enrollment[type]
        """Enroll the user as a student, teacher, TA, observer, or designer. If no
        value is given, the type will be inferred by enrollment[role] if supplied,
        otherwise 'StudentEnrollment' will be used."""
        self._validate_enum(enrollment_type, ["StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", "DesignerEnrollment"])
        data["enrollment[type]"] = enrollment_type

        # OPTIONAL - enrollment[role]
        """Assigns a custom course-level role to the user."""
        if enrollment_role is not None:
            data["enrollment[role]"] = enrollment_role

        # OPTIONAL - enrollment[role_id]
        """Assigns a custom course-level role to the user."""
        if enrollment_role_id is not None:
            data["enrollment[role_id]"] = enrollment_role_id

        # OPTIONAL - enrollment[enrollment_state]
        """If set to 'active,' student will be immediately enrolled in the course.
        Otherwise they will be required to accept a course invitation. Default is
        'invited.'.
        
        If set to 'inactive', student will be listed in the course roster for
        teachers, but will not be able to participate in the course until
        their enrollment is activated."""
        if enrollment_enrollment_state is not None:
            self._validate_enum(enrollment_enrollment_state, ["active", "invited", "inactive"])
            data["enrollment[enrollment_state]"] = enrollment_enrollment_state

        # OPTIONAL - enrollment[course_section_id]
        """The ID of the course section to enroll the student in. If the
        section-specific URL is used, this argument is redundant and will be
        ignored."""
        if enrollment_course_section_id is not None:
            data["enrollment[course_section_id]"] = enrollment_course_section_id

        # OPTIONAL - enrollment[limit_privileges_to_course_section]
        """If set, the enrollment will only allow the user to see and interact with
        users enrolled in the section given by course_section_id.
        * For teachers and TAs, this includes grading privileges.
        * Section-limited students will not see any users (including teachers
          and TAs) not enrolled in their sections.
        * Users may have other enrollments that grant privileges to
          multiple sections in the same course."""
        if enrollment_limit_privileges_to_course_section is not None:
            data["enrollment[limit_privileges_to_course_section]"] = enrollment_limit_privileges_to_course_section

        # OPTIONAL - enrollment[notify]
        """If true, a notification will be sent to the enrolled user.
        Notifications are not sent by default."""
        if enrollment_notify is not None:
            data["enrollment[notify]"] = enrollment_notify

        # OPTIONAL - enrollment[self_enrollment_code]
        """If the current user is not allowed to manage enrollments in this
        course, but the course allows self-enrollment, the user can self-
        enroll as a student in the default section by passing in a valid
        code. When self-enrolling, the user_id must be 'self'. The
        enrollment_state will be set to 'active' and all other arguments
        will be ignored."""
        if enrollment_self_enrollment_code is not None:
            data["enrollment[self_enrollment_code]"] = enrollment_self_enrollment_code

        # OPTIONAL - enrollment[self_enrolled]
        """If true, marks the enrollment as a self-enrollment, which gives
        students the ability to drop the course if desired. Defaults to false."""
        if enrollment_self_enrolled is not None:
            data["enrollment[self_enrolled]"] = enrollment_self_enrolled

        # OPTIONAL - enrollment[associated_user_id]
        """For an observer enrollment, the ID of a student to observe. The
        caller must have +manage_students+ permission in the course.
        This is a one-off operation; to automatically observe all a
        student's enrollments (for example, as a parent), please use
        the {api:UserObserveesController#create User Observees API}."""
        if enrollment_associated_user_id is not None:
            data["enrollment[associated_user_id]"] = enrollment_associated_user_id

        self.logger.debug("POST /api/v1/courses/{course_id}/enrollments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/enrollments".format(**path), data=data, params=params, single_item=True)

    def enroll_user_sections(self, section_id, enrollment_type, enrollment_user_id, enrollment_associated_user_id=None, enrollment_course_section_id=None, enrollment_enrollment_state=None, enrollment_limit_privileges_to_course_section=None, enrollment_notify=None, enrollment_role=None, enrollment_role_id=None, enrollment_self_enrolled=None, enrollment_self_enrollment_code=None):
        """
        Enroll a user.

        Create a new user enrollment for a course or section.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """ID"""
        path["section_id"] = section_id

        # REQUIRED - enrollment[user_id]
        """The ID of the user to be enrolled in the course."""
        data["enrollment[user_id]"] = enrollment_user_id

        # REQUIRED - enrollment[type]
        """Enroll the user as a student, teacher, TA, observer, or designer. If no
        value is given, the type will be inferred by enrollment[role] if supplied,
        otherwise 'StudentEnrollment' will be used."""
        self._validate_enum(enrollment_type, ["StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", "DesignerEnrollment"])
        data["enrollment[type]"] = enrollment_type

        # OPTIONAL - enrollment[role]
        """Assigns a custom course-level role to the user."""
        if enrollment_role is not None:
            data["enrollment[role]"] = enrollment_role

        # OPTIONAL - enrollment[role_id]
        """Assigns a custom course-level role to the user."""
        if enrollment_role_id is not None:
            data["enrollment[role_id]"] = enrollment_role_id

        # OPTIONAL - enrollment[enrollment_state]
        """If set to 'active,' student will be immediately enrolled in the course.
        Otherwise they will be required to accept a course invitation. Default is
        'invited.'.
        
        If set to 'inactive', student will be listed in the course roster for
        teachers, but will not be able to participate in the course until
        their enrollment is activated."""
        if enrollment_enrollment_state is not None:
            self._validate_enum(enrollment_enrollment_state, ["active", "invited", "inactive"])
            data["enrollment[enrollment_state]"] = enrollment_enrollment_state

        # OPTIONAL - enrollment[course_section_id]
        """The ID of the course section to enroll the student in. If the
        section-specific URL is used, this argument is redundant and will be
        ignored."""
        if enrollment_course_section_id is not None:
            data["enrollment[course_section_id]"] = enrollment_course_section_id

        # OPTIONAL - enrollment[limit_privileges_to_course_section]
        """If set, the enrollment will only allow the user to see and interact with
        users enrolled in the section given by course_section_id.
        * For teachers and TAs, this includes grading privileges.
        * Section-limited students will not see any users (including teachers
          and TAs) not enrolled in their sections.
        * Users may have other enrollments that grant privileges to
          multiple sections in the same course."""
        if enrollment_limit_privileges_to_course_section is not None:
            data["enrollment[limit_privileges_to_course_section]"] = enrollment_limit_privileges_to_course_section

        # OPTIONAL - enrollment[notify]
        """If true, a notification will be sent to the enrolled user.
        Notifications are not sent by default."""
        if enrollment_notify is not None:
            data["enrollment[notify]"] = enrollment_notify

        # OPTIONAL - enrollment[self_enrollment_code]
        """If the current user is not allowed to manage enrollments in this
        course, but the course allows self-enrollment, the user can self-
        enroll as a student in the default section by passing in a valid
        code. When self-enrolling, the user_id must be 'self'. The
        enrollment_state will be set to 'active' and all other arguments
        will be ignored."""
        if enrollment_self_enrollment_code is not None:
            data["enrollment[self_enrollment_code]"] = enrollment_self_enrollment_code

        # OPTIONAL - enrollment[self_enrolled]
        """If true, marks the enrollment as a self-enrollment, which gives
        students the ability to drop the course if desired. Defaults to false."""
        if enrollment_self_enrolled is not None:
            data["enrollment[self_enrolled]"] = enrollment_self_enrolled

        # OPTIONAL - enrollment[associated_user_id]
        """For an observer enrollment, the ID of a student to observe. The
        caller must have +manage_students+ permission in the course.
        This is a one-off operation; to automatically observe all a
        student's enrollments (for example, as a parent), please use
        the {api:UserObserveesController#create User Observees API}."""
        if enrollment_associated_user_id is not None:
            data["enrollment[associated_user_id]"] = enrollment_associated_user_id

        self.logger.debug("POST /api/v1/sections/{section_id}/enrollments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/enrollments".format(**path), data=data, params=params, single_item=True)

    def conclude_deactivate_or_delete_enrollment(self, id, course_id, task=None):
        """
        Conclude, deactivate, or delete an enrollment.

        Conclude, deactivate, or delete an enrollment. If the +task+ argument isn't given, the enrollment
        will be concluded.
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

        # OPTIONAL - task
        """The action to take on the enrollment.
        When inactive, a user will still appear in the course roster to admins, but be unable to participate.
        ("inactivate" and "deactivate" are equivalent tasks)"""
        if task is not None:
            self._validate_enum(task, ["conclude", "delete", "inactivate", "deactivate"])
            params["task"] = task

        self.logger.debug("DELETE /api/v1/courses/{course_id}/enrollments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/enrollments/{id}".format(**path), data=data, params=params, single_item=True)

    def re_activate_enrollment(self, id, course_id):
        """
        Re-activate an enrollment.

        Activates an inactive enrollment
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

        self.logger.debug("PUT /api/v1/courses/{course_id}/enrollments/{id}/reactivate with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/enrollments/{id}/reactivate".format(**path), data=data, params=params, single_item=True)


class Grade(BaseModel):
    """Grade Model."""

    def __init__(self, current_score=None, final_score=None, html_url=None, current_grade=None, final_grade=None):
        """Init method for Grade class."""
        self._current_score = current_score
        self._final_score = final_score
        self._html_url = html_url
        self._current_grade = current_grade
        self._final_grade = final_grade

        self.logger = logging.getLogger('pycanvas.Grade')

    @property
    def current_score(self):
        """The user's current score in the class. Only included if user has permissions to view this score."""
        return self._current_score

    @current_score.setter
    def current_score(self, value):
        """Setter for current_score property."""
        self.logger.warn("Setting values on current_score will NOT update the remote Canvas instance.")
        self._current_score = value

    @property
    def final_score(self):
        """The user's final score for the class. Only included if user has permissions to view this score."""
        return self._final_score

    @final_score.setter
    def final_score(self, value):
        """Setter for final_score property."""
        self.logger.warn("Setting values on final_score will NOT update the remote Canvas instance.")
        self._final_score = value

    @property
    def html_url(self):
        """The URL to the Canvas web UI page for the user's grades, if this is a student enrollment."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def current_grade(self):
        """The user's current grade in the class. Only included if user has permissions to view this grade."""
        return self._current_grade

    @current_grade.setter
    def current_grade(self, value):
        """Setter for current_grade property."""
        self.logger.warn("Setting values on current_grade will NOT update the remote Canvas instance.")
        self._current_grade = value

    @property
    def final_grade(self):
        """The user's final grade for the class. Only included if user has permissions to view this grade."""
        return self._final_grade

    @final_grade.setter
    def final_grade(self, value):
        """Setter for final_grade property."""
        self.logger.warn("Setting values on final_grade will NOT update the remote Canvas instance.")
        self._final_grade = value


class Enrollment(BaseModel):
    """Enrollment Model."""

    def __init__(self, limit_privileges_to_course_section=None, course_section_id=None, updated_at=None, current_period_computed_current_score=None, grades=None, course_id=None, multiple_grading_periods_enabled=None, id=None, user_id=None, sis_user_id=None, root_account_id=None, current_period_computed_current_grade=None, end_at=None, computed_final_grade=None, sis_import_id=None, role=None, enrollment_state=None, type=None, course_integration_id=None, section_integration_id=None, start_at=None, computed_current_score=None, current_grading_period_id=None, html_url=None, current_period_computed_final_score=None, computed_current_grade=None, associated_user_id=None, last_activity_at=None, sis_account_id=None, totals_for_all_grading_periods_option=None, computed_final_score=None, current_period_computed_final_grade=None, sis_course_id=None, current_grading_period_title=None, sis_section_id=None, total_activity_time=None):
        """Init method for Enrollment class."""
        self._limit_privileges_to_course_section = limit_privileges_to_course_section
        self._course_section_id = course_section_id
        self._updated_at = updated_at
        self._current_period_computed_current_score = current_period_computed_current_score
        self._grades = grades
        self._course_id = course_id
        self._multiple_grading_periods_enabled = multiple_grading_periods_enabled
        self._id = id
        self._user_id = user_id
        self._sis_user_id = sis_user_id
        self._root_account_id = root_account_id
        self._current_period_computed_current_grade = current_period_computed_current_grade
        self._end_at = end_at
        self._computed_final_grade = computed_final_grade
        self._sis_import_id = sis_import_id
        self._role = role
        self._enrollment_state = enrollment_state
        self._type = type
        self._course_integration_id = course_integration_id
        self._section_integration_id = section_integration_id
        self._start_at = start_at
        self._computed_current_score = computed_current_score
        self._current_grading_period_id = current_grading_period_id
        self._html_url = html_url
        self._current_period_computed_final_score = current_period_computed_final_score
        self._computed_current_grade = computed_current_grade
        self._associated_user_id = associated_user_id
        self._last_activity_at = last_activity_at
        self._sis_account_id = sis_account_id
        self._totals_for_all_grading_periods_option = totals_for_all_grading_periods_option
        self._computed_final_score = computed_final_score
        self._current_period_computed_final_grade = current_period_computed_final_grade
        self._sis_course_id = sis_course_id
        self._current_grading_period_title = current_grading_period_title
        self._sis_section_id = sis_section_id
        self._total_activity_time = total_activity_time

        self.logger = logging.getLogger('pycanvas.Enrollment')

    @property
    def limit_privileges_to_course_section(self):
        """User can only access his or her own course section. Applies to Teacher and TA enrollments."""
        return self._limit_privileges_to_course_section

    @limit_privileges_to_course_section.setter
    def limit_privileges_to_course_section(self, value):
        """Setter for limit_privileges_to_course_section property."""
        self.logger.warn("Setting values on limit_privileges_to_course_section will NOT update the remote Canvas instance.")
        self._limit_privileges_to_course_section = value

    @property
    def course_section_id(self):
        """The unique id of the user's section."""
        return self._course_section_id

    @course_section_id.setter
    def course_section_id(self, value):
        """Setter for course_section_id property."""
        self.logger.warn("Setting values on course_section_id will NOT update the remote Canvas instance.")
        self._course_section_id = value

    @property
    def updated_at(self):
        """The updated time of the enrollment, in ISO8601 format."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def current_period_computed_current_score(self):
        """optional: The student's score in the course for the current grading period, ignoring ungraded assignments. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_period_computed_current_score

    @current_period_computed_current_score.setter
    def current_period_computed_current_score(self, value):
        """Setter for current_period_computed_current_score property."""
        self.logger.warn("Setting values on current_period_computed_current_score will NOT update the remote Canvas instance.")
        self._current_period_computed_current_score = value

    @property
    def grades(self):
        """The URL to the Canvas web UI page containing the grades associated with this enrollment."""
        return self._grades

    @grades.setter
    def grades(self, value):
        """Setter for grades property."""
        self.logger.warn("Setting values on grades will NOT update the remote Canvas instance.")
        self._grades = value

    @property
    def course_id(self):
        """The unique id of the course."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def multiple_grading_periods_enabled(self):
        """optional: Indicates whether the course the enrollment belongs to has the Multiple Grading Periods feature enabled. (applies only to student enrollments, and only available in course endpoints)."""
        return self._multiple_grading_periods_enabled

    @multiple_grading_periods_enabled.setter
    def multiple_grading_periods_enabled(self, value):
        """Setter for multiple_grading_periods_enabled property."""
        self.logger.warn("Setting values on multiple_grading_periods_enabled will NOT update the remote Canvas instance.")
        self._multiple_grading_periods_enabled = value

    @property
    def id(self):
        """The ID of the enrollment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def user_id(self):
        """The unique id of the user."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def sis_user_id(self):
        """The SIS User ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn("Setting values on sis_user_id will NOT update the remote Canvas instance.")
        self._sis_user_id = value

    @property
    def root_account_id(self):
        """The unique id of the user's account."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

    @property
    def current_period_computed_current_grade(self):
        """optional: The letter grade equivalent of current_period_computed_current_score, if available. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_period_computed_current_grade

    @current_period_computed_current_grade.setter
    def current_period_computed_current_grade(self, value):
        """Setter for current_period_computed_current_grade property."""
        self.logger.warn("Setting values on current_period_computed_current_grade will NOT update the remote Canvas instance.")
        self._current_period_computed_current_grade = value

    @property
    def end_at(self):
        """The end time of the enrollment, in ISO8601 format."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def computed_final_grade(self):
        """optional: The letter grade equivalent of computed_final_score, if available. (applies only to student enrollments, and only available in course endpoints)."""
        return self._computed_final_grade

    @computed_final_grade.setter
    def computed_final_grade(self, value):
        """Setter for computed_final_grade property."""
        self.logger.warn("Setting values on computed_final_grade will NOT update the remote Canvas instance.")
        self._computed_final_grade = value

    @property
    def sis_import_id(self):
        """The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def role(self):
        """The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def enrollment_state(self):
        """The state of the user's enrollment in the course."""
        return self._enrollment_state

    @enrollment_state.setter
    def enrollment_state(self, value):
        """Setter for enrollment_state property."""
        self.logger.warn("Setting values on enrollment_state will NOT update the remote Canvas instance.")
        self._enrollment_state = value

    @property
    def type(self):
        """The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def course_integration_id(self):
        """The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information."""
        return self._course_integration_id

    @course_integration_id.setter
    def course_integration_id(self, value):
        """Setter for course_integration_id property."""
        self.logger.warn("Setting values on course_integration_id will NOT update the remote Canvas instance.")
        self._course_integration_id = value

    @property
    def section_integration_id(self):
        """The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information."""
        return self._section_integration_id

    @section_integration_id.setter
    def section_integration_id(self, value):
        """Setter for section_integration_id property."""
        self.logger.warn("Setting values on section_integration_id will NOT update the remote Canvas instance.")
        self._section_integration_id = value

    @property
    def start_at(self):
        """The start time of the enrollment, in ISO8601 format."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def computed_current_score(self):
        """optional: The student's score in the course, ignoring ungraded assignments. (applies only to student enrollments, and only available in course endpoints)."""
        return self._computed_current_score

    @computed_current_score.setter
    def computed_current_score(self, value):
        """Setter for computed_current_score property."""
        self.logger.warn("Setting values on computed_current_score will NOT update the remote Canvas instance.")
        self._computed_current_score = value

    @property
    def current_grading_period_id(self):
        """optional: The id of the currently active grading period, if one exists. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_grading_period_id

    @current_grading_period_id.setter
    def current_grading_period_id(self, value):
        """Setter for current_grading_period_id property."""
        self.logger.warn("Setting values on current_grading_period_id will NOT update the remote Canvas instance.")
        self._current_grading_period_id = value

    @property
    def html_url(self):
        """The URL to the Canvas web UI page for this course enrollment."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def current_period_computed_final_score(self):
        """optional: The student's score in the course for the current grading period, including ungraded assignments with a score of 0. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_period_computed_final_score

    @current_period_computed_final_score.setter
    def current_period_computed_final_score(self, value):
        """Setter for current_period_computed_final_score property."""
        self.logger.warn("Setting values on current_period_computed_final_score will NOT update the remote Canvas instance.")
        self._current_period_computed_final_score = value

    @property
    def computed_current_grade(self):
        """optional: The letter grade equivalent of computed_current_score, if available. (applies only to student enrollments, and only available in course endpoints)."""
        return self._computed_current_grade

    @computed_current_grade.setter
    def computed_current_grade(self, value):
        """Setter for computed_current_grade property."""
        self.logger.warn("Setting values on computed_current_grade will NOT update the remote Canvas instance.")
        self._computed_current_grade = value

    @property
    def associated_user_id(self):
        """The unique id of the associated user. Will be null unless type is ObserverEnrollment."""
        return self._associated_user_id

    @associated_user_id.setter
    def associated_user_id(self, value):
        """Setter for associated_user_id property."""
        self.logger.warn("Setting values on associated_user_id will NOT update the remote Canvas instance.")
        self._associated_user_id = value

    @property
    def last_activity_at(self):
        """The last activity time of the user for the enrollment, in ISO8601 format."""
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, value):
        """Setter for last_activity_at property."""
        self.logger.warn("Setting values on last_activity_at will NOT update the remote Canvas instance.")
        self._last_activity_at = value

    @property
    def sis_account_id(self):
        """The SIS Account ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information."""
        return self._sis_account_id

    @sis_account_id.setter
    def sis_account_id(self, value):
        """Setter for sis_account_id property."""
        self.logger.warn("Setting values on sis_account_id will NOT update the remote Canvas instance.")
        self._sis_account_id = value

    @property
    def totals_for_all_grading_periods_option(self):
        """optional: Indicates whether the course the enrollment belongs to has the Display Totals for 'All Grading Periods' feature enabled. (applies only to student enrollments, and only available in course endpoints)."""
        return self._totals_for_all_grading_periods_option

    @totals_for_all_grading_periods_option.setter
    def totals_for_all_grading_periods_option(self, value):
        """Setter for totals_for_all_grading_periods_option property."""
        self.logger.warn("Setting values on totals_for_all_grading_periods_option will NOT update the remote Canvas instance.")
        self._totals_for_all_grading_periods_option = value

    @property
    def computed_final_score(self):
        """optional: The student's score in the course including ungraded assignments with a score of 0. (applies only to student enrollments, and only available in course endpoints)."""
        return self._computed_final_score

    @computed_final_score.setter
    def computed_final_score(self, value):
        """Setter for computed_final_score property."""
        self.logger.warn("Setting values on computed_final_score will NOT update the remote Canvas instance.")
        self._computed_final_score = value

    @property
    def current_period_computed_final_grade(self):
        """optional: The letter grade equivalent of current_period_computed_final_score, if available. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_period_computed_final_grade

    @current_period_computed_final_grade.setter
    def current_period_computed_final_grade(self, value):
        """Setter for current_period_computed_final_grade property."""
        self.logger.warn("Setting values on current_period_computed_final_grade will NOT update the remote Canvas instance.")
        self._current_period_computed_final_grade = value

    @property
    def sis_course_id(self):
        """The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information."""
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, value):
        """Setter for sis_course_id property."""
        self.logger.warn("Setting values on sis_course_id will NOT update the remote Canvas instance.")
        self._sis_course_id = value

    @property
    def current_grading_period_title(self):
        """optional: The name of the currently active grading period, if one exists. If the course the enrollment belongs to does not have Multiple Grading Periods enabled, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints)."""
        return self._current_grading_period_title

    @current_grading_period_title.setter
    def current_grading_period_title(self, value):
        """Setter for current_grading_period_title property."""
        self.logger.warn("Setting values on current_grading_period_title will NOT update the remote Canvas instance.")
        self._current_grading_period_title = value

    @property
    def sis_section_id(self):
        """The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information."""
        return self._sis_section_id

    @sis_section_id.setter
    def sis_section_id(self, value):
        """Setter for sis_section_id property."""
        self.logger.warn("Setting values on sis_section_id will NOT update the remote Canvas instance.")
        self._sis_section_id = value

    @property
    def total_activity_time(self):
        """The total activity time of the user for the enrollment, in seconds."""
        return self._total_activity_time

    @total_activity_time.setter
    def total_activity_time(self, value):
        """Setter for total_activity_time property."""
        self.logger.warn("Setting values on total_activity_time will NOT update the remote Canvas instance.")
        self._total_activity_time = value

