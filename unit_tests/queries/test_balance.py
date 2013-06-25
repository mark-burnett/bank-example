from bank.queries import balance

import mock
import unittest


class TestBalanceHandler(unittest.TestCase):
    def setUp(self):
        self.storage = mock.Mock()
        self.handler = balance.Handler(self.storage)

    def test_execute(self):
        account = mock.MagicMock()
        request = mock.Mock()

        self.storage.load_object.return_value = account

        with mock.patch('bank.queries.balance.DataResponse') as DR:
            response = self.handler.execute(request)
            DR.assert_called_once_with(account.balance)

        self.storage.load_object.assert_called_once_with(request.account_id)


if __name__ == '__main__':
    unittest.main()
