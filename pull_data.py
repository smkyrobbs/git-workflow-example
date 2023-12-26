import csv
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES
from rich import print as rprint

#print(DEVICES)
for device in DEVICES:
    hostname = device["hostname"]
    with IOSXEDriver(
        host=device["host"],
        auth_username="john",
        auth_password="cisco",
        auth_strict_key=False,
    ) as conn:
        response = conn.send_command("show version")
        structured_data = response.textfsm_parse_output()[0]
        version = structured_data["version"]
        serial = structured_data["serial"][0]
        #rprint(f"{hostname} - {version} - {serial}:")

        with open('test.csv', 'a') as csv_data:
            writer = csv.writer(csv_data)
            my_data = ("Ladipo",hostname,serial,version)
            writer.writerow(my_data)
        #rprint(structured_data)
        