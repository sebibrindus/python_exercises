def is_palindrome_short(string):
    return string[::-1].casefold() == string.casefold() #short version
    # the line above is performing a slice on the string passed as parameter to the function
    # and also after that it compares this to the original string

def is_palindrome_long(string):
    backwards = string[::-1]  # this part returns the reversed string
    if backwards.casefold() == string.casefold():
        return True
    else:
        return False

def is_palindrome_sentence(string):
    string_calculator = ""
    for char in string:
        if char.isalnum():
            string_calculator += char
    print(string_calculator)
    return is_palindrome_short(string_calculator)

user_input = input("Please input a user_input or sentence to check for palindrome: ")
# line above is storing user input into a variable
# user input can be user_input or sentence, code can handle both

sentence = False
words = user_input.split() # splitting the user input into separate words
count = words.__len__() # counting if there is a single word or more
if count >=2:
    sentence = True
else:
    word = True
# Lines above determine if the user`s input is a sentence or a single word

print("-" * 40)

if sentence is True:
    if is_palindrome_sentence(user_input):
        print("Your sentence is a palindrome.")
    else:
        print("Your sentence is NOT a palindrome.")
else:
    if is_palindrome_long(user_input):
        print("Long version of the function says: \n{} is a palindrome".format(user_input))
    else:
        print("Long version of the function says: \n{} is NOT a palindrome".format(user_input))
    # calling long version of the function above

    print("-" * 40)

    if (is_palindrome_short(user_input)):
        print("Short version of the function says: \n{} is a palindrome.".format(user_input))
    else:
        print("Short version of the function says: \n{} is NOT a palindrome.".format(user_input))
    # calling short version of the function above



