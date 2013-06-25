from bank import exceptions
from bank.response import ErrorResponse


class Dispatcher(object):
    def __init__(self, handlers):
        self._handlers = handlers

    def dispatch(self, request):
        handler = self.get_handler(request)

        response = handler.handle_request(request)
        if isinstance(response, ErrorResponse):
            raise exceptions.RequestFailure(request, response)
        else:
            return response

    def get_handler(self, request):
        return self._handlers[request.__class__]
