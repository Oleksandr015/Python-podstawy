import unittest
from unittest.mock import patch, MagicMock

from exercises.templates.exercise_8_patch_find_pattern_in_file.file_reader import read_file_lines

"""

ZADANIE DLA CHETNYCH - TRUDNE!

Do mockowania funckji open zależy użyć ścieżki 'builtins.open'.

"""


class TestReadFileLines(unittest.TestCase):

    def test_open_called_with_path_and_in_read_mode(self):
        # Chcemy sprawdzić czy funkcja open została wywołana raz oraz czy została z oczekiwanymi parametrami.
        # (podpowiedź: metoda assert_called_once_with)
        pass

    def test_file_closed_called(self):
        # Testujemy czy plik został zakmnięty (assert_called_once na metodzie <file>.close()). Oczywiście nadal
        # mockujemy funkcję open().
        pass

    def test_returns_expected_lines(self):
        # Testujemy czy metoda <file>.readlines zwraca oczekiwaną wartość. Nadal mockujemy open().
        pass
