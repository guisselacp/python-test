user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")

# Runnable Example
# Create a set
directions = set(['north', 'south', 'east', 'west'])

# Print its members
for direction in directions:
    print(direction)

# Add an item to the set:
directions.add('northwest')

print()
# Print the members again
# Notice the order cannot be relied upon!
for direction in directions:
    print(direction)

# Challenge
data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

scores = [6, 9, 8, 7, 8, 9]

for key, value in data.items():
    #use data[key] to call the value
    if data[key] != "student":
        data[key] = data[key].capitalize()
print(data)

for ind in range(len(scores)):
    scores[ind] +=1
print(scores)    