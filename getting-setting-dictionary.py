keys = ['username', 'first_name', 'last_name', 'age']
default_value = ''
user = dict.fromkeys(keys, default_value)
print(user)
user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)
print(user['age'])
print(user.get('home', "doesn't exist"))
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user.keys()))
print(list(user.values()))
print(user)

# Challenge
data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

name = data.get("first_name")
print(name)
species = data.get("species")
print(species)
#data.update({"age": "42"})
data['age'] = 42 # Add a new key and value

# this will print the data to the terminal
print(data)