# Data Transfer to CrateDB Container

This Python script facilitates the transfer of files from the host machine to a CrateDB container. It copies a list of specified files to a designated directory within the CrateDB container, enabling easy access to these files within the CrateDB environment.

## Usage

To use this script, follow these steps:

1. **Prepare Your Files**: Ensure that the files you want to transfer to the CrateDB container are located in the same directory as the script or provide the correct paths to these files in the script.

2. **Run the Script**: Execute the script by running the Python file directly. You can do this by navigating to the directory containing the script in your terminal or command prompt and using the following command:
    ```bash
    python dataToDocker.py
    ```
    Replace `dataToDocker.py` with the actual name of your Python script if you change it.

3. **Specify CrateDB Container Name and Directory**: Ensure that you've specified the correct CrateDB container name (`crate_container_name`) and the directory (`container_data_dir`) within the container where you want to transfer the files.

## Script Overview

The script performs the following operations:

### Step 1: Create Directory in CrateDB Container

It creates a directory within the CrateDB container where the files will be copied. The directory path is specified by the variable `container_data_dir`.

### Step 2: Copy Files to CrateDB Container

The script iterates over a list of files (`files_to_copy`) and copies each file to the directory created in the CrateDB container. It uses the `docker cp` command to achieve this.

### Step 3: Print Confirmation

Once the files are successfully copied, the script prints a confirmation message indicating that the files have been copied to the designated directory within the CrateDB container.

## Example Usage

Here's an example of how to use the script in the console (another option is to open any code editor like the typical "Visual Studio Code" and working from the beginning with all the files in the same directory, hit "run python file". I assume you have python installed):

```bash
python dataToDocker.py
