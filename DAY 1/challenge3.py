import random
import string

print("Hello, Welcome to the password generator app!")
length =int(input("\n Please enter what length you'd like your:"))

#Define data
lower = string.ascii_lowercase
upper =  string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine all the data
all = lower + upper + num + symbols

#Generate passwords
password = "".join(random.sample(all, length))

print("Your new password is: ", password)