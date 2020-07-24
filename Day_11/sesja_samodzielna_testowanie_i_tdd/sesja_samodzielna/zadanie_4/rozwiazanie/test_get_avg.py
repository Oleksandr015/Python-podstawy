import unittest
from unittest.mock import MagicMock, patch

from sesja_samodzielna.zadanie_4.rozwiazanie.get_avg import get_avg


class TestGetAvg(unittest.TestCase):

    def test_for_integer_average(self):
        _get_data_mock = MagicMock(return_value="123")

        with patch('sesja_samodzielna.zadanie_4.rozwiazanie.get_avg._get_data', _get_data_mock):
            how_much = 3
            expected = 2
            self.assertEqual(get_avg(how_much), expected)
            _get_data_mock.assert_called_once_with(how_much)

    def test_for_non_integer_average(self):
        _get_data_mock = MagicMock(return_value="12")

        with patch('sesja_samodzielna.zadanie_4.rozwiazanie.get_avg._get_data', _get_data_mock):
            how_much = 2
            expected = 1.5
            self.assertEqual(get_avg(how_much), expected)
            _get_data_mock.assert_called_once_with(how_much)
