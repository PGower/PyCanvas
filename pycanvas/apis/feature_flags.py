"""FeatureFlags API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class FeatureFlagsAPI(BaseCanvasAPI):
    """FeatureFlags API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for FeatureFlagsAPI."""
        super(FeatureFlagsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.FeatureFlagsAPI")

    def list_features_courses(self, course_id):
        """
        List features.

        List all features that apply to a given Account, Course, or User.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/features with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/features".format(**path), data=data, params=params, all_pages=True)

    def list_features_accounts(self, account_id):
        """
        List features.

        List all features that apply to a given Account, Course, or User.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/features with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/features".format(**path), data=data, params=params, all_pages=True)

    def list_features_users(self, user_id):
        """
        List features.

        List all features that apply to a given Account, Course, or User.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/features with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/features".format(**path), data=data, params=params, all_pages=True)

    def list_enabled_features_courses(self, course_id):
        """
        List enabled features.

        List all features that are enabled on a given Account, Course, or User.
        Only the feature names are returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/features/enabled with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/features/enabled".format(**path), data=data, params=params, no_data=True)

    def list_enabled_features_accounts(self, account_id):
        """
        List enabled features.

        List all features that are enabled on a given Account, Course, or User.
        Only the feature names are returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/features/enabled with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/features/enabled".format(**path), data=data, params=params, no_data=True)

    def list_enabled_features_users(self, user_id):
        """
        List enabled features.

        List all features that are enabled on a given Account, Course, or User.
        Only the feature names are returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/features/enabled with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/features/enabled".format(**path), data=data, params=params, no_data=True)

    def get_feature_flag_courses(self, feature, course_id):
        """
        Get feature flag.

        Get the feature flag that applies to a given Account, Course, or User.
        The flag may be defined on the object, or it may be inherited from a parent
        account. You can look at the context_id and context_type of the returned object
        to determine which is the case. If these fields are missing, then the object
        is the global Canvas default.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("GET /api/v1/courses/{course_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def get_feature_flag_accounts(self, feature, account_id):
        """
        Get feature flag.

        Get the feature flag that applies to a given Account, Course, or User.
        The flag may be defined on the object, or it may be inherited from a parent
        account. You can look at the context_id and context_type of the returned object
        to determine which is the case. If these fields are missing, then the object
        is the global Canvas default.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("GET /api/v1/accounts/{account_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def get_feature_flag_users(self, user_id, feature):
        """
        Get feature flag.

        Get the feature flag that applies to a given Account, Course, or User.
        The flag may be defined on the object, or it may be inherited from a parent
        account. You can look at the context_id and context_type of the returned object
        to determine which is the case. If these fields are missing, then the object
        is the global Canvas default.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("GET /api/v1/users/{user_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def set_feature_flag_courses(self, feature, course_id, state=None):
        """
        Set feature flag.

        Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
        a feature flag for the same feature in any state other than "allowed".
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        # OPTIONAL - state
        """"off":: The feature is not available for the course, user, or account and sub-accounts.
        "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
                    sub-accounts and courses by setting a feature flag on the sub-account or course.
        "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts."""
        if state is not None:
            self._validate_enum(state, ["off", "allowed", "on"])
            data["state"] = state

        self.logger.debug("PUT /api/v1/courses/{course_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def set_feature_flag_accounts(self, feature, account_id, state=None):
        """
        Set feature flag.

        Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
        a feature flag for the same feature in any state other than "allowed".
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        # OPTIONAL - state
        """"off":: The feature is not available for the course, user, or account and sub-accounts.
        "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
                    sub-accounts and courses by setting a feature flag on the sub-account or course.
        "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts."""
        if state is not None:
            self._validate_enum(state, ["off", "allowed", "on"])
            data["state"] = state

        self.logger.debug("PUT /api/v1/accounts/{account_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def set_feature_flag_users(self, user_id, feature, state=None):
        """
        Set feature flag.

        Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
        a feature flag for the same feature in any state other than "allowed".
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        # OPTIONAL - state
        """"off":: The feature is not available for the course, user, or account and sub-accounts.
        "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in
                    sub-accounts and courses by setting a feature flag on the sub-account or course.
        "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts."""
        if state is not None:
            self._validate_enum(state, ["off", "allowed", "on"])
            data["state"] = state

        self.logger.debug("PUT /api/v1/users/{user_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def remove_feature_flag_courses(self, feature, course_id):
        """
        Remove feature flag.

        Remove feature flag for a given Account, Course, or User.  (Note that the flag must
        be defined on the Account, Course, or User directly.)  The object will then inherit
        the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
        then lower-level account flags that were masked by this one will apply again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("DELETE /api/v1/courses/{course_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def remove_feature_flag_accounts(self, feature, account_id):
        """
        Remove feature flag.

        Remove feature flag for a given Account, Course, or User.  (Note that the flag must
        be defined on the Account, Course, or User directly.)  The object will then inherit
        the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
        then lower-level account flags that were masked by this one will apply again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)

    def remove_feature_flag_users(self, user_id, feature):
        """
        Remove feature flag.

        Remove feature flag for a given Account, Course, or User.  (Note that the flag must
        be defined on the Account, Course, or User directly.)  The object will then inherit
        the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
        then lower-level account flags that were masked by this one will apply again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - feature
        """ID"""
        path["feature"] = feature

        self.logger.debug("DELETE /api/v1/users/{user_id}/features/flags/{feature} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/features/flags/{feature}".format(**path), data=data, params=params, single_item=True)


class Featureflag(BaseModel):
    """Featureflag Model."""

    def __init__(self, context_type=None, context_id=None, state=None, locked=None, feature=None):
        """Init method for Featureflag class."""
        self._context_type = context_type
        self._context_id = context_id
        self._state = state
        self._locked = locked
        self._feature = feature

        self.logger = logging.getLogger('pycanvas.Featureflag')

    @property
    def context_type(self):
        """The type of object to which this flag applies (Account, Course, or User). (This field is not present if this FeatureFlag represents the global Canvas default)."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """The id of the object to which this flag applies (This field is not present if this FeatureFlag represents the global Canvas default)."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def state(self):
        """The policy for the feature at this context.  can be 'off', 'allowed', or 'on'."""
        return self._state

    @state.setter
    def state(self, value):
        """Setter for state property."""
        self.logger.warn("Setting values on state will NOT update the remote Canvas instance.")
        self._state = value

    @property
    def locked(self):
        """If set, this feature flag cannot be changed in the caller's context because the flag is set 'off' or 'on' in a higher context."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def feature(self):
        """The feature this flag controls."""
        return self._feature

    @feature.setter
    def feature(self, value):
        """Setter for feature property."""
        self.logger.warn("Setting values on feature will NOT update the remote Canvas instance.")
        self._feature = value


class Feature(BaseModel):
    """Feature Model."""

    def __init__(self, development=None, display_name=None, name=None, autoexpand=None, enable_at=None, beta=None, feature_flag=None, applies_to=None, root_opt_in=None, release_notes_url=None):
        """Init method for Feature class."""
        self._development = development
        self._display_name = display_name
        self._name = name
        self._autoexpand = autoexpand
        self._enable_at = enable_at
        self._beta = beta
        self._feature_flag = feature_flag
        self._applies_to = applies_to
        self._root_opt_in = root_opt_in
        self._release_notes_url = release_notes_url

        self.logger = logging.getLogger('pycanvas.Feature')

    @property
    def development(self):
        """Whether the feature is in active development. Features in this state are only visible in test and beta instances and are not yet available for production use."""
        return self._development

    @development.setter
    def development(self, value):
        """Setter for development property."""
        self.logger.warn("Setting values on development will NOT update the remote Canvas instance.")
        self._development = value

    @property
    def display_name(self):
        """The user-visible name of the feature."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def name(self):
        """The symbolic name of the feature, used in FeatureFlags."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def autoexpand(self):
        """Whether the details of the feature are autoexpanded on page load vs. the user clicking to expand."""
        return self._autoexpand

    @autoexpand.setter
    def autoexpand(self, value):
        """Setter for autoexpand property."""
        self.logger.warn("Setting values on autoexpand will NOT update the remote Canvas instance.")
        self._autoexpand = value

    @property
    def enable_at(self):
        """The date this feature will be globally enabled, or null if this is not planned. (This information is subject to change.)."""
        return self._enable_at

    @enable_at.setter
    def enable_at(self, value):
        """Setter for enable_at property."""
        self.logger.warn("Setting values on enable_at will NOT update the remote Canvas instance.")
        self._enable_at = value

    @property
    def beta(self):
        """Whether the feature is a beta feature. If true, the feature may not be fully polished and may be subject to change in the future."""
        return self._beta

    @beta.setter
    def beta(self, value):
        """Setter for beta property."""
        self.logger.warn("Setting values on beta will NOT update the remote Canvas instance.")
        self._beta = value

    @property
    def feature_flag(self):
        """The FeatureFlag that applies to the caller."""
        return self._feature_flag

    @feature_flag.setter
    def feature_flag(self, value):
        """Setter for feature_flag property."""
        self.logger.warn("Setting values on feature_flag will NOT update the remote Canvas instance.")
        self._feature_flag = value

    @property
    def applies_to(self):
        """The type of object the feature applies to (RootAccount, Account, Course, or User):
 * RootAccount features may only be controlled by flags on root accounts.
 * Account features may be controlled by flags on accounts and their parent accounts.
 * Course features may be controlled by flags on courses and their parent accounts.
 * User features may be controlled by flags on users and site admin only."""
        return self._applies_to

    @applies_to.setter
    def applies_to(self, value):
        """Setter for applies_to property."""
        self.logger.warn("Setting values on applies_to will NOT update the remote Canvas instance.")
        self._applies_to = value

    @property
    def root_opt_in(self):
        """If true, a feature that is 'allowed' globally will be 'off' by default in root accounts. Otherwise, root accounts inherit the global 'allowed' setting, which allows sub-accounts and courses to turn features on with no root account action."""
        return self._root_opt_in

    @root_opt_in.setter
    def root_opt_in(self, value):
        """Setter for root_opt_in property."""
        self.logger.warn("Setting values on root_opt_in will NOT update the remote Canvas instance.")
        self._root_opt_in = value

    @property
    def release_notes_url(self):
        """A URL to the release notes describing the feature."""
        return self._release_notes_url

    @release_notes_url.setter
    def release_notes_url(self, value):
        """Setter for release_notes_url property."""
        self.logger.warn("Setting values on release_notes_url will NOT update the remote Canvas instance.")
        self._release_notes_url = value

