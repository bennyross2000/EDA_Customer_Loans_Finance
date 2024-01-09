import yaml
from sqlalchemy import create_engine as sqlalchemy_create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.create_custom_engine()

    def load_credentials(self):
        with open('credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def create_custom_engine(self):
        connection_string = f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        engine = sqlalchemy_create_engine(connection_string)
        return engine

    def extract_data_to_dataframe(self):
        query = "SELECT * FROM loan_payments"  # Example query, replace with your query
        data_frame = pd.read_sql(query, self.engine)
        return data_frame

    def save_to_csv(self, data_frame, file_path):
        full_file_path = 'C:\\Users\\admin\\EDA - Customer Loans\\loan_payments.csv'
        data_frame.to_csv(full_file_path, index=False)




