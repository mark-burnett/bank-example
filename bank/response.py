import abc


class ResponseBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '%s:\n%s' % (self.__class__.__name__, self.data)


class ErrorResponse(ResponseBase):
    pass


class DataResponse(ResponseBase):
    pass
