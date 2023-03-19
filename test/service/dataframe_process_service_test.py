import random
import string
import timeit
import unittest

import pandas as pd

from src.service.dataframe_process_service import DataframeProcessService


class DataframeSimpleCleaner:
    def clean(self, records: pd.DataFrame) -> pd.DataFrame:
        return records.dropna()


class DataframeProcessServiceTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.dataframe_cleaner = DataframeSimpleCleaner()

    def test_should_add_length_of_text_column_to_the_dataframe(self):
        # given
        text_list = self.__generate_long_text_list(10000)
        records = pd.DataFrame({"text": text_list})

        dataframe_process_service = DataframeProcessService(
            records, self.dataframe_cleaner
        )

        # when
        records = dataframe_process_service.add_length_of_text_column_to_dataframe()
        # then
        self.assertFalse(records.empty)

    def test_speed_difference_between_old_and_new_version(self):
        # given
        text_list = self.__generate_long_text_list(10000)
        old_records = pd.DataFrame({"text": text_list})

        old_dataframe_process_service = DataframeProcessService(
            old_records, self.dataframe_cleaner
        )
        new_dataframe_process_service = DataframeProcessService(
            old_records, self.dataframe_cleaner
        )

        # when
        old_execution_time = timeit.timeit(
            old_dataframe_process_service.add_new_columns_to_dataframe,
            number=5,
        )
        new_execution_time = timeit.timeit(
            new_dataframe_process_service.add_length_of_text_column_to_dataframe,
            number=5,
        )
        # then
        self.assertFalse(old_execution_time < new_execution_time)

    def test_can_add_length_of_text_column(self):
        # given
        text_list = self.__generate_long_text_list(10) + [None]
        records = pd.DataFrame({"text": text_list})

        dataframe_process_service = DataframeProcessService(
            records, self.dataframe_cleaner
        )

        # when
        records = dataframe_process_service.add_length_of_text_column_to_dataframe()

        # then
        # truthful equal to find if records['length_of_text] equal to length of records['text']
        for index, row in records.iterrows():
            self.assertEqual(row["length_of_text"], len(row["text"]))

    @staticmethod
    def __generate_long_text_list(number_of_values: int) -> list:
        text_list = []
        for x in range(number_of_values):
            text = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits, k=random.randint(1, 10)
                )
            )
            text_list.append(text)
        return text_list
