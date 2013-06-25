from bank import exceptions
from bank.entities import account
from bank.handler import IHandler
from bank.request import RequestBase
from bank.response import DataResponse


ACCOUNT_TYPES = {
    'asset': account.AssetAccount,
    'equity': account.EquityAccount,
    'expense': account.ExpenseAccount,
    'income': account.IncomeAccount,
    'liability': account.LiabilityAccount,
}


class Request(RequestBase):
    def __init__(self, set_of_accounts=None, name='', account_type=None,
            balance=0):
        if set_of_accounts is None:
            raise exceptions.InvalidRequestError(self,
                    'set_of_accounts cannot by None')

        if account_type not in ACCOUNT_TYPES:
            raise exceptions.InvalidRequestError(self,
                    'account_type must be in %s' % ACCOUNT_TYPES.keys())

        self.set_of_accounts = set_of_accounts
        self.name = name
        self.account_type = account_type
        self.balance = balance


class Handler(IHandler):
    def execute(self, request):
        soa = self.storage.load_object(request.set_of_accounts)

        account_class = ACCOUNT_TYPES[request.account_type]
        account = account_class(name=request.name, balance=request.balance)
        soa.add_account(account)

        object_id = self.storage.save_object(account)

        return DataResponse(object_id)
