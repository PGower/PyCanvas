import datetime.date
import datetime.datetime
import dateutil.parser

from base import BaseModel

from ..meta.course import CourseModelMetadata

class Course(BaseModel):
    metadata = CourseModelMetadata

    attributes = CourseModelMetadata.attributes

    def __init__(self,
                 account_id=None,
                 allow_student_assignment_edits=None,
                 allow_student_forum_attachments=None,
                 allow_wiki_comments=None,
                 apply_assignment_group_weights=None,
                 calendar=None,
                 course_code=None,
                 course_format=None,
                 course_progress=None,
                 default_view=None,
                 end_at=None,
                 enrollment_term_id=None,
                 enrollments=None,
                 hide_final_grades=None,
                 id=None,
                 integration_id=None,
                 is_public=None,
                 is_public_to_auth_users=None,
                 license=None,
                 name=None,
                 needs_grading_count=None,
                 open_enrollment=None,
                 permissions=None,
                 public_description=None,
                 public_syllabus=None,
                 restrict_enrollments_to_course_dates=None,
                 root_account_id=None,
                 self_enrollment=None,
                 sis_course_id=None,
                 start_at=None,
                 storage_quota_mb=None,
                 storage_quota_used_mb=None,
                 syllabus_body=None,
                 term=None,
                 total_students=None,
                 workflow_state=None,
                 *args,
                 **kwargs):
        self.open_enrollment = open_enrollment
        self.syllabus_body = syllabus_body
        self.start_at = start_at
        self.hide_final_grades = hide_final_grades
        self.workflow_state = workflow_state
        self.public_syllabus = public_syllabus
        self.storage_quota_mb = storage_quota_mb
        self.storage_quota_used_mb = storage_quota_used_mb
        self.account_id = account_id
        self.enrollment_term_id = enrollment_term_id
        self.course_format = course_format
        self.is_public = is_public
        self.enrollments = enrollments
        self.needs_grading_count = needs_grading_count
        self.calendar = calendar
        self.allow_wiki_comments = allow_wiki_comments
        self.id = id
        self.permissions = permissions
        self.integration_id = integration_id
        self.default_view = default_view
        self.term = term
        self.is_public_to_auth_users = is_public_to_auth_users
        self.name = name
        self.license = license
        self.allow_student_forum_attachments = allow_student_forum_attachments
        self.root_account_id = root_account_id
        self.restrict_enrollments_to_course_dates = restrict_enrollments_to_course_dates
        self.end_at = end_at
        self.allow_student_assignment_edits = allow_student_assignment_edits
        self.sis_course_id = sis_course_id
        self.apply_assignment_group_weights = apply_assignment_group_weights
        self.course_code = course_code
        self.public_description = public_description
        self.course_progress = course_progress
        self.self_enrollment = self_enrollment
        self.total_students = total_students
