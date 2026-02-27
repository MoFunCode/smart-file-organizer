import os
import shutil

# Dictionary mapping file extensions to category folders
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".odt", ".csv"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css", ".json", ".xml", ".sql"],
    "Executables": [".exe", ".dmg", ".pkg", ".deb", ".rpm", ".app"],
}


def get_files_in_directory(directory_path):
    """Get all files in the specified directory (not subdirectories)."""
    files = []

    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        # Only add files, not folders
        if os.path.isfile(full_path):
            files.append(full_path)

    return files


def create_category_folders(directory_path):
    """Create folders for each category if they don't exist."""
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory_path, category)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {category}")
        else:
            print(f"Folder already exists: {category}")


def get_file_category(file_path):
    """Determine which category a file belongs to based on its extension."""
    # [1] splits path into (name, extension), lower() makes it case-insensitive
    file_extension = os.path.splitext(file_path)[1].lower()

    # .items() gives us both keys and values from the dictionary
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category

    return "Others"


def organize_file(file_path, target_directory):
    """Move a file to its appropriate category folder, handling duplicates."""
    category = get_file_category(file_path)
    filename = os.path.basename(file_path)
    destination_folder = os.path.join(target_directory, category)
    destination_path = os.path.join(destination_folder, filename)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Handle duplicate filenames by adding _1, _2, etc.
    if os.path.exists(destination_path):
        name, extension = os.path.splitext(filename)
        counter = 1

        while os.path.exists(destination_path):
            new_filename = f"{name}_{counter}{extension}"
            destination_path = os.path.join(destination_folder, new_filename)
            counter += 1

        print(f"Duplicate found! Renamed to: {os.path.basename(destination_path)}")

    shutil.move(file_path, destination_path)
    print(f"Moved: {filename} → {category}/")


def organize_directory(directory_path):
    """Organize all files in a directory into categorized folders."""
    print(f"\n{'=' * 50}")
    print(f"Starting organization of: {directory_path}")
    print(f"{'=' * 50}\n")

    print("Creating category folders...")
    create_category_folders(directory_path)
    print()

    print("Scanning for files...")
    files = get_files_in_directory(directory_path)
    print(f"Found {len(files)} file(s) to organize\n")

    if len(files) == 0:
        print("No files to organize!")
    else:
        print("Organizing files...")
        for file_path in files:
            organize_file(file_path, directory_path)

    print(f"\n{'=' * 50}")
    print("Organization complete!")
    print(f"{'=' * 50}\n")


# This block only runs when you execute this file directly
if __name__ == "__main__":
    # Example: "/Users/yourname/Desktop/test_organizer"
    target_folder = "/path/to/your/folder"
    organize_directory(target_folder)