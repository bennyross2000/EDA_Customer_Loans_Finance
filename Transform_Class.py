import pandas as pd

class DataTransform:
    def __init__(self, df):
        self.df = df

    def convert_date_columns(self, columns, date_format='%b-%y'):
        self.df[columns] = self.df[columns].apply(lambda x: pd.to_datetime(x, errors='coerce', format=date_format))
        return self.df

    def convert_categorical_columns(self, columns):
        for col in columns:
            # Check for empty strings and convert them to NaN before changing to category
            self.df[col].replace('', pd.NA, inplace=True)
            self.df[col] = self.df[col].astype('category')
        return self.df

    def convert_numeric_columns(self, columns):
        self.df[columns] = self.df[columns].apply(pd.to_numeric, errors='coerce')
        # Explicitly convert the entire column to float64
        self.df[columns] = self.df[columns].astype('float64')
        return self.df

