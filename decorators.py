def my_decorator(func):
    def wrapper():
        print("The function has not been called yet. Let's call it.")
        func()
        print("The function was called and has returned a result.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")
    
say_hello()

# Runnable Example
def define_units(unit):
    """Define the units"""
    def decorator_define_units(func):
        func.unit = unit
        return func
    return decorator_define_units

@define_units('m^2')
def area(length, width):
    """Calculate area of rectangle or parallelogram"""
    return length * width

# The unit defined in the decorator can be used with dot notation
# In this case the function area units can be used as area.unit
print(f'The area is {area(3,5)}{area.unit}')

# Challenge
