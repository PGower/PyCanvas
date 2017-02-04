"""Base Model class for all PyCanvas Models."""
import json
from six import iteritems


class BaseModel(object):
    """Base Model Class for all PyCanvas Models."""

    attributes = {}

    def to_json(self, recursive=False, levels=0):
        """Return a JSON representation of the model data.

        :param recursive: If true then recursively convert child objects to JSON as well.
        :param levels: The number of levels of child objects to convert to JSON. If 0 convert all.
        """
        r = self.to_dict()
        return json.dumps(r)
    to_JSON = to_json

    @classmethod
    def from_json(cls, json_text):
        """Return a model equivalent of the passed JSON data."""
        d = json.loads(json_text)
        a = []

        for name, defn in cls.attributes.items():
            

        
        

    def to_dict(self, filter_none=True):
        """Return the model properties as a dict."""
        r = {}
        # Get required params first
        for name, defn in self.attributes.items():
            if defn.get('required', False):
                r[name] = getattr(self, name)
            else:
                v = getattr(self, name)
                if filter_none and v is None:
                    continue
                r[name] = v
        return r




    def __validate_assignment(self, name, value, meta):
        """Validate the value for attribute name."""
        if 



    def __unicode__(self):
        """String description of the model."""
        _id = getattr(self, 'id', 'None')
        _name = getattr(self, 'name', 'None')
        _class = self.__class__.__name__
        return u'{}(id:{}, name:{})'.format(_class, _id, _name)

    def __str__(self):
        """Return _unicode__."""
        return unicode(self).encode('utf-8')

    def __repr__(self):
        """Concise representation of the model."""
        _class = self.__class__.__name__
        a = []
        for k in self.attribute_types.keys():
            name = k
            kind = self.attribute_types[k]
            value = getattr(self, name, None)
            a.append(name, kind, value)
        return u'{}({})'.format(_class, ','.join(['{}={}({})'.format(n, k, v) for n, k, v in a]))


class MissingRequiredAttributeError(Exception):
    def __init__(self, missing_attribute):
        self.ma = missing_attribute

    def __unicode__(self):
        return u'Missing required attribute: {}'.format(self.ma)