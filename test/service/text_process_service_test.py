import unittest

from src.service.text_process_service import TextProcessService


class TextProcessServiceTest(unittest.TestCase):

    def test_should_extract_information(self):
        # given
        text = 'I started to listen Nirvana band in 2009!'

        text_process_service = TextProcessService()

        # when
        text_information = text_process_service.extract_information(text)

        # then
        self.assertIsNotNone(text_information)
