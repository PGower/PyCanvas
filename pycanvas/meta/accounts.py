from datetime import date, datetime
from base import BaseMetadata, ValidationError
import dateutil.parser

class AccountsServiceMetadata(BaseMetadata):
    apis = ['list_accounts', 'list_accounts_for_course_admins', 'get_single_account', 'get_sub_accounts_of_account', 'list_active_courses_in_account', 'update_account', 'delete_user_from_root_account', 'create_new_sub_account', ]

    list_accounts = {
        'method': 'GET',
        'path': '/v1/accounts',
        'help': 'List accounts that the current user can view or manage.  Typically,students and even teachers will get an empty list in response, onlyaccount admins can view the accounts that they are in.',
        'params': {
            'include': {
                'param_type': 'query',
                'type': [],
                'help': 'Array of additional information to include. "lti_guid":: the "tool_consumer_instance_guid" that will be sent for this account on LTI launches "registration_settings":: returns info about the privacy policy and terms of use',
                'required': False,
                'enum': ['lti_guid', 'registration_settings', ],
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
        'returns': '[model:Account]',
    }

    list_accounts_for_course_admins = {
        'method': 'GET',
        'path': '/v1/course_accounts',
        'help': 'List accounts that the current user can view through their admin course enrollments.(Teacher, TA, or designer enrollments).Only returns "id", "name", "workflow_state", "root_account_id" and "parent_account_id"',
        'params': {
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
        'returns': '[model:Account]',
    }

    get_single_account = {
        'method': 'GET',
        'path': '/v1/accounts/{id}',
        'help': 'Retrieve information on an individual account, given by id or sissis_account_id.',
        'params': {
            'id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'model:Account',
    }

    get_sub_accounts_of_account = {
        'method': 'GET',
        'path': '/v1/accounts/{account_id}/sub_accounts',
        'help': 'List accounts that are sub-accounts of the given account.',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
            'recursive': {
                'param_type': 'query',
                'type': bool,
                'help': 'If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false.',
                'required': False,
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
        'returns': '[model:Account]',
    }

    list_active_courses_in_account = {
        'method': 'GET',
        'path': '/v1/accounts/{account_id}/courses',
        'help': 'Retrieve the list of courses in this account.',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
            'with_enrollments': {
                'param_type': 'query',
                'type': bool,
                'help': 'If true, include only courses with at least one enrollment. If false, include only courses with no enrollments. If not present, do not filter on course enrollment status.',
                'required': False,
            },
            'published': {
                'param_type': 'query',
                'type': bool,
                'help': 'If true, include only published courses. If false, exclude published courses. If not present, do not filter on published status.',
                'required': False,
            },
            'completed': {
                'param_type': 'query',
                'type': bool,
                'help': 'If true, include only completed courses (these may be in state "completed", or their enrollment term may have ended). If false, exclude completed courses. If not present, do not filter on completed status.',
                'required': False,
            },
            'by_teachers': {
                'param_type': 'query',
                'type': [],
                'help': 'List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users.',
                'required': False,
            },
            'by_subaccounts': {
                'param_type': 'query',
                'type': [],
                'help': 'List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts.',
                'required': False,
            },
            'hide_enrollmentless_courses': {
                'param_type': 'query',
                'type': bool,
                'help': 'If present, only return courses that have at least one enrollment. Equivalent to "with_enrollments=true"; retained for compatibility.',
                'required': False,
            },
            'state': {
                'param_type': 'query',
                'type': [],
                'help': 'If set, only return courses that are in the given state(s). By default, all states but "deleted" are returned.',
                'required': False,
                'enum': ['created', 'claimed', 'available', 'completed', 'deleted', 'all', ],
            },
            'enrollment_term_id': {
                'param_type': 'query',
                'type': int,
                'help': 'If set, only includes courses from the specified term.',
                'required': False,
            },
            'search_term': {
                'param_type': 'query',
                'type': str,
                'help': 'The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters.',
                'required': False,
            },
            'include': {
                'param_type': 'query',
                'type': [],
                'help': '- All explanations can be seen in the {api:CoursesController#index Course API index documentation}',
                'required': False,
                'enum': ['needs_grading_count', 'syllabus_body', 'total_scores', 'term', 'course_progress', 'sections', 'storage_quota_used_mb', ],
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

    update_account = {
        'method': 'PUT',
        'path': '/v1/accounts/{id}',
        'help': 'Update an existing account.',
        'params': {
            'id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
            'account[name]': {
                'param_type': 'form',
                'type': str,
                'help': 'Updates the account name',
                'required': False,
            },
            'account[default_time_zone]': {
                'param_type': 'form',
                'type': str,
                'help': 'The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.',
                'required': False,
            },
            'account[default_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default course storage quota to be used, if not otherwise specified.',
                'required': False,
            },
            'account[default_user_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default user storage quota to be used, if not otherwise specified.',
                'required': False,
            },
            'account[default_group_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default group storage quota to be used, if not otherwise specified.',
                'required': False,
            },
        },
        'returns': 'model:Account',
    }

    delete_user_from_root_account = {
        'method': 'DELETE',
        'path': '/v1/accounts/{account_id}/users/{user_id}',
        'help': 'Delete a user record from a Canvas root account. If a user is associatedwith multiple root accounts (in a multi-tenant instance of Canvas), thisaction will NOT remove them from the other accounts.WARNING: This API will allow a user to remove themselves from the account.If they do this, they won"t be able to make API calls or log into Canvas atthat account.',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
            'user_id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
        },
        'returns': 'model:User',
    }

    create_new_sub_account = {
        'method': 'POST',
        'path': '/v1/accounts/{account_id}/sub_accounts',
        'help': 'Add a new sub-account to a given account.',
        'params': {
            'account_id': {
                'param_type': 'path',
                'type': str,
                'help': 'ID',
                'required': True,
            },
            'account[name]': {
                'param_type': 'form',
                'type': str,
                'help': 'The name of the new sub-account.',
                'required': True,
            },
            'account[default_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default course storage quota to be used, if not otherwise specified.',
                'required': False,
            },
            'account[default_user_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default user storage quota to be used, if not otherwise specified.',
                'required': False,
            },
            'account[default_group_storage_quota_mb]': {
                'param_type': 'form',
                'type': int,
                'help': 'The default group storage quota to be used, if not otherwise specified.',
                'required': False,
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
        'returns': '[model:Account]',
    }


class AccountModelMetadata(BaseMetadata):
    help = ''

    attributes = {
        'integration_id': str,
        'default_time_zone': str,
        'name': str,
        'default_storage_quota_mb': int,
        'sis_account_id': str,
        'root_account_id': int,
        'default_group_storage_quota_mb': int,
        'id': int,
        'sis_import_id': int,
        'lti_guid': str,
        'workflow_state': str,
        'parent_account_id': int,
        'default_user_storage_quota_mb': int,
    }