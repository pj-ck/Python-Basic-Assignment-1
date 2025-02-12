'''Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.
Identify and list duplicate files by comparing their checksums.
Optionally, give the user the option to delete or move duplicate files.
'''


import os
import hashlib

def calculate_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def find_duplicates(directory, min_size):
    checksums = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) >= min_size:
                checksum = calculate_checksum(file_path)
                if checksum in checksums:
                    duplicates.append((file_path, checksums[checksum], checksum))
                else:
                    checksums[checksum] = file_path
    return duplicates

def create_report(duplicates):
    with open("duplicate_report.txt", "w") as report:
        for dup, original, checksum in duplicates:
            report.write(f"Duplicate: {dup}\nOriginal: {original}\nChecksum: {checksum}\n\n")
    print(" Duplicate report saved as 'duplicate_report.txt'.")

if __name__ == "__main__":
    directory = input(" Enter the directory path: ")
    min_size_mb = int(input("Enter minimum file size in MB (e.g., 1 for 1MB): ")) * 1024 * 1024

    if os.path.isdir(directory):
        duplicates = find_duplicates(directory, min_size_mb)
        if duplicates:
            for dup, original, _ in duplicates:
                print(f"Duplicate: {dup}\nOriginal: {original}\n")
            create_report(duplicates)
        else:
            print("No duplicate files found.")
    else:
        print(" Invalid directory path.")
