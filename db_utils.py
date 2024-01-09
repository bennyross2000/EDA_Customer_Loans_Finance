import yaml

class RDSDatabaseConnector:

def load_credentials(file_path):
    with open(file_path, 'r') as file:
        try:
            credentials_data = yaml.safe_load(file)
            return credentials_data
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return {}

# Example usage:
# credentials_file_path = 'path/to/credentials.yaml'
# credentials = load_credentials(credentials_file_path)
# print(credentials)  # To check the loaded credentials dictionary
