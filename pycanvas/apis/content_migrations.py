"""ContentMigrations API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class ContentMigrationsAPI(BaseCanvasAPI):
    """ContentMigrations API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ContentMigrationsAPI."""
        super(ContentMigrationsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.ContentMigrationsAPI")

    def list_migration_issues_accounts(self, account_id, content_migration_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_courses(self, course_id, content_migration_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_groups(self, group_id, content_migration_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_users(self, user_id, content_migration_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id

        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def get_migration_issue_accounts(self, id, account_id, content_migration_id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_courses(self, id, course_id, content_migration_id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_groups(self, id, group_id, content_migration_id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_users(self, id, user_id, content_migration_id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_accounts(self, id, account_id, workflow_state, content_migration_id):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - workflow_state - Set the workflow_state of the issue.
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state

        self.logger.debug("PUT /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_courses(self, id, course_id, workflow_state, content_migration_id):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - workflow_state - Set the workflow_state of the issue.
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state

        self.logger.debug("PUT /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_groups(self, id, group_id, workflow_state, content_migration_id):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - workflow_state - Set the workflow_state of the issue.
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state

        self.logger.debug("PUT /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_users(self, id, user_id, workflow_state, content_migration_id):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - content_migration_id - ID
        path["content_migration_id"] = content_migration_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - workflow_state - Set the workflow_state of the issue.
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state

        self.logger.debug("PUT /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def list_content_migrations_accounts(self, account_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_courses(self, course_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_groups(self, group_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_users(self, user_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def get_content_migration_accounts(self, id, account_id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_courses(self, id, course_id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_groups(self, id, group_id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_users(self, id, user_id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_accounts(self, account_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, settings_file_url=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - migration_type - The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        data["migration_type"] = migration_type
        # OPTIONAL - pre_attachment[name] - Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name
        # OPTIONAL - pre_attachment[*] - Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*
        # OPTIONAL - settings[file_url] - A URL to download the file from. Must not require authentication.
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url
        # OPTIONAL - settings[source_course_id] - The course to copy from for a course copy migration. (required if doing course copy)
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id
        # OPTIONAL - settings[folder_id] - The folder to unzip the .zip file into for a zip_file_import.
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id
        # OPTIONAL - settings[overwrite_quizzes] - Whether to overwrite quizzes with the same identifiers between content packages.
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes
        # OPTIONAL - settings[question_bank_id] - The existing question bank ID to import questions into if not specified in the content package.
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id
        # OPTIONAL - settings[question_bank_name] - The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name
        # OPTIONAL - date_shift_options[shift_dates] - Whether to shift dates in the copied course
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates
        # OPTIONAL - date_shift_options[old_start_date] - The original start date of the source content/course
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date
        # OPTIONAL - date_shift_options[old_end_date] - The original end date of the source content/course
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date
        # OPTIONAL - date_shift_options[new_start_date] - The new start date for the content/course
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date
        # OPTIONAL - date_shift_options[new_end_date] - The new end date for the source content/course
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date
        # OPTIONAL - date_shift_options[day_substitutions][X] - Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X
        # OPTIONAL - date_shift_options[remove_dates] - Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*.
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates

        self.logger.debug("POST /api/v1/accounts/{account_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_courses(self, course_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, settings_file_url=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - migration_type - The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        data["migration_type"] = migration_type
        # OPTIONAL - pre_attachment[name] - Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name
        # OPTIONAL - pre_attachment[*] - Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*
        # OPTIONAL - settings[file_url] - A URL to download the file from. Must not require authentication.
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url
        # OPTIONAL - settings[source_course_id] - The course to copy from for a course copy migration. (required if doing course copy)
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id
        # OPTIONAL - settings[folder_id] - The folder to unzip the .zip file into for a zip_file_import.
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id
        # OPTIONAL - settings[overwrite_quizzes] - Whether to overwrite quizzes with the same identifiers between content packages.
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes
        # OPTIONAL - settings[question_bank_id] - The existing question bank ID to import questions into if not specified in the content package.
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id
        # OPTIONAL - settings[question_bank_name] - The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name
        # OPTIONAL - date_shift_options[shift_dates] - Whether to shift dates in the copied course
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates
        # OPTIONAL - date_shift_options[old_start_date] - The original start date of the source content/course
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date
        # OPTIONAL - date_shift_options[old_end_date] - The original end date of the source content/course
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date
        # OPTIONAL - date_shift_options[new_start_date] - The new start date for the content/course
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date
        # OPTIONAL - date_shift_options[new_end_date] - The new end date for the source content/course
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date
        # OPTIONAL - date_shift_options[day_substitutions][X] - Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X
        # OPTIONAL - date_shift_options[remove_dates] - Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*.
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates

        self.logger.debug("POST /api/v1/courses/{course_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_groups(self, group_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, settings_file_url=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - migration_type - The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        data["migration_type"] = migration_type
        # OPTIONAL - pre_attachment[name] - Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name
        # OPTIONAL - pre_attachment[*] - Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*
        # OPTIONAL - settings[file_url] - A URL to download the file from. Must not require authentication.
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url
        # OPTIONAL - settings[source_course_id] - The course to copy from for a course copy migration. (required if doing course copy)
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id
        # OPTIONAL - settings[folder_id] - The folder to unzip the .zip file into for a zip_file_import.
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id
        # OPTIONAL - settings[overwrite_quizzes] - Whether to overwrite quizzes with the same identifiers between content packages.
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes
        # OPTIONAL - settings[question_bank_id] - The existing question bank ID to import questions into if not specified in the content package.
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id
        # OPTIONAL - settings[question_bank_name] - The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name
        # OPTIONAL - date_shift_options[shift_dates] - Whether to shift dates in the copied course
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates
        # OPTIONAL - date_shift_options[old_start_date] - The original start date of the source content/course
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date
        # OPTIONAL - date_shift_options[old_end_date] - The original end date of the source content/course
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date
        # OPTIONAL - date_shift_options[new_start_date] - The new start date for the content/course
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date
        # OPTIONAL - date_shift_options[new_end_date] - The new end date for the source content/course
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date
        # OPTIONAL - date_shift_options[day_substitutions][X] - Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X
        # OPTIONAL - date_shift_options[remove_dates] - Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*.
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates

        self.logger.debug("POST /api/v1/groups/{group_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_users(self, user_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, settings_file_url=None, settings_folder_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - migration_type - The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        data["migration_type"] = migration_type
        # OPTIONAL - pre_attachment[name] - Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name
        # OPTIONAL - pre_attachment[*] - Other file upload properties, See {file:file_uploads.html File Upload Documentation}
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*
        # OPTIONAL - settings[file_url] - A URL to download the file from. Must not require authentication.
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url
        # OPTIONAL - settings[source_course_id] - The course to copy from for a course copy migration. (required if doing course copy)
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id
        # OPTIONAL - settings[folder_id] - The folder to unzip the .zip file into for a zip_file_import.
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id
        # OPTIONAL - settings[overwrite_quizzes] - Whether to overwrite quizzes with the same identifiers between content packages.
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes
        # OPTIONAL - settings[question_bank_id] - The existing question bank ID to import questions into if not specified in the content package.
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id
        # OPTIONAL - settings[question_bank_name] - The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence.
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name
        # OPTIONAL - date_shift_options[shift_dates] - Whether to shift dates in the copied course
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates
        # OPTIONAL - date_shift_options[old_start_date] - The original start date of the source content/course
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date
        # OPTIONAL - date_shift_options[old_end_date] - The original end date of the source content/course
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date
        # OPTIONAL - date_shift_options[new_start_date] - The new start date for the content/course
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date
        # OPTIONAL - date_shift_options[new_end_date] - The new end date for the source content/course
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date
        # OPTIONAL - date_shift_options[day_substitutions][X] - Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X
        # OPTIONAL - date_shift_options[remove_dates] - Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*.
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates

        self.logger.debug("POST /api/v1/users/{user_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_accounts(self, id, account_id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as create except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem. If the
        first upload has a problem you can supply new _pre_attachment_ values to
        start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_courses(self, id, course_id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as create except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem. If the
        first upload has a problem you can supply new _pre_attachment_ values to
        start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/courses/{course_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_groups(self, id, group_id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as create except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem. If the
        first upload has a problem you can supply new _pre_attachment_ values to
        start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/groups/{group_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_users(self, id, user_id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as create except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem. If the
        first upload has a problem you can supply new _pre_attachment_ values to
        start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/users/{user_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def list_migration_systems_accounts(self, account_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id - ID
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_courses(self, course_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_groups(self, group_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_users(self, user_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id - ID
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)


class Contentmigration(BaseModel):
    """Contentmigration Model."""

    def __init__(self, progress_url=None, user_id=None, workflow_state=None, migration_type_title=None, finished_at=None, migration_type=None, migration_issues_url=None, pre_attachment=None, attachment=None, started_at=None, id=None):
        """Init method for Contentmigration class."""
        self._progress_url = progress_url
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._migration_type_title = migration_type_title
        self._finished_at = finished_at
        self._migration_type = migration_type
        self._migration_issues_url = migration_issues_url
        self._pre_attachment = pre_attachment
        self._attachment = attachment
        self._started_at = started_at
        self._id = id

        self.logger = logging.getLogger('pycanvas.Contentmigration')

    @property
    def progress_url(self):
        """The api endpoint for polling the current progress."""
        return self._progress_url

    @progress_url.setter
    def progress_url(self, value):
        """Setter for progress_url property."""
        self.logger.warn("Setting values on progress_url will NOT update the remote Canvas instance.")
        self._progress_url = value

    @property
    def user_id(self):
        """The user who started the migration."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def migration_type_title(self):
        """the name of the content migration type."""
        return self._migration_type_title

    @migration_type_title.setter
    def migration_type_title(self, value):
        """Setter for migration_type_title property."""
        self.logger.warn("Setting values on migration_type_title will NOT update the remote Canvas instance.")
        self._migration_type_title = value

    @property
    def finished_at(self):
        """timestamp."""
        return self._finished_at

    @finished_at.setter
    def finished_at(self, value):
        """Setter for finished_at property."""
        self.logger.warn("Setting values on finished_at will NOT update the remote Canvas instance.")
        self._finished_at = value

    @property
    def migration_type(self):
        """the type of content migration."""
        return self._migration_type

    @migration_type.setter
    def migration_type(self, value):
        """Setter for migration_type property."""
        self.logger.warn("Setting values on migration_type will NOT update the remote Canvas instance.")
        self._migration_type = value

    @property
    def migration_issues_url(self):
        """API url to the content migration's issues."""
        return self._migration_issues_url

    @migration_issues_url.setter
    def migration_issues_url(self, value):
        """Setter for migration_issues_url property."""
        self.logger.warn("Setting values on migration_issues_url will NOT update the remote Canvas instance.")
        self._migration_issues_url = value

    @property
    def pre_attachment(self):
        """file uploading data, see {file:file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call."""
        return self._pre_attachment

    @pre_attachment.setter
    def pre_attachment(self, value):
        """Setter for pre_attachment property."""
        self.logger.warn("Setting values on pre_attachment will NOT update the remote Canvas instance.")
        self._pre_attachment = value

    @property
    def attachment(self):
        """attachment api object for the uploaded file may not be present for all migrations."""
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        """Setter for attachment property."""
        self.logger.warn("Setting values on attachment will NOT update the remote Canvas instance.")
        self._attachment = value

    @property
    def started_at(self):
        """timestamp."""
        return self._started_at

    @started_at.setter
    def started_at(self, value):
        """Setter for started_at property."""
        self.logger.warn("Setting values on started_at will NOT update the remote Canvas instance.")
        self._started_at = value

    @property
    def id(self):
        """the unique identifier for the migration."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Migrationissue(BaseModel):
    """Migrationissue Model."""

    def __init__(self, error_message=None, description=None, workflow_state=None, created_at=None, fix_issue_html_url=None, updated_at=None, issue_type=None, content_migration_url=None, error_report_html_url=None, id=None):
        """Init method for Migrationissue class."""
        self._error_message = error_message
        self._description = description
        self._workflow_state = workflow_state
        self._created_at = created_at
        self._fix_issue_html_url = fix_issue_html_url
        self._updated_at = updated_at
        self._issue_type = issue_type
        self._content_migration_url = content_migration_url
        self._error_report_html_url = error_report_html_url
        self._id = id

        self.logger = logging.getLogger('pycanvas.Migrationissue')

    @property
    def error_message(self):
        """Site administrator error message (If the requesting user has permissions)."""
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        """Setter for error_message property."""
        self.logger.warn("Setting values on error_message will NOT update the remote Canvas instance.")
        self._error_message = value

    @property
    def description(self):
        """Description of the issue for the end-user."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def workflow_state(self):
        """Current state of the issue: active, resolved."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def created_at(self):
        """timestamp."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def fix_issue_html_url(self):
        """HTML Url to the Canvas page to investigate the issue."""
        return self._fix_issue_html_url

    @fix_issue_html_url.setter
    def fix_issue_html_url(self, value):
        """Setter for fix_issue_html_url property."""
        self.logger.warn("Setting values on fix_issue_html_url will NOT update the remote Canvas instance.")
        self._fix_issue_html_url = value

    @property
    def updated_at(self):
        """timestamp."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def issue_type(self):
        """Severity of the issue: todo, warning, error."""
        return self._issue_type

    @issue_type.setter
    def issue_type(self, value):
        """Setter for issue_type property."""
        self.logger.warn("Setting values on issue_type will NOT update the remote Canvas instance.")
        self._issue_type = value

    @property
    def content_migration_url(self):
        """API url to the content migration."""
        return self._content_migration_url

    @content_migration_url.setter
    def content_migration_url(self, value):
        """Setter for content_migration_url property."""
        self.logger.warn("Setting values on content_migration_url will NOT update the remote Canvas instance.")
        self._content_migration_url = value

    @property
    def error_report_html_url(self):
        """Link to a Canvas error report if present (If the requesting user has permissions)."""
        return self._error_report_html_url

    @error_report_html_url.setter
    def error_report_html_url(self, value):
        """Setter for error_report_html_url property."""
        self.logger.warn("Setting values on error_report_html_url will NOT update the remote Canvas instance.")
        self._error_report_html_url = value

    @property
    def id(self):
        """the unique identifier for the issue."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Migrator(BaseModel):
    """Migrator Model."""

    def __init__(self, required_settings=None, type=None, name=None, requires_file_upload=None):
        """Init method for Migrator class."""
        self._required_settings = required_settings
        self._type = type
        self._name = name
        self._requires_file_upload = requires_file_upload

        self.logger = logging.getLogger('pycanvas.Migrator')

    @property
    def required_settings(self):
        """A list of fields this system requires."""
        return self._required_settings

    @required_settings.setter
    def required_settings(self, value):
        """Setter for required_settings property."""
        self.logger.warn("Setting values on required_settings will NOT update the remote Canvas instance.")
        self._required_settings = value

    @property
    def type(self):
        """The value to pass to the create endpoint."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def name(self):
        """Description of the package type expected."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def requires_file_upload(self):
        """Whether this endpoint requires a file upload."""
        return self._requires_file_upload

    @requires_file_upload.setter
    def requires_file_upload(self, value):
        """Setter for requires_file_upload property."""
        self.logger.warn("Setting values on requires_file_upload will NOT update the remote Canvas instance.")
        self._requires_file_upload = value

