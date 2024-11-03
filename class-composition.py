class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Engine:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        self.fuel = fuel
    
class InternalCombustion(Vehicle, Engine):
    def __init__(self, make, model, capacity, fuel):
        Vehicle.__init__(self, make, model)
        Engine.__init__(self, capacity, fuel)
        
class Electric(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)
        
volkswagen = InternalCombustion("Volkswagen", "Golf", 1.7, "Diesel")
tesla = Electric("Tesla", "X")

# Runnable Example
class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, fname, sname, no_of_years):
        # instance attributes
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"First Name: {self.fname}\n Surname: {self.sname}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"


class ExternalContract:
    """
    Class for contract employees
    """

    def __init__(self, contract_cost):
        self.contract_cost = contract_cost

    def cost(self):
        """
        Returns the contract cost added to the salary
        """
        return self.contract_cost + 30000


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """
    def calculate_holidays(self, no_of_years):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 20
        bonus = 0
        if no_of_years < 3:
            bonus = 1
        elif no_of_years <= 5:
            bonus = 2
        elif no_of_years > 5:
            bonus = 3
        return f'Holidays: {BASE_HOLIDAY + bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class. 
    """
    def __init__(self, fname, sname, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, fname, sname, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def details(self):
        """
        Method to return direct developer details as a string
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n'


class ContractDeveloper(HolidayMixin, Employee, ExternalContract):
    """
    Class is a subclass of Employee, composition relationship
    with ExternalContract and using HolidayMixin
    """
    def __init__(self, fname, sname, no_of_years, prog_language, contract_cost):
        self.prog_language = prog_language
        Employee.__init__(self, fname, sname, no_of_years)
        ExternalContract.__init__(self, contract_cost)

    def details(self):
        """
        Returns inherited details plus contract cost
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n Contract cost: {ExternalContract.cost(self)}'



dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
print(dev.details())
print(dev.calculate_holidays(dev.no_of_years))
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects. 
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays(contractor.no_of_years))

# Challenge
class TicketMixin:
    """Mixin to calculate ticket price based on age"""
    def calculate_ticket_price(self, age):
        
        if age < 12:
            price= 0
        elif age < 18:
            price = 15
        elif age < 60:
            price = 20
        else:
            price = 10
        return price
class Customer(TicketMixin):
    """
    Create instance of Customer
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        return f"{self.name} age {self.age} ticket price is {self.calculate_ticket_price(self.age)}"
customer = Customer("Ryan Phillips", 22)
print(customer.describe())
