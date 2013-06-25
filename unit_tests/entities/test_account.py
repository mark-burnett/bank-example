from bank.entities import account

import unittest


class TestCreditAccountBase(unittest.TestCase):
    def setUp(self):
        self.account = account.CreditAccountBase(name='foo', balance=42)

    def test_credit(self):
        self.account.credit(7)
        self.assertEqual(35, self.account.balance)

    def test_debit(self):
        self.account.debit(7)
        self.assertEqual(49, self.account.balance)


class TestDebitAccountBase(unittest.TestCase):
    def setUp(self):
        self.account = account.DebitAccountBase(name='foo', balance=42)

    def test_credit(self):
        self.account.credit(7)
        self.assertEqual(49, self.account.balance)

    def test_debit(self):
        self.account.debit(7)
        self.assertEqual(35, self.account.balance)


if __name__ == '__main__':
    unittest.main()
