i = 2
while i < 10:
    j = 2
    while j <= i/j:
        if not i % j: # to understand: if (i%j == 0):
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1
    
# Challenge
x = 0
while x <= 3:
    y = 200
    while y <= 203:
        print(x,y)
        y += 1
    x += 1      