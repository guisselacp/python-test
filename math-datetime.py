# Math
import math

print(math.pi)
print(math.sqrt(4))

# Challenge - Math
import math
num = 81.5
round_up = math.ceil(num)
print(round_up)
round_down = math.floor(num)
print(round_down)
square_root = math.sqrt(round_down)
print(square_root)

# Datetime
from datetime import datetime

x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

the_date = datetime.now().date()
print(the_date)

the_time = datetime.now().time()
print(the_time)

# Challenge - Datetime
from datetime import datetime

today = datetime.now().date()
print(today)
