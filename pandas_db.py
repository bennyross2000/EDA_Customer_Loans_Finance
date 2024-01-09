import pandas as pd

def load_data(file_path):
    # Load the CSV file into a Pandas DataFrame
    data_frame = pd.read_csv(file_path)

    # Print the shape of the data
    print("Shape of the data:", data_frame.shape)

    # Display a sample of the data (first few rows)
    print("\nSample of the data:")
    print(data_frame.head())

    return data_frame

# File path to your CSV file
file_path = r'C:\Users\admin\EDA - Customer Loans\loan_payments.csv'  # Replace with your actual file path

# Call the function to load the data
loaded_data = load_data(file_path)
