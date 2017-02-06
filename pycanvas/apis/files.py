"""Files API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class FilesAPI(BaseCanvasAPI):
    """Files API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for FilesAPI."""
        super(FilesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.FilesAPI")

    def get_quota_information_courses(self, course_id):
        """
        Get quota information.

        Returns the total and used storage quota for the course, group, or user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/files/quota with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/files/quota".format(**path), data=data, params=params, no_data=True)

    def get_quota_information_groups(self, group_id):
        """
        Get quota information.

        Returns the total and used storage quota for the course, group, or user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/files/quota with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/files/quota".format(**path), data=data, params=params, no_data=True)

    def get_quota_information_users(self, user_id):
        """
        Get quota information.

        Returns the total and used storage quota for the course, group, or user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/files/quota with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/files/quota".format(**path), data=data, params=params, no_data=True)

    def list_files_courses(self, course_id, content_types=None, include=None, only=None, order=None, search_term=None, sort=None):
        """
        List files.

        Returns the paginated list of files for the folder or course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - content_types
        """Filter results by content-type. You can specify type/subtype pairs (e.g.,
        'image/jpeg'), or simply types (e.g., 'image', which will match
        'image/gif', 'image/jpeg', etc.)."""
        if content_types is not None:
            params["content_types"] = content_types

        # OPTIONAL - search_term
        """The partial name of the files to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        # OPTIONAL - only
        """Array of information to restrict to. Overrides include[]
        
        "names":: only returns file name information"""
        if only is not None:
            params["only"] = only

        # OPTIONAL - sort
        """Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`."""
        if sort is not None:
            self._validate_enum(sort, ["name", "size", "created_at", "updated_at", "content_type", "user"])
            params["sort"] = sort

        # OPTIONAL - order
        """The sorting order. Defaults to 'asc'."""
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        self.logger.debug("GET /api/v1/courses/{course_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/files".format(**path), data=data, params=params, all_pages=True)

    def list_files_users(self, user_id, content_types=None, include=None, only=None, order=None, search_term=None, sort=None):
        """
        List files.

        Returns the paginated list of files for the folder or course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # OPTIONAL - content_types
        """Filter results by content-type. You can specify type/subtype pairs (e.g.,
        'image/jpeg'), or simply types (e.g., 'image', which will match
        'image/gif', 'image/jpeg', etc.)."""
        if content_types is not None:
            params["content_types"] = content_types

        # OPTIONAL - search_term
        """The partial name of the files to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        # OPTIONAL - only
        """Array of information to restrict to. Overrides include[]
        
        "names":: only returns file name information"""
        if only is not None:
            params["only"] = only

        # OPTIONAL - sort
        """Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`."""
        if sort is not None:
            self._validate_enum(sort, ["name", "size", "created_at", "updated_at", "content_type", "user"])
            params["sort"] = sort

        # OPTIONAL - order
        """The sorting order. Defaults to 'asc'."""
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        self.logger.debug("GET /api/v1/users/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/files".format(**path), data=data, params=params, all_pages=True)

    def list_files_groups(self, group_id, content_types=None, include=None, only=None, order=None, search_term=None, sort=None):
        """
        List files.

        Returns the paginated list of files for the folder or course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # OPTIONAL - content_types
        """Filter results by content-type. You can specify type/subtype pairs (e.g.,
        'image/jpeg'), or simply types (e.g., 'image', which will match
        'image/gif', 'image/jpeg', etc.)."""
        if content_types is not None:
            params["content_types"] = content_types

        # OPTIONAL - search_term
        """The partial name of the files to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        # OPTIONAL - only
        """Array of information to restrict to. Overrides include[]
        
        "names":: only returns file name information"""
        if only is not None:
            params["only"] = only

        # OPTIONAL - sort
        """Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`."""
        if sort is not None:
            self._validate_enum(sort, ["name", "size", "created_at", "updated_at", "content_type", "user"])
            params["sort"] = sort

        # OPTIONAL - order
        """The sorting order. Defaults to 'asc'."""
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        self.logger.debug("GET /api/v1/groups/{group_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/files".format(**path), data=data, params=params, all_pages=True)

    def list_files_folders(self, id, content_types=None, include=None, only=None, order=None, search_term=None, sort=None):
        """
        List files.

        Returns the paginated list of files for the folder or course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - content_types
        """Filter results by content-type. You can specify type/subtype pairs (e.g.,
        'image/jpeg'), or simply types (e.g., 'image', which will match
        'image/gif', 'image/jpeg', etc.)."""
        if content_types is not None:
            params["content_types"] = content_types

        # OPTIONAL - search_term
        """The partial name of the files to match and return."""
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        # OPTIONAL - only
        """Array of information to restrict to. Overrides include[]
        
        "names":: only returns file name information"""
        if only is not None:
            params["only"] = only

        # OPTIONAL - sort
        """Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`."""
        if sort is not None:
            self._validate_enum(sort, ["name", "size", "created_at", "updated_at", "content_type", "user"])
            params["sort"] = sort

        # OPTIONAL - order
        """The sorting order. Defaults to 'asc'."""
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        self.logger.debug("GET /api/v1/folders/{id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/folders/{id}/files".format(**path), data=data, params=params, all_pages=True)

    def get_public_inline_preview_url(self, id, submission_id=None):
        """
        Get public inline preview url.

        Determine the URL that should be used for inline preview of the file.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - submission_id
        """The id of the submission the file is associated with.  Provide this argument to gain access to a file
        that has been submitted to an assignment (Canvas will verify that the file belongs to the submission
        and the calling user has rights to view the submission)."""
        if submission_id is not None:
            params["submission_id"] = submission_id

        self.logger.debug("GET /api/v1/files/{id}/public_url with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/files/{id}/public_url".format(**path), data=data, params=params, no_data=True)

    def get_file_files(self, id, include=None):
        """
        Get file.

        Returns the standard attachment json object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/files/{id}".format(**path), data=data, params=params, single_item=True)

    def get_file_courses(self, id, course_id, include=None):
        """
        Get file.

        Returns the standard attachment json object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/files/{id}".format(**path), data=data, params=params, single_item=True)

    def get_file_groups(self, id, group_id, include=None):
        """
        Get file.

        Returns the standard attachment json object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/groups/{group_id}/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/files/{id}".format(**path), data=data, params=params, single_item=True)

    def get_file_users(self, id, user_id, include=None):
        """
        Get file.

        Returns the standard attachment json object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """Array of additional information to include.
        
        "user":: the user who uploaded the file or last edited its content
        "usage_rights":: copyright and license information for the file (see UsageRights)"""
        if include is not None:
            self._validate_enum(include, ["user"])
            params["include"] = include

        self.logger.debug("GET /api/v1/users/{user_id}/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/files/{id}".format(**path), data=data, params=params, single_item=True)

    def update_file(self, id, hidden=None, lock_at=None, locked=None, name=None, on_duplicate=None, parent_folder_id=None, unlock_at=None):
        """
        Update file.

        Update some settings on the specified file
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - name
        """The new display name of the file"""
        if name is not None:
            data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to move this file into.
        The new folder must be in the same context as the original parent folder.
        If the file is in a context without folders this does not apply."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - on_duplicate
        """If the file is moved to a folder containing a file with the same name,
        or renamed to a name matching an existing file, the API call will fail
        unless this parameter is supplied.
        
        "overwrite":: Replace the existing file with the same name
        "rename":: Add a qualifier to make the new filename unique"""
        if on_duplicate is not None:
            self._validate_enum(on_duplicate, ["overwrite", "rename"])
            data["on_duplicate"] = on_duplicate

        # OPTIONAL - lock_at
        """The datetime to lock the file at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the file at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the file as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the file as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        self.logger.debug("PUT /api/v1/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/files/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_file(self, id):
        """
        Delete file.

        Remove the specified file
        
          curl -XDELETE 'https://<canvas>/api/v1/files/<file_id>' \
               -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/files/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/files/{id}".format(**path), data=data, params=params, no_data=True)

    def list_folders(self, id):
        """
        List folders.

        Returns the paginated list of folders in the folder.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/folders/{id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/folders/{id}/folders".format(**path), data=data, params=params, all_pages=True)

    def list_all_folders_courses(self, course_id):
        """
        List all folders.

        Returns the paginated list of all folders for the given context. This will
        be returned as a flat list containing all subfolders as well.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/folders".format(**path), data=data, params=params, all_pages=True)

    def list_all_folders_users(self, user_id):
        """
        List all folders.

        Returns the paginated list of all folders for the given context. This will
        be returned as a flat list containing all subfolders as well.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/folders".format(**path), data=data, params=params, all_pages=True)

    def list_all_folders_groups(self, group_id):
        """
        List all folders.

        Returns the paginated list of all folders for the given context. This will
        be returned as a flat list containing all subfolders as well.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/folders".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_courses_full_path(self, course_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/folders/by_path/*full_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/folders/by_path/*full_path".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_courses(self, course_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/folders/by_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/folders/by_path".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_users_full_path(self, user_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/folders/by_path/*full_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/folders/by_path/*full_path".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_users(self, user_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/folders/by_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/folders/by_path".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_groups_full_path(self, group_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/folders/by_path/*full_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/folders/by_path/*full_path".format(**path), data=data, params=params, all_pages=True)

    def resolve_path_groups(self, group_id):
        """
        Resolve path.

        Given the full path to a folder, returns a list of all Folders in the path hierarchy,
        starting at the root folder, and ending at the requested folder. The given path is
        relative to the context's root folder and does not include the root folder's name
        (e.g., "course files"). If an empty path is given, the context's root folder alone
        is returned. Otherwise, if no folder exists with the given full path, a Not Found
        error is returned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/folders/by_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/folders/by_path".format(**path), data=data, params=params, all_pages=True)

    def get_folder_courses(self, id, course_id):
        """
        Get folder.

        Returns the details for a folder
        
        You can get the root folder from a context by using 'root' as the :id.
        For example, you could get the root folder for a course like:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/folders/{id}".format(**path), data=data, params=params, single_item=True)

    def get_folder_users(self, id, user_id):
        """
        Get folder.

        Returns the details for a folder
        
        You can get the root folder from a context by using 'root' as the :id.
        For example, you could get the root folder for a course like:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/users/{user_id}/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/folders/{id}".format(**path), data=data, params=params, single_item=True)

    def get_folder_groups(self, id, group_id):
        """
        Get folder.

        Returns the details for a folder
        
        You can get the root folder from a context by using 'root' as the :id.
        For example, you could get the root folder for a course like:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/groups/{group_id}/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/folders/{id}".format(**path), data=data, params=params, single_item=True)

    def get_folder_folders(self, id):
        """
        Get folder.

        Returns the details for a folder
        
        You can get the root folder from a context by using 'root' as the :id.
        For example, you could get the root folder for a course like:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/folders/{id}".format(**path), data=data, params=params, single_item=True)

    def update_folder(self, id, hidden=None, lock_at=None, locked=None, name=None, parent_folder_id=None, position=None, unlock_at=None):
        """
        Update folder.

        Updates a folder
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - name
        """The new name of the folder"""
        if name is not None:
            data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - lock_at
        """The datetime to lock the folder at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the folder at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the folder as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the folder as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        # OPTIONAL - position
        """Set an explicit sort position for the folder"""
        if position is not None:
            data["position"] = position

        self.logger.debug("PUT /api/v1/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/folders/{id}".format(**path), data=data, params=params, single_item=True)

    def create_folder_courses(self, name, course_id, hidden=None, lock_at=None, locked=None, parent_folder_id=None, parent_folder_path=None, position=None, unlock_at=None):
        """
        Create folder.

        Creates a folder in the specified context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - name
        """The name of the folder"""
        data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - parent_folder_path
        """The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_path is not None:
            data["parent_folder_path"] = parent_folder_path

        # OPTIONAL - lock_at
        """The datetime to lock the folder at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the folder at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the folder as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the folder as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        # OPTIONAL - position
        """Set an explicit sort position for the folder"""
        if position is not None:
            data["position"] = position

        self.logger.debug("POST /api/v1/courses/{course_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/folders".format(**path), data=data, params=params, single_item=True)

    def create_folder_users(self, name, user_id, hidden=None, lock_at=None, locked=None, parent_folder_id=None, parent_folder_path=None, position=None, unlock_at=None):
        """
        Create folder.

        Creates a folder in the specified context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - name
        """The name of the folder"""
        data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - parent_folder_path
        """The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_path is not None:
            data["parent_folder_path"] = parent_folder_path

        # OPTIONAL - lock_at
        """The datetime to lock the folder at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the folder at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the folder as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the folder as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        # OPTIONAL - position
        """Set an explicit sort position for the folder"""
        if position is not None:
            data["position"] = position

        self.logger.debug("POST /api/v1/users/{user_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/folders".format(**path), data=data, params=params, single_item=True)

    def create_folder_groups(self, name, group_id, hidden=None, lock_at=None, locked=None, parent_folder_id=None, parent_folder_path=None, position=None, unlock_at=None):
        """
        Create folder.

        Creates a folder in the specified context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - name
        """The name of the folder"""
        data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - parent_folder_path
        """The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_path is not None:
            data["parent_folder_path"] = parent_folder_path

        # OPTIONAL - lock_at
        """The datetime to lock the folder at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the folder at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the folder as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the folder as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        # OPTIONAL - position
        """Set an explicit sort position for the folder"""
        if position is not None:
            data["position"] = position

        self.logger.debug("POST /api/v1/groups/{group_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/folders".format(**path), data=data, params=params, single_item=True)

    def create_folder_folders(self, name, folder_id, hidden=None, lock_at=None, locked=None, parent_folder_id=None, parent_folder_path=None, position=None, unlock_at=None):
        """
        Create folder.

        Creates a folder in the specified context
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - folder_id
        """ID"""
        path["folder_id"] = folder_id

        # REQUIRED - name
        """The name of the folder"""
        data["name"] = name

        # OPTIONAL - parent_folder_id
        """The id of the folder to store the file in. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_id is not None:
            data["parent_folder_id"] = parent_folder_id

        # OPTIONAL - parent_folder_path
        """The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used."""
        if parent_folder_path is not None:
            data["parent_folder_path"] = parent_folder_path

        # OPTIONAL - lock_at
        """The datetime to lock the folder at"""
        if lock_at is not None:
            data["lock_at"] = lock_at

        # OPTIONAL - unlock_at
        """The datetime to unlock the folder at"""
        if unlock_at is not None:
            data["unlock_at"] = unlock_at

        # OPTIONAL - locked
        """Flag the folder as locked"""
        if locked is not None:
            data["locked"] = locked

        # OPTIONAL - hidden
        """Flag the folder as hidden"""
        if hidden is not None:
            data["hidden"] = hidden

        # OPTIONAL - position
        """Set an explicit sort position for the folder"""
        if position is not None:
            data["position"] = position

        self.logger.debug("POST /api/v1/folders/{folder_id}/folders with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/folders/{folder_id}/folders".format(**path), data=data, params=params, single_item=True)

    def delete_folder(self, id, force=None):
        """
        Delete folder.

        Remove the specified folder. You can only delete empty folders unless you
        set the 'force' flag
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - force
        """Set to 'true' to allow deleting a non-empty folder"""
        if force is not None:
            params["force"] = force

        self.logger.debug("DELETE /api/v1/folders/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/folders/{id}".format(**path), data=data, params=params, no_data=True)

    def upload_file(self, folder_id):
        """
        Upload a file.

        Upload a file to a folder.
        
        This API endpoint is the first step in uploading a file.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.
        
        Only those with the "Manage Files" permission on a course or group can
        upload files to a folder in that course or group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - folder_id
        """ID"""
        path["folder_id"] = folder_id

        self.logger.debug("POST /api/v1/folders/{folder_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/folders/{folder_id}/files".format(**path), data=data, params=params, no_data=True)

    def copy_file(self, dest_folder_id, source_file_id, on_duplicate=None):
        """
        Copy a file.

        Copy a file from elsewhere in Canvas into a folder.
        
        Copying a file across contexts (between courses and users) is permitted,
        but the source and destination must belong to the same institution.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - dest_folder_id
        """ID"""
        path["dest_folder_id"] = dest_folder_id

        # REQUIRED - source_file_id
        """The id of the source file"""
        data["source_file_id"] = source_file_id

        # OPTIONAL - on_duplicate
        """What to do if a file with the same name already exists at the destination.
        If such a file exists and this parameter is not given, the call will fail.
        
        "overwrite":: Replace an existing file with the same name
        "rename":: Add a qualifier to make the new filename unique"""
        if on_duplicate is not None:
            self._validate_enum(on_duplicate, ["overwrite", "rename"])
            data["on_duplicate"] = on_duplicate

        self.logger.debug("POST /api/v1/folders/{dest_folder_id}/copy_file with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/folders/{dest_folder_id}/copy_file".format(**path), data=data, params=params, single_item=True)

    def copy_folder(self, dest_folder_id, source_folder_id):
        """
        Copy a folder.

        Copy a folder (and its contents) from elsewhere in Canvas into a folder.
        
        Copying a folder across contexts (between courses and users) is permitted,
        but the source and destination must belong to the same institution.
        If the source and destination folders are in the same context, the
        source folder may not contain the destination folder. A folder will be
        renamed at its destination if another folder with the same name already
        exists.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - dest_folder_id
        """ID"""
        path["dest_folder_id"] = dest_folder_id

        # REQUIRED - source_folder_id
        """The id of the source folder"""
        data["source_folder_id"] = source_folder_id

        self.logger.debug("POST /api/v1/folders/{dest_folder_id}/copy_folder with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/folders/{dest_folder_id}/copy_folder".format(**path), data=data, params=params, single_item=True)

    def set_usage_rights_courses(self, file_ids, course_id, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None):
        """
        Set usage rights.

        Sets copyright and license information for one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - file_ids
        """List of ids of files to set usage rights for."""
        data["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders to search for files to set usage rights for.
        Note that new files uploaded to these folders do not automatically inherit these rights."""
        if folder_ids is not None:
            data["folder_ids"] = folder_ids

        # OPTIONAL - publish
        """Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save)."""
        if publish is not None:
            data["publish"] = publish

        # REQUIRED - usage_rights[use_justification]
        """The intellectual property justification for using the files in Canvas"""
        self._validate_enum(usage_rights_use_justification, ["own_copyright", "used_by_permission", "fair_use", "public_domain", "creative_commons"])
        data["usage_rights[use_justification]"] = usage_rights_use_justification

        # OPTIONAL - usage_rights[legal_copyright]
        """The legal copyright line for the files"""
        if usage_rights_legal_copyright is not None:
            data["usage_rights[legal_copyright]"] = usage_rights_legal_copyright

        # OPTIONAL - usage_rights[license]
        """The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types."""
        if usage_rights_license is not None:
            data["usage_rights[license]"] = usage_rights_license

        self.logger.debug("PUT /api/v1/courses/{course_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/usage_rights".format(**path), data=data, params=params, single_item=True)

    def set_usage_rights_groups(self, group_id, file_ids, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None):
        """
        Set usage rights.

        Sets copyright and license information for one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - file_ids
        """List of ids of files to set usage rights for."""
        data["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders to search for files to set usage rights for.
        Note that new files uploaded to these folders do not automatically inherit these rights."""
        if folder_ids is not None:
            data["folder_ids"] = folder_ids

        # OPTIONAL - publish
        """Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save)."""
        if publish is not None:
            data["publish"] = publish

        # REQUIRED - usage_rights[use_justification]
        """The intellectual property justification for using the files in Canvas"""
        self._validate_enum(usage_rights_use_justification, ["own_copyright", "used_by_permission", "fair_use", "public_domain", "creative_commons"])
        data["usage_rights[use_justification]"] = usage_rights_use_justification

        # OPTIONAL - usage_rights[legal_copyright]
        """The legal copyright line for the files"""
        if usage_rights_legal_copyright is not None:
            data["usage_rights[legal_copyright]"] = usage_rights_legal_copyright

        # OPTIONAL - usage_rights[license]
        """The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types."""
        if usage_rights_license is not None:
            data["usage_rights[license]"] = usage_rights_license

        self.logger.debug("PUT /api/v1/groups/{group_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/usage_rights".format(**path), data=data, params=params, single_item=True)

    def set_usage_rights_users(self, user_id, file_ids, usage_rights_use_justification, folder_ids=None, publish=None, usage_rights_legal_copyright=None, usage_rights_license=None):
        """
        Set usage rights.

        Sets copyright and license information for one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - file_ids
        """List of ids of files to set usage rights for."""
        data["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders to search for files to set usage rights for.
        Note that new files uploaded to these folders do not automatically inherit these rights."""
        if folder_ids is not None:
            data["folder_ids"] = folder_ids

        # OPTIONAL - publish
        """Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save)."""
        if publish is not None:
            data["publish"] = publish

        # REQUIRED - usage_rights[use_justification]
        """The intellectual property justification for using the files in Canvas"""
        self._validate_enum(usage_rights_use_justification, ["own_copyright", "used_by_permission", "fair_use", "public_domain", "creative_commons"])
        data["usage_rights[use_justification]"] = usage_rights_use_justification

        # OPTIONAL - usage_rights[legal_copyright]
        """The legal copyright line for the files"""
        if usage_rights_legal_copyright is not None:
            data["usage_rights[legal_copyright]"] = usage_rights_legal_copyright

        # OPTIONAL - usage_rights[license]
        """The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types."""
        if usage_rights_license is not None:
            data["usage_rights[license]"] = usage_rights_license

        self.logger.debug("PUT /api/v1/users/{user_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/usage_rights".format(**path), data=data, params=params, single_item=True)

    def remove_usage_rights_courses(self, file_ids, course_id, folder_ids=None):
        """
        Remove usage rights.

        Removes copyright and license information associated with one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - file_ids
        """List of ids of files to remove associated usage rights from."""
        params["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders. Usage rights will be removed from all files in these folders."""
        if folder_ids is not None:
            params["folder_ids"] = folder_ids

        self.logger.debug("DELETE /api/v1/courses/{course_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/usage_rights".format(**path), data=data, params=params, no_data=True)

    def remove_usage_rights_groups(self, group_id, file_ids, folder_ids=None):
        """
        Remove usage rights.

        Removes copyright and license information associated with one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        # REQUIRED - file_ids
        """List of ids of files to remove associated usage rights from."""
        params["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders. Usage rights will be removed from all files in these folders."""
        if folder_ids is not None:
            params["folder_ids"] = folder_ids

        self.logger.debug("DELETE /api/v1/groups/{group_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/usage_rights".format(**path), data=data, params=params, no_data=True)

    def remove_usage_rights_users(self, user_id, file_ids, folder_ids=None):
        """
        Remove usage rights.

        Removes copyright and license information associated with one or more files
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        # REQUIRED - file_ids
        """List of ids of files to remove associated usage rights from."""
        params["file_ids"] = file_ids

        # OPTIONAL - folder_ids
        """List of ids of folders. Usage rights will be removed from all files in these folders."""
        if folder_ids is not None:
            params["folder_ids"] = folder_ids

        self.logger.debug("DELETE /api/v1/users/{user_id}/usage_rights with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/usage_rights".format(**path), data=data, params=params, no_data=True)

    def list_licenses_courses(self, course_id):
        """
        List licenses.

        Lists licenses that can be applied
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/content_licenses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_licenses".format(**path), data=data, params=params, all_pages=True)

    def list_licenses_groups(self, group_id):
        """
        List licenses.

        Lists licenses that can be applied
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """ID"""
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/content_licenses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_licenses".format(**path), data=data, params=params, all_pages=True)

    def list_licenses_users(self, user_id):
        """
        List licenses.

        Lists licenses that can be applied
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """ID"""
        path["user_id"] = user_id

        self.logger.debug("GET /api/v1/users/{user_id}/content_licenses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_licenses".format(**path), data=data, params=params, all_pages=True)


class Folder(BaseModel):
    """Folder Model."""

    def __init__(self, folders_count=None, locked=None, name=None, parent_folder_id=None, context_type=None, context_id=None, created_at=None, updated_at=None, lock_at=None, files_url=None, hidden_for_user=None, files_count=None, full_name=None, for_submissions=None, position=None, hidden=None, locked_for_user=None, id=None, folders_url=None, unlock_at=None):
        """Init method for Folder class."""
        self._folders_count = folders_count
        self._locked = locked
        self._name = name
        self._parent_folder_id = parent_folder_id
        self._context_type = context_type
        self._context_id = context_id
        self._created_at = created_at
        self._updated_at = updated_at
        self._lock_at = lock_at
        self._files_url = files_url
        self._hidden_for_user = hidden_for_user
        self._files_count = files_count
        self._full_name = full_name
        self._for_submissions = for_submissions
        self._position = position
        self._hidden = hidden
        self._locked_for_user = locked_for_user
        self._id = id
        self._folders_url = folders_url
        self._unlock_at = unlock_at

        self.logger = logging.getLogger('pycanvas.Folder')

    @property
    def folders_count(self):
        """folders_count."""
        return self._folders_count

    @folders_count.setter
    def folders_count(self, value):
        """Setter for folders_count property."""
        self.logger.warn("Setting values on folders_count will NOT update the remote Canvas instance.")
        self._folders_count = value

    @property
    def locked(self):
        """locked."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def name(self):
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def parent_folder_id(self):
        """parent_folder_id."""
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, value):
        """Setter for parent_folder_id property."""
        self.logger.warn("Setting values on parent_folder_id will NOT update the remote Canvas instance.")
        self._parent_folder_id = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """context_id."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def lock_at(self):
        """lock_at."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def files_url(self):
        """files_url."""
        return self._files_url

    @files_url.setter
    def files_url(self, value):
        """Setter for files_url property."""
        self.logger.warn("Setting values on files_url will NOT update the remote Canvas instance.")
        self._files_url = value

    @property
    def hidden_for_user(self):
        """hidden_for_user."""
        return self._hidden_for_user

    @hidden_for_user.setter
    def hidden_for_user(self, value):
        """Setter for hidden_for_user property."""
        self.logger.warn("Setting values on hidden_for_user will NOT update the remote Canvas instance.")
        self._hidden_for_user = value

    @property
    def files_count(self):
        """files_count."""
        return self._files_count

    @files_count.setter
    def files_count(self, value):
        """Setter for files_count property."""
        self.logger.warn("Setting values on files_count will NOT update the remote Canvas instance.")
        self._files_count = value

    @property
    def full_name(self):
        """full_name."""
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        """Setter for full_name property."""
        self.logger.warn("Setting values on full_name will NOT update the remote Canvas instance.")
        self._full_name = value

    @property
    def for_submissions(self):
        """If true, indicates this is a read-only folder containing files submitted to assignments."""
        return self._for_submissions

    @for_submissions.setter
    def for_submissions(self, value):
        """Setter for for_submissions property."""
        self.logger.warn("Setting values on for_submissions will NOT update the remote Canvas instance.")
        self._for_submissions = value

    @property
    def position(self):
        """position."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def hidden(self):
        """hidden."""
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Setter for hidden property."""
        self.logger.warn("Setting values on hidden will NOT update the remote Canvas instance.")
        self._hidden = value

    @property
    def locked_for_user(self):
        """locked_for_user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def folders_url(self):
        """folders_url."""
        return self._folders_url

    @folders_url.setter
    def folders_url(self, value):
        """Setter for folders_url property."""
        self.logger.warn("Setting values on folders_url will NOT update the remote Canvas instance.")
        self._folders_url = value

    @property
    def unlock_at(self):
        """unlock_at."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value


class Usagerights(BaseModel):
    """Usagerights Model.
    Describes the copyright and license information for a File"""

    def __init__(self, license=None, license_name=None, file_ids=None, legal_copyright=None, use_justification=None, message=None):
        """Init method for Usagerights class."""
        self._license = license
        self._license_name = license_name
        self._file_ids = file_ids
        self._legal_copyright = legal_copyright
        self._use_justification = use_justification
        self._message = message

        self.logger = logging.getLogger('pycanvas.Usagerights')

    @property
    def license(self):
        """License identifier for the file."""
        return self._license

    @license.setter
    def license(self, value):
        """Setter for license property."""
        self.logger.warn("Setting values on license will NOT update the remote Canvas instance.")
        self._license = value

    @property
    def license_name(self):
        """Readable license name."""
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        """Setter for license_name property."""
        self.logger.warn("Setting values on license_name will NOT update the remote Canvas instance.")
        self._license_name = value

    @property
    def file_ids(self):
        """List of ids of files that were updated."""
        return self._file_ids

    @file_ids.setter
    def file_ids(self, value):
        """Setter for file_ids property."""
        self.logger.warn("Setting values on file_ids will NOT update the remote Canvas instance.")
        self._file_ids = value

    @property
    def legal_copyright(self):
        """Copyright line for the file."""
        return self._legal_copyright

    @legal_copyright.setter
    def legal_copyright(self, value):
        """Setter for legal_copyright property."""
        self.logger.warn("Setting values on legal_copyright will NOT update the remote Canvas instance.")
        self._legal_copyright = value

    @property
    def use_justification(self):
        """Justification for using the file in a Canvas course. Valid values are 'own_copyright', 'public_domain', 'used_by_permission', 'fair_use', 'creative_commons'."""
        return self._use_justification

    @use_justification.setter
    def use_justification(self, value):
        """Setter for use_justification property."""
        self.logger.warn("Setting values on use_justification will NOT update the remote Canvas instance.")
        self._use_justification = value

    @property
    def message(self):
        """Explanation of the action performed."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn("Setting values on message will NOT update the remote Canvas instance.")
        self._message = value


class License(BaseModel):
    """License Model."""

    def __init__(self, url=None, id=None, name=None):
        """Init method for License class."""
        self._url = url
        self._id = id
        self._name = name

        self.logger = logging.getLogger('pycanvas.License')

    @property
    def url(self):
        """a link to the license text."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def id(self):
        """a short string identifying the license."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """the name of the license."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class File(BaseModel):
    """File Model."""

    def __init__(self, media_entry_id=None, display_name=None, unlock_at=None, mime_class=None, url=None, created_at=None, modified_at=None, updated_at=None, preview_url=None, lock_info=None, lock_at=None, thumbnail_url=None, hidden_for_user=None, lock_explanation=None, locked=None, hidden=None, locked_for_user=None, content_type=None, id=None, size=None):
        """Init method for File class."""
        self._media_entry_id = media_entry_id
        self._display_name = display_name
        self._unlock_at = unlock_at
        self._mime_class = mime_class
        self._url = url
        self._created_at = created_at
        self._modified_at = modified_at
        self._updated_at = updated_at
        self._preview_url = preview_url
        self._lock_info = lock_info
        self._lock_at = lock_at
        self._thumbnail_url = thumbnail_url
        self._hidden_for_user = hidden_for_user
        self._lock_explanation = lock_explanation
        self._locked = locked
        self._hidden = hidden
        self._locked_for_user = locked_for_user
        self._content_type = content_type
        self._id = id
        self._size = size

        self.logger = logging.getLogger('pycanvas.File')

    @property
    def media_entry_id(self):
        """identifier for file in third-party transcoding service."""
        return self._media_entry_id

    @media_entry_id.setter
    def media_entry_id(self, value):
        """Setter for media_entry_id property."""
        self.logger.warn("Setting values on media_entry_id will NOT update the remote Canvas instance.")
        self._media_entry_id = value

    @property
    def display_name(self):
        """display_name."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def unlock_at(self):
        """unlock_at."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def mime_class(self):
        """simplified content-type mapping."""
        return self._mime_class

    @mime_class.setter
    def mime_class(self, value):
        """Setter for mime_class property."""
        self.logger.warn("Setting values on mime_class will NOT update the remote Canvas instance.")
        self._mime_class = value

    @property
    def url(self):
        """url."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def modified_at(self):
        """modified_at."""
        return self._modified_at

    @modified_at.setter
    def modified_at(self, value):
        """Setter for modified_at property."""
        self.logger.warn("Setting values on modified_at will NOT update the remote Canvas instance.")
        self._modified_at = value

    @property
    def updated_at(self):
        """updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def preview_url(self):
        """optional: url to the document preview (only included in submission endpoints)."""
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        """Setter for preview_url property."""
        self.logger.warn("Setting values on preview_url will NOT update the remote Canvas instance.")
        self._preview_url = value

    @property
    def lock_info(self):
        """lock_info."""
        return self._lock_info

    @lock_info.setter
    def lock_info(self, value):
        """Setter for lock_info property."""
        self.logger.warn("Setting values on lock_info will NOT update the remote Canvas instance.")
        self._lock_info = value

    @property
    def lock_at(self):
        """lock_at."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def thumbnail_url(self):
        """thumbnail_url."""
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, value):
        """Setter for thumbnail_url property."""
        self.logger.warn("Setting values on thumbnail_url will NOT update the remote Canvas instance.")
        self._thumbnail_url = value

    @property
    def hidden_for_user(self):
        """hidden_for_user."""
        return self._hidden_for_user

    @hidden_for_user.setter
    def hidden_for_user(self, value):
        """Setter for hidden_for_user property."""
        self.logger.warn("Setting values on hidden_for_user will NOT update the remote Canvas instance.")
        self._hidden_for_user = value

    @property
    def lock_explanation(self):
        """lock_explanation."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def locked(self):
        """locked."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def hidden(self):
        """hidden."""
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Setter for hidden property."""
        self.logger.warn("Setting values on hidden will NOT update the remote Canvas instance.")
        self._hidden = value

    @property
    def locked_for_user(self):
        """locked_for_user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

    @property
    def content_type(self):
        """content_type."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn("Setting values on content_type will NOT update the remote Canvas instance.")
        self._content_type = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def size(self):
        """size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size property."""
        self.logger.warn("Setting values on size will NOT update the remote Canvas instance.")
        self._size = value

