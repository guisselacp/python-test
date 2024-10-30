# Break
for number in range(10):
    if number == 5:
        break    # break here

    print(f'Number is  {number}')

print('Left the loop')

# Challenge
x = 0
for x in range(9):
    if x == 8:
        break
    print(f'{x}')

# Continue
for number in range(10):
    if number == 5:
        continue    # continue here

    print(f'Number is  {number}')

print('Left the loop')

# Challenge


# Pass
for number in range(10):
    if number == 5:
        pass    # pass here

    print(f'Number is  {number}')

print('Left the loop')

# Challenge
x = 0

while x < 14 :
    if x > 4 and x < 11:
        pass
    else:
        print(f'{x}')
    x += 1  