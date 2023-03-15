import pandas as pd


class DataframeProcessService:

    def add_new_columns_to_dataframe(self, records: pd.DataFrame) -> pd.DataFrame:
        length_of_text_list = []
        for index, row in records.iterrows():
            length_of_text_list.append(row['text'])
        records['length_of_text'] = length_of_text_list
        return records
