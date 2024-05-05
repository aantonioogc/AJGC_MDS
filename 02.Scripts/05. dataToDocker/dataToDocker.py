import subprocess

# List of files to copy to the container
files_to_copy = [
    "yelp_academic_dataset_business_transformed.csv",
    "yelp_academic_dataset_checkin_transformed.csv",
    "yelp_academic_dataset_review_transformed.csv",
    "yelp_academic_dataset_tip_transformed.csv",
    "yelp_academic_dataset_user_transformed.csv",
    "yelp_academic_dataset_business_transformed.json",
    "yelp_academic_dataset_checkin_transformed.json",
    "yelp_academic_dataset_review_transformed.json",
    "yelp_academic_dataset_tip_transformed.json",
    "yelp_academic_dataset_user_transformed.json"
]

# CrateDB container name
crate_container_name = "cratedb"

# Path to the data directory in the CrateDB container
container_data_dir = "/dataset/"

# Create the dataset directory in the CrateDB container
create_dir_command = f"docker exec -i {crate_container_name} mkdir -p {container_data_dir}"
subprocess.run(create_dir_command, shell=True)

# Copy each file to the dataset directory in the CrateDB container
for file_name in files_to_copy:
    copy_command = f"docker cp {file_name} {crate_container_name}:{container_data_dir}"
    subprocess.run(copy_command, shell=True)

print("Files copied successfully to the /dataset/ directory in the CrateDB container.")
