import random

print("I'm thinking of a number between 1 and 100")
guess = 0 #give guess starting value
numbers = random.randrange(1,100) # this line generates a random number
guess = '' # ask for number

while (guess != numbers):
    guess = int(input("What is your guess?\n"))
    if (guess > numbers):
        print("Wrong! You guessed too high!!")
    elif (guess < numbers):
        print("Wrong! You guessed too low")   
print("Congratulations! You won!")     