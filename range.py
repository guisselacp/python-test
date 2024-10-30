# Return integers from 1 through 5
for i in range(1,6,1):
    print(i)

# Runnable Example
foods = ['bacon', 'sausage', 'egg', 'spam']

for ind in range(len(foods)):
	# In this example only the index is iterated over not the value
    print(ind, foods[ind])
print(foods)
# In this case we need to calculate the length of the foods collection
# Then we generate a range of integers equal to that length
# Then we iterate over that range of integers    

#Challenge
users = ['anna', 'chris', 'brian']

for index in range(len(users)):
    users[index] = users[index].capitalize()
    #update = [user.capitalize()for user in users]
print(users)


