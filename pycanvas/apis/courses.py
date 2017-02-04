from datetime import date, datetime
from base import BaseApi

from ..meta.courses import CoursesServiceMetadata


class CoursesService(BaseApi):
    """Canvas Courses REST API."""

    def list_your_courses(self, enrollment_role=None, enrollment_role_id=None, enrollment_type=None, include=None, page=None, per_page=None, state=None, *args, **kwargs):
        """Returns the list of active courses for the current user."""
        api_meta = CoursesServiceMetadata.list_your_courses
        return self.api_precall(api_meta, locals())

    def create_new_course(self, account_id, course_allow_student_forum_attachments=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_apply_assignment_group_weights=None, course_course_code=None, course_course_format=None, course_end_at=None, course_grading_standard_id=None, course_hide_final_grades=None, course_integration_id=None, course_is_public=None, course_is_public_to_auth_users=None, course_license=None, course_name=None, course_open_enrollment=None, course_public_description=None, course_public_syllabus=None, course_restrict_enrollments_to_course_dates=None, course_self_enrollment=None, course_sis_course_id=None, course_start_at=None, course_syllabus_body=None, course_term_id=None, enroll_me=None, offer=None, *args, **kwargs):
        """Create a new course"""
        api_meta = CoursesServiceMetadata.create_new_course
        return self.api_precall(api_meta, locals())

    def upload_file(self, course_id, *args, **kwargs):
        """Upload a file to the course.This API endpoint is the first step in uploading a file to a course.See the {file:file_uploads.html File Upload Documentation} for details onthe file upload workflow.Only those with the "Manage Files" permission on a course can upload filesto the course. By default, this is Teachers, TAs and Designers."""
        api_meta = CoursesServiceMetadata.upload_file
        return self.api_precall(api_meta, locals())

    def list_students(self, course_id, page=None, per_page=None, *args, **kwargs):
        """Returns the list of students enrolled in this course.DEPRECATED: Please use the {api:CoursesController#users course users} endpointand pass "student" as the enrollment_type."""
        api_meta = CoursesServiceMetadata.list_students
        return self.api_precall(api_meta, locals())

    def list_users_in_course_users(self, course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, page=None, per_page=None, search_term=None, user_id=None, *args, **kwargs):
        """Returns the list of users in this course. And optionally the user"s enrollments in the course."""
        api_meta = CoursesServiceMetadata.list_users_in_course_users
        return self.api_precall(api_meta, locals())

    def list_users_in_course_search_users(self, course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, page=None, per_page=None, search_term=None, user_id=None, *args, **kwargs):
        """Returns the list of users in this course. And optionally the user"s enrollments in the course."""
        api_meta = CoursesServiceMetadata.list_users_in_course_search_users
        return self.api_precall(api_meta, locals())

    def list_recently_logged_in_students(self, course_id, page=None, per_page=None, *args, **kwargs):
        """Returns the list of users in this course, ordered by how recently they havelogged in. The records include the "last_login" field which containsa timestamp of the last time that user logged into canvas.  The queryinguser must have the "View usage reports" permission."""
        api_meta = CoursesServiceMetadata.list_recently_logged_in_students
        return self.api_precall(api_meta, locals())

    def get_single_user(self, id, course_id, *args, **kwargs):
        """Return information on a single user.Accepts the same include[] parameters as the :users: action, and returns asingle user with the same fields as that action."""
        api_meta = CoursesServiceMetadata.get_single_user
        return self.api_precall(api_meta, locals())

    def preview_processed_html(self, course_id, html=None, *args, **kwargs):
        """Preview html content processed for this course"""
        api_meta = CoursesServiceMetadata.preview_processed_html
        return self.api_precall(api_meta, locals())

    def course_activity_stream(self, course_id, *args, **kwargs):
        """Returns the current user"s course-specific activity stream, paginated.For full documentation, see the API documentation for the user activitystream, in the user api."""
        api_meta = CoursesServiceMetadata.course_activity_stream
        return self.api_precall(api_meta, locals())

    def course_activity_stream_summary(self, course_id, *args, **kwargs):
        """Returns a summary of the current user"s course-specific activity stream.For full documentation, see the API documentation for the user activitystream summary, in the user api."""
        api_meta = CoursesServiceMetadata.course_activity_stream_summary
        return self.api_precall(api_meta, locals())

    def course_todo_items(self, course_id, *args, **kwargs):
        """Returns the current user"s course-specific todo items.For full documentation, see the API documentation for the user todo items, in the user api."""
        api_meta = CoursesServiceMetadata.course_todo_items
        return self.api_precall(api_meta, locals())

    def conclude_course(self, id, event, *args, **kwargs):
        """Delete or conclude an existing course"""
        api_meta = CoursesServiceMetadata.conclude_course
        return self.api_precall(api_meta, locals())

    def get_course_settings(self, course_id, *args, **kwargs):
        """Returns some of a course"s settings."""
        api_meta = CoursesServiceMetadata.get_course_settings
        return self.api_precall(api_meta, locals())

    def update_course_settings(self, course_id, allow_student_discussion_editing=None, allow_student_discussion_topics=None, allow_student_forum_attachments=None, allow_student_organized_groups=None, hide_distribution_graphs=None, hide_final_grades=None, lock_all_announcements=None, restrict_student_future_view=None, restrict_student_past_view=None, *args, **kwargs):
        """Can update the following course settings:"""
        api_meta = CoursesServiceMetadata.update_course_settings
        return self.api_precall(api_meta, locals())

    def get_single_course_courses(self, id, include=None, *args, **kwargs):
        """Return information on a single course.Accepts the same include[] parameters as the list action plus:"""
        api_meta = CoursesServiceMetadata.get_single_course_courses
        return self.api_precall(api_meta, locals())

    def get_single_course_accounts(self, id, account_id, include=None, *args, **kwargs):
        """Return information on a single course.Accepts the same include[] parameters as the list action plus:"""
        api_meta = CoursesServiceMetadata.get_single_course_accounts
        return self.api_precall(api_meta, locals())

    def update_course(self, id, course_account_id, course_allow_student_forum_attachments=None, course_allow_student_wiki_edits=None, course_allow_wiki_comments=None, course_apply_assignment_group_weights=None, course_course_code=None, course_course_format=None, course_end_at=None, course_grading_standard_id=None, course_hide_final_grades=None, course_integration_id=None, course_is_public=None, course_license=None, course_name=None, course_open_enrollment=None, course_public_description=None, course_public_syllabus=None, course_restrict_enrollments_to_course_dates=None, course_self_enrollment=None, course_sis_course_id=None, course_start_at=None, course_syllabus_body=None, course_term_id=None, offer=None, *args, **kwargs):
        """Update an existing course.Arguments are the same as Courses#create, with a few exceptions (enroll_me)."""
        api_meta = CoursesServiceMetadata.update_course
        return self.api_precall(api_meta, locals())

    def update_courses(self, event, course_ids, account_id, *args, **kwargs):
        """Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}to query the status of an operation.The action to take on each course.  Must be one of "offer", "conclude", "delete", or "undelete".  * "offer" makes a course visible to students. This action is also called "publish" on the web site.  * "conclude" prevents future enrollments and makes a course read-only for all participants. The course still appears    in prior-enrollment lists.  * "delete" completely removes the course from the web site (including course menus and prior-enrollment lists).    All enrollments are deleted. Course content may be physically deleted at a future date.  * "undelete" attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude    rather than delete a course if there is any possibility the course will be used again.) The recovered course    will be unpublished. Deleted enrollments will not be recovered."""
        api_meta = CoursesServiceMetadata.update_courses
        return self.api_precall(api_meta, locals())

    def reset_course(self, course_id, *args, **kwargs):
        """Deletes the current course, and creates a new equivalent course withno content, but all sections and users moved over."""
        api_meta = CoursesServiceMetadata.reset_course
        return self.api_precall(api_meta, locals())

    def get_course_copy_status(self, id, course_id, *args, **kwargs):
        """DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}Retrieve the status of a course copy"""
        api_meta = CoursesServiceMetadata.get_course_copy_status
        return self.api_precall(api_meta, locals())

    def copy_course_content(self, course_id, except=None, only=None, source_course=None, *args, **kwargs):
        """DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}Copies content from one course into another. The default is to copy all coursecontent. You can control specific types to copy by using either the "except" optionor the "only" option.The response is the same as the course copy status endpoint"""
        api_meta = CoursesServiceMetadata.copy_course_content
        return self.api_precall(api_meta, locals())

