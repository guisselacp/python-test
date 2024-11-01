squares = {}
for x in (2, 4, 6):
    squares[x] = x**2
print(squares)

# Dictionary Comprehension (same result)
squares = {x: x**2 for x in (2, 4, 6)}
print(squares)

# Runnable
# 1. {'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}
fruits = ['apple', 'mango', 'banana','cherry']
print({f:len(f) for f in fruits})

# 2. {0: '', 1: '*', 2: '**', 3: '***', 4: '****'}
print({i:(i*'*') for i in range(0,5)})

# 3. {0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
print({i:(True if i%2==0 else False) for i in range(10)})

# 4. {(0, 0): True, (0, 1): False, (0, 2): False, (0, 3): False, (1, 0): False, (1, 1): True, (1, 2): False,
# (1, 3): False, (2, 0): False, (2, 1): False, (2, 2): True, (2, 3): False, (3, 0): False, (3, 1): False,
# (3, 2): False, (3, 3): True}
print({(i,j): (True if i==j else False) for i in range(4) for j in range(4)})

# Challenge
cards = ['king', 'queen', 'jack', 'ace']
cards_dict= { }
cards_dict = {key:key.upper() for key in cards}
print(cards_dict)