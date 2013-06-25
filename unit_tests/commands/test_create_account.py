from bank.commands import create_account
from bank.exceptions import InvalidRequestError

import mock
import unittest


class TestCreateAccountRequest(unittest.TestCase):
    def test_init_OK(self):
        request = create_account.Request(set_of_accounts='soa_key',
                name='foo', account_type='asset', balance=24)
        self.assertEqual('soa_key', request.set_of_accounts)
        self.assertEqual('foo', request.name)
        self.assertEqual('asset', request.account_type)
        self.assertEqual(24, request.balance)

    def test_init_soa_error(self):
        with self.assertRaises(InvalidRequestError):
            create_account.Request(account_type='asset')

    def test_init_account_type_error(self):
        bogus_account_type = mock.Mock()

        with self.assertRaises(InvalidRequestError):
            create_account.Request(set_of_accounts='soa_key',
                    account_type=bogus_account_type)


class TestCreateAccountHandler(unittest.TestCase):
    def setUp(self):
        self.storage = mock.Mock()
        self.handler = create_account.Handler(self.storage)

    def test_execute(self):
        request = mock.Mock()
        request.account_type = 'test'

        soa = mock.Mock()
        self.storage.load_object.return_value = soa

        account_class = mock.Mock()
        account_types = {
            'test': account_class,
        }
        with mock.patch('bank.commands.create_account.ACCOUNT_TYPES',
                new=account_types):
            with mock.patch('bank.commands.create_account.DataResponse') as DR:
                response = self.handler.execute(request)
                DR.assert_called_once_with(
                        self.storage.save_object.return_value)
                self.assertEqual(DR.return_value, response)

        account_class.assert_called_once_with(
                name=request.name, balance=request.balance)
        soa.add_account.assert_called_once_with(account_class.return_value)

        self.storage.save_object.assert_called_once(account_class.return_value)


if __name__ == '__main__':
    unittest.main()
