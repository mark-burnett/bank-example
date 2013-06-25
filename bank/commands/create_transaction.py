from bank.entities import entry
from bank.entities import transaction
from bank.handler import IHandler
from bank.request import RequestBase
from bank.response import DataResponse
from dateutil import parser

import datetime


class Request(RequestBase):
    def __init__(self, ledger, credits, debits, description='', timestamp=None):
        self.ledger = ledger
        self.credits = credits
        self.debits = debits
        self.description = description
        self.timestamp = timestamp


class Handler(IHandler):
    def execute(self, request):
        ledger = self.storage.load_object(request.ledger)

        entries = []

        for account_id, amount in request.credits:
            credit_account = self.storage.load_object(account_id)
            entries.append(entry.CreditEntry(
                account=credit_account, amount=amount))

        for account_id, amount in request.debits:
            debit_account = self.storage.load_object(account_id)
            entries.append(entry.DebitEntry(
                account=debit_account, amount=amount))

        if request.timestamp:
            timestamp = parser.parse(request.timestamp)
        else:
            timestamp = datetime.datetime.now()

        trans = transaction.Transaction(timestamp=timestamp, entries=entries,
                description=request.description)

        ledger.add_transaction(trans)

        object_id = self.storage.save_object(trans)

        return DataResponse(object_id)
