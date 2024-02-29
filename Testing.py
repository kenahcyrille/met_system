import os
import json
import random
import string

# Schema definition
schema = {
    "type": "object",
    "properties": {
        "program": {
            "type": "string",
            "enum": ["Program_A", "Program_B", "Program_C"]
        },
        "products": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["Product_A", "Product_B", "Product_C"]
            }
        },
        "job_id": {
            "type": "string"
        }
    },
    "defaults": {
        "program": "Program_B",
        "products": ["Product_A", "Product_C"]
    },
    "required": ["program", "products"],
    "retain_on_export": ["program"]
}

# Function to generate random string
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate metadata for a data file
def generate_metadata():
    metadata = {}
    metadata["program"] = random.choice(schema["properties"]["program"]["enum"])
    metadata["products"] = random.sample(schema["properties"]["products"]["items"]["enum"], random.randint(1, 3))
    metadata["job_id"] = generate_random_string(8)
    return metadata

# Function to generate data files and corresponding metadata
def generate_data_with_metadata(num_files):
    data_folder = "data"
    metadata_folder = "metadata"

    # Create folders if they don't exist
    os.makedirs(data_folder, exist_ok=True)
    os.makedirs(metadata_folder, exist_ok=True)

    # Generate data files and metadata
    for i in range(num_files):
        # Generate random data file
        data_file_name = f"{data_folder}/data_{i}.txt"
        with open(data_file_name, "w") as f:
            f.write(generate_random_string(100))

        # Generate metadata for the data file
        metadata = generate_metadata()
        metadata_file_name = f"{metadata_folder}/metadata_{i}.json"
        with open(metadata_file_name, "w") as f:
            json.dump(metadata, f, indent=4)
        
        print(f"Generated data file: {data_file_name}")
        print(f"Generated metadata file: {metadata_file_name}")
        print()

# Generate 5 data files with corresponding metadata
generate_data_with_metadata(5)
