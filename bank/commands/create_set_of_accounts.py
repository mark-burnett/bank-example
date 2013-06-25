from bank.entities import ledger
from bank.entities import set_of_accounts
from bank.handler import IHandler
from bank.request import RequestBase
from bank.response import DataResponse


class Request(RequestBase):
    def __init__(self, name=''):
        self.name = name


class Handler(IHandler):
    def execute(self, request):
        general_ledger = ledger.Ledger([])
        soa = set_of_accounts.SetOfAccounts(name=request.name,
                accounts={}, ledger=general_ledger)

        ledger_id = self.storage.save_object(general_ledger)
        soa_id = self.storage.save_object(soa)

        return DataResponse({'set_of_accounts': soa_id, 'ledger': ledger_id})
