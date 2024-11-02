# Example
def addition(a, b):
    return a + b

print(addition(2,2))
# Example where you create a list (standard)
def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total
list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

# Example where I use *arg
def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

# Example where I use **kwarg
def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))

# Challenge
# Challenge *arg
def make_string(*strings):
    return " ".join(strings)

my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")    
print(my_string)    

# Challenge **kwarg
def get_age(**data):
    for key, value in data.items():
        if key == "age":
            return value
    return "no age provided" 
pats_age = get_age(name="pat", level=4, age=33, occupation="postman")
print(pats_age)
