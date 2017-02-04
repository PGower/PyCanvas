import datetime.date
import datetime.datetime
import dateutil.parser

from base import BaseModel

from ..meta.calendarlink import CalendarlinkModelMetadata

class Calendarlink(BaseModel):
    metadata = CalendarlinkModelMetadata

    attributes = CalendarlinkModelMetadata.attributes

    def __init__(self, ics=None, *args, **kwargs):
        """"""
        self.ics = ics
