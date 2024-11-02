# A lambda function can take any number of arguments, but can only have one expression.
def print_message():
    print("Hello World!")

print_message()

# Runnable Example
add = lambda a, b : a + b
print(add(5, 12))

# Calling a function
# 2. This function runs for the name and age function calls
def get_user_input(prompt):
    return input(prompt)

# 4. This function runs twice
def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)

# 1. name and age are the first two function calls to run sequentially
name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

# 3. Then function calls run sequentially
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")

# Challenge
def print_hello_world():
    print("Hello World!")
print_hello_world()

# Taking Parameters and Returning Results
def print_message(name):
    print(f"Hello {name}")

username = input("What's your name? ")
print_message(username)

# Runnable Example
def print_message(name="World"):
    return f"Hello {name}"

username = input("What's your name? ")
print(print_message())
print(print_message(username))