import pandas as pd
from typing import Protocol


class DataframeCleanerProtocol(Protocol):
    def clean(self, records: pd.DataFrame) -> pd.DataFrame:
        ...


class DataframeProcessService:
    def __init__(
        self,
        records: pd.DataFrame,
        cleaner: DataframeCleanerProtocol,  # ingest a cleaner for the dataframe depends on the business logic
    ) -> None:

        if not isinstance(records, pd.DataFrame):
            raise TypeError("records must be a pandas DataFrame")

        self.records = cleaner.clean(records)

    # old version
    def add_new_columns_to_dataframe(self) -> pd.DataFrame:
        length_of_text_list = []
        for index, row in self.records.iterrows():
            length_of_text_list.append(row["text"])
        self.records["length_of_text"] = length_of_text_list
        return self.records

    def add_new_columns_to_dataframe_by_column_name(
        self, column_list_names: list[str]
    ) -> pd.DataFrame:
        for column_name in column_list_names:
            self.records[column_name] = ""
        return self.records

    def add_length_of_text_column_to_dataframe(self) -> pd.DataFrame:
        assert "text" in self.records.columns
        self.records["length_of_text"] = self.records["text"].str.len()
        return self.records
