# JSON Records Limiter

This Python script limits the number of JSON records in an input file and writes them to an output file. It reads each line of the input file, parses it as JSON, and writes the records to the output file until the specified maximum number of records is reached.

## Usage

To use this script, follow these steps:

1. **Prepare Your JSON File**: Make sure you have a JSON file ready for processing. The script will read from this file and write to a new output file with limited records.

2. **Run the Script**: Execute the script by running the Python file directly. You can do this by navigating to the directory containing the script in your terminal or command prompt and using the following command:
    ```bash
    python transformJSON.py
    ```
    Replace `transformJSON.py` with the actual name of your Python script if you change it.

3. **Specify Input and Output Files**: By default, the script is configured to process 'yelp_academic_dataset_user.json' as the input file and 'yelp_academic_dataset_user_transformed.json' as the output file. If you want to use different files, you can edit the script directly.

## Script Overview

The script performs the following operations:

### Step 1: Open Files

The script opens the input JSON file for reading and the output JSON file for writing.

### Step 2: Read and Write JSON Records

It then iterates over each line in the input file. For each line, it loads the JSON data and writes it to the output file. The script continues this process until either all lines in the input file are processed or the specified maximum number of records is reached.

### Step 3: Close Files

Finally, the script closes both the input and output files.

## Example Usage

Here's an example of how to use the script in console (another option is to open any code editor like the typical "Visual Studio Code" and working from the beginning with all the files in the same directory, hit "run python file". I assume you have python installed):

```bash
python transformJSON.py yelp_academic_dataset_user.json yelp_academic_dataset_user_transformed.json
