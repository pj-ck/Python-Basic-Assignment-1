'''
Write a Python program to simulate a basic version control system for a directory of files. The script should:
Accept a directory path as input and store versions of files whenever changes are made.
Each time a file is modified, the script should create a new version and save it in a separate folder (e.g., ./versions).
Keep track of file versions by naming them with a version number or timestamp (e.g., file_v1.txt, file_v2.txt).
When a file is restored to a previous version, it should be copied from the version folder back to the original directory.
'''

import os
import shutil
import time

VERSION_DIR = './versions'


def save_version(file_path):
    if not os.path.exists(VERSION_DIR):
        os.makedirs(VERSION_DIR)
        
    filename = os.path.basename(file_path)
    timestamp = int(time.time())
    version_file = f"{filename}_v{timestamp}"
    shutil.copy2(file_path, os.path.join(VERSION_DIR, version_file))
    print(f"Version saved as {version_file}")


def restore_version(filename, version_timestamp):
    version_file = f"{filename}_v{version_timestamp}"
    version_path = os.path.join(VERSION_DIR, version_file)
    if os.path.exists(version_path):
        shutil.copy2(version_path, filename)
        print(f"Restored {filename} to version {version_timestamp}")
    else:
        print("Version not found.")


def cleanup_versions(filename, keep_last_n):
    files = [f for f in os.listdir(VERSION_DIR) if f.startswith(filename + '_v')]
    files.sort(key=lambda x: int(x.split('_v')[-1]), reverse=True)

    for old_version in files[keep_last_n:]:
        os.remove(os.path.join(VERSION_DIR, old_version))
        print(f"Deleted old version: {old_version}")


def main():
    while True:
        print("\n--Version Control System --")
        print("1️.Save Version")
        print("2️. Restore Version")
        print("3️. Cleanup Old Versions")
        print("4️.Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            file_path = input("Enter file path: ")
            if os.path.exists(file_path):
                save_version(file_path)
            else:
                print(" File not found.")
                
        elif choice == '2':
            filename = input("Enter filename: ")
            version_timestamp = input("Enter version timestamp: ")
            restore_version(filename, version_timestamp)
            
        elif choice == '3':
            filename = input("Enter filename: ")
            keep_last_n = int(input("How many recent versions to keep? "))
            cleanup_versions(filename, keep_last_n)
            
        elif choice == '4':
            print(" Exiting...")
            break
            
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
