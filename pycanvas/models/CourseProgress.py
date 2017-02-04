import datetime.date
import datetime.datetime
import dateutil.parser

from base import BaseModel

from ..meta.courseprogress import CourseprogressModelMetadata

class Courseprogress(BaseModel):
    metadata = CourseprogressModelMetadata

    attributes = CourseprogressModelMetadata.attributes

    def __init__(self, completed_at=None, next_requirement_url=None, requirement_completed_count=None, requirement_count=None, *args, **kwargs):
        """"""
        self.requirement_count = requirement_count
        self.next_requirement_url = next_requirement_url
        self.requirement_completed_count = requirement_completed_count
        self.completed_at = completed_at
        