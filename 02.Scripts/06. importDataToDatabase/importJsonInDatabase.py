import subprocess
import pandas as pd
import json

# Function to get data type of a DataFrame column
def get_data_type(column):
    data_type = "STRING"
    if column.dtype == "int64":
        data_type = "INTEGER"
    elif column.dtype == "float64":
        data_type = "FLOAT"
    return data_type

# Function to create a table and load data
def create_table_and_load_data(json_file):
    # Read data from the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data_list = [json.loads(line) for line in f]

    # Convert to DataFrame
    df = pd.DataFrame(data_list)

    # Table name based on the JSON file name
    table_name = json_file.replace("_transformed.json", "").replace("yelp_academic_dataset_", "") + "_json"

    # Get data types for each column
    column_types = {column: get_data_type(df[column]) for column in df.columns}

    # Command to create the table in CrateDB if it does not exist
    create_table_command = f"docker exec -i cratedb /usr/local/bin/crash -c \"CREATE TABLE IF NOT EXISTS {table_name} (" \
                            f"{', '.join([f'{column} {column_types[column]}' for column in column_types])}" \
                            f");\""

    # Execute command to create the table
    subprocess.run(create_table_command, shell=True)

    # Path to the JSON file within the CrateDB container
    container_json_path = f"/dataset/{json_file}"

    # Command to import data from the JSON file to CrateDB
    import_data_command = f"docker exec -i cratedb /usr/local/bin/crash -c \"COPY {table_name} FROM '{container_json_path}'\""

    # Execute command to import data
    subprocess.run(import_data_command, shell=True)

    print(f"Data from '{json_file}' has been successfully imported to table '{table_name}' in CrateDB.")

# List of JSON files corresponding to each table
json_files = [
    "yelp_academic_dataset_business_transformed.json",
    "yelp_academic_dataset_checkin_transformed.json",
    "yelp_academic_dataset_review_transformed.json",
    "yelp_academic_dataset_tip_transformed.json",
    "yelp_academic_dataset_user_transformed.json"
]

# Process each JSON file
for json_file in json_files:
    create_table_and_load_data(json_file)
