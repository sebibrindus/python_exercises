def factorial(max_range: int) -> int:
    '''
    A function that multiplies every number between 1 and a given max number
    :param max_range: the maximum range for the factorial
    :return: returns the total product of the numbers
    '''
    product = 1
    for i in range(1, max_range + 1, 1):
        product *= i
    return product


max_factorial = int(input("Please enter a max number: "))

for i in range(1, max_factorial + 1, 1):
    print(str(i) + ": " + str(factorial(i)))
# the loop above prints all factorials between 1 and the given number

