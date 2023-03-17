import unittest

from src.service.text_process_service import TextProcessService


class TextProcessServiceTest(unittest.TestCase):
    def setUp(self):
        self.text_process_service = TextProcessService()

    def test_should_extract_information(self):
        # given
        text = 'I started to listen Nirvana band in 2009!'
        expected_result = {
            'number_of_words': 8,
            'length_of_text': 41,
            'unique_alphabetic_characters': ['I', 's', 't', 'a', 'r', 'e', 'd', 'o', 'l', 'i', 'n',
                                             'N', 'v', 'b'],
            'unique_numerical_characters': ['2', '0', '9'],
            'unique_other_characters': [' ', '!']
        }

        # when
        text_information = self.text_process_service.extract_information(text)

        # then
        self.assertIsNotNone(text_information)
        self.assertEqual(text_information, expected_result)

    def test_extract_information_empty_text(self):
        text = ""
        expected_result = {
            'number_of_words': 0,
            'length_of_text': 0,
            'unique_alphabetic_characters': [],
            'unique_numerical_characters': [],
            'unique_other_characters': []
        }

        text_information = self.text_process_service.extract_information(text)

        self.assertEqual(text_information, expected_result)

    def test_extract_information_with_spaces_only(self):
        text = "    "
        expected_result = {
            'number_of_words': 0,
            'length_of_text': 4,
            'unique_alphabetic_characters': [],
            'unique_numerical_characters': [],
            'unique_other_characters': [' ']
        }

        text_information = self.text_process_service.extract_information(text)

        self.assertEqual(text_information, expected_result)

    def test_extract_information_with_alphabetic_only(self):
        text = "Hello"
        expected_result = {
            'number_of_words': 1,
            'length_of_text': 5,
            'unique_alphabetic_characters': ['H', 'e', 'l', 'o'],
            'unique_numerical_characters': [],
            'unique_other_characters': []
        }

        text_information = self.text_process_service.extract_information(text)

        self.assertEqual(text_information, expected_result)

    def test_extract_information_with_numeric_only(self):
        text = "213"
        expected_result = {
            'number_of_words': 1,
            'length_of_text': 3,
            'unique_alphabetic_characters': [],
            'unique_numerical_characters': ['2', '1', '3'],
            'unique_other_characters': []
        }

        text_information = self.text_process_service.extract_information(text)

        self.assertEqual(text_information, expected_result)

    def test_extract_information_with_other_characters_only(self):
        text = "..."
        expected_result = {
            'number_of_words': 1,
            'length_of_text': 3,
            'unique_alphabetic_characters': [],
            'unique_numerical_characters': [],
            'unique_other_characters': ['.']
        }

        text_information = self.text_process_service.extract_information(text)

        self.assertEqual(text_information, expected_result)
