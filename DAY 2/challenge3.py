import random

number = random.randint(1, 200)
win = False
attempt = 0
print("Your hit:", number)
while win == False:
    guess = int(input("Enter your guess: "))
    attempt += 1
    if guess == number:
        print('You won!')
        print('Number of attempts: ', attempt)
        break
    else:
        if number > int(guess):
            print('Your guess was low, Please enter a higher number')
        else:
            print('Your guess was high, Please enter a lower number')