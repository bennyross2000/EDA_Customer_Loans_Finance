from db_utils_3 import RDSDatabaseConnector

credentials = {
    'RDS_HOST': 'eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com',
    'RDS_PASSWORD': 'EDAloananalyst',
    'RDS_USER': 'loansanalyst',
    'RDS_DATABASE': 'payments',
    'RDS_PORT': '5432'
}

def main():
    rds_connector = RDSDatabaseConnector(credentials)

    data_frame = rds_connector.extract_data_to_dataframe()

    file_path = 'C:/Users/admin/EDA - Customer Loans/loan_payments.csv'

    rds_connector.save_to_csv(data_frame, file_path)

if __name__ == "__main__":
    main()
