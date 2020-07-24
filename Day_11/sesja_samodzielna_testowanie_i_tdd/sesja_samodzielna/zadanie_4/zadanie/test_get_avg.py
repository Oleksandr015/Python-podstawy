import unittest
from unittest.mock import patch, MagicMock

from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_4.zadanie.get_avg import get_avg


class TestGetAvg(unittest.TestCase):


    def test_avg_numbers(self):
        get_data_fun_mock = MagicMock(return_value= '3')

        with patch('Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_4.zadanie.get_avg._get_data',
                   get_data_fun_mock):
            path = 'test_path'
            expected = 3
            result = get_avg(path)
            self.assertEqual(expected, result)
            get_data_fun_mock.assert_called_once_with(path)