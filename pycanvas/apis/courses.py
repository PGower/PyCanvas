"""Courses API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CoursesAPI(BaseCanvasAPI):
    """Courses API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CoursesAPI."""
        super(CoursesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CoursesAPI")

    def list_your_courses(self, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, state=None):
        """
        List your courses.

        Returns the list of active courses for the current user.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - enrollment_type
        """When set, only return courses where the user is enrolled as this type. For
        example, set to "teacher" to return only courses where the user is
        enrolled as a Teacher.  This argument is ignored if enrollment_role is given."""
        if enrollment_type is not None:
            self._validate_enum(enrollment_type, ["teacher", "student", "ta", "observer", "designer"])
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """Deprecated
        When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a base role type of
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'."""
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role type of
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'."""
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - enrollment_state
        """When set, only return courses where the user has an enrollment with the given state.
        This will respect section/course/term date overrides."""
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "invited_or_pending", "completed"])
            params["enrollment_state"] = enrollment_state

        # OPTIONAL - include
        """- "needs_grading_count": Optional information to include with each Course.
          When needs_grading_count is given, and the current user has grading
          rights, the total number of submissions needing grading for all
          assignments is returned.
        - "syllabus_body": Optional information to include with each Course.
          When syllabus_body is given the user-generated html for the course
          syllabus is returned.
        - "public_description": Optional information to include with each Course.
          When public_description is given the user-generated text for the course
          public description is returned.
        - "total_scores": Optional information to include with each Course.
          When total_scores is given, any student enrollments will also
          include the fields 'computed_current_score', 'computed_final_score',
          'computed_current_grade', and 'computed_final_grade' (see Enrollment
          documentation for more information on these fields). This argument
          is ignored if the course is configured to hide final grades.
        - "current_grading_period_scores": Optional information to include with
          each Course. When current_grading_period_scores is given and total_scores
          is given, any student enrollments will also include the fields
          'multiple_grading_periods_enabled',
          'totals_for_all_grading_periods_option', 'current_grading_period_title',
          'current_grading_period_id', current_period_computed_current_score',
          'current_period_computed_final_score',
          'current_period_computed_current_grade', and
          'current_period_computed_final_grade' (see Enrollment documentation for
          more information on these fields). In addition, when this argument is
          passed, the course will have a 'multiple_grading_periods_enabled' attribute
          on it. This argument is ignored if the course is configured to hide final
          grades or if the total_scores argument is not included.
        - "term": Optional information to include with each Course. When
          term is given, the information for the enrollment term for each course
          is returned.
        - "course_progress": Optional information to include with each Course.
          When course_progress is given, each course will include a
          'course_progress' object with the fields: 'requirement_count', an integer
          specifying the total number of requirements in the course,
          'requirement_completed_count', an integer specifying the total number of
          requirements in this course that have been completed, and
          'next_requirement_url', a string url to the next requirement item, and
          'completed_at', the date the course was completed (null if incomplete).
          'next_requirement_url' will be null if all requirements have been
          completed or the current module does not require sequential progress.
          "course_progress" will return an error message if the course is not
          module based or the user is not enrolled as a student in the course.
        - "sections": Section enrollment information to include with each Course.
          Returns an array of hashes containing the section ID (id), section name
          (name), start and end dates (start_at, end_at), as well as the enrollment
          type (enrollment_role, e.g. 'StudentEnrollment').
        - "storage_quota_used_mb": The amount of storage space used by the files in this course
        - "total_students": Optional information to include with each Course.
          Returns an integer for the total amount of active and invited students.
        - "passback_status": Include the grade passback_status
        - "favorites": Optional information to include with each Course.
          Indicates if the user has marked the course as a favorite course.
        - "teachers": Teacher information to include with each Course.
          Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information
          for each teacher in the course.
        - "observed_users": Optional information to include with each Course.
          Will include data for observed users if the current user has an
          observer enrollment.
        - "tabs": Optional information to include with each Course.
          Will include the list of tabs configured for each course.  See the
          {api:TabsController#index List available tabs API} for more information."""
        if include is not None:
            self._validate_enum(include, ["needs_grading_count", "syllabus_body", "public_description", "total_scores", "current_grading_period_scores", "term", "course_progress", "sections", "storage_quota_used_mb", "total_students", "passback_status", "favorites", "teachers", "observed_users"])
            params["include"] = include

        # OPTIONAL - state
        """If set, only return courses that are in the given state(s).
        By default, "available" is returned for students and observers, and
        anything except "deleted", for all other enrollment types"""
        if state is not None:
            self._validate_enum(state, ["unpublished", "available", "completed", "deleted"])
            params["state"] = state

        self.logger.debug("GET /api/v1/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses".format(**path), data=data, params=params, all_pages=True)

    def list_courses_for_user(self, user_id, enrollment_state=None, include=None, state=None):
        """
        List courses for a user.

        Returns a list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - include
        """- "needs_grading_count": Optional information to include with each Course.
          When needs_grading_count is given, and the current user has grading
          rights, the total number of submissions needing grading for all
          assignments is returned.
        - "syllabus_body": Optional information to include with each Course.
          When syllabus_body is given the user-generated html for the course
          syllabus is returned.
        - "public_description": Optional information to include with each Course.
          When public_description is given the user-generated text for the course
          public description is returned.
        - "total_scores": Optional information to include with each Course.
          When total_scores is given, any student enrollments will also
          include the fields 'computed_current_score', 'computed_final_score',
          'computed_current_grade', and 'computed_final_grade' (see Enrollment
          documentation for more information on these fields). This argument
          is ignored if the course is configured to hide final grades.
        - "current_grading_period_scores": Optional information to include with
          each Course. When current_grading_period_scores is given and total_scores
          is given, any student enrollments will also include the fields
          'multiple_grading_periods_enabled',
          'totals_for_all_grading_periods_option', 'current_grading_period_title',
          'current_grading_period_id', current_period_computed_current_score',
          'current_period_computed_final_score',
          'current_period_computed_current_grade', and
          'current_period_computed_final_grade' (see Enrollment documentation for
          more information on these fields). In addition, when this argument is
          passed, the course will have a 'multiple_grading_periods_enabled' attribute
          on it. This argument is ignored if the course is configured to hide final
          grades or if the total_scores argument is not included.
        - "term": Optional information to include with each Course. When
          term is given, the information for the enrollment term for each course
          is returned.
        - "course_progress": Optional information to include with each Course.
          When course_progress is given, each course will include a
          'course_progress' object with the fields: 'requirement_count', an integer
          specifying the total number of requirements in the course,
          'requirement_completed_count', an integer specifying the total number of
          requirements in this course that have been completed, and
          'next_requirement_url', a string url to the next requirement item, and
          'completed_at', the date the course was completed (null if incomplete).
          'next_requirement_url' will be null if all requirements have been
          completed or the current module does not require sequential progress.
          "course_progress" will return an error message if the course is not
          module based or the user is not enrolled as a student in the course.
        - "sections": Section enrollment information to include with each Course.
          Returns an array of hashes containing the section ID (id), section name
          (name), start and end dates (start_at, end_at), as well as the enrollment
          type (enrollment_role, e.g. 'StudentEnrollment').
        - "storage_quota_used_mb": The amount of storage space used by the files in this course
        - "total_students": Optional information to include with each Course.
          Returns an integer for the total amount of active and invited students.
        - "passback_status": Include the grade passback_status
        - "favorites": Optional information to include with each Course.
          Indicates if the user has marked the course as a favorite course.
        - "teachers": Teacher information to include with each Course.
          Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information
          for each teacher in the course.
        - "observed_users": Optional information to include with each Course.
          Will include data for observed users if the current user has an
          observer enrollment.
        - "tabs": Optional information to include with each Course.
          Will include the list of tabs configured for each course.  See the
          {api:TabsController#index List available tabs API} for more information."""
        if include is not None:
            self._validate_enum(include, ["needs_grading_count", "syllabus_body", "public_description", "total_scores", "current_grading_period_scores", "term", "course_progress", "sections", "storage_quota_used_mb", "total_students", "passback_status", "favorites", "teachers", "observed_users"])
            params["include"] = include

        # OPTIONAL - state
        """If set, only return courses that are in the given state(s).
        By default, "available" is returned for students and observers, and
        anything except "deleted", for all other enrollment types"""
        if state is not None:
            self._validate_enum(state, ["unpublished", "available", "completed", "deleted"])
            params["state"] = state

        # OPTIONAL - enrollment_state
        """When set, only return courses where the user has an enrollment with the given state.
        This will respect section/course/term date overrides."""
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "invited_or_pending", "completed"])
            params["enrollment_state"] = enrollment_state

        self.logger.debug("GET /api/v1/users/{user_id}/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/courses".format(**path), data=data, params=params, all_pages=True)

    def create_new_course(self, account_id, course_allow_student_forum_attachments=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_apply_assignment_group_weights=None, course_course_code=None, course_course_format=None, course_end_at=None, course_grading_standard_id=None, course_hide_final_grades=None, course_integration_id=None, course_is_public=None, course_is_public_to_auth_users=None, course_license=None, course_name=None, course_open_enrollment=None, course_public_description=None, course_public_syllabus=None, course_public_syllabus_to_auth=None, course_restrict_enrollments_to_course_dates=None, course_self_enrollment=None, course_sis_course_id=None, course_start_at=None, course_syllabus_body=None, course_term_id=None, course_time_zone=None, enable_sis_reactivation=None, enroll_me=None, offer=None):
        """
        Create a new course.

        Create a new course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - course[name]
        """The name of the course. If omitted, the course will be named "Unnamed
        Course.""""
        if course_name is not None:
            data["course[name]"] = course_name

        # OPTIONAL - course[course_code]
        """The course code for the course."""
        if course_course_code is not None:
            data["course[course_code]"] = course_course_code

        # OPTIONAL - course[start_at]
        """Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z"""
        if course_start_at is not None:
            data["course[start_at]"] = course_start_at

        # OPTIONAL - course[end_at]
        """Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z"""
        if course_end_at is not None:
            data["course[end_at]"] = course_end_at

        # OPTIONAL - course[license]
        """The name of the licensing. Should be one of the following abbreviations
        (a descriptive name is included in parenthesis for reference):
        - 'private' (Private Copyrighted)
        - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)
        - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)
        - 'cc_by_nc' (CC Attribution Non-Commercial)
        - 'cc_by_nd' (CC Attribution No Derivatives)
        - 'cc_by_sa' (CC Attribution Share Alike)
        - 'cc_by' (CC Attribution)
        - 'public_domain' (Public Domain)."""
        if course_license is not None:
            data["course[license]"] = course_license

        # OPTIONAL - course[is_public]
        """Set to true if course is public to both authenticated and unauthenticated users."""
        if course_is_public is not None:
            data["course[is_public]"] = course_is_public

        # OPTIONAL - course[is_public_to_auth_users]
        """Set to true if course is public only to authenticated users."""
        if course_is_public_to_auth_users is not None:
            data["course[is_public_to_auth_users]"] = course_is_public_to_auth_users

        # OPTIONAL - course[public_syllabus]
        """Set to true to make the course syllabus public."""
        if course_public_syllabus is not None:
            data["course[public_syllabus]"] = course_public_syllabus

        # OPTIONAL - course[public_syllabus_to_auth]
        """Set to true to make the course syllabus public for authenticated users."""
        if course_public_syllabus_to_auth is not None:
            data["course[public_syllabus_to_auth]"] = course_public_syllabus_to_auth

        # OPTIONAL - course[public_description]
        """A publicly visible description of the course."""
        if course_public_description is not None:
            data["course[public_description]"] = course_public_description

        # OPTIONAL - course[allow_student_wiki_edits]
        """If true, students will be able to modify the course wiki."""
        if course_allow_student_wiki_edits is not None:
            data["course[allow_student_wiki_edits]"] = course_allow_student_wiki_edits

        # OPTIONAL - course[allow_wiki_comments]
        """If true, course members will be able to comment on wiki pages."""
        if course_allow_wiki_comments is not None:
            data["course[allow_wiki_comments]"] = course_allow_wiki_comments

        # OPTIONAL - course[allow_student_forum_attachments]
        """If true, students can attach files to forum posts."""
        if course_allow_student_forum_attachments is not None:
            data["course[allow_student_forum_attachments]"] = course_allow_student_forum_attachments

        # OPTIONAL - course[open_enrollment]
        """Set to true if the course is open enrollment."""
        if course_open_enrollment is not None:
            data["course[open_enrollment]"] = course_open_enrollment

        # OPTIONAL - course[self_enrollment]
        """Set to true if the course is self enrollment."""
        if course_self_enrollment is not None:
            data["course[self_enrollment]"] = course_self_enrollment

        # OPTIONAL - course[restrict_enrollments_to_course_dates]
        """Set to true to restrict user enrollments to the start and end dates of the
        course."""
        if course_restrict_enrollments_to_course_dates is not None:
            data["course[restrict_enrollments_to_course_dates]"] = course_restrict_enrollments_to_course_dates

        # OPTIONAL - course[term_id]
        """The unique ID of the term to create to course in."""
        if course_term_id is not None:
            data["course[term_id]"] = course_term_id

        # OPTIONAL - course[sis_course_id]
        """The unique SIS identifier."""
        if course_sis_course_id is not None:
            data["course[sis_course_id]"] = course_sis_course_id

        # OPTIONAL - course[integration_id]
        """The unique Integration identifier."""
        if course_integration_id is not None:
            data["course[integration_id]"] = course_integration_id

        # OPTIONAL - course[hide_final_grades]
        """If this option is set to true, the totals in student grades summary will
        be hidden."""
        if course_hide_final_grades is not None:
            data["course[hide_final_grades]"] = course_hide_final_grades

        # OPTIONAL - course[apply_assignment_group_weights]
        """Set to true to weight final grade based on assignment groups percentages."""
        if course_apply_assignment_group_weights is not None:
            data["course[apply_assignment_group_weights]"] = course_apply_assignment_group_weights

        # OPTIONAL - course[time_zone]
        """The time zone for the course. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        if course_time_zone is not None:
            data["course[time_zone]"] = course_time_zone

        # OPTIONAL - offer
        """If this option is set to true, the course will be available to students
        immediately."""
        if offer is not None:
            data["offer"] = offer

        # OPTIONAL - enroll_me
        """Set to true to enroll the current user as the teacher."""
        if enroll_me is not None:
            data["enroll_me"] = enroll_me

        # OPTIONAL - course[syllabus_body]
        """The syllabus body for the course"""
        if course_syllabus_body is not None:
            data["course[syllabus_body]"] = course_syllabus_body

        # OPTIONAL - course[grading_standard_id]
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course."""
        if course_grading_standard_id is not None:
            data["course[grading_standard_id]"] = course_grading_standard_id

        # OPTIONAL - course[course_format]
        """Optional. Specifies the format of the course. (Should be 'on_campus', 'online', or 'blended')"""
        if course_course_format is not None:
            data["course[course_format]"] = course_course_format

        # OPTIONAL - enable_sis_reactivation
        """When true, will first try to re-activate a deleted course with matching sis_course_id if possible."""
        if enable_sis_reactivation is not None:
            data["enable_sis_reactivation"] = enable_sis_reactivation

        self.logger.debug("POST /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/courses".format(**path), data=data, params=params, single_item=True)

    def upload_file(self, course_id):
        """
        Upload a file.

        Upload a file to the course.
        
        This API endpoint is the first step in uploading a file to a course.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.
        
        Only those with the "Manage Files" permission on a course can upload files
        to the course. By default, this is Teachers, TAs and Designers.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("POST /api/v1/courses/{course_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/files".format(**path), data=data, params=params, no_data=True)

    def list_students(self, course_id):
        """
        List students.

        Returns the list of students enrolled in this course.
        
        DEPRECATED: Please use the {api:CoursesController#users course users} endpoint
        and pass "student" as the enrollment_type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/students with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/students".format(**path), data=data, params=params, all_pages=True)

    def list_users_in_course_users(self, course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, user_id=None, user_ids=None):
        """
        List users in course.

        Returns the list of users in this course. And optionally the user's enrollments in the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - search_term
        """The partial name or full ID of the users to match and return in the results list."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - enrollment_type
        """When set, only return users where the user is enrolled as this type.
        "student_view" implies include[]=test_student.
        This argument is ignored if enrollment_role is given."""
        if enrollment_type is not None:
            self._validate_enum(enrollment_type, ["teacher", "student", "student_view", "ta", "observer", "designer"])
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """Deprecated
        When set, only return users enrolled with the specified course-level role.  This can be
        a role created with the {api:RoleOverridesController#add_role Add Role API} or a
        base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'ObserverEnrollment', or 'DesignerEnrollment'."""
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'."""
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - include
        """- "email": Optional user email.
        - "enrollments":
        Optionally include with each Course the user's current and invited
        enrollments. If the user is enrolled as a student, and the account has
        permission to manage or view all grades, each enrollment will include a
        'grades' key with 'current_score', 'final_score', 'current_grade' and
        'final_grade' values.
        - "locked": Optionally include whether an enrollment is locked.
        - "avatar_url": Optionally include avatar_url.
        - "bio": Optionally include each user's bio.
        - "test_student": Optionally include the course's Test Student,
        if present. Default is to not include Test Student.
        - "custom_links": Optionally include plugin-supplied custom links for each student,
        such as analytics information"""
        if include is not None:
            self._validate_enum(include, ["email", "enrollments", "locked", "avatar_url", "test_student", "bio", "custom_links"])
            params["include"] = include

        # OPTIONAL - user_id
        """If this parameter is given and it corresponds to a user in the course,
        the +page+ parameter will be ignored and the page containing the specified user
        will be returned instead."""
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - user_ids
        """If included, the course users set will only include users with IDs
        specified by the param. Note: this will not work in conjunction
        with the "user_id" argument but multiple user_ids can be included."""
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - enrollment_state
        """When set, only return users where the enrollment workflow state is of one of the given types.
        "active" and "invited" enrollments are returned by default."""
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "invited", "rejected", "completed", "inactive"])
            params["enrollment_state"] = enrollment_state

        self.logger.debug("GET /api/v1/courses/{course_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/users".format(**path), data=data, params=params, all_pages=True)

    def list_users_in_course_search_users(self, course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, user_id=None, user_ids=None):
        """
        List users in course.

        Returns the list of users in this course. And optionally the user's enrollments in the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - search_term
        """The partial name or full ID of the users to match and return in the results list."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - enrollment_type
        """When set, only return users where the user is enrolled as this type.
        "student_view" implies include[]=test_student.
        This argument is ignored if enrollment_role is given."""
        if enrollment_type is not None:
            self._validate_enum(enrollment_type, ["teacher", "student", "student_view", "ta", "observer", "designer"])
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """Deprecated
        When set, only return users enrolled with the specified course-level role.  This can be
        a role created with the {api:RoleOverridesController#add_role Add Role API} or a
        base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'ObserverEnrollment', or 'DesignerEnrollment'."""
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'."""
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - include
        """- "email": Optional user email.
        - "enrollments":
        Optionally include with each Course the user's current and invited
        enrollments. If the user is enrolled as a student, and the account has
        permission to manage or view all grades, each enrollment will include a
        'grades' key with 'current_score', 'final_score', 'current_grade' and
        'final_grade' values.
        - "locked": Optionally include whether an enrollment is locked.
        - "avatar_url": Optionally include avatar_url.
        - "bio": Optionally include each user's bio.
        - "test_student": Optionally include the course's Test Student,
        if present. Default is to not include Test Student.
        - "custom_links": Optionally include plugin-supplied custom links for each student,
        such as analytics information"""
        if include is not None:
            self._validate_enum(include, ["email", "enrollments", "locked", "avatar_url", "test_student", "bio", "custom_links"])
            params["include"] = include

        # OPTIONAL - user_id
        """If this parameter is given and it corresponds to a user in the course,
        the +page+ parameter will be ignored and the page containing the specified user
        will be returned instead."""
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - user_ids
        """If included, the course users set will only include users with IDs
        specified by the param. Note: this will not work in conjunction
        with the "user_id" argument but multiple user_ids can be included."""
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - enrollment_state
        """When set, only return users where the enrollment workflow state is of one of the given types.
        "active" and "invited" enrollments are returned by default."""
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "invited", "rejected", "completed", "inactive"])
            params["enrollment_state"] = enrollment_state

        self.logger.debug("GET /api/v1/courses/{course_id}/search_users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/search_users".format(**path), data=data, params=params, all_pages=True)

    def list_recently_logged_in_students(self, course_id):
        """
        List recently logged in students.

        Returns the list of users in this course, ordered by how recently they have
        logged in. The records include the 'last_login' field which contains
        a timestamp of the last time that user logged into canvas.  The querying
        user must have the 'View usage reports' permission.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/recent_students with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/recent_students".format(**path), data=data, params=params, all_pages=True)

    def get_single_user(self, id, course_id):
        """
        Get single user.

        Return information on a single user.
        
        Accepts the same include[] parameters as the :users: action, and returns a
        single user with the same fields as that action.
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

        self.logger.debug("GET /api/v1/courses/{course_id}/users/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/users/{id}".format(**path), data=data, params=params, single_item=True)

    def preview_processed_html(self, course_id, html=None):
        """
        Preview processed html.

        Preview html content processed for this course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - html
        """The html content to process"""
        if html is not None:
            data["html"] = html

        self.logger.debug("POST /api/v1/courses/{course_id}/preview_html with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/preview_html".format(**path), data=data, params=params, no_data=True)

    def course_activity_stream(self, course_id):
        """
        Course activity stream.

        Returns the current user's course-specific activity stream, paginated.
        
        For full documentation, see the API documentation for the user activity
        stream, in the user api.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/activity_stream with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/activity_stream".format(**path), data=data, params=params, no_data=True)

    def course_activity_stream_summary(self, course_id):
        """
        Course activity stream summary.

        Returns a summary of the current user's course-specific activity stream.
        
        For full documentation, see the API documentation for the user activity
        stream summary, in the user api.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/activity_stream/summary with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/activity_stream/summary".format(**path), data=data, params=params, no_data=True)

    def course_todo_items(self, course_id):
        """
        Course TODO items.

        Returns the current user's course-specific todo items.
        
        For full documentation, see the API documentation for the user todo items, in the user api.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/todo with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/todo".format(**path), data=data, params=params, no_data=True)

    def conclude_course(self, id, event):
        """
        Conclude a course.

        Delete or conclude an existing course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - event
        """The action to take on the course."""
        self._validate_enum(event, ["delete", "conclude"])
        params["event"] = event

        self.logger.debug("DELETE /api/v1/courses/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{id}".format(**path), data=data, params=params, no_data=True)

    def get_course_settings(self, course_id):
        """
        Get course settings.

        Returns some of a course's settings.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/settings".format(**path), data=data, params=params, no_data=True)

    def update_course_settings(self, course_id, allow_student_discussion_editing=None, allow_student_discussion_topics=None, allow_student_forum_attachments=None, allow_student_organized_groups=None, hide_distribution_graphs=None, hide_final_grades=None, home_page_announcement_limit=None, lock_all_announcements=None, restrict_student_future_view=None, restrict_student_past_view=None, show_announcements_on_home_page=None):
        """
        Update course settings.

        Can update the following course settings:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - allow_student_discussion_topics
        """Let students create discussion topics"""
        if allow_student_discussion_topics is not None:
            data["allow_student_discussion_topics"] = allow_student_discussion_topics

        # OPTIONAL - allow_student_forum_attachments
        """Let students attach files to discussions"""
        if allow_student_forum_attachments is not None:
            data["allow_student_forum_attachments"] = allow_student_forum_attachments

        # OPTIONAL - allow_student_discussion_editing
        """Let students edit or delete their own discussion posts"""
        if allow_student_discussion_editing is not None:
            data["allow_student_discussion_editing"] = allow_student_discussion_editing

        # OPTIONAL - allow_student_organized_groups
        """Let students organize their own groups"""
        if allow_student_organized_groups is not None:
            data["allow_student_organized_groups"] = allow_student_organized_groups

        # OPTIONAL - hide_final_grades
        """Hide totals in student grades summary"""
        if hide_final_grades is not None:
            data["hide_final_grades"] = hide_final_grades

        # OPTIONAL - hide_distribution_graphs
        """Hide grade distribution graphs from students"""
        if hide_distribution_graphs is not None:
            data["hide_distribution_graphs"] = hide_distribution_graphs

        # OPTIONAL - lock_all_announcements
        """Disable comments on announcements"""
        if lock_all_announcements is not None:
            data["lock_all_announcements"] = lock_all_announcements

        # OPTIONAL - restrict_student_past_view
        """Restrict students from viewing courses after end date"""
        if restrict_student_past_view is not None:
            data["restrict_student_past_view"] = restrict_student_past_view

        # OPTIONAL - restrict_student_future_view
        """Restrict students from viewing courses before start date"""
        if restrict_student_future_view is not None:
            data["restrict_student_future_view"] = restrict_student_future_view

        # OPTIONAL - show_announcements_on_home_page
        """Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home_page_announcement_limit)"""
        if show_announcements_on_home_page is not None:
            data["show_announcements_on_home_page"] = show_announcements_on_home_page

        # OPTIONAL - home_page_announcement_limit
        """Limit the number of announcements on the home page if enabled via show_announcements_on_home_page"""
        if home_page_announcement_limit is not None:
            data["home_page_announcement_limit"] = home_page_announcement_limit

        self.logger.debug("PUT /api/v1/courses/{course_id}/settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/settings".format(**path), data=data, params=params, no_data=True)

    def get_single_course_courses(self, id, include=None):
        """
        Get a single course.

        Return information on a single course.
        
        Accepts the same include[] parameters as the list action plus:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """- "all_courses": Also search recently deleted courses.
        - "permissions": Include permissions the current user has
          for the course.
        - "observed_users": include observed users in the enrollments"""
        if include is not None:
            self._validate_enum(include, ["needs_grading_count", "syllabus_body", "public_description", "total_scores", "current_grading_period_scores", "term", "course_progress", "sections", "storage_quota_used_mb", "total_students", "passback_status", "favorites", "teachers", "observed_users", "all_courses", "permissions", "observed_users"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{id}".format(**path), data=data, params=params, single_item=True)

    def get_single_course_accounts(self, id, account_id, include=None):
        """
        Get a single course.

        Return information on a single course.
        
        Accepts the same include[] parameters as the list action plus:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """- "all_courses": Also search recently deleted courses.
        - "permissions": Include permissions the current user has
          for the course.
        - "observed_users": include observed users in the enrollments"""
        if include is not None:
            self._validate_enum(include, ["needs_grading_count", "syllabus_body", "public_description", "total_scores", "current_grading_period_scores", "term", "course_progress", "sections", "storage_quota_used_mb", "total_students", "passback_status", "favorites", "teachers", "observed_users", "all_courses", "permissions", "observed_users"])
            params["include"] = include

        self.logger.debug("GET /api/v1/accounts/{account_id}/courses/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/courses/{id}".format(**path), data=data, params=params, single_item=True)

    def update_course(self, id, course_account_id=None, course_allow_student_forum_attachments=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_apply_assignment_group_weights=None, course_course_code=None, course_course_format=None, course_end_at=None, course_event=None, course_grading_standard_id=None, course_hide_final_grades=None, course_image_id=None, course_image_url=None, course_integration_id=None, course_is_public=None, course_is_public_to_auth_users=None, course_license=None, course_name=None, course_open_enrollment=None, course_public_description=None, course_public_syllabus=None, course_public_syllabus_to_auth=None, course_remove_image=None, course_restrict_enrollments_to_course_dates=None, course_self_enrollment=None, course_sis_course_id=None, course_start_at=None, course_storage_quota_mb=None, course_syllabus_body=None, course_term_id=None, course_time_zone=None, offer=None):
        """
        Update a course.

        Update an existing course.
        
        Arguments are the same as Courses#create, with a few exceptions (enroll_me).
        
        If a user has content management rights, but not full course editing rights, the only attribute
        editable through this endpoint will be "syllabus_body"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - course[account_id]
        """The unique ID of the account to move the course to."""
        if course_account_id is not None:
            data["course[account_id]"] = course_account_id

        # OPTIONAL - course[name]
        """The name of the course. If omitted, the course will be named "Unnamed
        Course.""""
        if course_name is not None:
            data["course[name]"] = course_name

        # OPTIONAL - course[course_code]
        """The course code for the course."""
        if course_course_code is not None:
            data["course[course_code]"] = course_course_code

        # OPTIONAL - course[start_at]
        """Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z"""
        if course_start_at is not None:
            data["course[start_at]"] = course_start_at

        # OPTIONAL - course[end_at]
        """Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z"""
        if course_end_at is not None:
            data["course[end_at]"] = course_end_at

        # OPTIONAL - course[license]
        """The name of the licensing. Should be one of the following abbreviations
        (a descriptive name is included in parenthesis for reference):
        - 'private' (Private Copyrighted)
        - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)
        - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)
        - 'cc_by_nc' (CC Attribution Non-Commercial)
        - 'cc_by_nd' (CC Attribution No Derivatives)
        - 'cc_by_sa' (CC Attribution Share Alike)
        - 'cc_by' (CC Attribution)
        - 'public_domain' (Public Domain)."""
        if course_license is not None:
            data["course[license]"] = course_license

        # OPTIONAL - course[is_public]
        """Set to true if course is public to both authenticated and unauthenticated users."""
        if course_is_public is not None:
            data["course[is_public]"] = course_is_public

        # OPTIONAL - course[is_public_to_auth_users]
        """Set to true if course is public only to authenticated users."""
        if course_is_public_to_auth_users is not None:
            data["course[is_public_to_auth_users]"] = course_is_public_to_auth_users

        # OPTIONAL - course[public_syllabus]
        """Set to true to make the course syllabus public."""
        if course_public_syllabus is not None:
            data["course[public_syllabus]"] = course_public_syllabus

        # OPTIONAL - course[public_syllabus_to_auth]
        """Set to true to make the course syllabus to public for authenticated users."""
        if course_public_syllabus_to_auth is not None:
            data["course[public_syllabus_to_auth]"] = course_public_syllabus_to_auth

        # OPTIONAL - course[public_description]
        """A publicly visible description of the course."""
        if course_public_description is not None:
            data["course[public_description]"] = course_public_description

        # OPTIONAL - course[allow_student_wiki_edits]
        """If true, students will be able to modify the course wiki."""
        if course_allow_student_wiki_edits is not None:
            data["course[allow_student_wiki_edits]"] = course_allow_student_wiki_edits

        # OPTIONAL - course[allow_wiki_comments]
        """If true, course members will be able to comment on wiki pages."""
        if course_allow_wiki_comments is not None:
            data["course[allow_wiki_comments]"] = course_allow_wiki_comments

        # OPTIONAL - course[allow_student_forum_attachments]
        """If true, students can attach files to forum posts."""
        if course_allow_student_forum_attachments is not None:
            data["course[allow_student_forum_attachments]"] = course_allow_student_forum_attachments

        # OPTIONAL - course[open_enrollment]
        """Set to true if the course is open enrollment."""
        if course_open_enrollment is not None:
            data["course[open_enrollment]"] = course_open_enrollment

        # OPTIONAL - course[self_enrollment]
        """Set to true if the course is self enrollment."""
        if course_self_enrollment is not None:
            data["course[self_enrollment]"] = course_self_enrollment

        # OPTIONAL - course[restrict_enrollments_to_course_dates]
        """Set to true to restrict user enrollments to the start and end dates of the
        course."""
        if course_restrict_enrollments_to_course_dates is not None:
            data["course[restrict_enrollments_to_course_dates]"] = course_restrict_enrollments_to_course_dates

        # OPTIONAL - course[term_id]
        """The unique ID of the term to create to course in."""
        if course_term_id is not None:
            data["course[term_id]"] = course_term_id

        # OPTIONAL - course[sis_course_id]
        """The unique SIS identifier."""
        if course_sis_course_id is not None:
            data["course[sis_course_id]"] = course_sis_course_id

        # OPTIONAL - course[integration_id]
        """The unique Integration identifier."""
        if course_integration_id is not None:
            data["course[integration_id]"] = course_integration_id

        # OPTIONAL - course[hide_final_grades]
        """If this option is set to true, the totals in student grades summary will
        be hidden."""
        if course_hide_final_grades is not None:
            data["course[hide_final_grades]"] = course_hide_final_grades

        # OPTIONAL - course[time_zone]
        """The time zone for the course. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        if course_time_zone is not None:
            data["course[time_zone]"] = course_time_zone

        # OPTIONAL - course[apply_assignment_group_weights]
        """Set to true to weight final grade based on assignment groups percentages."""
        if course_apply_assignment_group_weights is not None:
            data["course[apply_assignment_group_weights]"] = course_apply_assignment_group_weights

        # OPTIONAL - course[storage_quota_mb]
        """Set the storage quota for the course, in megabytes. The caller must have
        the "Manage storage quotas" account permission."""
        if course_storage_quota_mb is not None:
            data["course[storage_quota_mb]"] = course_storage_quota_mb

        # OPTIONAL - offer
        """If this option is set to true, the course will be available to students
        immediately."""
        if offer is not None:
            data["offer"] = offer

        # OPTIONAL - course[event]
        """The action to take on each course.
        * 'claim' makes a course no longer visible to students. This action is also called "unpublish" on the web site.
          A course cannot be unpublished if students have received graded submissions.
        * 'offer' makes a course visible to students. This action is also called "publish" on the web site.
        * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears
          in prior-enrollment lists.
        * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).
          All enrollments are deleted. Course content may be physically deleted at a future date.
        * 'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude
          rather than delete a course if there is any possibility the course will be used again.) The recovered course
          will be unpublished. Deleted enrollments will not be recovered."""
        if course_event is not None:
            self._validate_enum(course_event, ["claim", "offer", "conclude", "delete", "undelete"])
            data["course[event]"] = course_event

        # OPTIONAL - course[syllabus_body]
        """The syllabus body for the course"""
        if course_syllabus_body is not None:
            data["course[syllabus_body]"] = course_syllabus_body

        # OPTIONAL - course[grading_standard_id]
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course."""
        if course_grading_standard_id is not None:
            data["course[grading_standard_id]"] = course_grading_standard_id

        # OPTIONAL - course[course_format]
        """Optional. Specifies the format of the course. (Should be either 'on_campus' or 'online')"""
        if course_course_format is not None:
            data["course[course_format]"] = course_course_format

        # OPTIONAL - course[image_id]
        """This is a file ID corresponding to an image file in the course that will
        be used as the course image.
        This will clear the course's image_url setting if set.  If you attempt
        to provide image_url and image_id in a request it will fail."""
        if course_image_id is not None:
            data["course[image_id]"] = course_image_id

        # OPTIONAL - course[image_url]
        """This is a URL to an image to be used as the course image.
        This will clear the course's image_id setting if set.  If you attempt
        to provide image_url and image_id in a request it will fail."""
        if course_image_url is not None:
            data["course[image_url]"] = course_image_url

        # OPTIONAL - course[remove_image]
        """If this option is set to true, the course image url and course image
        ID are both set to nil"""
        if course_remove_image is not None:
            data["course[remove_image]"] = course_remove_image

        self.logger.debug("PUT /api/v1/courses/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{id}".format(**path), data=data, params=params, no_data=True)

    def update_courses(self, event, account_id, course_ids):
        """
        Update courses.

        Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}
        to query the status of an operation.
        
        The action to take on each course.  Must be one of 'offer', 'conclude', 'delete', or 'undelete'.
          * 'offer' makes a course visible to students. This action is also called "publish" on the web site.
          * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears
            in prior-enrollment lists.
          * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).
            All enrollments are deleted. Course content may be physically deleted at a future date.
          * 'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude
            rather than delete a course if there is any possibility the course will be used again.) The recovered course
            will be unpublished. Deleted enrollments will not be recovered.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - course_ids
        """List of ids of courses to update. At most 500 courses may be updated in one call."""
        data["course_ids"] = course_ids

        # REQUIRED - event
        """no description"""
        self._validate_enum(event, ["offer", "conclude", "delete", "undelete"])
        data["event"] = event

        self.logger.debug("PUT /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/courses".format(**path), data=data, params=params, single_item=True)

    def reset_course(self, course_id):
        """
        Reset a course.

        Deletes the current course, and creates a new equivalent course with
        no content, but all sections and users moved over.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("POST /api/v1/courses/{course_id}/reset_content with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/reset_content".format(**path), data=data, params=params, single_item=True)

    def get_effective_due_dates(self, course_id, assignment_ids=None):
        """
        Get effective due dates.

        For each assignment in the course, returns each assigned student's ID
        and their corresponding due date along with some Multiple Grading Periods
        data. Returns a collection with keys representing assignment IDs and values
        as a collection containing keys representing student IDs and values representing
        the student's effective due_at, the grading_period_id of which the due_at falls
        in, and whether or not the grading period is closed (in_closed_grading_period)
        
        The list of assignment IDs for which effective student due dates are
        requested. If not provided, all assignments in the course will be used.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - assignment_ids
        """no description"""
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids

        self.logger.debug("GET /api/v1/courses/{course_id}/effective_due_dates with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/effective_due_dates".format(**path), data=data, params=params, single_item=True)

    def permissions(self, course_id, permissions=None):
        """
        Permissions.

        Returns permission information for provided course & current_user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - permissions
        """List of permissions to check against authenticated user"""
        if permissions is not None:
            params["permissions"] = permissions

        self.logger.debug("GET /api/v1/courses/{course_id}/permissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/permissions".format(**path), data=data, params=params, no_data=True)

    def get_course_copy_status(self, id, course_id):
        """
        Get course copy status.

        DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}
        
        Retrieve the status of a course copy
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

        self.logger.debug("GET /api/v1/courses/{course_id}/course_copy/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/course_copy/{id}".format(**path), data=data, params=params, no_data=True)

    def copy_course_content(self, course_id, except=None, only=None, source_course=None):
        """
        Copy course content.

        DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}
        
        Copies content from one course into another. The default is to copy all course
        content. You can control specific types to copy by using either the 'except' option
        or the 'only' option.
        
        The response is the same as the course copy status endpoint
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - source_course
        """ID or SIS-ID of the course to copy the content from"""
        if source_course is not None:
            data["source_course"] = source_course

        # OPTIONAL - except
        """A list of the course content types to exclude, all areas not listed will
        be copied."""
        if except is not None:
            self._validate_enum(except, ["course_settings", "assignments", "external_tools", "files", "topics", "calendar_events", "quizzes", "wiki_pages", "modules", "outcomes"])
            data["except"] = except

        # OPTIONAL - only
        """A list of the course content types to copy, all areas not listed will not
        be copied."""
        if only is not None:
            self._validate_enum(only, ["course_settings", "assignments", "external_tools", "files", "topics", "calendar_events", "quizzes", "wiki_pages", "modules", "outcomes"])
            data["only"] = only

        self.logger.debug("POST /api/v1/courses/{course_id}/course_copy with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/course_copy".format(**path), data=data, params=params, no_data=True)


class Course(BaseModel):
    """Course Model."""

    def __init__(self, open_enrollment=None, storage_quota_used_mb=None, is_public=None, calendar=None, allow_wiki_comments=None, id=None, public_syllabus_to_auth=None, default_view=None, is_public_to_auth_users=None, access_restricted_by_date=None, root_account_id=None, end_at=None, storage_quota_mb=None, self_enrollment=None, syllabus_body=None, start_at=None, account_id=None, workflow_state=None, public_syllabus=None, grading_standard_id=None, apply_assignment_group_weights=None, enrollment_term_id=None, course_format=None, enrollments=None, needs_grading_count=None, permissions=None, integration_id=None, term=None, name=None, license=None, allow_student_forum_attachments=None, restrict_enrollments_to_course_dates=None, time_zone=None, hide_final_grades=None, allow_student_assignment_edits=None, sis_course_id=None, course_progress=None, public_description=None, course_code=None, total_students=None):
        """Init method for Course class."""
        self._open_enrollment = open_enrollment
        self._storage_quota_used_mb = storage_quota_used_mb
        self._is_public = is_public
        self._calendar = calendar
        self._allow_wiki_comments = allow_wiki_comments
        self._id = id
        self._public_syllabus_to_auth = public_syllabus_to_auth
        self._default_view = default_view
        self._is_public_to_auth_users = is_public_to_auth_users
        self._access_restricted_by_date = access_restricted_by_date
        self._root_account_id = root_account_id
        self._end_at = end_at
        self._storage_quota_mb = storage_quota_mb
        self._self_enrollment = self_enrollment
        self._syllabus_body = syllabus_body
        self._start_at = start_at
        self._account_id = account_id
        self._workflow_state = workflow_state
        self._public_syllabus = public_syllabus
        self._grading_standard_id = grading_standard_id
        self._apply_assignment_group_weights = apply_assignment_group_weights
        self._enrollment_term_id = enrollment_term_id
        self._course_format = course_format
        self._enrollments = enrollments
        self._needs_grading_count = needs_grading_count
        self._permissions = permissions
        self._integration_id = integration_id
        self._term = term
        self._name = name
        self._license = license
        self._allow_student_forum_attachments = allow_student_forum_attachments
        self._restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates
        self._time_zone = time_zone
        self._hide_final_grades = hide_final_grades
        self._allow_student_assignment_edits = allow_student_assignment_edits
        self._sis_course_id = sis_course_id
        self._course_progress = course_progress
        self._public_description = public_description
        self._course_code = course_code
        self._total_students = total_students

        self.logger = logging.getLogger('pycanvas.Course')

    @property
    def open_enrollment(self):
        """open_enrollment."""
        return self._open_enrollment

    @open_enrollment.setter
    def open_enrollment(self, value):
        """Setter for open_enrollment property."""
        self.logger.warn("Setting values on open_enrollment will NOT update the remote Canvas instance.")
        self._open_enrollment = value

    @property
    def storage_quota_used_mb(self):
        """storage_quota_used_mb."""
        return self._storage_quota_used_mb

    @storage_quota_used_mb.setter
    def storage_quota_used_mb(self, value):
        """Setter for storage_quota_used_mb property."""
        self.logger.warn("Setting values on storage_quota_used_mb will NOT update the remote Canvas instance.")
        self._storage_quota_used_mb = value

    @property
    def is_public(self):
        """is_public."""
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        """Setter for is_public property."""
        self.logger.warn("Setting values on is_public will NOT update the remote Canvas instance.")
        self._is_public = value

    @property
    def calendar(self):
        """course calendar."""
        return self._calendar

    @calendar.setter
    def calendar(self, value):
        """Setter for calendar property."""
        self.logger.warn("Setting values on calendar will NOT update the remote Canvas instance.")
        self._calendar = value

    @property
    def allow_wiki_comments(self):
        """allow_wiki_comments."""
        return self._allow_wiki_comments

    @allow_wiki_comments.setter
    def allow_wiki_comments(self, value):
        """Setter for allow_wiki_comments property."""
        self.logger.warn("Setting values on allow_wiki_comments will NOT update the remote Canvas instance.")
        self._allow_wiki_comments = value

    @property
    def id(self):
        """the unique identifier for the course."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def public_syllabus_to_auth(self):
        """public_syllabus_to_auth."""
        return self._public_syllabus_to_auth

    @public_syllabus_to_auth.setter
    def public_syllabus_to_auth(self, value):
        """Setter for public_syllabus_to_auth property."""
        self.logger.warn("Setting values on public_syllabus_to_auth will NOT update the remote Canvas instance.")
        self._public_syllabus_to_auth = value

    @property
    def default_view(self):
        """the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future."""
        return self._default_view

    @default_view.setter
    def default_view(self, value):
        """Setter for default_view property."""
        self.logger.warn("Setting values on default_view will NOT update the remote Canvas instance.")
        self._default_view = value

    @property
    def is_public_to_auth_users(self):
        """is_public_to_auth_users."""
        return self._is_public_to_auth_users

    @is_public_to_auth_users.setter
    def is_public_to_auth_users(self, value):
        """Setter for is_public_to_auth_users property."""
        self.logger.warn("Setting values on is_public_to_auth_users will NOT update the remote Canvas instance.")
        self._is_public_to_auth_users = value

    @property
    def access_restricted_by_date(self):
        """optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings."""
        return self._access_restricted_by_date

    @access_restricted_by_date.setter
    def access_restricted_by_date(self, value):
        """Setter for access_restricted_by_date property."""
        self.logger.warn("Setting values on access_restricted_by_date will NOT update the remote Canvas instance.")
        self._access_restricted_by_date = value

    @property
    def root_account_id(self):
        """the root account associated with the course."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

    @property
    def end_at(self):
        """the end date for the course, if applicable."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def storage_quota_mb(self):
        """storage_quota_mb."""
        return self._storage_quota_mb

    @storage_quota_mb.setter
    def storage_quota_mb(self, value):
        """Setter for storage_quota_mb property."""
        self.logger.warn("Setting values on storage_quota_mb will NOT update the remote Canvas instance.")
        self._storage_quota_mb = value

    @property
    def self_enrollment(self):
        """self_enrollment."""
        return self._self_enrollment

    @self_enrollment.setter
    def self_enrollment(self, value):
        """Setter for self_enrollment property."""
        self.logger.warn("Setting values on self_enrollment will NOT update the remote Canvas instance.")
        self._self_enrollment = value

    @property
    def syllabus_body(self):
        """optional: user-generated HTML for the course syllabus."""
        return self._syllabus_body

    @syllabus_body.setter
    def syllabus_body(self, value):
        """Setter for syllabus_body property."""
        self.logger.warn("Setting values on syllabus_body will NOT update the remote Canvas instance.")
        self._syllabus_body = value

    @property
    def start_at(self):
        """the start date for the course, if applicable."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def account_id(self):
        """the account associated with the course."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn("Setting values on account_id will NOT update the remote Canvas instance.")
        self._account_id = value

    @property
    def workflow_state(self):
        """the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def public_syllabus(self):
        """public_syllabus."""
        return self._public_syllabus

    @public_syllabus.setter
    def public_syllabus(self, value):
        """Setter for public_syllabus property."""
        self.logger.warn("Setting values on public_syllabus will NOT update the remote Canvas instance.")
        self._public_syllabus = value

    @property
    def grading_standard_id(self):
        """the grading standard associated with the course."""
        return self._grading_standard_id

    @grading_standard_id.setter
    def grading_standard_id(self, value):
        """Setter for grading_standard_id property."""
        self.logger.warn("Setting values on grading_standard_id will NOT update the remote Canvas instance.")
        self._grading_standard_id = value

    @property
    def apply_assignment_group_weights(self):
        """weight final grade based on assignment group percentages."""
        return self._apply_assignment_group_weights

    @apply_assignment_group_weights.setter
    def apply_assignment_group_weights(self, value):
        """Setter for apply_assignment_group_weights property."""
        self.logger.warn("Setting values on apply_assignment_group_weights will NOT update the remote Canvas instance.")
        self._apply_assignment_group_weights = value

    @property
    def enrollment_term_id(self):
        """the enrollment term associated with the course."""
        return self._enrollment_term_id

    @enrollment_term_id.setter
    def enrollment_term_id(self, value):
        """Setter for enrollment_term_id property."""
        self.logger.warn("Setting values on enrollment_term_id will NOT update the remote Canvas instance.")
        self._enrollment_term_id = value

    @property
    def course_format(self):
        """course_format."""
        return self._course_format

    @course_format.setter
    def course_format(self, value):
        """Setter for course_format property."""
        self.logger.warn("Setting values on course_format will NOT update the remote Canvas instance.")
        self._course_format = value

    @property
    def enrollments(self):
        """A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn("Setting values on enrollments will NOT update the remote Canvas instance.")
        self._enrollments = value

    @property
    def needs_grading_count(self):
        """optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn("Setting values on needs_grading_count will NOT update the remote Canvas instance.")
        self._needs_grading_count = value

    @property
    def permissions(self):
        """optional: the permissions the user has for the course. returned only for a single course and include[]=permissions."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

    @property
    def integration_id(self):
        """the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def term(self):
        """optional: the enrollment term object for the course returned only if include[]=term."""
        return self._term

    @term.setter
    def term(self, value):
        """Setter for term property."""
        self.logger.warn("Setting values on term will NOT update the remote Canvas instance.")
        self._term = value

    @property
    def name(self):
        """the full name of the course."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def license(self):
        """license."""
        return self._license

    @license.setter
    def license(self, value):
        """Setter for license property."""
        self.logger.warn("Setting values on license will NOT update the remote Canvas instance.")
        self._license = value

    @property
    def allow_student_forum_attachments(self):
        """allow_student_forum_attachments."""
        return self._allow_student_forum_attachments

    @allow_student_forum_attachments.setter
    def allow_student_forum_attachments(self, value):
        """Setter for allow_student_forum_attachments property."""
        self.logger.warn("Setting values on allow_student_forum_attachments will NOT update the remote Canvas instance.")
        self._allow_student_forum_attachments = value

    @property
    def restrict_enrollments_to_course_dates(self):
        """restrict_enrollments_to_course_dates."""
        return self._restrict_enrollments_to_course_dates

    @restrict_enrollments_to_course_dates.setter
    def restrict_enrollments_to_course_dates(self, value):
        """Setter for restrict_enrollments_to_course_dates property."""
        self.logger.warn("Setting values on restrict_enrollments_to_course_dates will NOT update the remote Canvas instance.")
        self._restrict_enrollments_to_course_dates = value

    @property
    def time_zone(self):
        """The course's IANA time zone name."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn("Setting values on time_zone will NOT update the remote Canvas instance.")
        self._time_zone = value

    @property
    def hide_final_grades(self):
        """hide_final_grades."""
        return self._hide_final_grades

    @hide_final_grades.setter
    def hide_final_grades(self, value):
        """Setter for hide_final_grades property."""
        self.logger.warn("Setting values on hide_final_grades will NOT update the remote Canvas instance.")
        self._hide_final_grades = value

    @property
    def allow_student_assignment_edits(self):
        """allow_student_assignment_edits."""
        return self._allow_student_assignment_edits

    @allow_student_assignment_edits.setter
    def allow_student_assignment_edits(self, value):
        """Setter for allow_student_assignment_edits property."""
        self.logger.warn("Setting values on allow_student_assignment_edits will NOT update the remote Canvas instance.")
        self._allow_student_assignment_edits = value

    @property
    def sis_course_id(self):
        """the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information."""
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, value):
        """Setter for sis_course_id property."""
        self.logger.warn("Setting values on sis_course_id will NOT update the remote Canvas instance.")
        self._sis_course_id = value

    @property
    def course_progress(self):
        """optional (beta): information on progress through the course returned only if include[]=course_progress."""
        return self._course_progress

    @course_progress.setter
    def course_progress(self, value):
        """Setter for course_progress property."""
        self.logger.warn("Setting values on course_progress will NOT update the remote Canvas instance.")
        self._course_progress = value

    @property
    def public_description(self):
        """optional: the public description of the course."""
        return self._public_description

    @public_description.setter
    def public_description(self, value):
        """Setter for public_description property."""
        self.logger.warn("Setting values on public_description will NOT update the remote Canvas instance.")
        self._public_description = value

    @property
    def course_code(self):
        """the course code."""
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        """Setter for course_code property."""
        self.logger.warn("Setting values on course_code will NOT update the remote Canvas instance.")
        self._course_code = value

    @property
    def total_students(self):
        """optional: the total number of active and invited students in the course."""
        return self._total_students

    @total_students.setter
    def total_students(self, value):
        """Setter for total_students property."""
        self.logger.warn("Setting values on total_students will NOT update the remote Canvas instance.")
        self._total_students = value


class Term(BaseModel):
    """Term Model."""

    def __init__(self, end_at=None, start_at=None, id=None, name=None):
        """Init method for Term class."""
        self._end_at = end_at
        self._start_at = start_at
        self._id = id
        self._name = name

        self.logger = logging.getLogger('pycanvas.Term')

    @property
    def end_at(self):
        """end_at."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def start_at(self):
        """start_at."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

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
    def name(self):
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Courseprogress(BaseModel):
    """Courseprogress Model."""

    def __init__(self, requirement_count=None, next_requirement_url=None, requirement_completed_count=None, completed_at=None):
        """Init method for Courseprogress class."""
        self._requirement_count = requirement_count
        self._next_requirement_url = next_requirement_url
        self._requirement_completed_count = requirement_completed_count
        self._completed_at = completed_at

        self.logger = logging.getLogger('pycanvas.Courseprogress')

    @property
    def requirement_count(self):
        """total number of requirements from all modules."""
        return self._requirement_count

    @requirement_count.setter
    def requirement_count(self, value):
        """Setter for requirement_count property."""
        self.logger.warn("Setting values on requirement_count will NOT update the remote Canvas instance.")
        self._requirement_count = value

    @property
    def next_requirement_url(self):
        """url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress."""
        return self._next_requirement_url

    @next_requirement_url.setter
    def next_requirement_url(self, value):
        """Setter for next_requirement_url property."""
        self.logger.warn("Setting values on next_requirement_url will NOT update the remote Canvas instance.")
        self._next_requirement_url = value

    @property
    def requirement_completed_count(self):
        """total number of requirements the user has completed from all modules."""
        return self._requirement_completed_count

    @requirement_completed_count.setter
    def requirement_completed_count(self, value):
        """Setter for requirement_completed_count property."""
        self.logger.warn("Setting values on requirement_completed_count will NOT update the remote Canvas instance.")
        self._requirement_completed_count = value

    @property
    def completed_at(self):
        """date the course was completed. null if the course has not been completed by this user."""
        return self._completed_at

    @completed_at.setter
    def completed_at(self, value):
        """Setter for completed_at property."""
        self.logger.warn("Setting values on completed_at will NOT update the remote Canvas instance.")
        self._completed_at = value


class Calendarlink(BaseModel):
    """Calendarlink Model."""

    def __init__(self, ics=None):
        """Init method for Calendarlink class."""
        self._ics = ics

        self.logger = logging.getLogger('pycanvas.Calendarlink')

    @property
    def ics(self):
        """The URL of the calendar in ICS format."""
        return self._ics

    @ics.setter
    def ics(self, value):
        """Setter for ics property."""
        self.logger.warn("Setting values on ics will NOT update the remote Canvas instance.")
        self._ics = value

