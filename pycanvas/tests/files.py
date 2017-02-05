"""Files API Tests for Version 1.0.

This is a testing template for the generated FilesAPI Class.
"""
import unittest
import requests
import secrets
from pycanvas.apis.files import FilesAPI
from pycanvas.apis.files import Folder
from pycanvas.apis.files import Usagerights
from pycanvas.apis.files import License
from pycanvas.apis.files import File


class TestFilesAPI(unittest.TestCase):
    """Tests for the FilesAPI."""

    def setUp(self):
        self.client = FilesAPI(secrets.instance_address, secrets.access_token)

    def test_get_quota_information_courses(self):
        """Integration test for the FilesAPI.get_quota_information_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_quota_information_courses(course_id)

    def test_get_quota_information_groups(self):
        """Integration test for the FilesAPI.get_quota_information_groups method."""
        group_id = None  # Change me!!

        r = self.client.get_quota_information_groups(group_id)

    def test_get_quota_information_users(self):
        """Integration test for the FilesAPI.get_quota_information_users method."""
        user_id = None  # Change me!!

        r = self.client.get_quota_information_users(user_id)

    def test_list_files_courses(self):
        """Integration test for the FilesAPI.list_files_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_files_courses(course_id, content_types=None, include=None, order=None, search_term=None, sort=None)

    def test_list_files_users(self):
        """Integration test for the FilesAPI.list_files_users method."""
        user_id = None  # Change me!!

        r = self.client.list_files_users(user_id, content_types=None, include=None, order=None, search_term=None, sort=None)

    def test_list_files_groups(self):
        """Integration test for the FilesAPI.list_files_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_files_groups(group_id, content_types=None, include=None, order=None, search_term=None, sort=None)

    def test_list_files_folders(self):
        """Integration test for the FilesAPI.list_files_folders method."""
        id = None  # Change me!!

        r = self.client.list_files_folders(id, content_types=None, include=None, order=None, search_term=None, sort=None)

    def test_get_quota_information(self):
        """Integration test for the FilesAPI.get_quota_information method."""
        id = None  # Change me!!

        r = self.client.get_quota_information(id)

    def test_get_file(self):
        """Integration test for the FilesAPI.get_file method."""
        id = None  # Change me!!

        r = self.client.get_file(id, include=None)

    def test_update_file(self):
        """Integration test for the FilesAPI.update_file method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_file(self):
        """Integration test for the FilesAPI.delete_file method."""
        id = None  # Change me!!

        r = self.client.delete_file(id)

    def test_list_folders(self):
        """Integration test for the FilesAPI.list_folders method."""
        id = None  # Change me!!

        r = self.client.list_folders(id)

    def test_list_all_folders_courses(self):
        """Integration test for the FilesAPI.list_all_folders_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_all_folders_courses(course_id)

    def test_list_all_folders_users(self):
        """Integration test for the FilesAPI.list_all_folders_users method."""
        user_id = None  # Change me!!

        r = self.client.list_all_folders_users(user_id)

    def test_list_all_folders_groups(self):
        """Integration test for the FilesAPI.list_all_folders_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_all_folders_groups(group_id)

    def test_resolve_path_courses_full_path(self):
        """Integration test for the FilesAPI.resolve_path_courses_full_path method."""
        course_id = None  # Change me!!

        r = self.client.resolve_path_courses_full_path(course_id)

    def test_resolve_path_courses(self):
        """Integration test for the FilesAPI.resolve_path_courses method."""
        course_id = None  # Change me!!

        r = self.client.resolve_path_courses(course_id)

    def test_resolve_path_users_full_path(self):
        """Integration test for the FilesAPI.resolve_path_users_full_path method."""
        user_id = None  # Change me!!

        r = self.client.resolve_path_users_full_path(user_id)

    def test_resolve_path_users(self):
        """Integration test for the FilesAPI.resolve_path_users method."""
        user_id = None  # Change me!!

        r = self.client.resolve_path_users(user_id)

    def test_resolve_path_groups_full_path(self):
        """Integration test for the FilesAPI.resolve_path_groups_full_path method."""
        group_id = None  # Change me!!

        r = self.client.resolve_path_groups_full_path(group_id)

    def test_resolve_path_groups(self):
        """Integration test for the FilesAPI.resolve_path_groups method."""
        group_id = None  # Change me!!

        r = self.client.resolve_path_groups(group_id)

    def test_get_folder_courses(self):
        """Integration test for the FilesAPI.get_folder_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_folder_courses(id, course_id)

    def test_get_folder_users(self):
        """Integration test for the FilesAPI.get_folder_users method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_folder_users(id, user_id)

    def test_get_folder_groups(self):
        """Integration test for the FilesAPI.get_folder_groups method."""
        group_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_folder_groups(id, group_id)

    def test_get_folder_folders(self):
        """Integration test for the FilesAPI.get_folder_folders method."""
        id = None  # Change me!!

        r = self.client.get_folder_folders(id)

    def test_update_folder(self):
        """Integration test for the FilesAPI.update_folder method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_folder_courses(self):
        """Integration test for the FilesAPI.create_folder_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_folder_users(self):
        """Integration test for the FilesAPI.create_folder_users method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_folder_groups(self):
        """Integration test for the FilesAPI.create_folder_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_folder_folders(self):
        """Integration test for the FilesAPI.create_folder_folders method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_folder(self):
        """Integration test for the FilesAPI.delete_folder method."""
        id = None  # Change me!!

        r = self.client.delete_folder(id, force=None)

    def test_upload_file(self):
        """Integration test for the FilesAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_copy_file(self):
        """Integration test for the FilesAPI.copy_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_copy_folder(self):
        """Integration test for the FilesAPI.copy_folder method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_usage_rights_courses(self):
        """Integration test for the FilesAPI.set_usage_rights_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_usage_rights_groups(self):
        """Integration test for the FilesAPI.set_usage_rights_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_usage_rights_users(self):
        """Integration test for the FilesAPI.set_usage_rights_users method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_usage_rights_courses(self):
        """Integration test for the FilesAPI.remove_usage_rights_courses method."""
        course_id = None  # Change me!!
        file_ids = None  # Change me!!

        r = self.client.remove_usage_rights_courses(file_ids, course_id, folder_ids=None)

    def test_remove_usage_rights_groups(self):
        """Integration test for the FilesAPI.remove_usage_rights_groups method."""
        group_id = None  # Change me!!
        file_ids = None  # Change me!!

        r = self.client.remove_usage_rights_groups(group_id, file_ids, folder_ids=None)

    def test_remove_usage_rights_users(self):
        """Integration test for the FilesAPI.remove_usage_rights_users method."""
        user_id = None  # Change me!!
        file_ids = None  # Change me!!

        r = self.client.remove_usage_rights_users(user_id, file_ids, folder_ids=None)

    def test_list_licenses_courses(self):
        """Integration test for the FilesAPI.list_licenses_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_licenses_courses(course_id)

    def test_list_licenses_groups(self):
        """Integration test for the FilesAPI.list_licenses_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_licenses_groups(group_id)

    def test_list_licenses_users(self):
        """Integration test for the FilesAPI.list_licenses_users method."""
        user_id = None  # Change me!!

        r = self.client.list_licenses_users(user_id)

