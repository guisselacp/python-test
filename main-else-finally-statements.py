def linecount(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    try:
        f = open(filename, 'r')
        s = f.readlines()
    except OSError as e:
        # OSError exception is used as it deals with system errors such as I/O errors
        # OSError returns an error code (errno) and message (strerror)
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")
    else:
        # This is the code that does the line counting
        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
        f.close()
    finally:
        # This will print whether the line count has been successful or not
        print(f'Finished with {filename}.')
    
linecount('gulliver.txt')
print("\n")
linecount('swift.txt')

# Runnable Example
def linecount(filename):
    """
    Counts the lines in a text file.
    Prints the opening line of a text file. 
    """
    try:
        with open(filename, 'r') as f:
            s = f.readlines()
    except OSError as e:
        errno, strerror = e.args
        print(f"There is an I/O error number, {errno}: {strerror}.")
    else:

        print(f'{filename} is {len(s)} line long.')
        print(f"The opening line of {filename} is '{s[0]}'")
    finally:
        print(f'Finished with {filename}.')
        
linecount('gulliver.txt')
print("\n")
linecount('swift.txt')

# Challenge
cars = {'ford': 5, 'hyundai': 6}
def update_cars(data, key, val):
    try:
        data[key]
    except KeyError as e:
        print(f"No key {e} in dictionary")
    else:
         data[key] = val
    finally:
        return data
update_cars(cars, "mazda", 8)


# Do Not Place Code Below This Line 
# This will print out the cars dictionary after the update_cars function is called
print(cars)

