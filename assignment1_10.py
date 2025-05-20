# 01:Using self keyword

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} Marks: {self.marks}")

student1 = Student("Fizza",90)
student1.display()

# Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total object count is: {cls.count}")

obj1 = Counter()
obj1 = Counter()
obj1 = Counter()

Counter.show_count()

# Public Variables and Methods
class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} Car is starting...")

my_car = Car("Toyta")

print("Car brand",my_car.brand)

my_car.start()

# Class Variables and Methods

# class Bank:
#     bank_name = "Habib Bank"

#     def __init__(self,customer_name):
#         self.customer_name = customer_name

#     @classmethod

#     def change_bank_name(cls,name):
#         cls.bank_name = name

#     def show_info(self):
#         print(f"Customer: {self.customer_name} Bank: {Bank.bank_name}")

# customer1 = Bank("Alice")
# customer2 = Bank("Bob")

# customer1.show_info()
# customer2.show_info()

# Bank.change_bank_name("Meezan Bank")

# customer1.show_info()
# customer2.show_info()
    
        
# Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
# Constructors and Destructors
result = MathUtils.add(5, 7)
print("Sum:", result)

class Logger:
    def __init__(self):
        print("Logger object has been created")

    def __del__(self):
        print("Logger object has been deleted")

log = Logger()

del log
        
# Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public variable
        self._salary = salary      # Protected variable
        self.__ssn = ssn           # Private variable

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Create an object
emp = Employee("Fizza", 5000, "112-22-7896")

# Accessing variables
print("Public:", emp.name)            
print("Protected:", emp._salary)      
# print("Private:", emp.__ssn)       

# Access private using name mangling
print("Private (using name mangling):", emp._Employee__ssn)  # ✅ Works

# The super() Function
class Person:
    def __init__(self,name):
        self.name = name
    
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher("Miss Fizza","Computer Science")

print("Name:",teacher1.name)
print("Subject:",teacher1.subject)
        
# Abstract Classes and Methods

from abc import ABC, abstractmethod

class shape(ABC):
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rect = Rectangle(5,4)
print("Area of rectangle:", rect.area())

# Instance Methods:

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def show_info(self):
        print(f"{self.name} says: Woof woof!")

my_dog = Dog("Buddy","Golder Retriever")

my_dog.show_info()

