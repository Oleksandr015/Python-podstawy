import unittest

class TestSum(unittest.TestCase):

     def test_sum(self):
         self.assertEqual(sum([1,2,3]), 6, "msg 123")

     def test_sum_tuple(self):
         self.assertEqual(sum((1,2,2)), 6, "msg 123")
