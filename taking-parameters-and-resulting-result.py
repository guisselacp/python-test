
def numbers(a,b,c):
    mult = a * b * c
    return mult
result = numbers(2,4,8)    
print(result)

# Challenge
def add_numbers(nums_tuple, min_value):
    return sum([n for n in nums_tuple if n >= min_value])
 
total = add_numbers((21, 4, 7, 19, 1), 15)
print(total)