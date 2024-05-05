# JSON to CrateDB Data Loader

This Python script automates the process of creating tables in CrateDB and importing data from JSON files into those tables. It reads each JSON file, determines the appropriate data types for each column, creates a corresponding table in CrateDB, and loads the data from the JSON file into the table.

## Usage

To use this script, follow these steps:

1. **Prepare Your JSON Files**: Ensure that the JSON files you want to import into CrateDB are located in the same directory as the script or provide the correct paths to these files in the script.

2. **Run the Script**: Execute the script by running the Python file directly. You can do this by navigating to the directory containing the script in your terminal or command prompt and using the following command:
    ```bash
    python importJsonInDatabase.py
    ```
    Replace `importJsonInDatabase.py` with the actual name of your Python script if you change it.

3. **Specify CrateDB Container Name and Directory**: Ensure that you've specified the correct CrateDB container name (`cratedb`) in the script.

## Script Overview

The script performs the following operations:

### Step 1: Read JSON Files

It reads each JSON file specified in the `json_files` list.

### Step 2: Determine Data Types

For each JSON file, the script parses the data and determines the appropriate data types for each column based on the data present in the file.

### Step 3: Create Table in CrateDB

Using the determined data types, the script generates a `CREATE TABLE` command for CrateDB and executes it to create a table for each JSON file.

### Step 4: Import Data to CrateDB

The script then imports the data from each JSON file into the corresponding table in CrateDB using the `COPY FROM` command.

### Step 5: Print Confirmation

Once the data is successfully imported, the script prints a confirmation message indicating that the data has been imported into CrateDB.

## Example Usage

Here's an example of how to use the script (another option is to open any code editor like the typical "Visual Studio Code" and working from the beginning with all the files in the same directory, hit "run python file". I assume you have python installed):

```bash
python importJsonInDatabase.py
