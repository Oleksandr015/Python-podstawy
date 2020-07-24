import unittest

from exercises.templates.exercise_7_mocks_products_and_cart.product import Product, PriceLessOrEqualZeroError


class TestProduct(unittest.TestCase):
    TEST_NAME = 'test'
    TEST_PRICE = 20

    def setUp(self) -> None:
        self.product = Product(self.TEST_NAME, self.TEST_PRICE)

    def test_product_get_name(self):
        pass

    def test_product_get_price(self):
        pass

    def test_raises_exception_on_less_or_equal_zero(self):
        pass
