import unittest

from sesja_samodzielna.zadanie_5.rozwiazanie.product import Product
from sesja_samodzielna.zadanie_5.rozwiazanie.warehouse import Warehouse


class TestWarehouse(unittest.TestCase):

    def setUp(self) -> None:
        self.product_25 = Product('name1', 25)
        self.product_75 = Product('name2', 75)
        self.warehouse_75 = Warehouse(75)

    def test_warehouse_overflows(self):
        expected = -1

        self.warehouse_75.add(self.product_25)
        result = self.warehouse_75.add(self.product_75)

        self.assertEqual(result, expected)

    def test_warehouse_returns_rest_space_correctly(self):
        expected = 50

        result = self.warehouse_75.add(self.product_25)

        self.assertEqual(result, expected)
