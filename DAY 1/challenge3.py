import random
import string

# length =int(input("\n Please enter what length you'd like your:"))

# #Define data
# lower = string.ascii_lowercase
# upper =  string.ascii_uppercase
# num = string.digits
# symbols = string.punctuation

# #combine all the data
# all = lower + upper + num + symbols

# #Generate passwords
# password = "".join(random.sample(all, length))

# print("Your new password is: ", password)

class generate_password:
    def __init__ (self, length):
        self.length = length
    
    def password(self):
        lower = string.ascii_lowercase
        upper =  string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        #combine all data
        all = lower + upper + num + symbols

        password = "".join(random.sample(all, self.length))

        return "Your new generated password is: {}".format(password)

length = generate_password(int(input("\n Please enter what length you'd like your:")))
print(generate_password.password( length))