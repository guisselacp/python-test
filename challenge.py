numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]

def get_odd_nums(list_of_nums):
    new_list = []
    for num in list_of_nums:
        if num % 2 != 0:
            new_list.append(num)
    return new_list
result = get_odd_nums(numbers)
print(result)




