'''
Q4. Automating Software Package Updates
Write a Python program to automate the checking and updating of installed software packages on a Linux server. The script should:
Function to check for available updates using the system’s package manager (e.g., apt, yum). and list all available updates.
Ask user to Update all at once or provide any specific package name to update (take package index number for ease)
Install the available updates based on user input.
If any updates fail to install, log the error and send an alert (e.g., console log).
Optionally, schedule the script to run at a certain cron.
'''


import subprocess
import logging


logging.basicConfig(
    filename='package_update.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running command '{command}': {e.stderr.strip()}")
        print(f" ERROR: {e.stderr.strip()}")
        return None


def check_for_updates():
    print("Checking for available updates...\n")
    run_command("sudo apt update")
    updates = run_command("apt list --upgradable")
    
    if updates and "upgradable" in updates:
        update_list = updates.split('\n')[1:]  
        for idx, package in enumerate(update_list, 1):
            print(f"{idx}. {package}")
        return update_list
    else:
        print("All packages are up to date!")
        return []


def update_packages(packages, choice):
    if choice.lower() == 'all':
        print("\n Updating all packages...\n")
        result = run_command("sudo apt upgrade -y")
        if result:
            print("All packages updated successfully.")
            logging.info("All packages updated successfully.")
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(packages):
                package_name = packages[index].split('/')[0]
                print(f"\n Updating package: {package_name}\n")
                result = run_command(f"sudo apt install --only-upgrade -y {package_name}")
                if result:
                    print(f"Package '{package_name}' updated successfully.")
                    logging.info(f"Package '{package_name}' updated successfully.")
            else:
                print("Invalid package index.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'all'.")


def main():
    updates = check_for_updates()
    if updates:
        choice = input("\n Enter the package index number to update (or type 'all' to update everything): ")
        update_packages(updates, choice)

if __name__ == "__main__":
    main()
