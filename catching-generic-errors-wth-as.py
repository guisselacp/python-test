def encode_name(name):
    try:
        name = name.encode('ascii')
    except UnicodeError as e:
        print(f'The name {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason}')
    return name
    
encode_name('Stéfan')

# Runnable Example
try:
    f = open('book.txt')
    s = f.readline()
except OSError as e:
    errno, strerror = e.args
    print(f"There is an I/O error number, {errno}: {strerror}.")

# Challenge
values = (10, 5)
def append_to_list(ls,val):
    try:
        ls.append(val)
    except AttributeError as e:
        print(e.args[0])
        return ls
append_to_list(values,4)

# Do Not Place Code Below This Line 
#this will print out the values variable after the append_to_list function is called
print(values)