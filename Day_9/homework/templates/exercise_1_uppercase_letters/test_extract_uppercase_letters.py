from unittest import TestCase

from Day_9.homework.templates.exercise_1_uppercase_letters.extract_uppercase_letters import extract_uppercase_letters


class TestExtractUppercaseLetter(TestCase):

    def test_no_uppercase_letters(self):
        expected = ""
        result = extract_uppercase_letters("dfgh")
        self.assertEqual(result, expected, 'string must contain just uppercase letter')

    def test_empty_string(self):
        empty_string = ""
        expected = ""
        result = extract_uppercase_letters(empty_string)
        self.assertEqual(result, expected, 'empty string was getting')

    def test_sentence_with_uppercase_letters(self):
        sentence = 'TYIJIJJdsfg'
        expected = 'TYIJIJJ'
        result = extract_uppercase_letters(sentence)
        self.assertEqual(result, expected, 'string must contain just uppercase letter')
