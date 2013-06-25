from bank import request
from bank.exceptions import UnknownRequestError

import mock
import unittest


class TestRequestBase(unittest.TestCase):
    def test_create_request(self):
        request_name = 'myrequest'
        request_args = {
            'foo': mock.Mock(),
            'bar': mock.Mock(),
        }

        request_class = mock.Mock()

        with mock.patch('bank.request.get_request_class') as grc:
            grc.return_value = request_class

            rq = request.create_request(request_name, **request_args)
            grc.assert_called_once_with(request_name)

        request_class.assert_called_once_with(**request_args)
        self.assertEqual(request_class.return_value, rq)

    def test_get_request_class_OK(self):
        request_name = 'myrequest'
        entry_point = mock.Mock()

        with mock.patch('pkg_resources.iter_entry_points') as iep:
            iep.return_value = [entry_point]
            cls = request.get_request_class(request_name)
            iep.assert_called_once_with('bank_handler_modules', request_name)

        entry_point.load.assert_called_once_with()
        self.assertEqual(entry_point.load.return_value.Request, cls)


    def test_get_request_class_error(self):
        request_name = 'myrequest'

        with mock.patch('pkg_resources.iter_entry_points') as iep:
            iep.return_value = []
            with self.assertRaises(UnknownRequestError):
                request.get_request_class(request_name)
            iep.assert_called_once_with('bank_handler_modules', request_name)


if __name__ == '__main__':
    unittest.main()
