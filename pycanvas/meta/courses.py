from datetime import date, datetime
from base import BaseModelMetadata, BaseServiceMetadata, ValidationError
import dateutil.parser

class CoursesServiceMetadata(BaseServiceMetadata):
    name = 'Courses'
    apis = ['list_your_courses', 'create_new_course', 'upload_file', 'list_students', 'list_users_in_course_users', 'list_users_in_course_search_users', 'list_recently_logged_in_students', 'get_single_user', 'preview_processed_html', 'course_activity_stream', 'course_activity_stream_summary', 'course_todo_items', 'conclude_course', 'get_course_settings', 'update_course_settings', 'get_single_course_courses', 'get_single_course_accounts', 'update_course', 'update_courses', 'reset_course', 'get_course_copy_status', 'copy_course_content', ]

    list_your_courses = {
        'method': 'GET',
        'path': '/v1/courses',
        'help': 'Returns the list of active courses for the current user.',
        'params': {
            'enrollment_type': {
                'param_type': 'query',
                'type': 'str',
                'help': 'When set, only return courses where the user is enrolled as this type. For example, set to "teacher" to return only courses where the user is enrolled as a Teacher. This argument is ignored if enrollment_role is given.',
                'required': False,
                'enum': ['teacher', 'student', 'ta', 'observer', 'designer', ],
            },
            'enrollment_role': {
                'param_type': 'query',
                'type': 'str',
                'help': 'Deprecated When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'enrollment_role_id': {
                'param_type': 'query',
                'type': 'int',
                'help': 'When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role type of "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'include': {
                'param_type': 'query',
                'type': '[str]',
                'help': '- "needs_grading_count": Optional information to include with each Course. When needs_grading_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned. - "syllabus_body": Optional information to include with each Course. When syllabus_body is given the user-generated html for the course syllabus is returned. - "total_scores": Optional information to include with each Course. When total_scores is given, any enrollments with type "student" will also include the fields "calculated_current_score", "calculated_final_score", "calculated_current_grade", and "calculated_final_grade". calculated_current_score is the student"s score in the course, ignoring ungraded assignments. calculated_final_score is the student"s score in the course including ungraded assignments with a score of 0. calculated_current_grade is the letter grade equivalent of calculated_current_score (if available). calculated_final_grade is the letter grade equivalent of calculated_final_score (if available). This argument is ignored if the course is configured to hide final grades. - "term": Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned. - "course_progress": Optional information to include with each Course. When course_progress is given, each course will include a "course_progress" object with the fields: "requirement_count", an integer specifying the total number of requirements in the course, "requirement_completed_count", an integer specifying the total number of requirements in this course that have been completed, and "next_requirement_url", a string url to the next requirement item, and "completed_at", the date the course was completed (null if incomplete). "next_requirement_url" will be null if all requirements have been completed or the current module does not require sequential progress. "course_progress" will return an error message if the course is not module based or the user is not enrolled as a student in the course. - "sections": Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start_at, end_at), as well as the enrollment type (enrollment_role, e.g. "StudentEnrollment"). - "storage_quota_used_mb": The amount of storage space used by the files in this course - "total_students": Optional information to include with each Course. Returns an integer for the total amount of active and invited students. - "passback_status": Include the grade passback_status',
                'required': False,
                'enum': ['needs_grading_count', 'syllabus_body', 'total_scores', 'term', 'course_progress', 'sections', 'storage_quota_used_mb', 'total_students', ],
            },
            'state': {
                'param_type': 'query',
                'type': '[str]',
                'help': 'If set, only return courses that are in the given state(s). By default, "available" is returned for students and observers, and anything except "deleted", for all other enrollment types',
                'required': False,
                'enum': ['unpublished', 'available', 'completed', 'deleted', ],
            },
            'per_page': {
                'param_type': 'query',
                'type': int,
                'help': 'Number of items to show on each page.',
                'required': False
            },
            'page': {
                'param_type': 'query',
                'type': int,
                'help': 'Page of items to load',
                'required': False
            },
        },
        'returns': '[model:Course]',
    }

    create_new_course = {
        'method': 'POST',
        'path': '/v1/accounts/{account_id}/courses',
        'help': 'Create a new course',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': 'int',
                'help': 'The unique ID of the account to create to course under.',
                'required': True,
            },
            'course[name]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The name of the course. If omitted, the course will be named "Unnamed Course."',
                'required': False,
            },
            'course[course_code]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The course code for the course.',
                'required': False,
            },
            'course[start_at]': {
                'param_type': 'form',
                'type': 'datetime.datetime',
                'help': 'Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z',
                'required': False,
            },
            'course[end_at]': {
                'param_type': 'form',
                'type': 'datetime.datetime',
                'help': 'Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z',
                'required': False,
            },
            'course[license]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - "private" (Private Copyrighted) - "cc_by_nc_nd" (CC Attribution Non-Commercial No Derivatives) - "cc_by_nc_sa" (CC Attribution Non-Commercial Share Alike) - "cc_by_nc" (CC Attribution Non-Commercial) - "cc_by_nd" (CC Attribution No Derivatives) - "cc_by_sa" (CC Attribution Share Alike) - "cc_by" (CC Attribution) - "public_domain" (Public Domain).',
                'required': False,
            },
            'course[is_public]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if course if public.',
                'required': False,
            },
            'course[is_public_to_auth_users]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if course if public to authenticated users.',
                'required': False,
            },
            'course[public_syllabus]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to make the course syllabus public.',
                'required': False,
            },
            'course[public_description]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'A publicly visible description of the course.',
                'required': False,
            },
            'course[allow_student_wiki_edits]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, students will be able to modify the course wiki.',
                'required': False,
            },
            'course[allow_wiki_comments]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, course members will be able to comment on wiki pages.',
                'required': False,
            },
            'course[allow_student_forum_attachments]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, students can attach files to forum posts.',
                'required': False,
            },
            'course[open_enrollment]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if the course is open enrollment.',
                'required': False,
            },
            'course[self_enrollment]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if the course is self enrollment.',
                'required': False,
            },
            'course[restrict_enrollments_to_course_dates]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to restrict user enrollments to the start and end dates of the course.',
                'required': False,
            },
            'course[term_id]': {
                'param_type': 'form',
                'type': 'int',
                'help': 'The unique ID of the term to create to course in.',
                'required': False,
            },
            'course[sis_course_id]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The unique SIS identifier.',
                'required': False,
            },
            'course[integration_id]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The unique Integration identifier.',
                'required': False,
            },
            'course[hide_final_grades]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If this option is set to true, the totals in student grades summary will be hidden.',
                'required': False,
            },
            'course[apply_assignment_group_weights]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to weight final grade based on assignment groups percentages.',
                'required': False,
            },
            'offer': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If this option is set to true, the course will be available to students immediately.',
                'required': False,
            },
            'enroll_me': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to enroll the current user as the teacher.',
                'required': False,
            },
            'course[syllabus_body]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The syllabus body for the course',
                'required': False,
            },
            'course[grading_standard_id]': {
                'param_type': 'form',
                'type': 'int',
                'help': 'The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course.',
                'required': False,
            },
            'course[course_format]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'Optional. Specifies the format of the course. (Should be either "on_campus" or "online")',
                'required': False,
            },
        },
        'returns': 'None',
    }

    upload_file = {
        'method': 'POST',
        'path': '/v1/courses/{course_id}/files',
        'help': 'Upload a file to the course.This API endpoint is the first step in uploading a file to a course.See the {file:file_uploads.html File Upload Documentation} for details onthe file upload workflow.Only those with the "Manage Files" permission on a course can upload filesto the course. By default, this is Teachers, TAs and Designers.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    list_students = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/students',
        'help': 'Returns the list of students enrolled in this course.DEPRECATED: Please use the {api:CoursesController#users course users} endpointand pass "student" as the enrollment_type.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'per_page': {
                'param_type': 'query',
                'type': int,
                'help': 'Number of items to show on each page.',
                'required': False
            },
            'page': {
                'param_type': 'query',
                'type': int,
                'help': 'Page of items to load',
                'required': False
            },
        },
        'returns': '[model:User]',
    }

    list_users_in_course_users = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/users',
        'help': 'Returns the list of users in this course. And optionally the user"s enrollments in the course.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'search_term': {
                'param_type': 'query',
                'type': 'str',
                'help': 'The partial name or full ID of the users to match and return in the results list.',
                'required': False,
            },
            'enrollment_type': {
                'param_type': 'query',
                'type': 'str',
                'help': 'When set, only return users where the user is enrolled as this type. This argument is ignored if enrollment_role is given.',
                'required': False,
                'enum': ['teacher', 'student', 'ta', 'observer', 'designer', ],
            },
            'enrollment_role': {
                'param_type': 'query',
                'type': 'str',
                'help': 'Deprecated When set, only return users enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'enrollment_role_id': {
                'param_type': 'query',
                'type': 'int',
                'help': 'When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'include': {
                'param_type': 'query',
                'type': '[str]',
                'help': '- "email": Optional user email. - "enrollments": Optionally include with each Course the user"s current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a "grades" key with "current_score", "final_score", "current_grade" and "final_grade" values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "bio": Optionally include each user"s bio. - "test_student": Optionally include the course"s Test Student, if present. Default is to not include Test Student.',
                'required': False,
                'enum': ['email', 'enrollments', 'locked', 'avatar_url', 'test_student', 'bio', ],
            },
            'user_id': {
                'param_type': 'query',
                'type': 'str',
                'help': 'If included, the user will be queried and if the user is part of the users set, the page parameter will be modified so that the page containing user_id will be returned.',
                'required': False,
            },
            'enrollment_state': {
                'param_type': 'query',
                'type': '[str]',
                'help': 'When set, only return users where the enrollment workflow state is of one of the given types. "active" and "invited" enrollments are returned by default.',
                'required': False,
                'enum': ['active', 'invited', 'rejected', 'completed', 'inactive', ],
            },
            'per_page': {
                'param_type': 'query',
                'type': int,
                'help': 'Number of items to show on each page.',
                'required': False
            },
            'page': {
                'param_type': 'query',
                'type': int,
                'help': 'Page of items to load',
                'required': False
            },
        },
        'returns': '[model:User]',
    }

    list_users_in_course_search_users = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/search_users',
        'help': 'Returns the list of users in this course. And optionally the user"s enrollments in the course.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'search_term': {
                'param_type': 'query',
                'type': 'str',
                'help': 'The partial name or full ID of the users to match and return in the results list.',
                'required': False,
            },
            'enrollment_type': {
                'param_type': 'query',
                'type': 'str',
                'help': 'When set, only return users where the user is enrolled as this type. This argument is ignored if enrollment_role is given.',
                'required': False,
                'enum': ['teacher', 'student', 'ta', 'observer', 'designer', ],
            },
            'enrollment_role': {
                'param_type': 'query',
                'type': 'str',
                'help': 'Deprecated When set, only return users enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'enrollment_role_id': {
                'param_type': 'query',
                'type': 'int',
                'help': 'When set, only return courses where the user is enrolled with the specified course-level role. This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", or "DesignerEnrollment".',
                'required': False,
            },
            'include': {
                'param_type': 'query',
                'type': '[str]',
                'help': '- "email": Optional user email. - "enrollments": Optionally include with each Course the user"s current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a "grades" key with "current_score", "final_score", "current_grade" and "final_grade" values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "bio": Optionally include each user"s bio. - "test_student": Optionally include the course"s Test Student, if present. Default is to not include Test Student.',
                'required': False,
                'enum': ['email', 'enrollments', 'locked', 'avatar_url', 'test_student', 'bio', ],
            },
            'user_id': {
                'param_type': 'query',
                'type': 'str',
                'help': 'If included, the user will be queried and if the user is part of the users set, the page parameter will be modified so that the page containing user_id will be returned.',
                'required': False,
            },
            'enrollment_state': {
                'param_type': 'query',
                'type': '[str]',
                'help': 'When set, only return users where the enrollment workflow state is of one of the given types. "active" and "invited" enrollments are returned by default.',
                'required': False,
                'enum': ['active', 'invited', 'rejected', 'completed', 'inactive', ],
            },
            'per_page': {
                'param_type': 'query',
                'type': int,
                'help': 'Number of items to show on each page.',
                'required': False
            },
            'page': {
                'param_type': 'query',
                'type': int,
                'help': 'Page of items to load',
                'required': False
            },
        },
        'returns': '[model:User]',
    }

    list_recently_logged_in_students = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/recent_students',
        'help': 'Returns the list of users in this course, ordered by how recently they havelogged in. The records include the "last_login" field which containsa timestamp of the last time that user logged into canvas.  The queryinguser must have the "View usage reports" permission.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'per_page': {
                'param_type': 'query',
                'type': int,
                'help': 'Number of items to show on each page.',
                'required': False
            },
            'page': {
                'param_type': 'query',
                'type': int,
                'help': 'Page of items to load',
                'required': False
            },
        },
        'returns': '[model:User]',
    }

    get_single_user = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/users/{id}',
        'help': 'Return information on a single user.Accepts the same include[] parameters as the :users: action, and returns asingle user with the same fields as that action.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    preview_processed_html = {
        'method': 'POST',
        'path': '/v1/courses/{course_id}/preview_html',
        'help': 'Preview html content processed for this course',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'html': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The html content to process',
                'required': False,
            },
        },
        'returns': 'None',
    }

    course_activity_stream = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/activity_stream',
        'help': 'Returns the current user"s course-specific activity stream, paginated.For full documentation, see the API documentation for the user activitystream, in the user api.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    course_activity_stream_summary = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/activity_stream/summary',
        'help': 'Returns a summary of the current user"s course-specific activity stream.For full documentation, see the API documentation for the user activitystream summary, in the user api.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    course_todo_items = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/todo',
        'help': 'Returns the current user"s course-specific todo items.For full documentation, see the API documentation for the user todo items, in the user api.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    conclude_course = {
        'method': 'DELETE',
        'path': '/v1/courses/{id}',
        'help': 'Delete or conclude an existing course',
        'params': {
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'event': {
                'param_type': 'query',
                'type': 'str',
                'help': 'The action to take on the course.',
                'required': True,
                'enum': ['delete', 'conclude', ],
            },
        },
        'returns': 'None',
    }

    get_course_settings = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/settings',
        'help': 'Returns some of a course"s settings.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    update_course_settings = {
        'method': 'PUT',
        'path': '/v1/courses/{course_id}/settings',
        'help': 'Can update the following course settings:',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'allow_student_discussion_topics': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Let students create discussion topics',
                'required': False,
            },
            'allow_student_forum_attachments': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Let students attach files to discussions',
                'required': False,
            },
            'allow_student_discussion_editing': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Let students edit or delete their own discussion posts',
                'required': False,
            },
            'allow_student_organized_groups': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Let students organize their own groups',
                'required': False,
            },
            'hide_final_grades': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Hide totals in student grades summary',
                'required': False,
            },
            'hide_distribution_graphs': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Hide grade distribution graphs from students',
                'required': False,
            },
            'lock_all_announcements': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Disable comments on announcements',
                'required': False,
            },
            'restrict_student_past_view': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Restrict students from viewing courses after end date',
                'required': False,
            },
            'restrict_student_future_view': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Restrict students from viewing courses before start date',
                'required': False,
            },
        },
        'returns': 'None',
    }

    get_single_course_courses = {
        'method': 'GET',
        'path': '/v1/courses/{id}',
        'help': 'Return information on a single course.Accepts the same include[] parameters as the list action plus:',
        'params': {
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'include': {
                'param_type': 'query',
                'type': '[str]',
                'help': '- "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has for the course.',
                'required': False,
                'enum': ['all_courses', 'permissions', ],
            },
        },
        'returns': 'None',
    }

    get_single_course_accounts = {
        'method': 'GET',
        'path': '/v1/accounts/{account_id}/courses/{id}',
        'help': 'Return information on a single course.Accepts the same include[] parameters as the list action plus:',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'include': {
                'param_type': 'query',
                'type': '[str]',
                'help': '- "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has for the course.',
                'required': False,
                'enum': ['all_courses', 'permissions', ],
            },
        },
        'returns': 'None',
    }

    update_course = {
        'method': 'PUT',
        'path': '/v1/courses/{id}',
        'help': 'Update an existing course.Arguments are the same as Courses#create, with a few exceptions (enroll_me).',
        'params': {
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'course[account_id]': {
                'param_type': 'form',
                'type': 'int',
                'help': 'The unique ID of the account to create to course under.',
                'required': True,
            },
            'course[name]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The name of the course. If omitted, the course will be named "Unnamed Course."',
                'required': False,
            },
            'course[course_code]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The course code for the course.',
                'required': False,
            },
            'course[start_at]': {
                'param_type': 'form',
                'type': 'datetime.datetime',
                'help': 'Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z',
                'required': False,
            },
            'course[end_at]': {
                'param_type': 'form',
                'type': 'datetime.datetime',
                'help': 'Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z',
                'required': False,
            },
            'course[license]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - "private" (Private Copyrighted) - "cc_by_nc_nd" (CC Attribution Non-Commercial No Derivatives) - "cc_by_nc_sa" (CC Attribution Non-Commercial Share Alike) - "cc_by_nc" (CC Attribution Non-Commercial) - "cc_by_nd" (CC Attribution No Derivatives) - "cc_by_sa" (CC Attribution Share Alike) - "cc_by" (CC Attribution) - "public_domain" (Public Domain).',
                'required': False,
            },
            'course[is_public]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if course if public.',
                'required': False,
            },
            'course[public_syllabus]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to make the course syllabus public.',
                'required': False,
            },
            'course[public_description]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'A publicly visible description of the course.',
                'required': False,
            },
            'course[allow_student_wiki_edits]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, students will be able to modify the course wiki.',
                'required': False,
            },
            'course[allow_wiki_comments]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, course members will be able to comment on wiki pages.',
                'required': False,
            },
            'course[allow_student_forum_attachments]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If true, students can attach files to forum posts.',
                'required': False,
            },
            'course[open_enrollment]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if the course is open enrollment.',
                'required': False,
            },
            'course[self_enrollment]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true if the course is self enrollment.',
                'required': False,
            },
            'course[restrict_enrollments_to_course_dates]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to restrict user enrollments to the start and end dates of the course.',
                'required': False,
            },
            'course[term_id]': {
                'param_type': 'form',
                'type': 'int',
                'help': 'The unique ID of the term to create to course in.',
                'required': False,
            },
            'course[sis_course_id]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The unique SIS identifier.',
                'required': False,
            },
            'course[integration_id]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The unique Integration identifier.',
                'required': False,
            },
            'course[hide_final_grades]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If this option is set to true, the totals in student grades summary will be hidden.',
                'required': False,
            },
            'course[apply_assignment_group_weights]': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'Set to true to weight final grade based on assignment groups percentages.',
                'required': False,
            },
            'offer': {
                'param_type': 'form',
                'type': 'bool',
                'help': 'If this option is set to true, the course will be available to students immediately.',
                'required': False,
            },
            'course[syllabus_body]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'The syllabus body for the course',
                'required': False,
            },
            'course[grading_standard_id]': {
                'param_type': 'form',
                'type': 'int',
                'help': 'The grading standard id to set for the course. If no value is provided for this argument the current grading_standard will be un-set from this course.',
                'required': False,
            },
            'course[course_format]': {
                'param_type': 'form',
                'type': 'str',
                'help': 'Optional. Specifies the format of the course. (Should be either "on_campus" or "online")',
                'required': False,
            },
        },
        'returns': 'None',
    }

    update_courses = {
        'method': 'PUT',
        'path': '/v1/accounts/{account_id}/courses',
        'help': 'Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}to query the status of an operation.The action to take on each course.  Must be one of "offer", "conclude", "delete", or "undelete".  * "offer" makes a course visible to students. This action is also called "publish" on the web site.  * "conclude" prevents future enrollments and makes a course read-only for all participants. The course still appears    in prior-enrollment lists.  * "delete" completely removes the course from the web site (including course menus and prior-enrollment lists).    All enrollments are deleted. Course content may be physically deleted at a future date.  * "undelete" attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude    rather than delete a course if there is any possibility the course will be used again.) The recovered course    will be unpublished. Deleted enrollments will not be recovered.',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'course_ids': {
                'param_type': 'form',
                'type': '[str]',
                'help': 'List of ids of courses to update. At most 500 courses may be updated in one call.',
                'required': True,
            },
            'event': {
                'param_type': 'form',
                'type': 'str',
                'help': 'no description',
                'required': True,
                'enum': ['offer', 'conclude', 'delete', 'undelete', ],
            },
        },
        'returns': 'None',
    }

    reset_course = {
        'method': 'POST',
        'path': '/v1/courses/{course_id}/reset_content',
        'help': 'Deletes the current course, and creates a new equivalent course withno content, but all sections and users moved over.',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    get_course_copy_status = {
        'method': 'GET',
        'path': '/v1/courses/{course_id}/course_copy/{id}',
        'help': 'DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}Retrieve the status of a course copy',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'None',
    }

    copy_course_content = {
        'method': 'POST',
        'path': '/v1/courses/{course_id}/course_copy',
        'help': 'DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}Copies content from one course into another. The default is to copy all coursecontent. You can control specific types to copy by using either the "except" optionor the "only" option.The response is the same as the course copy status endpoint',
        'params': {
            'course_id': {
                'param_type': 'path',
                'type': 'str',
                'help': 'ID',
                'required': True,
            },
            'source_course': {
                'param_type': 'form',
                'type': 'str',
                'help': 'ID or SIS-ID of the course to copy the content from',
                'required': False,
            },
            'except': {
                'param_type': 'form',
                'type': '[str]',
                'help': 'A list of the course content types to exclude, all areas not listed will be copied.',
                'required': False,
                'enum': ['course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes', ],
            },
            'only': {
                'param_type': 'form',
                'type': '[str]',
                'help': 'A list of the course content types to copy, all areas not listed will not be copied.',
                'required': False,
                'enum': ['course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes', ],
            },
        },
        'returns': 'None',
    }

service = CoursesServiceMetadata

class CourseModelMetadata(BaseModelMetadata):
    help = ''
    name = 'Course'

    attributes = {
        'open_enrollment': {
            'kind': 'bool',
            'required': False,
        },
        'storage_quota_used_mb': {
            'kind': 'float',
            'required': False,
        },
        'needs_grading_count': {
            'kind': 'int',
            'required': False,
        },
        'calendar': {
            'kind': 'model:Calendarlink',
            'required': False,
        },
        'allow_wiki_comments': {
            'kind': 'bool',
            'required': False,
        },
        'id': {
            'kind': 'int',
            'required': False,
        },
        'hide_final_grades': {
            'kind': 'bool',
            'required': False,
        },
        'default_view': {
            'kind': 'str',
            'required': False,
            'enum': ['feed', 'wiki', 'modules', 'syllabus', 'assignments', ],
        },
        'is_public_to_auth_users': {
            'kind': 'bool',
            'required': False,
        },
        'root_account_id': {
            'kind': 'int',
            'required': False,
        },
        'end_at': {
            'kind': 'datetime.datetime',
            'required': False,
        },
        'storage_quota_mb': {
            'kind': 'int',
            'required': False,
        },
        'self_enrollment': {
            'kind': 'bool',
            'required': False,
        },
        'permissions': {
            'kind': '{str:bool}',
            'required': False,
        },
        'start_at': {
            'kind': 'datetime.datetime',
            'required': False,
        },
        'account_id': {
            'kind': 'int',
            'required': False,
        },
        'workflow_state': {
            'kind': 'str',
            'required': False,
            'enum': ['unpublished', 'available', 'completed', 'deleted', ],
        },
        'public_syllabus': {
            'kind': 'bool',
            'required': False,
        },
        'apply_assignment_group_weights': {
            'kind': 'bool',
            'required': False,
        },
        'enrollment_term_id': {
            'kind': 'int',
            'required': False,
        },
        'course_format': {
            'kind': 'str',
            'required': False,
        },
        'enrollments': {
            'kind': '[model:Enrollment]',
            'required': False,
        },
        'is_public': {
            'kind': 'bool',
            'required': False,
        },
        'name': {
            'kind': 'str',
            'required': False,
        },
        'integration_id': {
            'kind': 'str',
            'required': False,
        },
        'term': {
            'kind': 'model:Term',
            'required': False,
        },
        'syllabus_body': {
            'kind': 'str',
            'required': False,
        },
        'license': {
            'kind': 'str',
            'required': False,
        },
        'allow_student_forum_attachments': {
            'kind': 'bool',
            'required': False,
        },
        'restrict_enrollments_to_course_dates': {
            'kind': 'bool',
            'required': False,
        },
        'allow_student_assignment_edits': {
            'kind': 'bool',
            'required': False,
        },
        'sis_course_id': {
            'kind': 'str',
            'required': False,
        },
        'course_progress': {
            'kind': 'model:Courseprogress',
            'required': False,
        },
        'public_description': {
            'kind': 'str',
            'required': False,
        },
        'course_code': {
            'kind': 'str',
            'required': False,
        },
        'total_students': {
            'kind': 'int',
            'required': False,
        },
    }

class TermModelMetadata(BaseModelMetadata):
    help = ''
    name = 'Term'

    attributes = {
        'end_at': {
            'kind': 'datetime.datetime',
            'required': False,
        },
        'start_at': {
            'kind': 'datetime.datetime',
            'required': False,
        },
        'id': {
            'kind': 'int',
            'required': False,
        },
        'name': {
            'kind': 'str',
            'required': False,
        },
    }

class CourseProgressModelMetadata(BaseModelMetadata):
    help = ''
    name = 'CourseProgress'

    attributes = {
        'requirement_count': {
            'kind': 'int',
            'required': False,
        },
        'next_requirement_url': {
            'kind': 'str',
            'required': False,
        },
        'requirement_completed_count': {
            'kind': 'int',
            'required': False,
        },
        'completed_at': {
            'kind': 'datetime.datetime',
            'required': False,
        },
    }

class CalendarLinkModelMetadata(BaseModelMetadata):
    help = ''
    name = 'CalendarLink'

    attributes = {
        'ics': {
            'kind': 'str',
            'required': False,
        },
    }


models = [CourseModelMetadata, TermModelMetadata, CourseProgressModelMetadata, CalendarLinkModelMetadata, ]