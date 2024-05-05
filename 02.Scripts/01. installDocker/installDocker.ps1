# Check if running as administrator
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Error "This script must be run as an administrator."
    exit
}

# Check if Docker Desktop is already installed
if (Test-Path "C:\Program Files\Docker\Docker\Docker Desktop Installer.exe") {
    Write-Output "Docker Desktop is already installed on this system."
    exit
}

# Check if Docker Desktop installer is available in the current directory
if (Test-Path ".\Docker Desktop Installer.exe") {
    Write-Output "Docker Desktop is already installed on this system."
    exit
}

# Download Docker Desktop for Windows if not installed
Invoke-WebRequest -Uri https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe -OutFile DockerDesktopInstaller.exe

# Install Docker Desktop
Start-Process -FilePath .\DockerDesktopInstaller.exe -ArgumentList "/silent" -Wait

# Wait until Docker Desktop is fully installed
Start-Sleep -Seconds 60

# Check the installed Docker version
$dockerVersion = docker --version

# Check if Docker Desktop is running
$dockerInfo = docker info

# Save the execution output to a file
$scriptOutput = @"
Docker Version:
$dockerVersion

Docker Info:
$dockerInfo
"@

$scriptOutput | Out-File -FilePath "DockerInstallationLog.txt"

Write-Output "Docker Desktop has been installed successfully. The execution output has been saved to 'DockerInstallationLog.txt'."
