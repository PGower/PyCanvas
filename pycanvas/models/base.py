"""Base Model class for all PyCanvas Models."""
import json
from six import iteritems


class BaseModel(object):
    """Base Model Class for all PyCanvas Models."""

    attribute_types = {}
    attribute_map = {}

    def to_json(self, recursive=False, levels=0):
        """Return a JSON representation of the model data.

        :param recursive: If true then recursively convert child objects to JSON as well.
        :param levels: The number of levels of child objects to convert to JSON. If 0 convert all.
        """
        r = self.to_dict()
        return json.dumps(r)
    to_JSON = to_json

    def from_json(self, json):


    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in iteritems(self.attribute_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

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
