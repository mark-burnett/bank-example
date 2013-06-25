from bank.commands import create_transaction
from bank.entities import entry

import mock
import unittest


class TestCreateTransactionRequest(unittest.TestCase):
    def test_init_OK(self):
        request = create_transaction.Request(ledger='ledger_key',
                credits=['foo'], debits=['bar'],
                description='desc', timestamp='ts')
        self.assertEqual('ledger_key', request.ledger)
        self.assertEqual(['foo'], request.credits)
        self.assertEqual(['bar'], request.debits)
        self.assertEqual('desc', request.description)
        self.assertEqual('ts', request.timestamp)


class TestCreateTransactionHandler(unittest.TestCase):
    def setUp(self):
        self.storage = mock.Mock()
        self.handler = create_transaction.Handler(self.storage)

    def test_execute(self):
        request = mock.Mock()
        request.timestamp = 'June 22, 2013'

        ledger = self.storage.load_object.return_value
        credit_account = self.storage.load_object.return_value
        debit_account = self.storage.load_object.return_value

        credits = [('foo', 7)]
        debits = [('bar', 7)]
        request.credits = credits
        request.debits = debits

        expected_entries = [
            entry.CreditEntry(account=credit_account, amount=7),
            entry.DebitEntry(account=debit_account, amount=7),
        ]

        with mock.patch('bank.commands.create_transaction.DataResponse') as DR:
            with mock.patch('bank.entities.transaction.Transaction') as T:
                self.handler.execute(request)
                self.storage.save_object.assert_called_once(T.return_value)
                ledger.add_transaction.assert_called_once_with(T.return_value)
                T.assert_called_once_with(timestamp=mock.ANY,
                        description=request.description,
                        entries=expected_entries)


            DR.assert_called_once_with(self.storage.save_object.return_value)


if __name__ == '__main__':
    unittest.main()
