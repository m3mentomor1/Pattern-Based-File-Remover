
# --------------------------------------------------
# File Name: file_remover.py
# --------------------------------------------------
# Date Completed: 12-08-2023
# --------------------------------------------------
# Description:
# This is a simple pattern-based file remover that 
# provides an efficient way to clean up files in a 
# specified directory based on a user-defined 
# naming pattern.
# --------------------------------------------------

import os
import glob

# Specify the directory and the pattern to match files (adjust it according to your file naming pattern)
directory_path = 'C:/**/**'
file_pattern = 'example.jpg'

# Get a list of files matching the pattern in the specified directory
files_to_delete = glob.glob(os.path.join(directory_path, file_pattern))

# Delete the files
for file_name in files_to_delete:
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error deleting file '{file_name}': {e}")
