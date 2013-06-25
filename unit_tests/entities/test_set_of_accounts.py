from bank import exceptions
from bank.entities import set_of_accounts

import mock
import unittest


class TestSetOfAccounts(unittest.TestCase):
    def setUp(self):
        self.account = mock.Mock()
        self.account.name = 'foo'
        self.ledger = mock.Mock()
        self.soa = set_of_accounts.SetOfAccounts(name='bar',
                accounts={}, ledger=self.ledger)

    def test_add_account_OK(self):
        self.soa.add_account(self.account)
        self.assertEqual(self.account, self.soa.accounts['foo'])

    def test_add_account_error(self):
        self.soa.add_account(self.account)
        with self.assertRaises(exceptions.DuplicateAccountError):
            self.soa.add_account(self.account)


if __name__ == '__main__':
    unittest.main()
