'''
Validate a given public IP address to check if it follows the correct format (IPv4).
Validate a given email address to check if it’s a valid Gmail address, considering:
It should contain "@gmail.com".
The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
Provide informative error messages for invalid IP or email.
'''

import re
import ipaddress


def validate_ip(ip):
    
    pattern = r'^((25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$'

    if re.match(pattern, ip):  
        try:
            ip_obj = ipaddress.IPv4Address(ip)  
            if not ip_obj.is_private:           
                print(f"Valid Public IP: {ip}")
            else:
                print(f"Private IP Address Detected: {ip}")
        except ipaddress.AddressValueError:
            print(f"Invalid IP Address: {ip}")
    else:
        print(f"Invalid IPv4 Format: {ip}")


def validate_gmail(email):
    
    pattern = r'^[a-z0-9._%+-]+@gmail\.com$'
    if re.match(pattern, email):
        print(f"Valid Gmail Address: {email}")
    else:
        print(f"Invalid Gmail Address: {email}")


ip = input("Enter an IPv4 address: ")
email = input("Enter a Gmail address: ")


validate_ip(ip)
validate_gmail(email)
