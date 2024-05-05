# Docker Desktop Installation Script

This PowerShell script automates the installation of Docker Desktop on Windows systems. It is designed to streamline the setup process by checking existing installations, downloading, and installing Docker Desktop silently if it's not already installed. The script requires administrative privileges to run.

## Prerequisites

- Windows Operating System
- PowerShell 5.1 or higher
- Administrative privileges

## Script Overview

The script performs several checks and operations to ensure Docker Desktop is installed and running on your Windows machine. Here's what the script does, step by step:

### Step 1: Check Administrative Privileges

The script starts by checking if it is being run with administrative privileges. It uses Windows security principles to verify this. If the script is not run as an administrator, it will terminate and prompt the user to restart the script with the necessary privileges.

### Step 2: Check Existing Docker Desktop Installation

Next, the script checks if Docker Desktop is already installed by looking for the Docker Desktop Installer executable in the default installation path (`C:\Program Files\Docker\Docker`). If found, it assumes Docker Desktop is installed and exits.

### Step 3: Check for Local Installer

The script also looks in the current directory for the Docker Desktop Installer executable. If the installer is found in the current directory, the script assumes installation is not required and exits.

### Step 4: Download Docker Desktop Installer

If no existing installation or local installer is found, the script uses `Invoke-WebRequest` to download the Docker Desktop installer from the official Docker Hub URL to the current directory.

### Step 5: Install Docker Desktop

After downloading, the script executes the installer silently using `Start-Process` with the `/silent` argument, ensuring that no user interaction is required during the installation process.

### Step 6: Wait for Installation to Complete

The script then pauses execution for 60 seconds to allow the installation process to complete.

### Step 7: Check Docker Version

Once the installation is presumed complete, the script checks the installed version of Docker by running `docker --version`.

### Step 8: Verify Docker Desktop is Running

It also checks if Docker Desktop is operational by running `docker info`.

### Step 9: Save Script Output

All the information collected (Docker version and Docker info) is saved to a log file named `DockerInstallationLog.txt` in the current directory.

### Step 10: Completion Message

Finally, the script outputs a message indicating that Docker Desktop has been successfully installed and provides the location of the saved log file.

## Usage

To run this script:
1. Open PowerShell as an Administrator.
2. Navigate to the directory containing the script.
3. Run the script by typing `.\script_name.ps1`.