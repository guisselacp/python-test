# Indexing
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
# As lists are zero-indexed index 0 is the first element
print(fruits[0])
print(fruits[2])
# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])
print(fruits[-6])

# Slicing
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])
print(fruits[-1])

# Runnable Example
fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:4:2])

# Challenge
names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]
name = names[2]
print(name)
two_names = names[2:4]
print(two_names)
other_names = names[1:6:2]
print(other_names)