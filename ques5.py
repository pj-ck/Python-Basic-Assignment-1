'''Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.
Identify and list duplicate files by comparing their checksums.
Optionally, give the user the option to delete or move duplicate files.
'''


import os
import hashlib
import shutil

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        print(f" Error reading {file_path}: {e}")
        return None

def find_duplicates(directory):
    checksums = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            if checksum:
                if checksum in checksums:
                    duplicates.append((file_path, checksums[checksum]))
                else:
                    checksums[checksum] = file_path

    return duplicates

def handle_duplicates(duplicates):
    if not duplicates:
        print("No duplicate files found.")
        return

    print("\n Duplicate Files Found:")
    for i, (dup, original) in enumerate(duplicates, 1):
        print(f"{i}. Duplicate: {dup}\n   Original: {original}\n")

    choice = input("Do you want to (d)elete, (m)ove, or (s)kip duplicates? [d/m/s]: ").lower()

    if choice == 'd':
        for dup, _ in duplicates:
            try:
                os.remove(dup)
                print(f"Deleted: {dup}")
            except Exception as e:
                print(f"Failed to delete {dup}: {e}")

    elif choice == 'm':
        target_dir = input("Enter the target directory to move duplicates: ")
        os.makedirs(target_dir, exist_ok=True)
        for dup, _ in duplicates:
            try:
                shutil.move(dup, target_dir)
                print(f"Moved: {dup} to {target_dir}")
            except Exception as e:
                print(f"Failed to move {dup}: {e}")

    else:
        print(" Skipping duplicate management.")

if __name__ == "__main__":
    directory = input(" Enter the directory path to scan for duplicates: ")
    if os.path.isdir(directory):
        duplicates = find_duplicates(directory)
        handle_duplicates(duplicates)
    else:
        print(" Invalid directory path.")
