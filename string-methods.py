my_string = "HELLO WORLD"
my_string_lower_case = my_string.lower()

print(my_string_lower_case)

my_string_2 = "hElLo WorLD"
my_string_2_upper_case = my_string_2.upper()

print (my_string_2_upper_case)
print (my_string.isalpha())

greetings = my_string.replace("WORLD", "Dave")
print(greetings)

motion = ("jump", "walk", "run", "sing")
new_string = "ing ".join(motion)
print(new_string)

print(my_string_2.split(" "))
spaced_string = "     42       "
print(spaced_string.strip())

#Challenge
dwarves = "Grumpy, Dopey, Doc, Happy, Bashful, Sneezy, Sleepy"
print(dwarves)

lowercase_string = dwarves.lower()
print(lowercase_string)

commas_removed = lowercase_string.replace(",", "")
print(commas_removed)

split_list = commas_removed.split()
print(split_list)