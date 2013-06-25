from bank.handler import IHandler
from bank.request import RequestBase
from bank.response import DataResponse


class Request(RequestBase):
    def __init__(self, account_id):
        self.account_id = account_id


class Handler(IHandler):
    def execute(self, request):
        account = self.storage.load_object(request.account_id)

        return DataResponse(account.balance)
