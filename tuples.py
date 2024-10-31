empty = ()
singleton = 'hello',
tup = 12345, 54321, 'hello!' # packing two ints and a string in a tuple
print(empty)
print(singleton)
print(tup)
print(tup[1])
x, y, z = tup # unpacking tuple into variables
print(z)

# Challenge
cars = "Tesla", "BMW", "Ferrari"
print(cars)
get_car = cars[1]
print(get_car)
car_one, car_two, car_three = cars
print(car_one)
print(car_two)
print(car_three)