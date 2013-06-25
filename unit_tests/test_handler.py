from bank.handler import IHandler
from bank.exceptions import RequestFailure
from bank.response import ErrorResponse

import mock
import unittest


class PassThroughHandler(IHandler):
    def execute(self, request):
        return request


class ErroringHandler(IHandler):
    def execute(self, request):
        raise RuntimeError()


class TestIHandler(unittest.TestCase):
    def test_initialization(self):
        storage = mock.Mock()
        handler = PassThroughHandler(storage)
        self.assertIs(storage, handler.storage)

    def test_handle_request_OK(self):
        handler = PassThroughHandler(None)

        request = mock.Mock()
        response = handler.handle_request(request)

        self.assertEqual(request, response)

    def test_handle_request_error(self):
        handler = ErroringHandler(None)

        request = mock.Mock()
        response = handler.handle_request(request)

        self.assertIsInstance(response, ErrorResponse)


if __name__ == '__main__':
    unittest.main()
