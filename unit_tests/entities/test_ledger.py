from bank.entities import ledger

import mock
import unittest


class TestLedger(unittest.TestCase):
    def setUp(self):
        self.ledger = ledger.Ledger(transactions=[])

    def test_add_transaction(self):
        t = mock.Mock()
        self.ledger.add_transaction(t)
        t.execute.assert_called_once_with()
        self.assertEqual([t], self.ledger.transactions)


if __name__ == '__main__':
    unittest.main()
