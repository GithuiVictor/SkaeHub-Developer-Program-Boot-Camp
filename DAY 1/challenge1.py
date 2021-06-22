def my_leap_year(year) :
    if year % 4 == 0 and year % 400 == 0:
        print(bool(year))
    elif year % 100 == 0:
        print(bool())

year = input("Enter your year of choice: ")
my_leap_year(int(year))