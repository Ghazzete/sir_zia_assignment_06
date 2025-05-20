# Class Methods

class Book:
    total_Books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_Books += 1

Book.increment_book_count()
print(Book.total_Books)

Book.increment_book_count()
print(Book.total_Books)

# Static Methods

class TemperatureConvetor:
    @staticmethod

    def celcius_to_fahrenheit(c):
      return (c * 9/5) + 32
    
f = TemperatureConvetor.celcius_to_fahrenheit(25)
print(f)

class Engine:
    def start(self):
        return "Engine started"
    
class Car:
    def __init__(self,engine):
        self.engine = engine

    def start_engine(self):
        return self.engine.start()
    
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_engine())

# Aggregation
class Employee:
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Department:
    def __init__(self,dep_name,employee: Employee):
        self.dep_name = dep_name
        self.employee = employee
        

    def display(self):
        print(f"Department: {self.dep_name}")
        self.employee.display()

emp1 = Employee(101, "Alice")

dept1 = Department("HR", emp1)

dept1.display()

del dept1
print("\n Department deleted but employee still exists:")
emp1.display()

#Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("show from Class A")

class B(A):
    def show(self):
        print("show from Class B")

class C(A):
    def show(self):
        print("show from Class C")

class D(B,C):
    pass

d = D()
d.show()

print(D.__mro__)

# Function Decorators

def log_function_call(func):
    def wraper():
        print("Function is being called")
        return func()
    return wraper

@log_function_call

def say_hello():
    print("Hello")

say_hello()

# Class Decorators

# Class decorator definition
def add_greeting(cls):

    def greet(self):
        return "Hello from Decorator!"
    setattr(cls, 'greet', greet)

    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Fizza")
print(p.greet())  

# Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self,price):
        self.price = price
        
@property

def price(self):
    """Getter method for price"""
    print("Greeting the price...")
    return self._Price

@price.setter
def price(self, value):
        """Setter method for price"""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        print("Setting the price...")
        self._price = value

@price.deleter
def price(self):
        """Deleter method for price"""
        print("Deleting the price...")
        del self._price

p = Product(100)
print(p.price)        

p.price = 150         

print(p.price)        

del p.price   

#callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(5)

print(callable(m))  

result = m(10)
print(result)       


# Creating a Custom Exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Access granted!")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)

#  Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for number in Countdown(5):
    print(number)

       