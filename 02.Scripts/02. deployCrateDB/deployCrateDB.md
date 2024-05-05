# CrateDB Docker Deployment Script

This PowerShell script facilitates the deployment of CrateDB using Docker on Windows systems. It is designed to automatically check for an existing CrateDB container, deploy a new container if needed, and ensure that the deployment is successful. Administrative privileges are not explicitly required unless Docker itself requires them for execution.

## Prerequisites

- Windows Operating System with PowerShell
- Docker Desktop for Windows installed and running
- Permissions to manage Docker containers

## Script Overview

The script performs a series of operations to ensure that a CrateDB Docker container is deployed and running on your system. Here is what the script accomplishes, detailed step by step:

### Step 1: Check for Existing CrateDB Container

The script starts by checking if there is any existing CrateDB container (running or stopped) on the system using `docker ps -a`. It filters Docker containers by name to find any that match 'cratedb'. If such a container is found, the script outputs a message indicating that CrateDB is already running and then terminates.

### Step 2: Pull CrateDB Docker Image

If no existing CrateDB container is found, the script proceeds to pull the latest CrateDB Docker image from the Docker Hub using `docker pull crate/crate`. This ensures that you have the latest version available.

### Step 3: Run CrateDB Container

After pulling the image, the script runs a new CrateDB container. It sets the container name to 'cratedb' and maps ports `4200` and `5432` to the same ports on the host. This setup allows accessing CrateDB’s web interface and PostgreSQL-compatible port respectively.

### Step 4: Wait for CrateDB Deployment

The script then pauses for 30 seconds using `Start-Sleep` to allow enough time for CrateDB to initialize and start. This wait ensures that subsequent commands that check the container status don't execute prematurely.

### Step 5: Verify CrateDB Deployment

After the wait, the script checks if the CrateDB container is still running. It again uses `docker ps` with a filter to check for the 'cratedb' container. If the container is up and running, it outputs a success message along with the URL to access the CrateDB web interface. If the container is not running, it outputs an error message indicating that the deployment failed.

## Usage

To run this script:
1. Open PowerShell.
2. Navigate to the directory containing the script.
3. Execute the script by typing `.\deploy_crate.ps1`.

## Note

- This script assumes that Docker is installed, running, and that you have the necessary permissions to manage Docker containers.
- Internet connectivity is required to pull the CrateDB Docker image from Docker Hub.
- Adjust the sleep duration in the script if your system is significantly slower or faster in deploying containers.