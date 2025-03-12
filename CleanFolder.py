import os  # Interacts with the file system
import shutil  # Moves files
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"]
}

def get_category(extension):
    """
    This function takes a file extension (like '.jpg')

    Returns the category to which it belongs, for example: if it's a '.jpg' file, it will return "Images".
    """
    for category, extensions in CATEGORIES.items():  # Loop through each category and its extensions
        if extension.lower() in extensions:  # If the file's extension is in the category
            return category  # Return the category name
    return "Others"  # If the extension doesn't match anything, classify it as "Others"

def sort_files(directory):
    """
    This function takes a directory as input and sorts the files within it into subfolders
    based on their type (image, document, archive, etc.).
    """
    if not os.path.exists(directory):  # Check if the directory exists
        print(f"The directory '{directory}' does not exist.")
        exit(1)
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        exit(1)
    
    CleanFolder = os.path.basename(__file__)  # Get the script's filename
    # Loop through all files in the directory
    for file in os.listdir(directory):  # List all files in the directory
        file_path = os.path.join(directory, file)  # Create the full file path
        
        if os.path.isfile(file_path) and file != CleanFolder and "README" not in file:  # If it's a valid file
            _, ext = os.path.splitext(file)  # Separate the file name from its extension
            category = get_category(ext)  # Find the category of the file based on its extension
            category_path = os.path.join(directory, category)  # Create the path for the subfolder of this category
            
            # If the subfolder doesn't exist yet, create it
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            
            # Move the file to the appropriate subfolder
            try:
                shutil.move(file_path, os.path.join(category_path, file))
                print(f"{file} -> {category}/")  # Print a message showing where the file was moved
            except:
                print(f"Error while moving {file}")

# Executed when the script is run
if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()
    sort_files(directory)