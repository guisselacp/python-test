numbers = [4, 7, 12, 33, 13, 67]
remove = numbers.pop
print(remove())
print(remove(0))

integers = [1, 2, 3, 4, 5, 6]
def is_mult_of_three(n):
    return n % 3 == 0
    
print(list(filter(is_mult_of_three, integers)))

# Runnable Example
def print_arguments( **args ):
    """Prints the arguments"""
    print(f'The arguments are {args}')

def pass_function(function_name, **args):
    """Takes a function as an argument
    Passes the argument 'l' to the function passed in 
    """
    print("This function takes another function as an argument")
    function_name(f=args['l'])

pass_function(print_arguments, l='spam')

