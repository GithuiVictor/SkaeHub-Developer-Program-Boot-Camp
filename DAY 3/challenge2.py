import numpy as np

# year = int(input("Please enter the year: "))
year = input("Please enter the year: ")

month = input("Please input the month: ")
if month == "January" or "january":
    month_number = 1
elif month == "February" or "february":
    month_number = 2
elif month == "March" or "march":
    month_number = 3
elif month == "April" or "april":
    month_number = 4
elif month == "May" or "may":
    month_number = 5
elif month == "June" or "june":
    month_number = 6
elif month == "July" or "july":
    month_number = 7
elif month == "August" or "august":
    month_number = 8
elif month == "September" or "september":
    month_number = 9
elif month == "October" or "october":
    month_number = 10
elif month == "November" or "november":
    month_number = 11
elif month == "December" or "december":
    month_number = 12

next_month = month_number + 1

number_of_weekdays = np.busday_count('{}-{}'.format(year, month_number), '{}-{}'.format(year, next_month))

print('Number of weekdays in {} {} is: {}'.format(month, year, number_of_weekdays))