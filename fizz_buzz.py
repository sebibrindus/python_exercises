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

print("*" * 40)
print("** Welcome to Fizz Buzz game! **")
print("** Press '0' to exit game")

# line below gets the input from the user and converts it to int
user_max = int(input("Please enter max number: "))
# the users enters the maximum value of the range to play

if(user_max == 0):
        exit

for i in range(1, user_max + 1, 1):
    print(fizz_buzz(i))