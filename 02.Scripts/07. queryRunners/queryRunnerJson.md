# CrateDB Query Performance Analyzer

This Python script automates the process of executing a set of predefined queries against a CrateDB database instance, measures their execution times, and exports the results to a CSV file. It allows users to analyze the performance of CrateDB queries under different conditions.

## Usage

To use this script, follow these steps:

1. **Modify Query List (Optional)**: If needed, modify the list of queries (`queries`) in the script to include the queries you want to analyze.

2. **Run the Script**: Execute the script by running the Python file directly. You can do this by navigating to the directory containing the script in your terminal or command prompt and using the following command:
    ```bash
    python queryRunnerJson.py
    ```
    Replace `queryRunnerJson.py` with the actual name of your Python script if you change it.

3. **View Results**: After the script finishes executing, it will export the results to a CSV file named `query_times_json.csv`. You can open this file using any spreadsheet software to analyze the performance of the queries.

## Script Overview

The script performs the following operations:

### Step 1: Connect to CrateDB

It establishes a connection to the CrateDB database instance running on `http://localhost:4200`.

### Step 2: Define Queries

The script defines a list of predefined queries to be executed against CrateDB. Each query is annotated with a description indicating its purpose.

### Step 3: Execute Queries

For each query in the list, the script executes the query multiple times (specified by `num_iterations`), measures the execution times, and records them.

### Step 4: Calculate Average Time

After executing each query multiple times, the script calculates the average execution time by excluding the maximum and minimum times to ensure a fair average.

### Step 5: Export Results

Finally, the script exports the results, including individual execution times and average time, to a CSV file named `query_times_json.csv`.

## Example Usage

Here's an example of how to use the script in the console (another option is to open any code editor like the typical "Visual Studio Code" and working from the beginning with all the files in the same directory, hit "run python file". I assume you have python installed):

```bash
python queryRunnerJson.py
