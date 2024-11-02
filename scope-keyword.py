# Global keyword
can_access = False
	
def update_access():
    global can_access
    age = int(input('Enter your age: '))
    if age >= 18:
        # The global keyword is used
        can_access = True
        return('You are old enough to enter')
    else:
        return('You are too young, you may not enter');

update_access()

print(can_access) # will now print True if an age >= 18 is entered

# Challenge Global keyword
test_passed = False
answer = "friend"

def speak_friend_and_enter():
    global test_passed
    if answer == "friend":
        test_passed = True
        
speak_friend_and_enter()
print(test_passed)

# Nonlocal keyword
def which_scope():
    my_age = 49 # local variable my_age
    def inner_scope():
        nonlocal my_age # No longer an issue because of this
        my_age += 1
        print(my_age)
    inner_scope()

which_scope()

# Challenge Nonlocal keyword
def outer_function():
    age = 10
    def become_adult():
        nonlocal age
        age = age + 11
        
    become_adult()
    return age

result = outer_function()
print(result)