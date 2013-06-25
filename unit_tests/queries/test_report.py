from bank.queries import report

import mock
import unittest


class TestReportHandler(unittest.TestCase):
    def setUp(self):
        self.storage = mock.Mock()
        self.handler = report.Handler(self.storage)

    def test_execute(self):
        obj = mock.MagicMock()
        request = mock.Mock()

        self.storage.load_object.return_value = obj

        with mock.patch('bank.queries.report.DataResponse') as DR:
            response = self.handler.execute(request)
            DR.assert_called_once_with(obj.__str__.return_value)

        self.storage.load_object.assert_called_once_with(request.object_id)
        obj.__str__.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
