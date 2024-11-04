# os.path()
import os

# This is how you would join two paths in your code
print(os.path.join('/home/runner/', 'os'))

path = "/home/runner/os/main.py"
# Splits the path into a pair (head, tail) where the tail is the end of the pathname
# The tail is after the / and the head is the pathname up to that point 
(dirname, filename) = os.path.split(path)
print(f'The directory path is {dirname}')
print(f'The filename is {filename}')
# Splits the filename into a pair (root, ext)
# The root is before the dot and the ext contains the dot with the suffix after it
(module, extension) = os.path.splitext(filename)
print(f'The module is {module}')
print(f'Its file suffix is {extension}')

# Random
import random

print(f'A random float between 0 & 1.0: {random.random()}')
print(f'A random int between 0 & 10: {random.randrange(11)}')
print('A random choice from a list: ' + random.choice(['paper', 'scissors', 'rock']))
deck = ['hearts', 'diamonds', 'spades', 'clubs']
random.shuffle(deck)
print(deck)

# Challenge - Random
import random

def ten_rand_nums():
    list = []
    n = 10
    for i in range(n):
        list.append(random.randint(0,100))
    return list
result = ten_rand_nums() 
print(result)
random.shuffle(result)
print(result)
