import random
# this is a work in progress. I will try to update it and optimise it while I gain new knowledge

# short game presentation and instructions below:
print("Welcome!")
print("--------------------------------------")
print("This is a number guessing game. \n"
      "The number you will have to guess can be found between one (1) and a number of your choice. \n"
      "You will have to enter the highest number of the range (from the keyboard) \n"
      "But please be careful, the higher the range, the higher the difficulty, \n"
      "as you will only have 5 chances to guess!")

print("--------------------------------------")
print("Enter '0' to quit game")
print("--------------------------------------")

# retrieving user input and storing into variable (converting input to int):
highest = int(input("Please choose a maximum number for the range: "))
# this is the highest number that determines the range (from 1)
if highest == 0:
    print("Thank you for playing! Goodbye!")
    exit()

# generating a random number between 1 and the number from the user:
answer = random.randint(1, highest)

# setting maximum number of chances
chances = 5  #

# asking the user to enter guesses:
while chances > 0:
    print("Please enter a number between 1 and {} ".format(highest))
    #  converting user input to int:
    user_guess = int(input())

    # if the user enters the number '0', the game exits
    if user_guess == 0:
        print("Thank you for playing! Goodbye!")
        exit()

    # verify if the user entered the number in the correct range
    if user_guess < 0 or user_guess > highest:
        print("Number entered is outside range. Please try again.")
        print("You have {} chances left. ".format(chances))
        continue

    # compare user input to correct answer
    if user_guess == answer:
        if chances == 5:
            print("Congratulations! You guessed on your first chance!")
            exit()
        else:
            print("Congratulations! You guessed the correct number: {}! ".format(answer))
            exit()
    elif user_guess < answer:
        print("Incorrect. Guess higher")
        chances -= 1
        print("You have {} chances left. ".format(chances))
    else:
        print("Incorrect. Guess lower")
        chances -= 1
        print("You have {} chances left. ".format(chances))

if chances == 0:
    print("Bad luck! No more chances!")
    exit()

