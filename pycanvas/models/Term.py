import datetime.date
import datetime.datetime
import dateutil.parser

from base import BaseModel

from ..meta.term import TermModelMetadata

class Term(BaseModel):
    metadata = TermModelMetadata

    attributes = TermModelMetadata.attributes

    def __init__(self, end_at=None, id=None, name=None, start_at=None, *args, **kwargs):
        """"""
        self.start_at = start_at
        self.id = id
        self.name = name
        self.end_at = end_at
