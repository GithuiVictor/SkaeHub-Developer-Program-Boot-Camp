# import csv

# data = csv.DictReader(open("departments.csv"))
# print("CSV file as a dictionary: \n")

# for row in data:
#     print(row)

import csv
#opening the file and reading it
#r opens the file
with open("job.csv", 'r') as file:
    #creating an object
    csv_file = csv.DictReader(file)
    #for loop for iterating over the csv_file object
    for row in csv_file:
        #creating dictionaries
        print(dict(row))