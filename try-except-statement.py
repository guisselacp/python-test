# Challenge
cars = {'ford': 10, 'opel': 5 }
def get_val(key):
        try:
            return cars[key]
        except:
            return None
ford = get_val("ford")
print(ford)
hyundai = get_val("hyundai")
print(hyundai)

# Runnable Example
while True:
    try:
        x = int(input('Enter a number.'))
        print(f'Number is {x}')
    except ValueError:
        print('Not a number')






