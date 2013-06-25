from bank.commands import create_set_of_accounts

import mock
import unittest


class TestCreateSetOfAccountsHandler(unittest.TestCase):
    def setUp(self):
        self.storage = mock.Mock()
        self.handler = create_set_of_accounts.Handler(self.storage)

    def test_execute(self):
        request = mock.Mock()

        with mock.patch('bank.entities.set_of_accounts.SetOfAccounts') as SOA:
            with mock.patch('bank.commands.create_set_of_accounts.DataResponse'
                    ) as DR:
                response = self.handler.execute(request)

                DR.assert_called_once_with({
                    'set_of_accounts': self.storage.save_object.return_value,
                    'ledger': self.storage.save_object.return_value,
                })

            SOA.assert_called_once_with(name=request.name,
                    accounts={}, ledger=mock.ANY)

            self.storage.save_object.assert_any_call(SOA.return_value)


if __name__ == '__main__':
    unittest.main()
