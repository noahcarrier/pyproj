import os
import shutil

# broad file categories dictionary
file_categories = {
    "Text Files": [".txt", ".docx", ".rtf", ".pdf", ".csv", ".xls", ".xlsx", ".md", ".json", ".xml"],
    "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm"],
    "Audio Files": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".app", ".jar"],
    "Scripts": [".py", ".js", ".php", ".html", ".css", ".ts", ".rb"],
    "Databases": [".sql", ".db", ".sqlite", ".mdb", ".accdb"],
    "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv", ".tsv"],
    "Presentations": [".ppt", ".pptx", ".key", ".odp"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Log Files": [".log", ".err", ".out", ".trace"],
    "System Files": [".sys", ".dll", ".ini", ".cfg"],
    "Temp Files": [".tmp", ".swp", ".bak", ".old"],
    "Programming Files": [".cpp", ".h", ".cs", ".java", ".swift", ".go", ".lua", ".ts", ".json"],
    "Documents": [".pdf", ".docx", ".doc", ".rtf", ".odt", ".tex"],
    "Web Files": [".html", ".css", ".js", ".php"],
    "Other Files": []
}

# prompt user for directory selection
directory = input("Enter the directory path to organize: ")

# check if the directory exists
if not os.path.isdir(directory):
    print("Error: The specified directory does not exist.")
    exit()

# iterate over files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # skip if it's a directory (we only want files)
    if os.path.isdir(file_path):
        continue
    
    # extract file extension
    _, file_extension = os.path.splitext(filename)
    
    # loop through file categories
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:  # check if the extension matches any category
            # make the category folder if it doesn't exist
            category_folder = os.path.join(directory, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder, exist_ok=True)
            
            # move the file into the category folder
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved {filename} to {category} folder.")
            break
    else:
        # if no category matched, move it to 'Other Files'
        other_folder = os.path.join(directory, "Other Files")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder, exist_ok=True)
        
        shutil.move(file_path, os.path.join(other_folder, filename))
        print(f"Moved {filename} to Other Files folder.")

