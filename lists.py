fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# Print all fruits
for fruit in fruits:
    print(fruit)

print()

# Get an item located in a list
second_item = fruits[1]
print(second_item)
print()

# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
fruits.sort()
print(fruits)

# Challenge
all_numbers = [1, 5, 44, 22, 13, 17, 56, 3, 88, 9, 97]
big_numbers = []
for number in all_numbers:
    if number > 40:
        big_numbers.append(number)
print(all_numbers)    
print(big_numbers)