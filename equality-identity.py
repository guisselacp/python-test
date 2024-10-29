num = 1
num_two = num
print(num == num_two)
print(id(num))
print(id(num_two))

#Runnable Example
a=1
b=1.0
print(a==b)
print(a is b)
print(id(a))
print(id(b))
# a and b have the same numeric value but a different type
c=b
print(b==c)
print(b is c)
print(id(b))
print(id(c))
# b and c are equal in value and identity
