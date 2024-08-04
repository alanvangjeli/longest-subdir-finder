import os
import sys


def find_longest_subdirectory(directory):
    longest_subdirectory = ""
    max_length = 0

    # Iterate through all subdirectories in the directory tree
    for dirpath, dirnames, filenames in os.walk(directory):
        for dir_name in dirnames:
            # Calculate the length of the directory name
            dir_length = len(dir_name)
            # Update if this is the longest found so far
            if dir_length > max_length:
                max_length = dir_length
                longest_subdirectory = dir_name

    return longest_subdirectory


if __name__ == "__main__":
    # Validate number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python longest_subdir.py <directory_path>")
        sys.exit(1)

    # Validate the given directory
    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    longest_subdirectory = find_longest_subdirectory(directory_path)
    print(longest_subdirectory)
