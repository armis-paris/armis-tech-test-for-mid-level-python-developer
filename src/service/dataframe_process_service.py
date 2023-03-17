import pandas as pd


class DataframeProcessService:
    def add_new_columns_to_dataframe(self, records: pd.DataFrame) -> pd.DataFrame:
        """
         To improve the DataframeProcessService I use the 'str.len()' methode to calculate the
         length of each string in the 'text' column
        """
        records['length_of_text'] = records['text'].str.len()
        return records
