matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

#Runnable Example
matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]

print([[row[i] for row in matrix] for i in range(4)])    

# Runnable Test
payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

print(payroll)

print(payroll['emp1']['name'])
print(payroll['emp1'].get('salary'))
print(payroll['emp1'].get('Wage'))
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}
print(payroll)
del payroll['emp3']

for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')
# Challenge
student_data= [
    {'name': 'John Smith', 'email': 'john@gmail.com', 'subjects': ['Math', 'Psychology', 'Physics', 'Chemistry','Biology']},{'name': 'Mary Jones', 'email': 'mary@gmail.com', 'subjects': ['Fine Art', 'Music','Biology', 'Geography','Politics']}
]
print(student_data)