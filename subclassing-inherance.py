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
class JobListing():
    """
    Creates an instance of JobListing
    """
    def __init__(self, job_title, department):
        self.job_title = job_title
        self.department = department
    
    def description(self):
        return f"Job opening for {self.job_title} in {self.department} department"
# This means the SalesManager will be derived from the base class JobListing.
class SalesManager(JobListing):
    def __init__(self, salary):
        JobListing.__init__(self, 'Sales Manager','Sales')
        self.salary = salary
sales_manager = SalesManager(45000)
print(sales_manager.description())
print(sales_manager.salary)
