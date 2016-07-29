"""Base Model class for all PyCanvas Models."""
import json


class BaseModel(object):
    """Base Model Class for all PyCanvas Models."""

    def to_json(self):
        """Return a JSON representation of the model data."""
        r = self.to_dict()
        return json.dumps(r)
