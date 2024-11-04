while True:
    try:
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except (ZeroDivisionError, ValueError):
        print('An error has occurred')

# Challenges
try:
    print(non_existent_variable)
except NameError:
    print("Variable not defined")


