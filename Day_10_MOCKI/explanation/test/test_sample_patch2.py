import unittest
from unittest.mock import patch, MagicMock


from Day_10_MOCKI.explanation.sample_patch_2 import get_first_line_length


class TestGetFirstLineLength(unittest.TestCase):

    def test_get_first_line_length(self):
        function_mock = MagicMock(return_value = 'B')

        with patch('Day_10_MOCKI.explanation.sample_patch_2.read_file_first_line', function_mock):
            path = 'test/path'
            result = get_first_line_length(path)
            self.assertEqual(result, 1)
            function_mock.assert_called_once_with(path)
