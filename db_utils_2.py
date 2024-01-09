import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self):
        self.credentials = self.load_credentials()
        self.engine = self.create_engine()

    def load_credentials(self,a):
        with open(a, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def create_engine(self):
        connection_string = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = create_engine(connection_string)
        return engine

    def extract_data_to_dataframe(self):
        query = "SELECT * FROM loan_payments" 
        data_frame = pd.read_sql(query, self.engine)
        return data_frame

    def save_to_csv(self, data_frame = pd.df, file_path):
        data_frame.to_csv(file_path, index=False)
