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
        a = int(input("Please enter an integer as the numerator: "))
        b = int(input("Please enter an integer as the denominator: "))
        print(a / b)
    except ZeroDivisionError:
        print("Please enter a valid denominator.")
    except ValueError:
        print("Both values have to be integers.")
    except Exception:
        print('Another error has occurred')






