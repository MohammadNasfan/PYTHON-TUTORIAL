import os
import shutil

# Path to the folder you want to organize
SOURCE_FOLDER = input("Enter the full path of the folder to organize: ")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
    "Others": []
}

# Create folders if they don't exist
for folder in FILE_TYPES:
    folder_path = os.path.join(SOURCE_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(SOURCE_FOLDER, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(SOURCE_FOLDER, "Others", file))

print("\n✅ Files organized successfully!")
