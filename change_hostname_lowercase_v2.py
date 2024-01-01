from scrapli.driver.core import IOSXEDriver
from rich import print as rprint
import logging
import getpass

logging.basicConfig(filename="log.txt", level=logging.DEBUG)

DEVICE = {"hostname" : "CSR_Practice",
          "host" : "192.168.78.134"}
username = input("USERNAME: ")
password = getpass.getpass("PASSWORD:")

def test_func():
    with IOSXEDriver(host=DEVICE["host"], auth_username=username, auth_password=password, auth_strict_key=False) as conn:
        response = conn.send_command("show version")
        structured_data = response.textfsm_parse_output()[0]
        host_name = structured_data["hostname"]
        
#This line of code tests to see if device follows naming convention.       
        if host_name.startswith("CSR"):
            with open ("Naming_Standards.txt",'a') as f:
                f.write(f"{host_name} follows naming convention\n")
        elif host_name.startswith("csr"):
            with open ("Naming_Standards.txt",'a') as f:
                f.write(f"{host_name} follows naming convention but needs to be adjusted\n")
        else:
            with open ("Remediate_Hostname.txt",'a') as f:
                f.write(f"{host_name} does not follow naming convention\n")

#Testing to see if any letter in the hostname is lowecase. If it is, this line of code will update the hostname to all uppercase.
        for c in host_name:
            if c.islower():
                print(f"{host_name} has lowercase characters in hostname")
                conn.send_configs([f"hostname {host_name.upper()}", "do wr"])
                break
            else:
                with open ("log_uppercase.txt",'a') as f:
                    f.write(f"{c} in {host_name} is uppercase\n")



if __name__ == "__main__":
    test_func()