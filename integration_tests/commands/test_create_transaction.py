from bank import exceptions
from bank import factory
from bank import request
from bank.memory_storage import MemoryStorage

import mock
import unittest


class TestTransactionBase(object):
    ACCOUNT_LIST = [
        ('A', 'asset'),
        ('I', 'income'),
        ('L', 'liability'),
        ('Q', 'equity'),
        ('X', 'expense'),
    ]

    def setUp(self):
        self.storage = MemoryStorage({})

        self.dispatcher = factory.make_dispatcher(self.storage)

        response = self.send_request('create_set_of_accounts', name='SET')
        self.set_of_accounts = response.data['set_of_accounts']
        self.ledger = response.data['ledger']

        self.accounts = self.make_accounts()

    def send_request(self, request_name, **kwargs):
        rq = request.create_request(request_name, **kwargs)
        return self.dispatcher.dispatch(rq)

    def make_account(self, name, account_type):
        response = self.send_request('create_account', name=name,
                set_of_accounts=self.set_of_accounts, account_type=account_type)
        return response.data

    def make_accounts(self):
        account_ids = {}
        for name, account_type in self.ACCOUNT_LIST:
            account_ids[name] = self.make_account(name, account_type)

        return account_ids

    def make_transaction(self, credits, debits, **kwargs):
        real_credits = [(self.accounts[name], amount)
                        for name, amount in credits]
        real_debits = [(self.accounts[name], amount)
                       for name, amount in debits]
        response = self.send_request('create_transaction', ledger=self.ledger,
                credits=real_credits, debits=real_debits, **kwargs)
        return response.data

    def get_balance(self, account_name):
        response = self.send_request('balance',
                account_id=self.accounts[account_name])
        return response.data


class TestSuccessfulTransactions(TestTransactionBase, unittest.TestCase):
    def test_single_transaction(self):
        self.make_transaction(credits=[('A', 100)], debits=[('I', 100)])

        self.assertEqual(100, self.get_balance('A'))
        self.assertEqual(100, self.get_balance('I'))

    def test_two_transactions(self):
        self.make_transaction(credits=[('A', 100)], debits=[('I', 100)])
        self.make_transaction(credits=[('X', 15)], debits=[('A', 15)])

        self.assertEqual(85, self.get_balance('A'))
        self.assertEqual(100, self.get_balance('I'))
        self.assertEqual(15, self.get_balance('X'))

    def test_split_transaction(self):
        self.make_transaction(credits=[('A', 80), ('X', 20)],
                debits=[('L', 100)])

        self.assertEqual(80, self.get_balance('A'))
        self.assertEqual(100, self.get_balance('L'))
        self.assertEqual(20, self.get_balance('X'))


class TestFailedTransactions(TestTransactionBase, unittest.TestCase):
    def test_single_transaction(self):
        with self.assertRaises(exceptions.RequestFailure):
            self.make_transaction(credits=[('A', 99)], debits=[('I', 100)])

    def test_split_transaction(self):
        with self.assertRaises(exceptions.RequestFailure):
            self.make_transaction(credits=[('A', 100), ('X', 10)],
                    debits=[('I', 100)])


if __name__ == '__main__':
    unittest.main()
