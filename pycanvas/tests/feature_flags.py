"""FeatureFlags API Tests for Version 1.0.

This is a testing template for the generated FeatureFlagsAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.feature_flags import FeatureFlagsAPI
from pycanvas.apis.feature_flags import Featureflag
from pycanvas.apis.feature_flags import Feature


class TestFeatureFlagsAPI(unittest.TestCase):
    """Tests for the FeatureFlagsAPI."""

    def setUp(self):
        self.client = FeatureFlagsAPI(secrets.instance_address, secrets.access_token)

    def test_list_features_courses(self):
        """Integration test for the FeatureFlagsAPI.list_features_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_features_courses(course_id)

    def test_list_features_accounts(self):
        """Integration test for the FeatureFlagsAPI.list_features_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_features_accounts(account_id)

    def test_list_features_users(self):
        """Integration test for the FeatureFlagsAPI.list_features_users method."""
        user_id = None  # Change me!!

        r = self.client.list_features_users(user_id)

    def test_list_enabled_features_courses(self):
        """Integration test for the FeatureFlagsAPI.list_enabled_features_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_enabled_features_courses(course_id)

    def test_list_enabled_features_accounts(self):
        """Integration test for the FeatureFlagsAPI.list_enabled_features_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_enabled_features_accounts(account_id)

    def test_list_enabled_features_users(self):
        """Integration test for the FeatureFlagsAPI.list_enabled_features_users method."""
        user_id = None  # Change me!!

        r = self.client.list_enabled_features_users(user_id)

    def test_get_feature_flag_courses(self):
        """Integration test for the FeatureFlagsAPI.get_feature_flag_courses method."""
        course_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.get_feature_flag_courses(feature, course_id)

    def test_get_feature_flag_accounts(self):
        """Integration test for the FeatureFlagsAPI.get_feature_flag_accounts method."""
        account_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.get_feature_flag_accounts(feature, account_id)

    def test_get_feature_flag_users(self):
        """Integration test for the FeatureFlagsAPI.get_feature_flag_users method."""
        user_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.get_feature_flag_users(user_id, feature)

    def test_set_feature_flag_courses(self):
        """Integration test for the FeatureFlagsAPI.set_feature_flag_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_feature_flag_accounts(self):
        """Integration test for the FeatureFlagsAPI.set_feature_flag_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_feature_flag_users(self):
        """Integration test for the FeatureFlagsAPI.set_feature_flag_users method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_feature_flag_courses(self):
        """Integration test for the FeatureFlagsAPI.remove_feature_flag_courses method."""
        course_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.remove_feature_flag_courses(feature, course_id)

    def test_remove_feature_flag_accounts(self):
        """Integration test for the FeatureFlagsAPI.remove_feature_flag_accounts method."""
        account_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.remove_feature_flag_accounts(feature, account_id)

    def test_remove_feature_flag_users(self):
        """Integration test for the FeatureFlagsAPI.remove_feature_flag_users method."""
        user_id = None  # Change me!!
        feature = None  # Change me!!

        r = self.client.remove_feature_flag_users(user_id, feature)

