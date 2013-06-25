from bank.handler import IHandler
from bank.request import RequestBase
from bank.response import DataResponse


class Request(RequestBase):
    def __init__(self, object_id):
        self.object_id = object_id


class Handler(IHandler):
    def execute(self, request):
        obj = self.storage.load_object(request.object_id)

        report = str(obj)
        return DataResponse(report)
