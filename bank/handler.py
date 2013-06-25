from bank.response import ErrorResponse

import abc


class IHandler(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, request):
        pass

    def __init__(self, storage):
        self.storage = storage

    def handle_request(self, request):
        try:
            response = self.execute(request)
        except Exception as e:
            response = ErrorResponse(str(e))

        return response
