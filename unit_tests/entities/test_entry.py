from bank.entities import entry

import mock
import unittest


class TestCreditEntry(unittest.TestCase):
    def setUp(self):
        self.account = mock.Mock()
        self.entry = entry.CreditEntry(account=self.account, amount=42)

    def test_credit_amount(self):
        self.assertEqual(42, self.entry.credit_amount)

    def test_debit_amount(self):
        self.assertEqual(0, self.entry.debit_amount)

    def test_execute(self):
        self.entry.execute()
        self.account.credit.assert_called_once_with(42)


class TestDebitEntry(unittest.TestCase):
    def setUp(self):
        self.account = mock.Mock()
        self.entry = entry.DebitEntry(account=self.account, amount=42)

    def test_credit_amount(self):
        self.assertEqual(0, self.entry.credit_amount)

    def test_debit_amount(self):
        self.assertEqual(42, self.entry.debit_amount)

    def test_execute(self):
        self.entry.execute()
        self.account.debit.assert_called_once_with(42)


if __name__ == '__main__':
    unittest.main()
