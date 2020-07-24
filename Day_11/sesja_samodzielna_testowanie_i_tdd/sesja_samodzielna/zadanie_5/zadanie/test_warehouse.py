import unittest
from unittest.mock import MagicMock


from Day_11.sesja_samodzielna_testowanie_i_tdd.sesja_samodzielna.zadanie_5.zadanie.warehouse import Warehouse


class TestWarehouse(unittest.TestCase):

    def setUp(self) -> None:
        self.product_mock_25 = MagicMock()
        self.product_mock_25.volume = 25

        self.product_mock_100 = MagicMock()
        self.product_mock_100.volume = 100

        self.warehouse_75 = Warehouse(75)

    def test_add_less_products(self):
        expected = 50
        result = self.warehouse_75.add(self.product_mock_25)
        self.assertEqual(result, expected)

    def test_add_product_to_the_full_warehouse(self):

        expected = -1
        result = self.warehouse_75.add(self.product_mock_100)
        self.assertEqual(expected, result)






