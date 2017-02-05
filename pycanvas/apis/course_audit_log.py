"""CourseAuditLog API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from base import BaseCanvasAPI
from base import BaseModel


class CourseAuditLogAPI(BaseCanvasAPI):
    """CourseAuditLog API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CourseAuditLogAPI."""
        super(CourseAuditLogAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.CourseAuditLogAPI")

    def query_by_course(self, course_id, end_time=None, start_time=None):
        """
        Query by course.

        List course change events for a given course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id - ID
        path["course_id"] = course_id
        # OPTIONAL - start_time - The beginning of the time range from which you want events.
        if start_time is not None:
            if issubclass(start_time.__class__, date) or issubclass(start_time.__class__, datetime):
                start_time = start_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(start_time.__class__, basestring):
                start_time = self._validate_iso8601_string(start_time)
            params["start_time"] = start_time
        # OPTIONAL - end_time - The end of the time range from which you want events.
        if end_time is not None:
            if issubclass(end_time.__class__, date) or issubclass(end_time.__class__, datetime):
                end_time = end_time.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            elif issubclass(end_time.__class__, basestring):
                end_time = self._validate_iso8601_string(end_time)
            params["end_time"] = end_time

        self.logger.debug("GET /api/v1/audit/course/courses/{course_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/audit/course/courses/{course_id}".format(**path), data=data, params=params, all_pages=True)


class Createdeventdata(BaseModel):
    """Createdeventdata Model.
    The created event data object returns all the fields that were set in the format of the following example.  If a field does not exist it was not set. The value of each field changed is in the format of [:old_value, :new_value].  The created event type also includes a created_source field to specify what triggered the creation of the course."""

    def __init__(self, is_public=None, conclude_at=None, start_at=None, name=None, created_source=None):
        """Init method for Createdeventdata class."""
        self._is_public = is_public
        self._conclude_at = conclude_at
        self._start_at = start_at
        self._name = name
        self._created_source = created_source

        self.logger = logging.getLogger('pycanvas.Createdeventdata')

    @property
    def is_public(self):
        """is_public."""
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        """Setter for is_public property."""
        self.logger.warn("Setting values on is_public will NOT update the remote Canvas instance.")
        self._is_public = value

    @property
    def conclude_at(self):
        """conclude_at."""
        return self._conclude_at

    @conclude_at.setter
    def conclude_at(self, value):
        """Setter for conclude_at property."""
        self.logger.warn("Setting values on conclude_at will NOT update the remote Canvas instance.")
        self._conclude_at = value

    @property
    def start_at(self):
        """start_at."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

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
    def created_source(self):
        """created_source."""
        return self._created_source

    @created_source.setter
    def created_source(self, value):
        """Setter for created_source property."""
        self.logger.warn("Setting values on created_source will NOT update the remote Canvas instance.")
        self._created_source = value


class Courseevent(BaseModel):
    """Courseevent Model."""

    def __init__(self, event_source=None, event_type=None, links=None, created_at=None, id=None, event_data=None):
        """Init method for Courseevent class."""
        self._event_source = event_source
        self._event_type = event_type
        self._links = links
        self._created_at = created_at
        self._id = id
        self._event_data = event_data

        self.logger = logging.getLogger('pycanvas.Courseevent')

    @property
    def event_source(self):
        """Course event source depending on the event type.  This will return a string containing the source of the event."""
        return self._event_source

    @event_source.setter
    def event_source(self, value):
        """Setter for event_source property."""
        self.logger.warn("Setting values on event_source will NOT update the remote Canvas instance.")
        self._event_source = value

    @property
    def event_type(self):
        """Course event type The event type defines the type and schema of the event_data object."""
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """Setter for event_type property."""
        self.logger.warn("Setting values on event_type will NOT update the remote Canvas instance.")
        self._event_type = value

    @property
    def links(self):
        """Jsonapi.org links."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn("Setting values on links will NOT update the remote Canvas instance.")
        self._links = value

    @property
    def created_at(self):
        """timestamp of the event."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def id(self):
        """ID of the event."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def event_data(self):
        """Course event data depending on the event type.  This will return an object containing the relevant event data.  An updated event type will return an UpdatedEventData object."""
        return self._event_data

    @event_data.setter
    def event_data(self, value):
        """Setter for event_data property."""
        self.logger.warn("Setting values on event_data will NOT update the remote Canvas instance.")
        self._event_data = value


class Courseeventlink(BaseModel):
    """Courseeventlink Model."""

    def __init__(self, copied_from=None, course=None, sis_batch=None, user=None, copied_to=None, page_view=None):
        """Init method for Courseeventlink class."""
        self._copied_from = copied_from
        self._course = course
        self._sis_batch = sis_batch
        self._user = user
        self._copied_to = copied_to
        self._page_view = page_view

        self.logger = logging.getLogger('pycanvas.Courseeventlink')

    @property
    def copied_from(self):
        """ID of the course that this course was copied from. This is only included if the event_type is copied_from."""
        return self._copied_from

    @copied_from.setter
    def copied_from(self, value):
        """Setter for copied_from property."""
        self.logger.warn("Setting values on copied_from will NOT update the remote Canvas instance.")
        self._copied_from = value

    @property
    def course(self):
        """ID of the course for the event."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn("Setting values on course will NOT update the remote Canvas instance.")
        self._course = value

    @property
    def sis_batch(self):
        """ID of the SIS batch that triggered the event."""
        return self._sis_batch

    @sis_batch.setter
    def sis_batch(self, value):
        """Setter for sis_batch property."""
        self.logger.warn("Setting values on sis_batch will NOT update the remote Canvas instance.")
        self._sis_batch = value

    @property
    def user(self):
        """ID of the user for the event (who made the change)."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def copied_to(self):
        """ID of the course that this course was copied to. This is only included if the event_type is copied_to."""
        return self._copied_to

    @copied_to.setter
    def copied_to(self, value):
        """Setter for copied_to property."""
        self.logger.warn("Setting values on copied_to will NOT update the remote Canvas instance.")
        self._copied_to = value

    @property
    def page_view(self):
        """ID of the page view during the event if it exists."""
        return self._page_view

    @page_view.setter
    def page_view(self, value):
        """Setter for page_view property."""
        self.logger.warn("Setting values on page_view will NOT update the remote Canvas instance.")
        self._page_view = value


class Updatedeventdata(BaseModel):
    """Updatedeventdata Model.
    The updated event data object returns all the fields that have changed in the format of the following example.  If a field does not exist it was not changed.  The value is an array that contains the before and after values for the change as in [:old_value, :new_value]."""

    def __init__(self, is_public=None, conclude_at=None, start_at=None, name=None):
        """Init method for Updatedeventdata class."""
        self._is_public = is_public
        self._conclude_at = conclude_at
        self._start_at = start_at
        self._name = name

        self.logger = logging.getLogger('pycanvas.Updatedeventdata')

    @property
    def is_public(self):
        """is_public."""
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        """Setter for is_public property."""
        self.logger.warn("Setting values on is_public will NOT update the remote Canvas instance.")
        self._is_public = value

    @property
    def conclude_at(self):
        """conclude_at."""
        return self._conclude_at

    @conclude_at.setter
    def conclude_at(self, value):
        """Setter for conclude_at property."""
        self.logger.warn("Setting values on conclude_at will NOT update the remote Canvas instance.")
        self._conclude_at = value

    @property
    def start_at(self):
        """start_at."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn("Setting values on start_at will NOT update the remote Canvas instance.")
        self._start_at = value

    @property
    def name(self):
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

