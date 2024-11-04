class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call} and is {self.definition}" 


class Parrot(Bird):
    def __init__(self, color):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())

# Challenge
class Employee:
    """
    Creates an instance of Employee
    """
    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary
    def calculate_monthly_salary(self):
        return self.annual_salary / 12
class CustomerServiceEmployee(Employee):
    """
    Creates an instance of CustomerServiceEmployee
    """
    def __init__(self, name, annual_salary, department):
        super().__init__( name, annual_salary)
        self.department = department
cs_manager =  CustomerServiceEmployee("Kelly Johnson", 42000, "Customer Service")
kellys_monthly_salary = cs_manager.calculate_monthly_salary()
print(kellys_monthly_salary)