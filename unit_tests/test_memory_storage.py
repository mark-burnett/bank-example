from bank.memory_storage import MemoryStorage

import mock
import unittest


class TestMemoryStorage(unittest.TestCase):
    def setUp(self):
        self.initial_object = mock.Mock()
        self.objects = {
            'initial_key': self.initial_object,
        }
        self.storage = MemoryStorage(self.objects)

    def test_save_object(self):
        obj = mock.Mock()
        with mock.patch('uuid.uuid4') as uuid4:
            key = self.storage.save_object(obj)

            uuid4.assert_called_once_with()

        self.assertEqual(uuid4.return_value.hex, key)
        self.assertEqual(obj, self.storage.load_object(key))

    def test_load_object(self):
        self.assertEqual(self.initial_object,
                self.storage.load_object('initial_key'))


if __name__ == '__main__':
    unittest.main()
