# Initializing list of dictionaries
lis =[{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print("data before")
print("Original list of dictionaries :")
print(lis)
# using sorted and lambda to print list sorted
# by age
sort_data = sorted(lis, key = lambda i: i['age'])
print("\nData after  sorting:")
print(sort_data)