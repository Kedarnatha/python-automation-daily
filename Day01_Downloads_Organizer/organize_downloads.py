import os
import shutil

# Your downloads folder path
source_folder = r"C:\Users\User\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "ZipFiles": [".zip", ".rar"]
}

# Create folders if not exist
for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.endswith(ext):
                    destination = os.path.join(source_folder, folder, file)
                    shutil.move(file_path, destination)
                    print(f"Moved {file} to {folder}")