"""Modules API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class ModulesAPI(BaseCanvasAPI):
    """Modules API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ModulesAPI."""
        super(ModulesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.ModulesAPI")

    def list_modules(self, course_id, include=None, search_term=None, student_id=None):
        """
        List modules.

        List the modules in a course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # OPTIONAL - include
        """- "items": Return module items inline if possible.
          This parameter suggests that Canvas return module items directly
          in the Module object JSON, to avoid having to make separate API
          requests for each module when enumerating modules and items. Canvas
          is free to omit 'items' for any particular module if it deems them
          too numerous to return inline. Callers must be prepared to use the
          {api:ContextModuleItemsApiController#index List Module Items API}
          if items are not returned.
        - "content_details": Requires include['items']. Returns additional
          details with module items specific to their associated content items.
          Includes standard lock information for each item."""
        if include is not None:
            self._validate_enum(include, ["items", "content_details"])
            params["include"] = include
        # OPTIONAL - search_term
        """The partial name of the modules (and module items, if include['items'] is
        specified) to match and return."""
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - student_id
        """Returns module completion information for the student with this id."""
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug("GET /api/v1/courses/{course_id}/modules with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/modules".format(**path), data=data, params=params, all_pages=True)

    def show_module(self, id, course_id, include=None, student_id=None):
        """
        Show module.

        Get information about a single module
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
        """- "items": Return module items inline if possible.
          This parameter suggests that Canvas return module items directly
          in the Module object JSON, to avoid having to make separate API
          requests for each module when enumerating modules and items. Canvas
          is free to omit 'items' for any particular module if it deems them
          too numerous to return inline. Callers must be prepared to use the
          {api:ContextModuleItemsApiController#index List Module Items API}
          if items are not returned.
        - "content_details": Requires include['items']. Returns additional
          details with module items specific to their associated content items.
          Includes standard lock information for each item."""
        if include is not None:
            self._validate_enum(include, ["items", "content_details"])
            params["include"] = include
        # OPTIONAL - student_id
        """Returns module completion information for the student with this id."""
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug("GET /api/v1/courses/{course_id}/modules/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/modules/{id}".format(**path), data=data, params=params, single_item=True)

    def create_module(self, course_id, module_name, module_position=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, module_require_sequential_progress=None, module_unlock_at=None):
        """
        Create a module.

        Create and return a new module
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - module[name]
        """The name of the module"""
        data["module[name]"] = module_name
        # OPTIONAL - module[unlock_at]
        """The date the module will unlock"""
        if module_unlock_at is not None:
            data["module[unlock_at]"] = module_unlock_at
        # OPTIONAL - module[position]
        """The position of this module in the course (1-based)"""
        if module_position is not None:
            data["module[position]"] = module_position
        # OPTIONAL - module[require_sequential_progress]
        """Whether module items must be unlocked in order"""
        if module_require_sequential_progress is not None:
            data["module[require_sequential_progress]"] = module_require_sequential_progress
        # OPTIONAL - module[prerequisite_module_ids]
        """IDs of Modules that must be completed before this one is unlocked.
        Prerequisite modules must precede this module (i.e. have a lower position
        value), otherwise they will be ignored"""
        if module_prerequisite_module_ids is not None:
            data["module[prerequisite_module_ids]"] = module_prerequisite_module_ids
        # OPTIONAL - module[publish_final_grade]
        """Whether to publish the student's final grade for the course upon
        completion of this module."""
        if module_publish_final_grade is not None:
            data["module[publish_final_grade]"] = module_publish_final_grade

        self.logger.debug("POST /api/v1/courses/{course_id}/modules with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/modules".format(**path), data=data, params=params, single_item=True)

    def update_module(self, id, course_id, module_name=None, module_position=None, module_prerequisite_module_ids=None, module_publish_final_grade=None, module_published=None, module_require_sequential_progress=None, module_unlock_at=None):
        """
        Update a module.

        Update and return an existing module
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
        # OPTIONAL - module[name]
        """The name of the module"""
        if module_name is not None:
            data["module[name]"] = module_name
        # OPTIONAL - module[unlock_at]
        """The date the module will unlock"""
        if module_unlock_at is not None:
            data["module[unlock_at]"] = module_unlock_at
        # OPTIONAL - module[position]
        """The position of the module in the course (1-based)"""
        if module_position is not None:
            data["module[position]"] = module_position
        # OPTIONAL - module[require_sequential_progress]
        """Whether module items must be unlocked in order"""
        if module_require_sequential_progress is not None:
            data["module[require_sequential_progress]"] = module_require_sequential_progress
        # OPTIONAL - module[prerequisite_module_ids]
        """IDs of Modules that must be completed before this one is unlocked
        Prerequisite modules must precede this module (i.e. have a lower position
        value), otherwise they will be ignored"""
        if module_prerequisite_module_ids is not None:
            data["module[prerequisite_module_ids]"] = module_prerequisite_module_ids
        # OPTIONAL - module[publish_final_grade]
        """Whether to publish the student's final grade for the course upon
        completion of this module."""
        if module_publish_final_grade is not None:
            data["module[publish_final_grade]"] = module_publish_final_grade
        # OPTIONAL - module[published]
        """Whether the module is published and visible to students"""
        if module_published is not None:
            data["module[published]"] = module_published

        self.logger.debug("PUT /api/v1/courses/{course_id}/modules/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/modules/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_module(self, id, course_id):
        """
        Delete module.

        Delete a module
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

        self.logger.debug("DELETE /api/v1/courses/{course_id}/modules/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/modules/{id}".format(**path), data=data, params=params, single_item=True)

    def re_lock_module_progressions(self, id, course_id):
        """
        Re-lock module progressions.

        Resets module progressions to their default locked state and
        recalculates them based on the current requirements.
        
        Adding progression requirements to an active course will not lock students
        out of modules they have already unlocked unless this action is called.
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

        self.logger.debug("PUT /api/v1/courses/{course_id}/modules/{id}/relock with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/modules/{id}/relock".format(**path), data=data, params=params, single_item=True)

    def list_module_items(self, course_id, module_id, include=None, search_term=None, student_id=None):
        """
        List module items.

        List the items in a module
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # OPTIONAL - include
        """If included, will return additional details specific to the content
        associated with each item. Refer to the {api:Modules:Module%20Item Module
        Item specification} for more details.
        Includes standard lock information for each item."""
        if include is not None:
            self._validate_enum(include, ["content_details"])
            params["include"] = include
        # OPTIONAL - search_term
        """The partial title of the items to match and return."""
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - student_id
        """Returns module completion information for the student with this id."""
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug("GET /api/v1/courses/{course_id}/modules/{module_id}/items with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/modules/{module_id}/items".format(**path), data=data, params=params, all_pages=True)

    def show_module_item(self, id, course_id, module_id, include=None, student_id=None):
        """
        Show module item.

        Get information about a single module item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - include
        """If included, will return additional details specific to the content
        associated with this item. Refer to the {api:Modules:Module%20Item Module
        Item specification} for more details.
        Includes standard lock information for each item."""
        if include is not None:
            self._validate_enum(include, ["content_details"])
            params["include"] = include
        # OPTIONAL - student_id
        """Returns module completion information for the student with this id."""
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug("GET /api/v1/courses/{course_id}/modules/{module_id}/items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}".format(**path), data=data, params=params, single_item=True)

    def create_module_item(self, course_id, module_id, module_item_type, module_item_content_id, module_item_completion_requirement_min_score=None, module_item_completion_requirement_type=None, module_item_external_url=None, module_item_indent=None, module_item_new_tab=None, module_item_page_url=None, module_item_position=None, module_item_title=None):
        """
        Create a module item.

        Create and return a new module item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # OPTIONAL - module_item[title]
        """The name of the module item and associated content"""
        if module_item_title is not None:
            data["module_item[title]"] = module_item_title
        # REQUIRED - module_item[type]
        """The type of content linked to the item"""
        self._validate_enum(module_item_type, ["File", "Page", "Discussion", "Assignment", "Quiz", "SubHeader", "ExternalUrl", "ExternalTool"])
        data["module_item[type]"] = module_item_type
        # REQUIRED - module_item[content_id]
        """The id of the content to link to the module item. Required, except for
        'ExternalUrl', 'Page', and 'SubHeader' types."""
        data["module_item[content_id]"] = module_item_content_id
        # OPTIONAL - module_item[position]
        """The position of this item in the module (1-based)."""
        if module_item_position is not None:
            data["module_item[position]"] = module_item_position
        # OPTIONAL - module_item[indent]
        """0-based indent level; module items may be indented to show a hierarchy"""
        if module_item_indent is not None:
            data["module_item[indent]"] = module_item_indent
        # OPTIONAL - module_item[page_url]
        """Suffix for the linked wiki page (e.g. 'front-page'). Required for 'Page'
        type."""
        if module_item_page_url is not None:
            data["module_item[page_url]"] = module_item_page_url
        # OPTIONAL - module_item[external_url]
        """External url that the item points to. [Required for 'ExternalUrl' and
        'ExternalTool' types."""
        if module_item_external_url is not None:
            data["module_item[external_url]"] = module_item_external_url
        # OPTIONAL - module_item[new_tab]
        """Whether the external tool opens in a new tab. Only applies to
        'ExternalTool' type."""
        if module_item_new_tab is not None:
            data["module_item[new_tab]"] = module_item_new_tab
        # OPTIONAL - module_item[completion_requirement][type]
        """Completion requirement for this module item.
        "must_view": Applies to all item types
        "must_contribute": Only applies to "Assignment", "Discussion", and "Page" types
        "must_submit", "min_score": Only apply to "Assignment" and "Quiz" types
        Inapplicable types will be ignored"""
        if module_item_completion_requirement_type is not None:
            self._validate_enum(module_item_completion_requirement_type, ["must_view", "must_contribute", "must_submit"])
            data["module_item[completion_requirement][type]"] = module_item_completion_requirement_type
        # OPTIONAL - module_item[completion_requirement][min_score]
        """Minimum score required to complete. Required for completion_requirement
        type 'min_score'."""
        if module_item_completion_requirement_min_score is not None:
            data["module_item[completion_requirement][min_score]"] = module_item_completion_requirement_min_score

        self.logger.debug("POST /api/v1/courses/{course_id}/modules/{module_id}/items with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/modules/{module_id}/items".format(**path), data=data, params=params, single_item=True)

    def update_module_item(self, id, course_id, module_id, module_item_completion_requirement_min_score=None, module_item_completion_requirement_type=None, module_item_external_url=None, module_item_indent=None, module_item_module_id=None, module_item_new_tab=None, module_item_position=None, module_item_published=None, module_item_title=None):
        """
        Update a module item.

        Update and return an existing module item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - module_item[title]
        """The name of the module item"""
        if module_item_title is not None:
            data["module_item[title]"] = module_item_title
        # OPTIONAL - module_item[position]
        """The position of this item in the module (1-based)"""
        if module_item_position is not None:
            data["module_item[position]"] = module_item_position
        # OPTIONAL - module_item[indent]
        """0-based indent level; module items may be indented to show a hierarchy"""
        if module_item_indent is not None:
            data["module_item[indent]"] = module_item_indent
        # OPTIONAL - module_item[external_url]
        """External url that the item points to. Only applies to 'ExternalUrl' type."""
        if module_item_external_url is not None:
            data["module_item[external_url]"] = module_item_external_url
        # OPTIONAL - module_item[new_tab]
        """Whether the external tool opens in a new tab. Only applies to
        'ExternalTool' type."""
        if module_item_new_tab is not None:
            data["module_item[new_tab]"] = module_item_new_tab
        # OPTIONAL - module_item[completion_requirement][type]
        """Completion requirement for this module item.
        "must_view": Applies to all item types
        "must_contribute": Only applies to "Assignment", "Discussion", and "Page" types
        "must_submit", "min_score": Only apply to "Assignment" and "Quiz" types
        Inapplicable types will be ignored"""
        if module_item_completion_requirement_type is not None:
            self._validate_enum(module_item_completion_requirement_type, ["must_view", "must_contribute", "must_submit"])
            data["module_item[completion_requirement][type]"] = module_item_completion_requirement_type
        # OPTIONAL - module_item[completion_requirement][min_score]
        """Minimum score required to complete, Required for completion_requirement
        type 'min_score'."""
        if module_item_completion_requirement_min_score is not None:
            data["module_item[completion_requirement][min_score]"] = module_item_completion_requirement_min_score
        # OPTIONAL - module_item[published]
        """Whether the module item is published and visible to students."""
        if module_item_published is not None:
            data["module_item[published]"] = module_item_published
        # OPTIONAL - module_item[module_id]
        """Move this item to another module by specifying the target module id here.
        The target module must be in the same course."""
        if module_item_module_id is not None:
            data["module_item[module_id]"] = module_item_module_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/modules/{module_id}/items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}".format(**path), data=data, params=params, single_item=True)

    def select_mastery_path(self, id, course_id, module_id, assignment_set_id=None, student_id=None):
        """
        Select a mastery path.

        Select a mastery path when module item includes several possible paths.
        Requires Mastery Paths feature to be enabled.  Returns a compound document
        with the assignments included in the given path and any module items
        related to those assignments
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id
        # OPTIONAL - assignment_set_id
        """Assignment set chosen, as specified in the mastery_paths portion of the
        context module item response"""
        if assignment_set_id is not None:
            data["assignment_set_id"] = assignment_set_id
        # OPTIONAL - student_id
        """Which student the selection applies to.  If not specified, current user is
        implied."""
        if student_id is not None:
            data["student_id"] = student_id

        self.logger.debug("POST /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path".format(**path), data=data, params=params, no_data=True)

    def delete_module_item(self, id, course_id, module_id):
        """
        Delete module item.

        Delete a module item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/modules/{module_id}/items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}".format(**path), data=data, params=params, single_item=True)

    def mark_module_item_as_done_not_done(self, id, course_id, module_id):
        """
        Mark module item as done/not done.

        Mark a module item as done/not done. Use HTTP method PUT to mark as done,
        and DELETE to mark as not done.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("PUT /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done".format(**path), data=data, params=params, no_data=True)

    def get_module_item_sequence(self, course_id, asset_id=None, asset_type=None):
        """
        Get module item sequence.

        Given an asset in a course, find the ModuleItem it belongs to, and also the previous and next Module Items
        in the course sequence.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # OPTIONAL - asset_type
        """The type of asset to find module sequence information for. Use the ModuleItem if it is known
        (e.g., the user navigated from a module item), since this will avoid ambiguity if the asset
        appears more than once in the module sequence."""
        if asset_type is not None:
            self._validate_enum(asset_type, ["ModuleItem", "File", "Page", "Discussion", "Assignment", "Quiz", "ExternalTool"])
            params["asset_type"] = asset_type
        # OPTIONAL - asset_id
        """The id of the asset (or the url in the case of a Page)"""
        if asset_id is not None:
            params["asset_id"] = asset_id

        self.logger.debug("GET /api/v1/courses/{course_id}/module_item_sequence with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/module_item_sequence".format(**path), data=data, params=params, single_item=True)

    def mark_module_item_read(self, id, course_id, module_id):
        """
        Mark module item read.

        Fulfills "must view" requirement for a module item. It is generally not necessary to do this explicitly,
        but it is provided for applications that need to access external content directly (bypassing the html_url
        redirect that normally allows Canvas to fulfill "must view" requirements).
        
        This endpoint cannot be used to complete requirements on locked or unpublished module items.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id
        # REQUIRED - PATH - module_id
        """ID"""
        path["module_id"] = module_id
        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("POST /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read".format(**path), data=data, params=params, no_data=True)


class Contentdetails(BaseModel):
    """Contentdetails Model."""

    def __init__(self, unlock_at=None, due_at=None, points_possible=None, lock_info=None, lock_at=None, lock_explanation=None, locked_for_user=None):
        """Init method for Contentdetails class."""
        self._unlock_at = unlock_at
        self._due_at = due_at
        self._points_possible = points_possible
        self._lock_info = lock_info
        self._lock_at = lock_at
        self._lock_explanation = lock_explanation
        self._locked_for_user = locked_for_user

        self.logger = logging.getLogger('pycanvas.Contentdetails')

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
    def due_at(self):
        """due_at."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def points_possible(self):
        """points_possible."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

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
    def lock_explanation(self):
        """lock_explanation."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def locked_for_user(self):
        """locked_for_user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value


class Moduleitemsequenceasset(BaseModel):
    """Moduleitemsequenceasset Model."""

    def __init__(self, module_id=None, type=None, id=None, title=None):
        """Init method for Moduleitemsequenceasset class."""
        self._module_id = module_id
        self._type = type
        self._id = id
        self._title = title

        self.logger = logging.getLogger('pycanvas.Moduleitemsequenceasset')

    @property
    def module_id(self):
        """module_id."""
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        """Setter for module_id property."""
        self.logger.warn("Setting values on module_id will NOT update the remote Canvas instance.")
        self._module_id = value

    @property
    def type(self):
        """type."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

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
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value


class Moduleitemcompletionrequirement(BaseModel):
    """Moduleitemcompletionrequirement Model."""

    def __init__(self, min_score=None, type=None, completed=None):
        """Init method for Moduleitemcompletionrequirement class."""
        self._min_score = min_score
        self._type = type
        self._completed = completed

        self.logger = logging.getLogger('pycanvas.Moduleitemcompletionrequirement')

    @property
    def min_score(self):
        """min_score."""
        return self._min_score

    @min_score.setter
    def min_score(self, value):
        """Setter for min_score property."""
        self.logger.warn("Setting values on min_score will NOT update the remote Canvas instance.")
        self._min_score = value

    @property
    def type(self):
        """type."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def completed(self):
        """completed."""
        return self._completed

    @completed.setter
    def completed(self, value):
        """Setter for completed property."""
        self.logger.warn("Setting values on completed will NOT update the remote Canvas instance.")
        self._completed = value


class Module(BaseModel):
    """Module Model."""

    def __init__(self, completed_at=None, items_count=None, unlock_at=None, workflow_state=None, items=None, prerequisite_module_ids=None, state=None, publish_final_grade=None, position=None, items_url=None, id=None, require_sequential_progress=None, name=None):
        """Init method for Module class."""
        self._completed_at = completed_at
        self._items_count = items_count
        self._unlock_at = unlock_at
        self._workflow_state = workflow_state
        self._items = items
        self._prerequisite_module_ids = prerequisite_module_ids
        self._state = state
        self._publish_final_grade = publish_final_grade
        self._position = position
        self._items_url = items_url
        self._id = id
        self._require_sequential_progress = require_sequential_progress
        self._name = name

        self.logger = logging.getLogger('pycanvas.Module')

    @property
    def completed_at(self):
        """the date the calling user completed the module (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included)."""
        return self._completed_at

    @completed_at.setter
    def completed_at(self, value):
        """Setter for completed_at property."""
        self.logger.warn("Setting values on completed_at will NOT update the remote Canvas instance.")
        self._completed_at = value

    @property
    def items_count(self):
        """The number of items in the module."""
        return self._items_count

    @items_count.setter
    def items_count(self, value):
        """Setter for items_count property."""
        self.logger.warn("Setting values on items_count will NOT update the remote Canvas instance.")
        self._items_count = value

    @property
    def unlock_at(self):
        """(Optional) the date this module will unlock."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def workflow_state(self):
        """the state of the module: 'active', 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def items(self):
        """The contents of this module, as an array of Module Items. (Present only if requested via include[]=items AND the module is not deemed too large by Canvas.)."""
        return self._items

    @items.setter
    def items(self, value):
        """Setter for items property."""
        self.logger.warn("Setting values on items will NOT update the remote Canvas instance.")
        self._items = value

    @property
    def prerequisite_module_ids(self):
        """IDs of Modules that must be completed before this one is unlocked."""
        return self._prerequisite_module_ids

    @prerequisite_module_ids.setter
    def prerequisite_module_ids(self, value):
        """Setter for prerequisite_module_ids property."""
        self.logger.warn("Setting values on prerequisite_module_ids will NOT update the remote Canvas instance.")
        self._prerequisite_module_ids = value

    @property
    def state(self):
        """The state of this Module for the calling user one of 'locked', 'unlocked', 'started', 'completed' (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included)."""
        return self._state

    @state.setter
    def state(self, value):
        """Setter for state property."""
        self.logger.warn("Setting values on state will NOT update the remote Canvas instance.")
        self._state = value

    @property
    def publish_final_grade(self):
        """if the student's final grade for the course should be published to the SIS upon completion of this module."""
        return self._publish_final_grade

    @publish_final_grade.setter
    def publish_final_grade(self, value):
        """Setter for publish_final_grade property."""
        self.logger.warn("Setting values on publish_final_grade will NOT update the remote Canvas instance.")
        self._publish_final_grade = value

    @property
    def position(self):
        """the position of this module in the course (1-based)."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def items_url(self):
        """The API URL to retrive this module's items."""
        return self._items_url

    @items_url.setter
    def items_url(self, value):
        """Setter for items_url property."""
        self.logger.warn("Setting values on items_url will NOT update the remote Canvas instance.")
        self._items_url = value

    @property
    def id(self):
        """the unique identifier for the module."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def require_sequential_progress(self):
        """Whether module items must be unlocked in order."""
        return self._require_sequential_progress

    @require_sequential_progress.setter
    def require_sequential_progress(self, value):
        """Setter for require_sequential_progress property."""
        self.logger.warn("Setting values on require_sequential_progress will NOT update the remote Canvas instance.")
        self._require_sequential_progress = value

    @property
    def name(self):
        """the name of this module."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value


class Moduleitemsequence(BaseModel):
    """Moduleitemsequence Model."""

    def __init__(self, items=None, modules=None):
        """Init method for Moduleitemsequence class."""
        self._items = items
        self._modules = modules

        self.logger = logging.getLogger('pycanvas.Moduleitemsequence')

    @property
    def items(self):
        """an array containing one hash for each appearence of the asset in the module sequence (up to 10 total)."""
        return self._items

    @items.setter
    def items(self, value):
        """Setter for items property."""
        self.logger.warn("Setting values on items will NOT update the remote Canvas instance.")
        self._items = value

    @property
    def modules(self):
        """an array containing each Module referenced above."""
        return self._modules

    @modules.setter
    def modules(self, value):
        """Setter for modules property."""
        self.logger.warn("Setting values on modules will NOT update the remote Canvas instance.")
        self._modules = value


class Completionrequirement(BaseModel):
    """Completionrequirement Model."""

    def __init__(self, min_score=None, type=None, completed=None):
        """Init method for Completionrequirement class."""
        self._min_score = min_score
        self._type = type
        self._completed = completed

        self.logger = logging.getLogger('pycanvas.Completionrequirement')

    @property
    def min_score(self):
        """minimum score required to complete (only present when type == 'min_score')."""
        return self._min_score

    @min_score.setter
    def min_score(self, value):
        """Setter for min_score property."""
        self.logger.warn("Setting values on min_score will NOT update the remote Canvas instance.")
        self._min_score = value

    @property
    def type(self):
        """one of 'must_view', 'must_submit', 'must_contribute', 'min_score'."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def completed(self):
        """whether the calling user has met this requirement (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included)."""
        return self._completed

    @completed.setter
    def completed(self, value):
        """Setter for completed property."""
        self.logger.warn("Setting values on completed will NOT update the remote Canvas instance.")
        self._completed = value


class Moduleitem(BaseModel):
    """Moduleitem Model."""

    def __init__(self, indent=None, title=None, url=None, completion_requirement=None, html_url=None, content_details=None, new_tab=None, external_url=None, position=None, module_id=None, content_id=None, type=None, id=None, page_url=None):
        """Init method for Moduleitem class."""
        self._indent = indent
        self._title = title
        self._url = url
        self._completion_requirement = completion_requirement
        self._html_url = html_url
        self._content_details = content_details
        self._new_tab = new_tab
        self._external_url = external_url
        self._position = position
        self._module_id = module_id
        self._content_id = content_id
        self._type = type
        self._id = id
        self._page_url = page_url

        self.logger = logging.getLogger('pycanvas.Moduleitem')

    @property
    def indent(self):
        """0-based indent level; module items may be indented to show a hierarchy."""
        return self._indent

    @indent.setter
    def indent(self, value):
        """Setter for indent property."""
        self.logger.warn("Setting values on indent will NOT update the remote Canvas instance.")
        self._indent = value

    @property
    def title(self):
        """the title of this item."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """(Optional) link to the Canvas API object, if applicable."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def completion_requirement(self):
        """Completion requirement for this module item."""
        return self._completion_requirement

    @completion_requirement.setter
    def completion_requirement(self, value):
        """Setter for completion_requirement property."""
        self.logger.warn("Setting values on completion_requirement will NOT update the remote Canvas instance.")
        self._completion_requirement = value

    @property
    def html_url(self):
        """link to the item in Canvas."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def content_details(self):
        """(Present only if requested through include[]=content_details) If applicable, returns additional details specific to the associated object."""
        return self._content_details

    @content_details.setter
    def content_details(self, value):
        """Setter for content_details property."""
        self.logger.warn("Setting values on content_details will NOT update the remote Canvas instance.")
        self._content_details = value

    @property
    def new_tab(self):
        """(only for 'ExternalTool' type) whether the external tool opens in a new tab."""
        return self._new_tab

    @new_tab.setter
    def new_tab(self, value):
        """Setter for new_tab property."""
        self.logger.warn("Setting values on new_tab will NOT update the remote Canvas instance.")
        self._new_tab = value

    @property
    def external_url(self):
        """(only for 'ExternalUrl' and 'ExternalTool' types) external url that the item points to."""
        return self._external_url

    @external_url.setter
    def external_url(self, value):
        """Setter for external_url property."""
        self.logger.warn("Setting values on external_url will NOT update the remote Canvas instance.")
        self._external_url = value

    @property
    def position(self):
        """the position of this item in the module (1-based)."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def module_id(self):
        """the id of the Module this item appears in."""
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        """Setter for module_id property."""
        self.logger.warn("Setting values on module_id will NOT update the remote Canvas instance.")
        self._module_id = value

    @property
    def content_id(self):
        """the id of the object referred to applies to 'File', 'Discussion', 'Assignment', 'Quiz', 'ExternalTool' types."""
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        """Setter for content_id property."""
        self.logger.warn("Setting values on content_id will NOT update the remote Canvas instance.")
        self._content_id = value

    @property
    def type(self):
        """the type of object referred to one of 'File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool'."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def id(self):
        """the unique identifier for the module item."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def page_url(self):
        """(only for 'Page' type) unique locator for the linked wiki page."""
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        """Setter for page_url property."""
        self.logger.warn("Setting values on page_url will NOT update the remote Canvas instance.")
        self._page_url = value


class Moduleitemsequencenode(BaseModel):
    """Moduleitemsequencenode Model."""

    def __init__(self, current=None, prev=None, next=None):
        """Init method for Moduleitemsequencenode class."""
        self._current = current
        self._prev = prev
        self._next = next

        self.logger = logging.getLogger('pycanvas.Moduleitemsequencenode')

    @property
    def current(self):
        """current."""
        return self._current

    @current.setter
    def current(self, value):
        """Setter for current property."""
        self.logger.warn("Setting values on current will NOT update the remote Canvas instance.")
        self._current = value

    @property
    def prev(self):
        """prev."""
        return self._prev

    @prev.setter
    def prev(self, value):
        """Setter for prev property."""
        self.logger.warn("Setting values on prev will NOT update the remote Canvas instance.")
        self._prev = value

    @property
    def next(self):
        """next."""
        return self._next

    @next.setter
    def next(self, value):
        """Setter for next property."""
        self.logger.warn("Setting values on next will NOT update the remote Canvas instance.")
        self._next = value


class Moduleitemcontentdetails(BaseModel):
    """Moduleitemcontentdetails Model."""

    def __init__(self, unlock_at=None, due_at=None, points_possible=None, lock_info=None, lock_at=None, lock_explanation=None, locked_for_user=None):
        """Init method for Moduleitemcontentdetails class."""
        self._unlock_at = unlock_at
        self._due_at = due_at
        self._points_possible = points_possible
        self._lock_info = lock_info
        self._lock_at = lock_at
        self._lock_explanation = lock_explanation
        self._locked_for_user = locked_for_user

        self.logger = logging.getLogger('pycanvas.Moduleitemcontentdetails')

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
    def due_at(self):
        """due_at."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def points_possible(self):
        """points_possible."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

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
    def lock_explanation(self):
        """lock_explanation."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def locked_for_user(self):
        """locked_for_user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

