# Reading Data from a User
username = input("Type in your name and press return: ")
# The programme will remain stopped until you respond to this prompt with some text and press the return key
# As the value type that is received from an input is a string
# We need to convert it to a number to be able to use it on line 7
# We can do this by wrapping the input inside the int() method
age = int(input("Please enter your age: "))

days = 365 * age
# days is a number
# To concatenate it to the string we have to convert it to a String
# Notice below we do this like: str(days)
print("Hello " + username + ", you have been alive for at least " + str(days) + " days")

# Returning Data to a User
import math

i = 10 + 20
print(i)
language = "Python"
version = 3
print(f'We are using {language}{version}')
# Here the format specifier .2f is used to truncate at 2 decimal places
print(f'The value of pi to 2 decimal places is {math.pi:.2f}')
# The currency symbol for pounds sterling has Unicode character number 163
pound = chr(163)
tabulate = {'Egg & Spam': 1, 'Egg, Bacon & Spam': 1.5, 'Egg, Bacon Sausage & Spam': 2, }
# Loops over a dictionary of menu items as keys and prices as values
for item, price in tabulate.items():
    # The format specifiers here denote a minimum width of 25 and 5 characters
    print(f'{item:25} - {pound}{price:5}')

# Runnable Example
for number in range(99, 0, -1):
    line_one = f"{number} bottle(s) of beer on the wall. {number} bottle(s) of beer"
    line_two = f"Take one down, pass it around. {number-1} bottle(s) of beer on the wall\n"

    print(line_one)
    print(line_two)