import csv

with open('spreadsheet2.csv', 'w') as csv_data:
    csvwriter = csv.writer(csv_data)
    csvwriter.writerow(["firstname", "Lastname", "email", "age"])
    csvwriter.writerow(["ladi", "ajayi", "ladi.ajayi@learn.com", "35"])
    csvwriter.writerow(["toyosi", "shekoni", "toyosi.shekoni@learn.com", "37"])