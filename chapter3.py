# OBJECT ORIENTED PROGRAMMING(PYTHON) 

# OVERVIEW OF OBJECT ORIENTED PROGRAMMING 
# CLASSES => objects with state & behavior 
# OBJECTS => instance of class 
# ATTRIBUTES => define a property of an object 
# ENCAPSULATION => hiding the internal details of an object 
# ABSTRACTION => extension of encapsulation, keeps object oriented programming simple 
# certain properties and methods from the code are hidden 
# POLYMORPHISM => ability of an object in object oriented programming to make many forms 
# INSTANTIATION => process of allocating memory for an object after its constructor is run 
# CONSTRUCTORS => are a unique method that Python calls for instantiations (creations) 
# of object definitions found within a class.


class Person:
    # init method or constructor 
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
p = Person("John", 36) 
print(p.name) 


# Methods inside a class => function defined inside a class 
# types of methods 
# Accessor methods => methods that simply observe but not change the state of an object 
# Mutators => methods that allow for the modification of an object state 

# BANKING APP 
# class that creates an object of customer id, firstname and lastname 
class BankCustomer:
    def __init__(self, id, firstname, lastname):
        self.id = id 
        self.firstname = firstname 
        self.lastname = lastname 
# method that displays the information 
    def displayinfo(self):
        print("Customer first name is " + self.firstname) 
        print("Customer last name is " + self.lastname) 
        print("Customer id is " + self.id) 

class BankAccount:
    def __init__(self, a_id, name, accounttype):
        self.a_id = a_id 
        self.name = name 
        self.accounttype = accounttype 
    def displayinfo(self): 
        print("Account id is " + self.a_id) 
        print("Account name is " + self.name) 
        print("Account type is " + self.accounttype) 

customer1 = BankCustomer(300, "John", "Doe") 
customer1.displayinfo() 


# ATTRIBUTES => class attributes vs instance attributes 
# instance attributes, each object is created with the class has its own copy of attributes 
# defined inside init 
# class attributes => all objects created from the class share the attributes 
# associated with the class as a whole and not instance 
# defined outside of init method 
class Manager:
    level = "L1" 
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 

p1 = Manager("Jesse", "Mensah") 
print(p1.fname) 
print(p1.lname) 
print(p1.level)

class CheckingAccount:
    type = "checking" 
    def __init__(self, id, balance):
        self.id = id 
        self.balance = balance 
ch1 = CheckingAccount(100, 2000) 
print(ch1.type) 


# @STATICMETHOD => this is a decorator 
# what it does is consider method to be static which will execute without class being instantiated 
# once method is static, you cannot use it to call instances of that class 
# they are used to perform some unrelated tasks 
# static methods cannot access instance attributes 
class MathFormula:
    @staticmethod 
    def display(message):
        print(message) 
    @staticmethod 
    def pow(x, y):
        return x ** y 
    @staticmethod 
    def isEven(x):
        if x % 2 == 0:
            return True 
        return False 
MathFormula.display("Hello")
MathFormula.display(MathFormula.pow(2, 3)) 

# CLASSMETHOD => same as static method but can access class attributes 
# an example 
class Sales:
    @staticmethod 
    # apply sales tax to an input amount and return result 
    def applySalesTax(amount):
        sales_tax = 0.06 
        return amount*(1 + sales_tax) 
    @staticmethod 
    # same as above 
    def applySalesTaxMany(amounts):
        out = list() 
        sales_tax = 0.06 
        out = [amount*(1 + sales_tax) for amount in amounts] 
        return out 
# comments => both methods contain sales tax 
# better to have sales tax as an attribute of the class so its not confused with an instance attribute 
# for all methods to share that attribute, we use classmethods 
class Sales:
    sales_tax = 0.06 
    @classmethod 
    def applySalesTax(cls, amount):
        return amount*(1 + cls.sales_tax) 
    @classmethod 
    def applySalesTaxMany(cls, amounts):
        out = list() 
        out = [amount*(1 + cls.sales_tax) for amount in amounts] 
        return out
print(Sales.applySalesTax(20)) 
print(Sales.applySalesTaxMany([20, 30, 40])) 


# INHERITANCE => inherit attributes and methods from other classes 
# POLYMORPHISM => uses those inherited methods to perform different tasks 
# base class 
class Person:
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname 
    def display(self):
        print(self.fname + " " + self.lname) 
x = Person("Jesse", "Mensah") 
x.display() 

# CREATING A CHILD CLASS 
class Employee(Person):
    pass 
e = Employee("Jesse", "Mensah") 
e.display() 

class AnotherEmployee(Person):
    def __init__(self, fname, lname, id):
        self.id = id 
        Person.__init__(self, fname, lname) 

class Director(AnotherEmployee):
    def __init__(self, emp_id, fname, lname, dlevel):
        self.dlevel = dlevel 
        AnotherEmployee.__init__(self, fname, lname, emp_id) 
d1 = Director(100, "Jesse", "Mensah", "L1") 
d1.display() 
print("Employee ID: " + d1.employeeid)

# OVERRIDING A METHOD 
class finalEmployee(Person):
    def display(self):
        print("Employee name is " + self.fname + " " + self.lname) 
ouremployee = finalEmployee("Jesse", "Mensah") 
ouremployee.employeeid = 100 
ouremployee.display()