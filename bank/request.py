from bank import exceptions

import abc
import pkg_resources


class RequestBase(object):
    __metaclass__ = abc.ABCMeta

    @property
    def classpath(self):
        return '%s:%s' % (self.__module__, self.__class__.__name__)

    def __str__(self):
        return '%s\n%s' % (self.classpath, self.__dict__)


def create_request(request_name, **kwargs):
    request_class = get_request_class(request_name)
    return request_class(**kwargs)


def get_request_class(request_name):
    cls = None
    for ep in pkg_resources.iter_entry_points(
            'bank_handler_modules', request_name):
        module = ep.load()
        cls = module.Request
        # Always take the first one found
        break

    if cls is None:
        raise exceptions.UnknownRequestError(request_name)

    return cls
