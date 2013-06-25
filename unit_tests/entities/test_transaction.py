from bank import exceptions
from bank.entities import transaction

import mock
import unittest


class TransactionTestBase(object):
    def setUp(self):
        self.timestamp = mock.Mock()

        self.entries = []
        for entry_type, entry_value in self.ENTRY_DATA:
            self.entries.append(self.make_entry(entry_type, entry_value))

        self.transaction = transaction.Transaction(
                timestamp=self.timestamp,
                entries=self.entries)

    def make_entry(self, entry_type, entry_value):
        entry = mock.Mock()

        if entry_type == 'credit':
            entry.credit_amount = entry_value
            entry.debit_amount = 0
        elif entry_type == 'debit':
            entry.credit_amount = 0
            entry.debit_amount = entry_value
        else:
            raise RuntimeError('Illegal entry type: %s' % entry_type)

        return entry


class TestTransactionAmounts(TransactionTestBase, unittest.TestCase):
    ENTRY_DATA = [
        ('credit', 1),
        ('credit', 2),
        ('debit',  3),
        ('debit',  4),
    ]

    def test_credit_amount(self):
        self.assertEqual(3, self.transaction.credit_amount)

    def test_debit_amount(self):
        self.assertEqual(7, self.transaction.debit_amount)


class TestInvalidTransaction(TransactionTestBase, unittest.TestCase):
    ENTRY_DATA = [
        ('credit', 7),
        ('credit', 2),
        ('debit',  4),
        ('debit',  9),
    ]

    def test_execute_error(self):
        with self.assertRaises(exceptions.InvalidTransactionError):
            self.transaction.execute()

    def test_is_valid_failure(self):
        self.assertFalse(self.transaction.is_valid())


class TestValidTransaction(TransactionTestBase, unittest.TestCase):
    ENTRY_DATA = [
        ('credit', 2),
        ('credit', 7),
        ('debit',  6),
        ('debit',  3),
    ]

    def test_execute_OK(self):
        self.transaction.execute()
        for entry in self.entries:
            entry.execute.assert_called_once_with()

    def test_is_valid_OK(self):
        self.assertTrue(self.transaction.is_valid())


if __name__ == '__main__':
    unittest.main()
