"""Sections API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class SectionsAPI(BaseCanvasAPI):
    """Sections API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SectionsAPI."""
        super(SectionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.SectionsAPI")

    def list_course_sections(self, course_id, include=None):
        """
        List course sections.

        Returns the list of sections for this course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - include - - "students": Associations to include with the group. Note: this is only available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned. - "enrollments": If 'students' is also included, return the section enrollment for each student - "total_students": Returns the total amount of active and invited students for the course section - "passback_status": Include the grade passback status.
        if include is not None:
            self._validate_enum(include, ["students", "avatar_url", "enrollments", "total_students", "passback_status"])
            params["include"] = include

        self.logger.debug("GET /api/v1/courses/{course_id}/sections with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/sections".format(**path), data=data, params=params, all_pages=True)

    def create_course_section(self, course_id, course_section_end_at=None, course_section_name=None, course_section_restrict_enrollments_to_section_dates=None, course_section_sis_section_id=None, course_section_start_at=None):
        """
        Create course section.

        Creates a new section for this course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - course_section[name] - The name of the section
        if course_section_name is not None:
            data["course_section[name]"] = course_section_name
        # OPTIONAL - course_section[sis_section_id] - The sis ID of the section
        if course_section_sis_section_id is not None:
            data["course_section[sis_section_id]"] = course_section_sis_section_id
        # OPTIONAL - course_section[start_at] - Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        if course_section_start_at is not None:
            if issubclass(course_section_start_at.__class__, date) or issubclass(course_section_start_at.__class__, datetime):
                course_section_start_at = course_section_start_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(course_section_start_at.__class__, basestring):
                course_section_start_at = self._validate_iso8601_string(course_section_start_at)
            data["course_section[start_at]"] = course_section_start_at
        # OPTIONAL - course_section[end_at] - Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        if course_section_end_at is not None:
            if issubclass(course_section_end_at.__class__, date) or issubclass(course_section_end_at.__class__, datetime):
                course_section_end_at = course_section_end_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(course_section_end_at.__class__, basestring):
                course_section_end_at = self._validate_iso8601_string(course_section_end_at)
            data["course_section[end_at]"] = course_section_end_at
        # OPTIONAL - course_section[restrict_enrollments_to_section_dates] - Set to true to restrict user enrollments to the start and end dates of the section.
        if course_section_restrict_enrollments_to_section_dates is not None:
            data["course_section[restrict_enrollments_to_section_dates]"] = course_section_restrict_enrollments_to_section_dates

        self.logger.debug("POST /api/v1/courses/{course_id}/sections with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/sections".format(**path), data=data, params=params, single_item=True)

    def cross_list_section(self, id, new_course_id):
        """
        Cross-list a Section.

        Move the Section to another course.  The new course may be in a different account (department),
        but must belong to the same root account (institution).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - PATH - new_course_id - ID
        path["new_course_id"] = new_course_id

        self.logger.debug("POST /api/v1/sections/{id}/crosslist/{new_course_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{id}/crosslist/{new_course_id}".format(**path), data=data, params=params, single_item=True)

    def de_cross_list_section(self, id):
        """
        De-cross-list a Section.

        Undo cross-listing of a Section, returning it to its original course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/sections/{id}/crosslist with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/sections/{id}/crosslist".format(**path), data=data, params=params, single_item=True)

    def edit_section(self, id):
        """
        Edit a section.

        Modify an existing section.  See the documentation for {api:SectionsController#create create API action}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("PUT /api/v1/sections/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/sections/{id}".format(**path), data=data, params=params, single_item=True)

    def get_section_information_courses(self, id, course_id):
        """
        Get section information.

        Gets details about a specific section
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/sections/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/sections/{id}".format(**path), data=data, params=params, single_item=True)

    def get_section_information_sections(self, id):
        """
        Get section information.

        Gets details about a specific section
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("GET /api/v1/sections/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_section(self, id):
        """
        Delete a section.

        Delete an existing section.  Returns the former Section.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id - ID
        path["id"] = id

        self.logger.debug("DELETE /api/v1/sections/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/sections/{id}".format(**path), data=data, params=params, single_item=True)


class Section(BaseModel):
    """Section Model."""

    def __init__(self, integration_id=None, start_at=None, name=None, sis_course_id=None, end_at=None, sis_import_id=None, sis_section_id=None, course_id=None, nonxlist_course_id=None, total_students=None, id=None):
        """Init method for Section class."""
        self._integration_id = integration_id
        self._start_at = start_at
        self._name = name
        self._sis_course_id = sis_course_id
        self._end_at = end_at
        self._sis_import_id = sis_import_id
        self._sis_section_id = sis_section_id
        self._course_id = course_id
        self._nonxlist_course_id = nonxlist_course_id
        self._total_students = total_students
        self._id = id

        self.logger = logging.getLogger('pycanvas.Section')

    @property
    def integration_id(self):
        """Optional: The integration ID of the section. This field is only included if the user has permission to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def start_at(self):
        """the start date for the section, if applicable."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def name(self):
        """The name of the section."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def sis_course_id(self):
        """The unique SIS identifier for the course in which the section belongs. This field is only included if the user has permission to view SIS information."""
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, value):
        """Setter for sis_course_id property."""
        self.logger.warn("Setting values on sis_course_id will NOT update the remote Canvas instance.")
        self._sis_course_id = value

    @property
    def end_at(self):
        """the end date for the section, if applicable."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn("Setting values on end_at will NOT update the remote Canvas instance.")
        self._end_at = value

    @property
    def sis_import_id(self):
        """The unique identifier for the SIS import if created through SIS. This field is only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def sis_section_id(self):
        """The sis id of the section. This field is only included if the user has permission to view SIS information."""
        return self._sis_section_id

    @sis_section_id.setter
    def sis_section_id(self, value):
        """Setter for sis_section_id property."""
        self.logger.warn("Setting values on sis_section_id will NOT update the remote Canvas instance.")
        self._sis_section_id = value

    @property
    def course_id(self):
        """The unique Canvas identifier for the course in which the section belongs."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def nonxlist_course_id(self):
        """The unique identifier of the original course of a cross-listed section."""
        return self._nonxlist_course_id

    @nonxlist_course_id.setter
    def nonxlist_course_id(self, value):
        """Setter for nonxlist_course_id property."""
        self.logger.warn("Setting values on nonxlist_course_id will NOT update the remote Canvas instance.")
        self._nonxlist_course_id = value

    @property
    def total_students(self):
        """optional: the total number of active and invited students in the section."""
        return self._total_students

    @total_students.setter
    def total_students(self, value):
        """Setter for total_students property."""
        self.logger.warn("Setting values on total_students will NOT update the remote Canvas instance.")
        self._total_students = value

    @property
    def id(self):
        """The unique identifier for the section."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

