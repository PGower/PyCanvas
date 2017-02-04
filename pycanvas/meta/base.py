class BaseServiceMetadata(object):
    pass


class BaseModelMetadata(object):
    pass


class ValidationError(object):
    def __init__(self, msg):
        self.msg = msg

    def __unicode__(self):
        return unicode(self.msg)