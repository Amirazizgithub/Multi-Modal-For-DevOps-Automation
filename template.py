from pathlib import Path

list_of_files = [
    "app.py",
    "__init__.py",
    "models/__init__.py",
    "models/ci_cd_model.py",
    "models/instance_creation_model.py",
    "models/logs_model.py",
    "models/monitoring_model.py",
    "models/storage_model.py",
    "core/__init__.py",
    "core/intent_classifier.py",
    "core/router.py",
    "utils/__init__.py",
    "utils/logger.py",
    "utils/message_preprocessor.py",
    "config/modules.json",
    "tests/__init__.py",
    "tests/test_api.py",
    "README.md",
    ".gitignore",
    ".env",
    "Dockerfile",
    ".dockerignore",
    "requirements.txt",
    ".github/workflows/ci-cd-pipeline.yaml",
]


# Create the directories of the folder and write the files if they do not exist
for file in list_of_files:
    file_path = Path(file)
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file, "w") as f:
            f.write("# Path: " + file)
print("Project structure created successfully!")
