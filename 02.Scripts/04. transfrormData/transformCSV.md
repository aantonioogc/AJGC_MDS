# JSON to CSV Converter

This Python script converts a JSON file into a CSV file. It reads each line of the JSON file, parses it as JSON, and writes the values as rows in the CSV file. The script offers the flexibility to specify the maximum number of records to convert.

## Usage

To use this script, follow these steps:

1. **Prepare Your JSON File**: Make sure you have a JSON file ready for conversion. You'll need to provide the path to this file when running the script.

2. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the script, and run the script using Python. Use the following command:
    ```bash
    python transformCSV.py
    ```
    Replace `transformCSV.py` with the actual name of your Python script if you change it.

4. **Specify Input and Output Files**: When running the script, you'll need to specify the input JSON file and the desired output CSV file. You can do this by editing the script directly or by passing arguments when running the script.

## Script Overview

The script performs the following operations:

### Step 1: Open Files

The script opens the input JSON file for reading and the output CSV file for writing.

### Step 2: Iterate Over JSON Lines

It then iterates over each line in the JSON file. For each line, it loads the JSON data and converts it into a Python dictionary.

### Step 3: Write to CSV

The script writes the values of the dictionary as a row in the CSV file. It continues this process until either all lines in the JSON file are processed or the specified maximum number of records is reached.

### Step 4: Close Files

Finally, the script closes both the input JSON file and the output CSV file.

## Example Usage

Here's an example of how to use the script in console (another option is to open any code editor like the typical "Visual Studio Code" and working from the beginning with all the files in the same directory, hit "run python file". I assume you have python installed):

```bash
python transformCSV.py yelp_academic_dataset_review.json yelp_academic_dataset_review_transformed.csv
