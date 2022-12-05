# Python Syntax  
print("Hello World")  

# Variables ??
age = 30 
tax_rate = 0.05 
print(age) 
print(tax_rate) 

# Does python have constants?? Yes 
# use constants when you do not want value to change during the lifecycle of the program 
CONST_AGE = 30 
print(CONST_AGE)

# Check the data types 
accountBalance = 100 
print(type(accountBalance)) 

# Mathematical operations 
# Python supports these types of operations 
# Arithmetic, Comparison, Assignment, Logical, Bitwise, Membership, Identity 

# Arithmetic 
# create a variables and output result into variable 
a = 10 
b = 6 
c = a + b 
print(c) # Same can be dine for other operations=> addition, subtraction, multi, division etc 


# Logical Operations 
# True, False 
a = True 
b = False 
print(a) 
print(b) 

# Task => Querying a Banking customer 
# Taking response from a user 
savings = input("Do you have savings account? ") 
checking = input("Do you have a checking account? ") 
print(savings); 
print(type(savings)); 
print(checking); 
print(type(checking)); 


# Comparison operations = less then, greater than, equal, not equal, equality, inequality 
firstValue = 10 
secondValue = 5 
print("Is first value greater than second value? ", firstValue > secondValue) 
print("Is first value less than second value? ", firstValue < secondValue)


# Control flow statements 
# Control structures 
# 1. Sequence control structures => line by line executions of a program 
# 2. Selection control structures => ask questions and make decisions based on results 
# 3. Iteration control structures => for comparisons 

# statement 1 => statement 2 => statement 3 
# sequential flow of data 
print((2 + 3) * 10) 
print(2 ** 10) 
print(6 / 3) 

# selection statements => if and else statements 
password = "admin" # set a condition 
rightPassword = (password == "admin") 
if rightPassword: 
    print("Successfull login") 
if rightPassword == False:
    print("Wrong password") 

# if-else statements 
serverName = "sql90012" 
password = "pfp2015" 

if serverName == password: 
    print("Access Granted") 
else:
    print("Access Denied") 



# LOOPS 
# ANATOMY OF A LOOP 
# for loop => repeat a block of code for a specific number of times 
# evaluates a condition, performs specific activities, then moves to the next set of instructions 
for word in range(3):
    print("Hello World") 

# while loop => repeats a set of instructions as long as condition is true 
# as long as condition evaluates to true, the loop will continue to execute 
number = 10 
while ((number < 100) == True):
    print(number) 
    number += 1 


# for vs while loops 
# FOR LOOP 
# automatically determines the start point and the end point based on the number of items in the dataset 
# uses indexed values, so we do not have to define the values in the script 
# WHILE LOOP 
# requires an initial condition 
# uses values defined rather than values that are inherent in the dataset 
# may not run if the initial condition is not met 

# TEST 
# put usernames into an empty list 
names = [] 
# variable that sets to either yes or no, lets make it empty first 
userContinue = "" 

while userContinue != "No":
    userName = input("Enter your name? ") 
    print("You entered: "+userName) 
    # add username to the list 
    names.append(userName) 
    # prompt user to continue ? Yes or No 
    uContinue = input("Continue (Yes or No) ")
print(names) 


# Collecting a limited number of usernames 
# set the number of usernames to 5 
theNames = [] 
theUserContinue = "" 
count = 0 # set the count to 0 
while count < 5 and theUserContinue != "N": 
    userName = input("Enter your name? ") 
    print("You entered: "+userName) 
    count += 1 
    theNames.append(userName) 
    theUserContinue = input("Continue (Y or N) ") 
print(theNames) 



# STRINGS AND STRING OPERATIONS 
# Create a string variable 
realName = "Jesse Mensah" 
print(realName) 
print(type(realName)) 
# find the length of the string 
print(len(realName)) # number of the strings 

# String operations => use methods like split, replace, find etc 
message = "Hello World" 
print(message.split())  

# Concatenation 
firstName = "Jesse" 
secondName = "Mensah" 
fullName = firstName + " " + secondName 
print(fullName) 

# Slicing a string 
firstMessage = "Hello World" 
messageSlice = firstMessage[0:5]  
print(messageSlice) 

# memberships 
secondMessage = "Hello World" 
print("He" in secondMessage) 

# Iterating through Strings 
# create a string variable 
thirdMessage = "Hello World!" 
for ctr in thirdMessage: 
    print(ctr) 


# Iterating through employees 
employees = ["Jesse", "Mensah", "Kwame", "Rita", "Luis"] 
for employee in employees: # iterate through the list 
    print(employee)
    for eachEmployee in employee:
        print(eachEmployee.upper()) 
    print("------")



# BASIC DATA STRUCTURES: LISTS, TUPLES, DICTIONARIES, SETS.
# LISTS => SEQUENCE OF DATA VALUES CALLED ITEMS OR ELEMENTS 
# TUPLE => TUPLE IS A COLLECTION THAT IS ORDERED AND IMMUTABLE. ALLOWS TO DUPLICATE MEMBERS 
# DICTIONARY => KAY VALUE PAIRS 
# SET => COLLECTION OF UNORDERED AND UNINDEXED. A SET DOES NOT ALLOW DUPLICATE MEMBERS. 
# INDEX => AN INDEX RETURNS THE POSITION OF A TARGET ELEMENT IN A LIST 


# CREATING LISTS => ORDERED VS CHANGEABLE 
nameinLists = ["Jesse", "Amoako", "Mensah"] 

# TUPLE => ENCLOSED IN PARENTHESIS 
# IS ORDERED AND IS IMMUTABLE 
t = (1, 2, a) 

# DICTIONARY => UNORDERED, CHANGEABLE AND INDEXED 
d = {"a": 1, "b": 10} 

# SET => UNORDERED COLLECTION OF ITEMS 
s = {1, 2, 3} 


# LIST OF EMPLOYEES 
# empty list 
list1 = [] 
num = input("Enter number: ") 
print(num) 
for num in range(0, int(num)): 
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ") 
    position = input("Enter position: ") 
    empnum = input("Enter employee number: ") 
    list_of_items = [firstName, lastName, position, empnum] 
    list1.append(list_of_items) 
for ctr in list1: 
    print(*ctr, sep=", ")

# Accessing data from list 
name = nameinLists[0] 
print(name) 


# Slicing lists => [start:stop:step] 
slicedLists = ['a', 'b', 'c', 'd'] 
print(slicedLists[0:3]) 


# Adding items to a list 
list_of_names = [] 
print(list_of_items) 
list_of_names.append("Jesse") 
print(list_of_items) 

# capturing information inside a list 
info = [] 
info.append(input("Please enter customer first name: ")) 
info.append(input("Please enter customer last name: ")) 
print(info) 


# List comprehensions => another option for creating lists. short way to create a list using existing values 
numbers = list() 
for i in range(0, 11):
    numbers.append(i) 
print(numbers) 

#using list comprehension 
numbers = [i for i in range(0, 11)] 
print(numbers) 

realNames = ['Jesse', 'Mensah'] 
upperNames = [name.upper() for name in realNames] 


# without list comprehension 
namesUpper = [] 
for name in realNames:
    namesUpper.append(realNames.upper()) 
print(namesUpper) 

# List comphrehension with if-else statement 
numbers = [1, 2, -1, 6, -5, 2] 
label = ["positive" if number >= 0 else "negative" for number in numbers] 
print(label) 

# TUPLES 
age_range = (18, 20) 
print(age_range) 
print(type(age_range)) 

# Tuple with bank customer information 
Customer = ("Jesse", "Mensah", 1005162) 
print(Customer) 

password = ('a', 'b', 'c', 'd') 
if len(password) >= 4:
    print("Your password meets the requirements")
else:
    print("Your password does not meet the requirements")

# getting the index of values in a tuple
print(Customer[-1]) 
# slicing tupes 
print(Customer[0:2]) 

# Immutability => Python supports immutability. 
# does not support append 
# does not support insert 
# does not support remove, pop, del 

# Can concatenate tuples 
name = ("Jesse", "Mensah") 
address = ("123 Main Street, Leola, AR, 19987") 
contact = ("474-888-9483")
fullContact = name + address + contact 
print(fullContact) 

# SEARCHING TUPLES 
#create a tuple 
tuple_of_names = ("Jesse", "Mensah", "Kwame", "Rita", "Luis") 
search_term = "Mensah" 
if search_term in tuple_of_names:
    print(search_term + " is in the tuple") 
for name in tuple_of_names:
    if name == search_term:
        print("We found " + search_term) 

# DICTIONARIES => key value pairs 
# methods used by dictionaries => keys(), items(), values(), pop() . 
accounts_dict = dict() 
accounts_dict["Jesse"] = 1000 
accounts_dict["Mensah"] = 2000 
accounts_dict["Kwame"] = 3000 
print(accounts_dict) 

print(accounts_dict.keys()) 
print(accounts_dict.items()) 
print(accounts_dict.values()) 
print(accounts_dict.pop("Jesse")) 


# SETS => A set is an unordered collection of items in which every set element is unique and must be immutable (cannot be changed). 
names = {"Jesse", "Mensah", "Felix"} 
print(names) 

# LOOPING THROUGH A SET 
for name in names: 
    print(name) 
# SET METHODS => ADD, delete, clear, pop, 
names.add("Kwame") 

names = ["Jesse", "Mensah", "Felix", "Jesse", "Mensah", "Felix"] 
namesset = set(names) 
print(namesset) 

# search for items inside a set 
cust_list = {"Wolf Inc", "Acme Inc",
"Murray Ltd",
"BankCorps",
"PierBank",
"BankRoad",
"Cashop",
"Welch-Mann",
"Oberbrunner, Hamill and Marvin", "Faust Inc.",
"Watera",
"Jacobson LLC", "Micron Computers",
}

print(cust_list) 
lower_list = [x.lower() for x in cust_list] 
if input("Enter a customer name: ").lower() in lower_list:
    print("The customer name you entered matches an existing customer.") 
else:
    print("The name did not match any in out customer list") 


# DIFFERENCE BETWEEN SETS 
shake_1 = {"kiwi", "banana", "peanut butter"}
shake_2 = {"banana" "kiwi", "spinach"}
shake_3 = shake_1.difference(shake_2)
print(shake_1) 
print(shake_2) 
print(shake_3) 

# COMMON ITEMS BETWEEN SETS 
shake_1 = {"kiwi", "banana", "peanut butter"}
shake_2 = {"banana" "kiwi", "spinach"}
shake_3 = shake_1.intersection(shake_2) 
print(shake_3) 

# COMBINING SETS 
shake_1 = {"kiwi", "banana", "peanut butter"} 
shake_2 = {"banana", "kiwi", "spinach"} 
shake_3 = {"orange", "apple", "almonds"}
#the union method combines two or more sets. We can add as many sets as needed. 
shake_4 = shake_1.union(shake_2,shake_3)
print(shake_4)


# FUNCTIONS IN PYTHON 
# block of code that performs a specific task 
# syntax 
# def function(function_parameters): 
#     function body 
#     return function_result

# FUNCTION FOR ADDING TWO NUMBERS 
def add_numbers(firstnumber, secondnumber):
    return firstnumber + secondnumber 
# values to call the function 
sum1 = add_numbers(100, 200)
sum2 = add_numbers(1000, 2000) 
print(sum1) 
print(sum2) 

# function to find numbers greater than a threhold 
def find_numbers_greater(numbers, threshold):
    for num in numbers:
        if (num > threshold):
            print(num) 
# put all the numbers inside a list 
numbers = [1, 2, 100, 1000, 2000, 20, 40, 199] 
find_numbers_greater(numbers, 100) 

# create a function to find numbers divisible by a factor 
def find_div(numbers, factor):
    for num in numbers:
        if num % factor == 0:
            print(num) 
numbers = [1, 2, 100, 1000, 2000, 20, 40, 199]
find_div(numbers, 10) 

# function to check a limit 
def check_limit(amount):
    if amount > 1000:
        print("You have exceeded your limit")
    else:
        print("You are within your limit") 

# default parameters 
def display(message="Hello"):
    print(message) 

def the_function(fname, lname):
    print(fname + " " + lname) 
the_function("Jesse", "Mensah") 

# Variable amount of information passed to a function 
def displayteam(*teammembers):
    for member in teammembers:
        print(member) 
displayteam("Jesse", "Mensah", "SQL Data Analyst")
print("------")
displayteam("David", "Johns", "Data Engineer") 


# Function that computes a sum of variable number of items 
def compute_sum(*numbers):
    total = 0 # variable set to 0 that holds total 
    for n in numbers:
        total += n # add number to total 
    return total 
numbers = 1, 5, 5, 7, 10, 1 
summation = compute_sum(*numbers) 
print(summation)


# ••ARGS  VS KWARGS(DICTIONARY ARGUMENTS) 
def myfunction(**family):
    print("Her last name is " + family["lname"]) 
myfunction(fname = "Jesse", lname = "Mensah") 

def display(**kwargs):
    # iterate through the list  
    for keyword, value in kwargs.items():
        print(keyword + ": " + value) 
display(fname = "Jesse", lname = "Mensah")
