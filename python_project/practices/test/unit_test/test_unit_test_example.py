import unittest
from src.unit_test.unit_test_example import UnitTestExample
from src.exception.invalid_data_error import InvalidDataError


class TestUnitTestExample(unittest.TestCase):
    def test_sum_list_valid_data(self):
        unit_t = UnitTestExample()
        self.assertEqual(unit_t.sum_list([1, 3, 2]), 6)

    def test_sum_list_invalid_data(self):
        unit_test = UnitTestExample()
        with self.assertRaises(InvalidDataError):
            unit_test.sum_list([1, 6, 'Hi'])

    def test_sum_list_none_value(self):
        unit_t = UnitTestExample()
        with self.assertRaises(InvalidDataError):
            unit_t.sum_list(None)
