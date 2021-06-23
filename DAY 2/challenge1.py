def is_power_of_four(number):
    while number % 4 == 0:
       number /= 4
    return number == 1

number = int(input("Enter a value: "))
print(is_power_of_four(number))