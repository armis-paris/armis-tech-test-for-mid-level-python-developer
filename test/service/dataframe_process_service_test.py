import random
import string
import unittest

import pandas as pd

from src.service.dataframe_process_service import DataframeProcessService


class DataframeProcessServiceTest(unittest.TestCase):

    def test_should_add_length_of_text_column_to_the_dataframe(self):
        # given
        text_list = self.__generate_long_text_list()
        records = pd.DataFrame({'text': text_list})

        dataframe_process_service = DataframeProcessService()

        # when
        records = dataframe_process_service.add_new_columns_to_dataframe(records)

        # then
        self.assertFalse(records.empty)

    @staticmethod
    def __generate_long_text_list() -> list:
        text_list = []
        for x in range(100000):
            text = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=random.randint(1, 10)))
            text_list.append(text)
        return text_list
