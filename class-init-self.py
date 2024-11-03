# Example __init__
class Car:
	def __init__(self, color, make, model, fueltype):
		self.color = color
		self.make = make
		self.model = model
		self.fueltype = fueltype

bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline')
print(bullitt)
print(bullitt.color)
print(bullitt.make)
print(bullitt.model)
print(bullitt.fueltype)

# Challenge __init__
class Customer:
    """
    Creates an instance of Customer
    """
    def __init__(self, fname, lname, email, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        
# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
print(customer_one)
print(customer_one.fname)
print(customer_one.lname)
print(customer_one.email)
print(customer_one.phone)

# Example - self
class Bird:
   """
   Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())
print(owl.kind)

# Challenge - self
class OrderItem:
    """
    Creates an instance of OrderItem
    """
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    def description(self):
        return f"{self.quantity} x {self.item} at ${self.price} each"

# The code below will use your class to print values to the terminal after 
# it has been written. Comment the lines below back in to test it  

order_item_one = OrderItem("bowtie", 10, 3)
print(order_item_one.description())

order_item_two = OrderItem("Fez", 25, 1)
print(order_item_two.description())

# Runnable Example - Creating Class Instances

class Bird:
   """
      Bird class
   """
   def __init__(self, kind, call):
      #properties
       self.kind = kind
       self.call = call

   #behaviour
   def description(self):
       """
       describe the bird
       """
       return f"A {self.kind} goes {self.call}" 
  
   def bird_call(self):
       print(self.call.upper())

owl = Bird('Owl', 'Twit Twoo!')
print(owl.call)
print(owl.description())
crow = Bird('Crow', 'Caaaw!')
print(crow.description())
owl.call = 'screech'
print(owl.description())
del owl.call
#print(owl.description())

# Challenge - Creating Class Instances
class User():
    """
    Creates an instance of User
    """
    def __init__(self, username, email, subscribed):
        self.username = username
        self.email = email
        self.subscribed = subscribed
    
    def description(self):
        """
        Describes the instance of User
        """
        return f"user: {self.username}, email: {self.email}, subscribed: {self.subscribed}"

user_one = User("arnold", "arnold@email.com", True)
print(user_one.email)
user_one.email = "murphy@email.com"
print(user_one.description())

# Runnable Example - Class Properties & Attributes - Class attribute of definition
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
        return f"A {self.kind} goes {self.call}" 
       
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())
print(owl.definition)
print(owl.call)
print(Bird.definition)
print(Bird.call)

# Challenge - Class Properties & Attributes - Class attribute of definition
class ContactInfo:
    """
    Creates an instance of ContactInfo
    """
    about =  "Contact information for customer"
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def description(self):
        return f"{self.name}:{self.email}"

print(ContactInfo.about)
contact = ContactInfo("dave", "lister@email.com")
print(contact.description())
 
