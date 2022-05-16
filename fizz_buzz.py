def fizz_buzz(number: int) -> str:
    '''

    A function that prints "Fizz" for every number that is divisible by 3.
    Also prints "Buzz" for every number that is divisible by 5.

    For 15, for example, which is divisible by both 3 and 5, the program will print "FizzBuzz"

    Numbers processed are in a range starting from 1 and up to a number that the user
    enters from keyboard.

    :param number: variable of type int to be processed
    :return: returns a string (Fizz/Buzz/or the number)
    '''

    fizz = "Fizz"
    buzz = "Buzz"

    if number % 3 == 0 and number % 5 == 0:
        return fizz + buzz
    elif number % 3 == 0:
        return fizz
    elif number % 5 == 0:
        return buzz
    else:
        return str(number)


def check_input(user_input):
    '''
    A function that checks if a users input is numeric or not (for this app we need to be int)
    :param user_input: has to be int for the range of the game
    :return: returns true if numeric, false if otherwise
    '''
    if user_input.isnumeric():
        return True
    else:
        return False


print("*" * 40)
print("** Welcome to Fizz Buzz game! **")
print("** Press '0' to exit game")

# line below gets the input from the user and converts it to int
user_max = input("Please enter max number: ")
# the users enters the maximum value of the range to play

if check_input(user_max) is False:
    print("Please enter a valid number. \nGame closed.")
    exit()
# if the user enters an invalid input, the program closes


if user_max == 0:
    exit()

next_number = 0

while next_number < user_max:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your answer: ")
    if player_answer != correct_answer:
        print("Your answer is wrong. Try again.")
        break
else:
    print("Well done, you reached {}".format(next_number))
