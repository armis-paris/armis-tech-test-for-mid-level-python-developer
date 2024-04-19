import random
import string
import unittest

import pandas as pd

from src.service.dataframe_process_service import DataframeProcessService


class DataframeProcessServiceTest(unittest.TestCase):

    def test_should_add_length_of_text_column_to_the_dataframe(self):
        # given
        text_list = self.__generate_long_text_list(100000)
        records = pd.DataFrame({'text': text_list})

        dataframe_process_service = DataframeProcessService()

        # when
        records = dataframe_process_service.add_new_columns_to_dataframe(records)

        # then
        self.assertFalse(records.empty)

    def test_should_add_length_of_text_column_to_the_dataframe_with_small_dataset(self):
        # given
        text_list = self.__generate_long_text_list(10)
        records = pd.DataFrame({'text': text_list})

        dataframe_process_service = DataframeProcessService()

        # when
        records = dataframe_process_service.add_new_columns_to_dataframe(records)

        # then
        self.assertFalse(records.empty)
        self.assertEqual(len(records), 10)
        self.assertTrue('length_of_text' in records.columns)

    @staticmethod
    def __generate_long_text_list(num_rows: int) -> list:
        text_list = []
        for x in range(num_rows):
            text = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=random.randint(1, 10)))
            text_list.append(text)
        return text_list
