import csv

data = csv.DictReader(open("departments.csv"))
print("CSV file as a dictionary: \n")

for row in data:
    print(row)