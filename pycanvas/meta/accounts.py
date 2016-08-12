from base import BaseMetadata

class AccountsServiceMetadata(BaseMetadata):
    def list_accounts(self):
        method = 'GET'



class AccountModelMetadata(BaseMetadata):
    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_account_id': 'parent_account_id',
        'root_account_id': 'root_account_id',
        'default_storage_quota_mb': 'default_storage_quota_mb',
        'default_user_storage_quota_mb': 'default_user_storage_quota_mb',
        'default_group_storage_quota_mb': 'default_group_storage_quota_mb',
        'default_time_zone': 'default_time_zone',
        'sis_account_id': 'sis_account_id',
        'integration_id': 'integration_id',
        'sis_import_id': 'sis_import_id',
        'lti_guid': 'lti_guid',
        'workflow_state': 'workflow_state'
    }

    attribute_types = {
        'id': int,
        'name': str,
        'parent_account_id': int,
        'root_account_id': int,
        'default_storage_quota_mb': int,
        'default_user_storage_quota_mb': int,
        'default_group_storage_quota_mb': int,
        'default_time_zone': str,
        'sis_account_id': str,
        'integration_id': str,
        'sis_import_id': int,
        'lti_guid': str,
        'workflow_state': str
    }


