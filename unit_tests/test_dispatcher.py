from bank.dispatcher import Dispatcher
from bank.exceptions import RequestFailure
from bank.response import ErrorResponse

import mock
import unittest


class TestDispatcher(unittest.TestCase):
    def setUp(self):
        self.request_classes = {
            'Rfoo': mock.Mock(),
            'Rbar': mock.Mock(),
        }
        self.handlers = {
            self.request_classes['Rfoo']: mock.Mock(),
            self.request_classes['Rbar']: mock.Mock(),
        }

        self.dispatcher = Dispatcher(self.handlers)

    def make_request(self, request_type):
        request = mock.MagicMock()
        request.__class__ = self.request_classes[request_type]
        return request

    def test_get_handler(self):
        request = self.make_request('Rfoo')
        self.assertEqual(self.handlers[self.request_classes['Rfoo']],
                self.dispatcher.get_handler(request))

    def test_dispatch_OK(self):
        request = self.make_request('Rbar')
        handler = self.dispatcher.get_handler(request)

        response = self.dispatcher.dispatch(request)

        self.assertEqual(handler.handle_request.return_value, response)
        handler.handle_request.assert_called_once_with(request)

    def test_dispatch_error(self):
        request = self.make_request('Rbar')
        handler = self.dispatcher.get_handler(request)
        handler.handle_request.return_value = mock.Mock(ErrorResponse)

        with self.assertRaises(RequestFailure):
            self.dispatcher.dispatch(request)


if __name__ == '__main__':
    unittest.main()
