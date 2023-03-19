import unittest
from parameterized import parameterized
from src.service.text_process_service import TextProcessService


class TextProcessServiceTest(unittest.TestCase):
    def test_should_extract_information(self):
        # given
        text = "I started to listen Nirvana band in 2009!"

        text_process_service = TextProcessService(text)

        # when
        text_information = text_process_service.extract_information()

        # then
        self.assertIsNotNone(text_information)

    @parameterized.expand(
        [
            ("Integers", 123),
            ("None", None),
            ("Floats", 1.23),
            ("Boolean", True),
            ("List", [1, 2, 3]),
            ("Tuple", (1, 2, 3)),
            ("Dictionary", {"a": 1, "b": 2, "c": 3}),
        ]
    )
    def test_should_raise_exception_on_wrong_types(self, name, test_input):
        # given
        text = None

        # when
        with self.assertRaises(Exception, msg="Text must be a string"):
            text_process_service = TextProcessService(test_input)
            text_process_service.extract_information()

    @parameterized.expand(
        [
            (
                "normal_string",
                "I started to listen Nirvana band in 2009!",
                {"N", "t", "I", "n", "o", "i", "l", "d", "b", "a", "v", "e", "r", "s"},
            ),
            ("empty string", "", set()),
        ]
    )
    def test_should_get_the_correct_unique_alpha_characters(
        self, name, test_input, expected
    ):
        print(type(test_input))
        # given
        text_process_service = TextProcessService(test_input)

        # when
        text_information = text_process_service.extract_information()

        # then
        self.assertEqual(text_information.unique_alphabetic_characters, expected)

    @parameterized.expand(
        [
            (
                "normal_string",
                "I started to listen Nirvana band in 2009!",
                {"2", "0", "9"},
            ),  # 2009
            (
                "empty string",
                "",
                set(),
            ),
        ]
    )
    def test_should_get_the_correct_unique_numeric_characters(
        self, name, test_input, expected
    ):
        # given
        text_process_service = TextProcessService(test_input)

        # when
        text_information = text_process_service.extract_information()

        # then
        self.assertEqual(text_information.unique_numerical_characters, expected)

    @parameterized.expand(
        [
            (
                "normal_string",
                "I started to listen Nirvana band in 2009!",
                {" ", "!"},
            ),
            ("empty string", "", set()),
        ]
    )
    def test_should_get_the_correct_count_for_unique_other_characters(
        self, name, test_input, expected
    ):
        # given
        text_process_service = TextProcessService(test_input)

        # when
        text_information = text_process_service.extract_information()
        # then
        self.assertEqual(text_information.unique_other_characters, expected)

    def test_canot_access_private_values(self):
        # given
        text = "I started to listen Nirvana band in 2009!"

        text_process_service = TextProcessService(text)

        # when
        with self.assertRaises(AttributeError):
            text_process_service.__text
