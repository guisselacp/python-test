#Determining Truth With Logical Operators Challenge
print(True and True)
print(True and False)
print(True or False)
print(not (4 < 5 and 4 < 10))

#Challenge
a = 10
b = 5

result_one =(a > b)  and (a > 10)
result_two = ((a == 5) or (b < 5))
result_three = (not (result_two))
print(result_one)
print(result_two)
print(result_three)

#Bool - Evaluate Values and Variables
a = []
b = ""
c = "Hello"
d = 0.0
e = 7

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))