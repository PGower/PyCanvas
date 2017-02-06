"""OutcomeGroups API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class OutcomeGroupsAPI(BaseCanvasAPI):
    """OutcomeGroups API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OutcomeGroupsAPI."""
        super(OutcomeGroupsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.OutcomeGroupsAPI")

    def redirect_to_root_outcome_group_for_context_global(self):
        """
        Redirect to root outcome group for context.

        Convenience redirect to find the root outcome group for a particular
        context. Will redirect to the appropriate outcome group's URL.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/global/root_outcome_group with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/global/root_outcome_group".format(**path), data=data, params=params, no_data=True)

    def redirect_to_root_outcome_group_for_context_accounts(self, account_id):
        """
        Redirect to root outcome group for context.

        Convenience redirect to find the root outcome group for a particular
        context. Will redirect to the appropriate outcome group's URL.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/root_outcome_group with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/root_outcome_group".format(**path), data=data, params=params, no_data=True)

    def redirect_to_root_outcome_group_for_context_courses(self, course_id):
        """
        Redirect to root outcome group for context.

        Convenience redirect to find the root outcome group for a particular
        context. Will redirect to the appropriate outcome group's URL.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/root_outcome_group with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/root_outcome_group".format(**path), data=data, params=params, no_data=True)

    def get_all_outcome_groups_for_context_accounts(self, account_id):
        """
        Get all outcome groups for context.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_groups".format(**path), data=data, params=params, all_pages=True)

    def get_all_outcome_groups_for_context_courses(self, course_id):
        """
        Get all outcome groups for context.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_groups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_groups".format(**path), data=data, params=params, all_pages=True)

    def get_all_outcome_links_for_context_accounts(self, account_id, outcome_group_style=None, outcome_style=None):
        """
        Get all outcome links for context.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # OPTIONAL - outcome_style
        """The detail level of the outcomes. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_style is not None:
            params["outcome_style"] = outcome_style

        # OPTIONAL - outcome_group_style
        """The detail level of the outcome groups. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_group_style is not None:
            params["outcome_group_style"] = outcome_group_style

        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_group_links with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_group_links".format(**path), data=data, params=params, all_pages=True)

    def get_all_outcome_links_for_context_courses(self, course_id, outcome_group_style=None, outcome_style=None):
        """
        Get all outcome links for context.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # OPTIONAL - outcome_style
        """The detail level of the outcomes. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_style is not None:
            params["outcome_style"] = outcome_style

        # OPTIONAL - outcome_group_style
        """The detail level of the outcome groups. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_group_style is not None:
            params["outcome_group_style"] = outcome_group_style

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_group_links with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_group_links".format(**path), data=data, params=params, all_pages=True)

    def show_outcome_group_global(self, id):
        """
        Show an outcome group.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/global/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/global/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def show_outcome_group_accounts(self, id, account_id):
        """
        Show an outcome group.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def show_outcome_group_courses(self, id, course_id):
        """
        Show an outcome group.

        
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

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def update_outcome_group_global(self, id, description=None, parent_outcome_group_id=None, title=None, vendor_guid=None):
        """
        Update an outcome group.

        Modify an existing outcome group. Fields not provided are left as is;
        unrecognized fields are ignored.
        
        When changing the parent outcome group, the new parent group must belong to
        the same context as this outcome group, and must not be a descendant of
        this outcome group (i.e. no cycles allowed).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - title
        """The new outcome group title."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - description
        """The new outcome group description."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - parent_outcome_group_id
        """The id of the new parent outcome group."""
        if parent_outcome_group_id is not None:
            data["parent_outcome_group_id"] = parent_outcome_group_id

        self.logger.debug("PUT /api/v1/global/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/global/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def update_outcome_group_accounts(self, id, account_id, description=None, parent_outcome_group_id=None, title=None, vendor_guid=None):
        """
        Update an outcome group.

        Modify an existing outcome group. Fields not provided are left as is;
        unrecognized fields are ignored.
        
        When changing the parent outcome group, the new parent group must belong to
        the same context as this outcome group, and must not be a descendant of
        this outcome group (i.e. no cycles allowed).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - title
        """The new outcome group title."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - description
        """The new outcome group description."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - parent_outcome_group_id
        """The id of the new parent outcome group."""
        if parent_outcome_group_id is not None:
            data["parent_outcome_group_id"] = parent_outcome_group_id

        self.logger.debug("PUT /api/v1/accounts/{account_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def update_outcome_group_courses(self, id, course_id, description=None, parent_outcome_group_id=None, title=None, vendor_guid=None):
        """
        Update an outcome group.

        Modify an existing outcome group. Fields not provided are left as is;
        unrecognized fields are ignored.
        
        When changing the parent outcome group, the new parent group must belong to
        the same context as this outcome group, and must not be a descendant of
        this outcome group (i.e. no cycles allowed).
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

        # OPTIONAL - title
        """The new outcome group title."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - description
        """The new outcome group description."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - parent_outcome_group_id
        """The id of the new parent outcome group."""
        if parent_outcome_group_id is not None:
            data["parent_outcome_group_id"] = parent_outcome_group_id

        self.logger.debug("PUT /api/v1/courses/{course_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_outcome_group_global(self, id):
        """
        Delete an outcome group.

        Deleting an outcome group deletes descendant outcome groups and outcome
        links. The linked outcomes themselves are only deleted if all links to the
        outcome were deleted.
        
        Aligned outcomes cannot be deleted; as such, if all remaining links to an
        aligned outcome are included in this group's descendants, the group
        deletion will fail.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/global/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/global/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_outcome_group_accounts(self, id, account_id):
        """
        Delete an outcome group.

        Deleting an outcome group deletes descendant outcome groups and outcome
        links. The linked outcomes themselves are only deleted if all links to the
        outcome were deleted.
        
        Aligned outcomes cannot be deleted; as such, if all remaining links to an
        aligned outcome are included in this group's descendants, the group
        deletion will fail.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_outcome_group_courses(self, id, course_id):
        """
        Delete an outcome group.

        Deleting an outcome group deletes descendant outcome groups and outcome
        links. The linked outcomes themselves are only deleted if all links to the
        outcome were deleted.
        
        Aligned outcomes cannot be deleted; as such, if all remaining links to an
        aligned outcome are included in this group's descendants, the group
        deletion will fail.
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

        self.logger.debug("DELETE /api/v1/courses/{course_id}/outcome_groups/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/outcome_groups/{id}".format(**path), data=data, params=params, single_item=True)

    def list_linked_outcomes_global(self, id, outcome_style=None):
        """
        List linked outcomes.

        List the immediate OutcomeLink children of the outcome group. Paginated.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - outcome_style
        """The detail level of the outcomes. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_style is not None:
            params["outcome_style"] = outcome_style

        self.logger.debug("GET /api/v1/global/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/global/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, all_pages=True)

    def list_linked_outcomes_accounts(self, id, account_id, outcome_style=None):
        """
        List linked outcomes.

        List the immediate OutcomeLink children of the outcome group. Paginated.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - outcome_style
        """The detail level of the outcomes. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_style is not None:
            params["outcome_style"] = outcome_style

        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, all_pages=True)

    def list_linked_outcomes_courses(self, id, course_id, outcome_style=None):
        """
        List linked outcomes.

        List the immediate OutcomeLink children of the outcome group. Paginated.
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

        # OPTIONAL - outcome_style
        """The detail level of the outcomes. Defaults to "abbrev".
        Specify "full" for more information."""
        if outcome_style is not None:
            params["outcome_style"] = outcome_style

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, all_pages=True)

    def create_link_outcome_global(self, id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, outcome_id=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - outcome_id
        """The ID of the existing outcome to link."""
        if outcome_id is not None:
            data["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("POST /api/v1/global/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/global/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, single_item=True)

    def create_link_outcome_global_outcome_id(self, id, outcome_id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - PATH - outcome_id
        """The ID of the existing outcome to link."""
        path["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("PUT /api/v1/global/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/global/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def create_link_outcome_accounts(self, id, account_id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, outcome_id=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - outcome_id
        """The ID of the existing outcome to link."""
        if outcome_id is not None:
            data["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("POST /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, single_item=True)

    def create_link_outcome_accounts_outcome_id(self, id, account_id, outcome_id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - PATH - outcome_id
        """The ID of the existing outcome to link."""
        path["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("PUT /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def create_link_outcome_courses(self, id, course_id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, outcome_id=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
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

        # OPTIONAL - outcome_id
        """The ID of the existing outcome to link."""
        if outcome_id is not None:
            data["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("POST /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/outcome_groups/{id}/outcomes".format(**path), data=data, params=params, single_item=True)

    def create_link_outcome_courses_outcome_id(self, id, course_id, outcome_id, calculation_int=None, calculation_method=None, description=None, display_name=None, mastery_points=None, ratings_description=None, ratings_points=None, title=None, vendor_guid=None):
        """
        Create/link an outcome.

        Link an outcome into the outcome group. The outcome to link can either be
        specified by a PUT to the link URL for a specific outcome (the outcome_id
        in the PUT URLs) or by supplying the information for a new outcome (title,
        description, ratings, mastery_points) in a POST to the collection.
        
        If linking an existing outcome, the outcome_id must identify an outcome
        available to this context; i.e. an outcome owned by this group's context,
        an outcome owned by an associated account, or a global outcome. With
        outcome_id present, any other parameters are ignored.
        
        If defining a new outcome, the outcome is created in the outcome group's
        context using the provided title, description, ratings, and mastery points;
        the title is required but all other fields are optional. The new outcome
        is then linked into the outcome group.
        
        If ratings are provided when creating a new outcome, an embedded rubric
        criterion is included in the new outcome. This criterion's mastery_points
        default to the maximum points in the highest rating if not specified in the
        mastery_points parameter. Any ratings lacking a description are given a
        default of "No description". Any ratings lacking a point value are given a
        default of 0. If no ratings are provided, the mastery_points parameter is
        ignored.
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

        # REQUIRED - PATH - outcome_id
        """The ID of the existing outcome to link."""
        path["outcome_id"] = outcome_id

        # OPTIONAL - title
        """The title of the new outcome. Required if outcome_id is absent."""
        if title is not None:
            data["title"] = title

        # OPTIONAL - display_name
        """A friendly name shown in reports for outcomes with cryptic titles,
        such as common core standards names."""
        if display_name is not None:
            data["display_name"] = display_name

        # OPTIONAL - description
        """The description of the new outcome."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard."""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        # OPTIONAL - mastery_points
        """The mastery threshold for the embedded rubric criterion."""
        if mastery_points is not None:
            data["mastery_points"] = mastery_points

        # OPTIONAL - ratings[description]
        """The description of a rating level for the embedded rubric criterion."""
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description

        # OPTIONAL - ratings[points]
        """The points corresponding to a rating level for the embedded rubric criterion."""
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points

        # OPTIONAL - calculation_method
        """The new calculation method.  Defaults to "highest""""
        if calculation_method is not None:
            self._validate_enum(calculation_method, ["decaying_average", "n_mastery", "latest", "highest"])
            data["calculation_method"] = calculation_method

        # OPTIONAL - calculation_int
        """The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery""""
        if calculation_int is not None:
            data["calculation_int"] = calculation_int

        self.logger.debug("PUT /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def unlink_outcome_global(self, id, outcome_id):
        """
        Unlink an outcome.

        Unlinking an outcome only deletes the outcome itself if this was the last
        link to the outcome in any group in any context. Aligned outcomes cannot be
        deleted; as such, if this is the last link to an aligned outcome, the
        unlinking will fail.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - PATH - outcome_id
        """ID"""
        path["outcome_id"] = outcome_id

        self.logger.debug("DELETE /api/v1/global/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/global/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def unlink_outcome_accounts(self, id, account_id, outcome_id):
        """
        Unlink an outcome.

        Unlinking an outcome only deletes the outcome itself if this was the last
        link to the outcome in any group in any context. Aligned outcomes cannot be
        deleted; as such, if this is the last link to an aligned outcome, the
        unlinking will fail.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - PATH - outcome_id
        """ID"""
        path["outcome_id"] = outcome_id

        self.logger.debug("DELETE /api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def unlink_outcome_courses(self, id, course_id, outcome_id):
        """
        Unlink an outcome.

        Unlinking an outcome only deletes the outcome itself if this was the last
        link to the outcome in any group in any context. Aligned outcomes cannot be
        deleted; as such, if this is the last link to an aligned outcome, the
        unlinking will fail.
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

        # REQUIRED - PATH - outcome_id
        """ID"""
        path["outcome_id"] = outcome_id

        self.logger.debug("DELETE /api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}".format(**path), data=data, params=params, single_item=True)

    def list_subgroups_global(self, id):
        """
        List subgroups.

        List the immediate OutcomeGroup children of the outcome group. Paginated.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/global/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/global/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, all_pages=True)

    def list_subgroups_accounts(self, id, account_id):
        """
        List subgroups.

        List the immediate OutcomeGroup children of the outcome group. Paginated.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, all_pages=True)

    def list_subgroups_courses(self, id, course_id):
        """
        List subgroups.

        List the immediate OutcomeGroup children of the outcome group. Paginated.
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

        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, all_pages=True)

    def create_subgroup_global(self, id, title, description=None, vendor_guid=None):
        """
        Create a subgroup.

        Creates a new empty subgroup under the outcome group with the given title
        and description.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - title
        """The title of the new outcome group."""
        data["title"] = title

        # OPTIONAL - description
        """The description of the new outcome group."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard"""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        self.logger.debug("POST /api/v1/global/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/global/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, single_item=True)

    def create_subgroup_accounts(self, id, title, account_id, description=None, vendor_guid=None):
        """
        Create a subgroup.

        Creates a new empty subgroup under the outcome group with the given title
        and description.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - title
        """The title of the new outcome group."""
        data["title"] = title

        # OPTIONAL - description
        """The description of the new outcome group."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard"""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        self.logger.debug("POST /api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, single_item=True)

    def create_subgroup_courses(self, id, title, course_id, description=None, vendor_guid=None):
        """
        Create a subgroup.

        Creates a new empty subgroup under the outcome group with the given title
        and description.
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

        # REQUIRED - title
        """The title of the new outcome group."""
        data["title"] = title

        # OPTIONAL - description
        """The description of the new outcome group."""
        if description is not None:
            data["description"] = description

        # OPTIONAL - vendor_guid
        """A custom GUID for the learning standard"""
        if vendor_guid is not None:
            data["vendor_guid"] = vendor_guid

        self.logger.debug("POST /api/v1/courses/{course_id}/outcome_groups/{id}/subgroups with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/outcome_groups/{id}/subgroups".format(**path), data=data, params=params, single_item=True)

    def import_outcome_group_global(self, id, source_outcome_group_id):
        """
        Import an outcome group.

        Creates a new subgroup of the outcome group with the same title and
        description as the source group, then creates links in that new subgroup to
        the same outcomes that are linked in the source group. Recurses on the
        subgroups of the source group, importing them each in turn into the new
        subgroup.
        
        Allows you to copy organizational structure, but does not create copies of
        the outcomes themselves, only new links.
        
        The source group must be either global, from the same context as this
        outcome group, or from an associated account. The source group cannot be
        the root outcome group of its context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - source_outcome_group_id
        """The ID of the source outcome group."""
        data["source_outcome_group_id"] = source_outcome_group_id

        self.logger.debug("POST /api/v1/global/outcome_groups/{id}/import with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/global/outcome_groups/{id}/import".format(**path), data=data, params=params, single_item=True)

    def import_outcome_group_accounts(self, id, account_id, source_outcome_group_id):
        """
        Import an outcome group.

        Creates a new subgroup of the outcome group with the same title and
        description as the source group, then creates links in that new subgroup to
        the same outcomes that are linked in the source group. Recurses on the
        subgroups of the source group, importing them each in turn into the new
        subgroup.
        
        Allows you to copy organizational structure, but does not create copies of
        the outcomes themselves, only new links.
        
        The source group must be either global, from the same context as this
        outcome group, or from an associated account. The source group cannot be
        the root outcome group of its context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # REQUIRED - source_outcome_group_id
        """The ID of the source outcome group."""
        data["source_outcome_group_id"] = source_outcome_group_id

        self.logger.debug("POST /api/v1/accounts/{account_id}/outcome_groups/{id}/import with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/outcome_groups/{id}/import".format(**path), data=data, params=params, single_item=True)

    def import_outcome_group_courses(self, id, course_id, source_outcome_group_id):
        """
        Import an outcome group.

        Creates a new subgroup of the outcome group with the same title and
        description as the source group, then creates links in that new subgroup to
        the same outcomes that are linked in the source group. Recurses on the
        subgroups of the source group, importing them each in turn into the new
        subgroup.
        
        Allows you to copy organizational structure, but does not create copies of
        the outcomes themselves, only new links.
        
        The source group must be either global, from the same context as this
        outcome group, or from an associated account. The source group cannot be
        the root outcome group of its context.
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

        # REQUIRED - source_outcome_group_id
        """The ID of the source outcome group."""
        data["source_outcome_group_id"] = source_outcome_group_id

        self.logger.debug("POST /api/v1/courses/{course_id}/outcome_groups/{id}/import with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/outcome_groups/{id}/import".format(**path), data=data, params=params, single_item=True)


class Outcomegroup(BaseModel):
    """Outcomegroup Model."""

    def __init__(self, vendor_guid=None, can_edit=None, description=None, title=None, url=None, context_id=None, import_url=None, id=None, parent_outcome_group=None, outcomes_url=None, subgroups_url=None, context_type=None):
        """Init method for Outcomegroup class."""
        self._vendor_guid = vendor_guid
        self._can_edit = can_edit
        self._description = description
        self._title = title
        self._url = url
        self._context_id = context_id
        self._import_url = import_url
        self._id = id
        self._parent_outcome_group = parent_outcome_group
        self._outcomes_url = outcomes_url
        self._subgroups_url = subgroups_url
        self._context_type = context_type

        self.logger = logging.getLogger('pycanvas.Outcomegroup')

    @property
    def vendor_guid(self):
        """A custom GUID for the learning standard."""
        return self._vendor_guid

    @vendor_guid.setter
    def vendor_guid(self, value):
        """Setter for vendor_guid property."""
        self.logger.warn("Setting values on vendor_guid will NOT update the remote Canvas instance.")
        self._vendor_guid = value

    @property
    def can_edit(self):
        """whether the current user can update the outcome group."""
        return self._can_edit

    @can_edit.setter
    def can_edit(self, value):
        """Setter for can_edit property."""
        self.logger.warn("Setting values on can_edit will NOT update the remote Canvas instance.")
        self._can_edit = value

    @property
    def description(self):
        """description of the outcome group. omitted in the abbreviated form."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def title(self):
        """title of the outcome group."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """the URL for fetching/updating the outcome group. should be treated as opaque."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def context_id(self):
        """the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def import_url(self):
        """the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form."""
        return self._import_url

    @import_url.setter
    def import_url(self, value):
        """Setter for import_url property."""
        self.logger.warn("Setting values on import_url will NOT update the remote Canvas instance.")
        self._import_url = value

    @property
    def id(self):
        """the ID of the outcome group."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def parent_outcome_group(self):
        """an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form."""
        return self._parent_outcome_group

    @parent_outcome_group.setter
    def parent_outcome_group(self, value):
        """Setter for parent_outcome_group property."""
        self.logger.warn("Setting values on parent_outcome_group will NOT update the remote Canvas instance.")
        self._parent_outcome_group = value

    @property
    def outcomes_url(self):
        """the URL for listing/creating outcome links under the outcome group. should be treated as opaque."""
        return self._outcomes_url

    @outcomes_url.setter
    def outcomes_url(self, value):
        """Setter for outcomes_url property."""
        self.logger.warn("Setting values on outcomes_url will NOT update the remote Canvas instance.")
        self._outcomes_url = value

    @property
    def subgroups_url(self):
        """the URL for listing/creating subgroups under the outcome group. should be treated as opaque."""
        return self._subgroups_url

    @subgroups_url.setter
    def subgroups_url(self, value):
        """Setter for subgroups_url property."""
        self.logger.warn("Setting values on subgroups_url will NOT update the remote Canvas instance.")
        self._subgroups_url = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value


class Outcomelink(BaseModel):
    """Outcomelink Model."""

    def __init__(self, url=None, context_id=None, context_type=None, can_unlink=None, outcome_group=None, assessed=None, outcome=None):
        """Init method for Outcomelink class."""
        self._url = url
        self._context_id = context_id
        self._context_type = context_type
        self._can_unlink = can_unlink
        self._outcome_group = outcome_group
        self._assessed = assessed
        self._outcome = outcome

        self.logger = logging.getLogger('pycanvas.Outcomelink')

    @property
    def url(self):
        """the URL for fetching/updating the outcome link. should be treated as opaque."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def context_id(self):
        """the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

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
    def can_unlink(self):
        """whether this outcome link is manageable and is not the last link to an aligned outcome."""
        return self._can_unlink

    @can_unlink.setter
    def can_unlink(self, value):
        """Setter for can_unlink property."""
        self.logger.warn("Setting values on can_unlink will NOT update the remote Canvas instance.")
        self._can_unlink = value

    @property
    def outcome_group(self):
        """an abbreviated OutcomeGroup object representing the group containing the outcome link."""
        return self._outcome_group

    @outcome_group.setter
    def outcome_group(self, value):
        """Setter for outcome_group property."""
        self.logger.warn("Setting values on outcome_group will NOT update the remote Canvas instance.")
        self._outcome_group = value

    @property
    def assessed(self):
        """whether this outcome has been used to assess a student in the context of this outcome link.  In other words, this will be set to true if the context is a course, and a student has been assessed with this outcome in that course."""
        return self._assessed

    @assessed.setter
    def assessed(self, value):
        """Setter for assessed property."""
        self.logger.warn("Setting values on assessed will NOT update the remote Canvas instance.")
        self._assessed = value

    @property
    def outcome(self):
        """an abbreviated Outcome object representing the outcome linked into the containing outcome group."""
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        """Setter for outcome property."""
        self.logger.warn("Setting values on outcome will NOT update the remote Canvas instance.")
        self._outcome = value

