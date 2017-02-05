"""Pages API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class PagesAPI(BaseCanvasAPI):
    """Pages API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PagesAPI."""
        super(PagesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.PagesAPI")

    def show_front_page_courses(self, course_id):
        """
        Show front page.

        Retrieve the content of the front page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/front_page with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/front_page".format(**path), data=data, params=params, single_item=True)

    def show_front_page_groups(self, group_id):
        """
        Show front page.

        Retrieve the content of the front page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id

        self.logger.debug("GET /api/v1/groups/{group_id}/front_page with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/front_page".format(**path), data=data, params=params, single_item=True)

    def update_create_front_page_courses(self, course_id, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_notify_of_update=None, wiki_page_published=None, wiki_page_title=None):
        """
        Update/create front page.

        Update the title or contents of the front page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - wiki_page[title] - The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        if wiki_page_title is not None:
            data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published

        self.logger.debug("PUT /api/v1/courses/{course_id}/front_page with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/front_page".format(**path), data=data, params=params, single_item=True)

    def update_create_front_page_groups(self, group_id, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_notify_of_update=None, wiki_page_published=None, wiki_page_title=None):
        """
        Update/create front page.

        Update the title or contents of the front page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - wiki_page[title] - The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        if wiki_page_title is not None:
            data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published

        self.logger.debug("PUT /api/v1/groups/{group_id}/front_page with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/front_page".format(**path), data=data, params=params, single_item=True)

    def list_pages_courses(self, course_id, order=None, published=None, search_term=None, sort=None):
        """
        List pages.

        List the wiki pages associated with a course or group
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - sort - Sort results by this field.
        if sort is not None:
            self._validate_enum(sort, ["title", "created_at", "updated_at"])
            params["sort"] = sort
        # OPTIONAL - order - The sorting order. Defaults to 'asc'.
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order
        # OPTIONAL - search_term - The partial title of the pages to match and return.
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - published - If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status.
        if published is not None:
            params["published"] = published

        self.logger.debug("GET /api/v1/courses/{course_id}/pages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/pages".format(**path), data=data, params=params, all_pages=True)

    def list_pages_groups(self, group_id, order=None, published=None, search_term=None, sort=None):
        """
        List pages.

        List the wiki pages associated with a course or group
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # OPTIONAL - sort - Sort results by this field.
        if sort is not None:
            self._validate_enum(sort, ["title", "created_at", "updated_at"])
            params["sort"] = sort
        # OPTIONAL - order - The sorting order. Defaults to 'asc'.
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order
        # OPTIONAL - search_term - The partial title of the pages to match and return.
        if search_term is not None:
            params["search_term"] = search_term
        # OPTIONAL - published - If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status.
        if published is not None:
            params["published"] = published

        self.logger.debug("GET /api/v1/groups/{group_id}/pages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/pages".format(**path), data=data, params=params, all_pages=True)

    def create_page_courses(self, course_id, wiki_page_title, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_front_page=None, wiki_page_notify_of_update=None, wiki_page_published=None):
        """
        Create page.

        Create a new wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - wiki_page[title] - The title for the new page.
        data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published
        # OPTIONAL - wiki_page[front_page] - Set an unhidden page as the front page (if true)
        if wiki_page_front_page is not None:
            data["wiki_page[front_page]"] = wiki_page_front_page

        self.logger.debug("POST /api/v1/courses/{course_id}/pages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/pages".format(**path), data=data, params=params, single_item=True)

    def create_page_groups(self, group_id, wiki_page_title, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_front_page=None, wiki_page_notify_of_update=None, wiki_page_published=None):
        """
        Create page.

        Create a new wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - wiki_page[title] - The title for the new page.
        data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published
        # OPTIONAL - wiki_page[front_page] - Set an unhidden page as the front page (if true)
        if wiki_page_front_page is not None:
            data["wiki_page[front_page]"] = wiki_page_front_page

        self.logger.debug("POST /api/v1/groups/{group_id}/pages with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/pages".format(**path), data=data, params=params, single_item=True)

    def show_page_courses(self, url, course_id):
        """
        Show page.

        Retrieve the content of a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("GET /api/v1/courses/{course_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def show_page_groups(self, url, group_id):
        """
        Show page.

        Retrieve the content of a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("GET /api/v1/groups/{group_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def update_create_page_courses(self, url, course_id, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_front_page=None, wiki_page_notify_of_update=None, wiki_page_published=None, wiki_page_title=None):
        """
        Update/create page.

        Update the title or contents of a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # OPTIONAL - wiki_page[title] - The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        if wiki_page_title is not None:
            data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published
        # OPTIONAL - wiki_page[front_page] - Set an unhidden page as the front page (if true)
        if wiki_page_front_page is not None:
            data["wiki_page[front_page]"] = wiki_page_front_page

        self.logger.debug("PUT /api/v1/courses/{course_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def update_create_page_groups(self, url, group_id, wiki_page_body=None, wiki_page_editing_roles=None, wiki_page_front_page=None, wiki_page_notify_of_update=None, wiki_page_published=None, wiki_page_title=None):
        """
        Update/create page.

        Update the title or contents of a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # OPTIONAL - wiki_page[title] - The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result.
        if wiki_page_title is not None:
            data["wiki_page[title]"] = wiki_page_title
        # OPTIONAL - wiki_page[body] - The content for the new page.
        if wiki_page_body is not None:
            data["wiki_page[body]"] = wiki_page_body
        # OPTIONAL - wiki_page[editing_roles] - Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas). "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user.
        if wiki_page_editing_roles is not None:
            self._validate_enum(wiki_page_editing_roles, ["teachers", "students", "members", "public"])
            data["wiki_page[editing_roles]"] = wiki_page_editing_roles
        # OPTIONAL - wiki_page[notify_of_update] - Whether participants should be notified when this page changes.
        if wiki_page_notify_of_update is not None:
            data["wiki_page[notify_of_update]"] = wiki_page_notify_of_update
        # OPTIONAL - wiki_page[published] - Whether the page is published (true) or draft state (false).
        if wiki_page_published is not None:
            data["wiki_page[published]"] = wiki_page_published
        # OPTIONAL - wiki_page[front_page] - Set an unhidden page as the front page (if true)
        if wiki_page_front_page is not None:
            data["wiki_page[front_page]"] = wiki_page_front_page

        self.logger.debug("PUT /api/v1/groups/{group_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def delete_page_courses(self, url, course_id):
        """
        Delete page.

        Delete a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("DELETE /api/v1/courses/{course_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def delete_page_groups(self, url, group_id):
        """
        Delete page.

        Delete a wiki page
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("DELETE /api/v1/groups/{group_id}/pages/{url} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/groups/{group_id}/pages/{url}".format(**path), data=data, params=params, single_item=True)

    def list_revisions_courses(self, url, course_id):
        """
        List revisions.

        List the revisions of a page. Callers must have update rights on the page in order to see page history.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("GET /api/v1/courses/{course_id}/pages/{url}/revisions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/pages/{url}/revisions".format(**path), data=data, params=params, all_pages=True)

    def list_revisions_groups(self, url, group_id):
        """
        List revisions.

        List the revisions of a page. Callers must have update rights on the page in order to see page history.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url

        self.logger.debug("GET /api/v1/groups/{group_id}/pages/{url}/revisions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/pages/{url}/revisions".format(**path), data=data, params=params, all_pages=True)

    def show_revision_courses_latest(self, url, course_id, summary=None):
        """
        Show revision.

        Retrieve the metadata and optionally content of a revision of the page.
        Note that retrieving historic versions of pages requires edit rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # OPTIONAL - summary - If set, exclude page content from results
        if summary is not None:
            params["summary"] = summary

        self.logger.debug("GET /api/v1/courses/{course_id}/pages/{url}/revisions/latest with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/pages/{url}/revisions/latest".format(**path), data=data, params=params, single_item=True)

    def show_revision_groups_latest(self, url, group_id, summary=None):
        """
        Show revision.

        Retrieve the metadata and optionally content of a revision of the page.
        Note that retrieving historic versions of pages requires edit rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # OPTIONAL - summary - If set, exclude page content from results
        if summary is not None:
            params["summary"] = summary

        self.logger.debug("GET /api/v1/groups/{group_id}/pages/{url}/revisions/latest with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/pages/{url}/revisions/latest".format(**path), data=data, params=params, single_item=True)

    def show_revision_courses_revision_id(self, url, course_id, revision_id, summary=None):
        """
        Show revision.

        Retrieve the metadata and optionally content of a revision of the page.
        Note that retrieving historic versions of pages requires edit rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # REQUIRED - PATH - revision_id - ID
        path["revision_id"] = revision_id
        # OPTIONAL - summary - If set, exclude page content from results
        if summary is not None:
            params["summary"] = summary

        self.logger.debug("GET /api/v1/courses/{course_id}/pages/{url}/revisions/{revision_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/pages/{url}/revisions/{revision_id}".format(**path), data=data, params=params, single_item=True)

    def show_revision_groups_revision_id(self, url, group_id, revision_id, summary=None):
        """
        Show revision.

        Retrieve the metadata and optionally content of a revision of the page.
        Note that retrieving historic versions of pages requires edit rights.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # REQUIRED - PATH - revision_id - ID
        path["revision_id"] = revision_id
        # OPTIONAL - summary - If set, exclude page content from results
        if summary is not None:
            params["summary"] = summary

        self.logger.debug("GET /api/v1/groups/{group_id}/pages/{url}/revisions/{revision_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/pages/{url}/revisions/{revision_id}".format(**path), data=data, params=params, single_item=True)

    def revert_to_revision_courses(self, url, course_id, revision_id):
        """
        Revert to revision.

        Revert a page to a prior revision.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # REQUIRED - PATH - revision_id - The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
        path["revision_id"] = revision_id

        self.logger.debug("POST /api/v1/courses/{course_id}/pages/{url}/revisions/{revision_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/pages/{url}/revisions/{revision_id}".format(**path), data=data, params=params, single_item=True)

    def revert_to_revision_groups(self, url, group_id, revision_id):
        """
        Revert to revision.

        Revert a page to a prior revision.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id - ID
        path["group_id"] = group_id
        # REQUIRED - PATH - url - ID
        path["url"] = url
        # REQUIRED - PATH - revision_id - The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions)
        path["revision_id"] = revision_id

        self.logger.debug("POST /api/v1/groups/{group_id}/pages/{url}/revisions/{revision_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/pages/{url}/revisions/{revision_id}".format(**path), data=data, params=params, single_item=True)


class Pagerevision(BaseModel):
    """Pagerevision Model."""

    def __init__(self, body=None, edited_by=None, title=None, url=None, updated_at=None, revision_id=None, latest=None):
        """Init method for Pagerevision class."""
        self._body = body
        self._edited_by = edited_by
        self._title = title
        self._url = url
        self._updated_at = updated_at
        self._revision_id = revision_id
        self._latest = latest

        self.logger = logging.getLogger('pycanvas.Pagerevision')

    @property
    def body(self):
        """the historic page contents."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def edited_by(self):
        """the User who saved this revision, if applicable (this may not be present if the page was imported from another system)."""
        return self._edited_by

    @edited_by.setter
    def edited_by(self, value):
        """Setter for edited_by property."""
        self.logger.warn("Setting values on edited_by will NOT update the remote Canvas instance.")
        self._edited_by = value

    @property
    def title(self):
        """the historic page title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """the following fields are not included in the index action and may be omitted from the show action via summary=1 the historic url of the page."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def updated_at(self):
        """the time when this revision was saved."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def revision_id(self):
        """an identifier for this revision of the page."""
        return self._revision_id

    @revision_id.setter
    def revision_id(self, value):
        """Setter for revision_id property."""
        self.logger.warn("Setting values on revision_id will NOT update the remote Canvas instance.")
        self._revision_id = value

    @property
    def latest(self):
        """whether this is the latest revision or not."""
        return self._latest

    @latest.setter
    def latest(self, value):
        """Setter for latest property."""
        self.logger.warn("Setting values on latest will NOT update the remote Canvas instance.")
        self._latest = value


class Page(BaseModel):
    """Page Model."""

    def __init__(self, body=None, lock_info=None, title=None, url=None, created_at=None, front_page=None, hide_from_students=None, updated_at=None, editing_roles=None, published=None, lock_explanation=None, last_edited_by=None, locked_for_user=None):
        """Init method for Page class."""
        self._body = body
        self._lock_info = lock_info
        self._title = title
        self._url = url
        self._created_at = created_at
        self._front_page = front_page
        self._hide_from_students = hide_from_students
        self._updated_at = updated_at
        self._editing_roles = editing_roles
        self._published = published
        self._lock_explanation = lock_explanation
        self._last_edited_by = last_edited_by
        self._locked_for_user = locked_for_user

        self.logger = logging.getLogger('pycanvas.Page')

    @property
    def body(self):
        """the page content, in HTML (present when requesting a single page; omitted when listing pages)."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def lock_info(self):
        """(Optional) Information for the user about the lock. Present when locked_for_user is true."""
        return self._lock_info

    @lock_info.setter
    def lock_info(self, value):
        """Setter for lock_info property."""
        self.logger.warn("Setting values on lock_info will NOT update the remote Canvas instance.")
        self._lock_info = value

    @property
    def title(self):
        """the title of the page."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def url(self):
        """the unique locator for the page."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def created_at(self):
        """the creation date for the page."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def front_page(self):
        """whether this page is the front page for the wiki."""
        return self._front_page

    @front_page.setter
    def front_page(self, value):
        """Setter for front_page property."""
        self.logger.warn("Setting values on front_page will NOT update the remote Canvas instance.")
        self._front_page = value

    @property
    def hide_from_students(self):
        """(DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value)."""
        return self._hide_from_students

    @hide_from_students.setter
    def hide_from_students(self, value):
        """Setter for hide_from_students property."""
        self.logger.warn("Setting values on hide_from_students will NOT update the remote Canvas instance.")
        self._hide_from_students = value

    @property
    def updated_at(self):
        """the date the page was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def editing_roles(self):
        """roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used."""
        return self._editing_roles

    @editing_roles.setter
    def editing_roles(self, value):
        """Setter for editing_roles property."""
        self.logger.warn("Setting values on editing_roles will NOT update the remote Canvas instance.")
        self._editing_roles = value

    @property
    def published(self):
        """whether the page is published (true) or draft state (false)."""
        return self._published

    @published.setter
    def published(self, value):
        """Setter for published property."""
        self.logger.warn("Setting values on published will NOT update the remote Canvas instance.")
        self._published = value

    @property
    def lock_explanation(self):
        """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def last_edited_by(self):
        """the User who last edited the page (this may not be present if the page was imported from another system)."""
        return self._last_edited_by

    @last_edited_by.setter
    def last_edited_by(self, value):
        """Setter for last_edited_by property."""
        self.logger.warn("Setting values on last_edited_by will NOT update the remote Canvas instance.")
        self._last_edited_by = value

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

