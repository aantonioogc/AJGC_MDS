# Check if CrateDB container is already running
if ((docker ps -a --format "{{.Names}}" | Select-String -Pattern "cratedb" -Quiet)) {
    Write-Output "CrateDB container is already running on this system."
    exit
}

# Pull CrateDB Docker image
docker pull crate/crate

# Run CrateDB container
docker run -d --name cratedb -p 4200:4200 -p 5432:5432 crate/crate

# Wait until CrateDB is fully deployed
Write-Output "Waiting for CrateDB to be fully deployed..."
Start-Sleep -Seconds 30

# Check if CrateDB container is running
if ((docker ps --format "{{.Names}}" | Select-String -Pattern "cratedb" -Quiet)) {
    Write-Output "CrateDB has been deployed successfully."
    Write-Output "You can access CrateDB at http://localhost:4200."
} else {
    Write-Error "Failed to deploy CrateDB."
}