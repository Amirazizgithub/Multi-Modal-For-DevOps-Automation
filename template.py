import os

# Define the folder structure
folders = {
    "mizzle_mate": [
        "app",
        "app/models",
        "app/core",
        "app/utils",
        "config",
    ]
}

files = [
    "app/main.py",
    "app/__init__.py",
    "app/models/__init__.py",
    "app/models/ci_cd_model.py",
    "app/models/instance_creation_model.py",
    "app/models/logs_model.py",
    "app/models/monitoring_model.py",
    "app/models/storage_model.py",
    "app/core/__init__.py",
    "app/core/intent_classifier.py",
    "app/core/router.py",
    "app/utils/__init__.py",
    "app/utils/logger.py",
    "config/modules.json",
    "Dockerfile",
    "requirements.txt",
]


# Function to create folders and files
def create_structure():
    for root, subdirs in folders.items():
        for subdir in subdirs:
            os.makedirs(os.path.join(root, subdir), exist_ok=True)

    for file_path in files:
        full_path = os.path.join("mizzle_mate", file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write("")  # Create empty file

    print("Project structure created successfully!")


# Execute folder creation
if __name__ == "__main__":
    create_structure()
