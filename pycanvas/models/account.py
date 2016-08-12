# coding: utf-8
from .base import BaseModel


class Account(BaseModel):
    """Canvas API Account  Model."""

    attribute_types = {
        'id': 'int',
        'name': 'str',
        'parent_account_id': 'int',
        'root_account_id': 'int',
        'default_storage_quota_mb': 'int',
        'default_user_storage_quota_mb': 'int',
        'default_group_storage_quota_mb': 'int',
        'default_time_zone': 'str',
        'sis_account_id': 'str',
        'integration_id': 'str',
        'sis_import_id': 'int',
        'lti_guid': 'str',
        'workflow_state': 'str'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 parent_account_id=None,
                 root_account_id=None,
                 default_storage_quota_mb=None,
                 default_user_storage_quota_mb=None,
                 default_group_storage_quota_mb=None,
                 default_time_zone=None, sis_account_id=None,
                 integration_id=None,
                 sis_import_id=None,
                 lti_guid=None,
                 workflow_state=None):
        """A Canvas Account Model."""
        self.id = id
        self.name = name
        self.parent_account_id = parent_account_id
        self.root_account_id = root_account_id
        self.default_storage_quota_mb = default_storage_quota_mb
        self.default_user_storage_quota_mb = default_user_storage_quota_mb
        self.default_group_storage_quota_mb = default_group_storage_quota_mb
        self.default_time_zone = default_time_zone
        self.sis_account_id = sis_account_id
        self.integration_id = integration_id
        self.sis_import_id = sis_import_id
        self.lti_guid = lti_guid
        self.workflow_state = workflow_state


# self._attribute_map = {
    #     'id': 'id',
    #     'name': 'name',
    #     'parent_account_id': 'parent_account_id',
    #     'root_account_id': 'root_account_id',
    #     'default_storage_quota_mb': 'default_storage_quota_mb',
    #     'default_user_storage_quota_mb': 'default_user_storage_quota_mb',
    #     'default_group_storage_quota_mb': 'default_group_storage_quota_mb',
    #     'default_time_zone': 'default_time_zone',
    #     'sis_account_id': 'sis_account_id',
    #     'integration_id': 'integration_id',
    #     'sis_import_id': 'sis_import_id',
    #     'lti_guid': 'lti_guid',
    #     'workflow_state': 'workflow_state'
    # }