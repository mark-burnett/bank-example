from bank import factory

import mock
import unittest


class TestFactory(unittest.TestCase):
    def test_make_dispatcher(self):
        storage = mock.Mock()

        module = mock.Mock()

        entry_point = mock.Mock()
        entry_point.load.return_value = module

        expected_handlers = {
            module.Request: module.Handler.return_value,
        }
        with mock.patch('pkg_resources.iter_entry_points') as iep:
            iep.return_value = [entry_point]
            with mock.patch('bank.dispatcher.Dispatcher') as Dispatcher:
                dispatcher = factory.make_dispatcher(storage)
                Dispatcher.assert_called_once_with(expected_handlers)
            iep.assert_called_once_with('bank_handler_modules')

        entry_point.load.assert_called_once_with()
        module.Handler.assert_called_once_with(storage=storage)


if __name__ == '__main__':
    unittest.main()
