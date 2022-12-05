# PROCESSING TEXT FILES, CSV FILES, JSON FILES 

# COMMON FUNCTIONS FOR INPUT AND OUTPUT 
# OPEN READ AND DISPLAY TEXT BASED FILES 

# PATH => USED TO IDENTIFY THE LOCATION OF A FILE AND USE IT IN A PROGRAM 
# PATH => A path identifies the location of the file to be utilized.
# ABSOLUTE PATH => A path that includes all information required to find the file, regard- less of where the script is stored.
# EXAMPLE => /Users/username/Desktop/Python/Chapter4/Chapter4.py 
# RELATIVE PATH => A path that starts from the directory where the Python script is stored and includes instructions 
# on how to get to the file using that directory as a starting point.
# data/ testfile.txt.

# BASIC PYTHON FUNCTIONS 
# INPUT(), OPEN(), READ(), WRITE(), CLOSE(), STRIP(), SPLIT(), JOIN(), APPEND(), REMOVE(), REPLACE(), FIND(), 
# LOWER(), UPPER(), STR(), INT(), FLOAT(), LEN(), PRINT(), TYPE(), DIR(), HELP(), ETC.

# SIMPLE FILE INPUT AND OUTPUT SCRIPT 
f = open("myfile.txt", "r") # open the file for reading 
print(f.readline()) # read the first line 
f.close() # close the file 

# another one 
f = open("data/flatland.txt", mode="r") 
print(f.read()) 
f.close() 

# limiting the amount to read 
f = open("data/flatland.txt", mode="r") 
print(f.read(200)) 
f.close() 


# function to read characters from a file 
def head(filepath, num_char):
    f = open(filepath, mode="r") 
    output = f.read(num_char) 
    f.close() 
    return output 
text = head("data/flatland.txt", 200) 
print(text) 

# another function 
def head(filepath, num_lines):
    f = open(filepath, mode="r") 
    lines = "" 
    for x in range(num_lines): 
        lines += f.readline() 
    f.close() 
    return lines 
text = head("data/flatland.txt", 5)
print(text) 


# iterate through a file 
f = open("data/flatland.txt", mode="r") 
for line in f:
    print(line) 
f.close() 


# iterating and checking the start of a line 
def line_starts_with(file_path, fchar):
    f = open(file_path, mode="r")
    output = "" 
    for line in f:
        if fchar == line[0]: 
            output += line 
    return output 
text = line_starts_with("data/flatland.txt", "T") 
print(text) 


# WRITE A LIST TO A FILE 
customers = ["Ax Lodevick", "Frank Prys", "Ania Hearle", "Justus Bodker", 
"Clementius Druce", "Ganny Penwright", "Alick Rens", "Gwen Drewitt", "Jessie Wychard",
"Brina Elliss", "Derril Damiral", "Jade Cutajar", "Brannon Goldsmith", "Valentin Salmons", 
"Tull Rennix", "Quintina Whanstall", "Lev Frunks", "Doris Heskin", "Idalina Moro", "Gillie Ledram"
]

def write_list_2_file(input_list, input_file_path):
    f = open(input_file_path, "a") 
    for name in input_list: 
        name = "\n" + name 
        f.write(name) 
    f.close() 

write_list_2_file(customers, "data/customers.txt")

# Checking for a files existence 
import os 
if os.path.exists("data/customers.txt"): 
    print("The file exists")
else:
    print("The file does not exist")

# checking for an entered files existence 
filename = input("Please enter a file name for checking for: ")
if os.path.exists("data/" + filename): 
    print("The file exists") 
else:
    print("The file does not exist") 

# prompting to remove a file 
file_name = input("Please enter a file name to remove: ")
directory = "data/" 
if os.path.exists(directory + file_name):
    print("The file exists.")
    user_input = input("Would you like to delete this file? [yes/no]: ")
    if user_input.lower() == "yes":
        os.remove(directory + file_name)
        print("The file has been removed.") 
else:
    print("The file does not exist")


# READING A CSV FILE 
import csv 

with open('data/stocks.csv', 'r') as f:
    csv_file = csv.reader(f, delimiter=',') 
    row = f.readline() # read the first line of the csv file 
    print(row) 
    row = f.readline() # read the first line of the csv file 
    print(row) 


# iterating through a csv file 
with open('data/stocks.csv', 'r') as f:
    csv_file = csv.reader(f, delimiter=',') 
    f.readline() 
    # csv_file is an iterable object that we can iterate on using a for loop
    for row in csv_file:
        print(row) 

# iterating through a csv file and printing the individual items column 
with open('data/stocks.csv', 'r') as f: 
    csv_file = csv.reader(f, delimiter=',') 
    for row in csv_file:
        print(row[0], " _ ", row[1])

# calculating the average opening price 
with open('data/stocks_short.csv') as f:
    csv_file = csv.reader(f, delimiter=', ')
    f.readline() 
    sum = 0 
    count = 0 
    for row in csv_file:
        sum += float(row[1]) 
        count += 1 
    print(sum/count) 

# USING THE DICTREADER CLASS 
with open('data/stocks_short.csv') as f:
    csv_file = csv.DictReader(f, delimiter=', ') 
    for row in csv_file:
        print(row) 

with open('data/stocks.csv') as f:
    csv_file = csv.DictReader(f, delimiter=', ') 
    vol = None 
    max_vol = None 

    for row in csv_file:
        vol = int(row["Volume"]) 
        if max_vol == None or max_vol < vol:
            max_vol = vol 
    print(max_vol) 


# Creating list from dataset 
def read_csv(filepath, delimeter=", "):
    import csv 
    dataset = list() 
    with open(filepath) as f:
        csv_file = csv.DictReader(f, delimiter=delimeter) 
        for row in csv_file:
            dataset.append(row) 
    return dataset 

dataset = read_csv("data/stocks.csv") 
print(len(dataset)) 
print("--------") 
print(dataset[0]) # first row in the dataset 


# WRITEROW() => from the writer class to write data to a file row by row 
import csv
row_1 = ["employee_id","first_name","last_name"] # header row 
row_2 = ["EMP2345235636","robert","balti"] # first row
row_3 = ["EMP2498799899","mark","smith"] # second row
row_4 = ["EMP2498989890","mary","caldwell"] # third row
with open('data/employee.csv', 'w') as csv_file: # open file in write mode # use the writer class to create a writer object
# that we will use to write data into the file
     writer = csv.writer(csv_file,delimiter=',')
     writer.writerow(row_1) # writing the header row 
     writer.writerow(row_2) # writing the first row 
     writer.writerow(row_3) # writing the second row 
     writer.writerow(row_4) # writing the third row
f = open('data/employee.csv', 'r') 
print(f.read())
f.close()


# APPEND OR OVERWRITE 
import os, csv 

while True:
    if os.path.exists('data/user_input.csv'):
        user_prompt = input("The file exists what would you like to append? [type quit to exit]: ") 
        if user_prompt.lower() == 'quit':
            break 
        else:
            with open('data/user_input.csv', 'a') as f:
                writer = csv.writer(f, delimiter=',') 
                writer.writerow([user_prompt]) 
    else:
        f = open('data/user_input.csv', 'w') 
        print("The file data/user_input.csv does not exist. It has been created.") 
f = open('data/user_input.csv', 'r') 
print(f.read()) 
f.close() 


# DATA ANALYSIS & EXCEPTION HANDLING 
# LAMBDAS 
# EXCEPTIONS 
# ETLS in PYTHON 

# LAMBDAS 
# ANONYMOUS FUNCTIONS => FUNCTION DEFINED THAT IS NOT BOUND TO AN INDENTIFIER 
# LAMBDA FUNCTION => FUNCTION THAT TAKES IN SEVERAL ARGUMENTS BUT CAN HAVE ONLY ONE EXPRESSION 
# MAP => The map() function returns a map object after applying 
# the given function to each item of a given iterable function.
# REDUCE => The reduce() function is a mathematical technique 
# called to an iterable that reduces it to a single cumulative value.
# lambda arguments: expression 

x = lambda a : a + 10 
print(x(5)) 

# CREATE A LAMBDA FOR POWER 
x = lambda a : a ** 2 
print(x(100)) 

# working with multiple inputs 
x = lambda a, b : a * b 
print(x(5, 6)) 

# order of parameters 
x = lambda a, b : a - b 
print(x(5, 6)) 

y = lambda a, b : a / b 
print(y(5, 6)) 

# items per person 
PerPerson = lambda items, people: items/people 
print(PerPerson(100, 5)) 

# lambda to concatenate strings 
x = lambda a, b, c: a + " " + b + " " + c 
print(x("This", "String", "Is Concatenated."))

# using a lambda inside another function 
def myfunc(n):
    return lambda a : a * n 
doubler = myfunc(2) 
print(doubler(11)) 

def pow_n(n):
    return lambda a: a ** n 
pow_2 = pow_n(2) 
print(pow_2(6)) 

# using the map() function 
# The map() function takes two arguments: a defined function and an iterable 
# object, such as a list, tuple, dictionary, or set.
def to_upper_case(s):
    return str(s).upper() 
names = ['Jesse', 'mike', 'james'] 
print(names) 

names_upper = map(to_upper_case, names) 
print(type(names_upper)) 
names_upper_list = list(names_upper) 
print(names_upper_list) 
print(type(names_upper_list)) 


# USING MAP ON A CSV FILE 
def fromCSV(path, delimiter, quotechar):
    import csv # import csv module 
    data = list() # convert the csv data into a list 
    with open(path, newline='') as csvfile:
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar) 
        # access the content of the file 
        for row in filecontent: # iterate through the rows 
            data.append(row) # save each row as a dictionary 
    return data # item in the data list 

def extract_month(row):
    #input is the entire row of the data 
    # extract the month from the date field 
    # add the month field to the row and return the row 
    value = row['Date'] 
    MM = "" 
    # Split function in python used to divide strings based on some delimiter 
    a = value.split("/") 
    MM = a[0] 
    # implement logic here 
    new_row = row.copy() 
    new_row.update({'Month' : MM})
    return new_row 

data = fromCSV(path='data/stocks.csv', delimeter=', ', quotechar='|') 
print(data[0]) 
data_mapped = map(extract_month, data) 
data_mapped_list = list(data_mapped) 
print(data_mapped_list[0]) 


# COMBINING MAP AND LAMBDA FUNCTIONS 
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8) 
print(list_numbers) 
print(tuple_numbers) 
map_iterator = map(lambda x, y: x + y, list_numbers, tuple_numbers)
map_list = list(map_iterator) 
print(map_list) 

# summing exchange rate and transaction amount 
exchange_rate = [1.25, 2, 1.3, 1.18] 
transaction_amount = (5, 6, 7, 8) 
print(exchange_rate) 
print(transaction_amount) 
map_iterator = map(lambda x, y: x * y, exchange_rate, transaction_amount) 
map_list = list(map_iterator) 
map_list = list(map_iterator) 
print(map_list) 

# filter function takes as input a condition that can be evaluated as true or false 
# and an iterable object ie list or dictionary 
def initial_h(dataset):
    for x in dataset:
        if str.lower(x[0]) == 'i':
            return True 
        else:
            return False 
names = ['Jesse', 'Mike', 'Amoako']
print(names) 

# extract the true results from the initial _h function to a new filter object 
names_filtered = filter(initial_h, names) 
print((names_filtered)) 

# convert the filter object to a list object 
names_filtered_list = list(names_filtered) 
print(type(names_filtered_list)) 
print(names_filtered_list) 

# FILTERING FOR NAMES CONTAINING AN 'E' 
def contains_e(dataset):
    if 'e' in dataset:
        return True 
    else:
        return False 
names = ['Jesse', 'Mike', 'Amoako'] 
print(names) 
names_filtered = filter(contains_e, names) 
print(type(names_filtered)) 
names_filtered_list = list(names_filtered) 
print(type(names_filtered_list)) 
print(names_filtered_list) 


# COMBINING A FILTER AND LAMBDA FUNCTION 
def fromCSV(path, delimiter, quotechar):
    import csv 
    data = list() 
    with open(path, newline='') as csvfile:
        filecontent = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar) 
        for row in filecontent:
            data.append(row) 
    return data 

data = fromCSV(path='data/stocks.csv', delimiter=', ', quotechar='|') 

# filter all elements in data where the open price is lower than close price 
data_filtered = filter(lambda x: x['Open'] < x['Close'], data) 
print(type(data_filtered)) 

data_filtered_list = list(data_filtered) 
for row in data_filtered_list:
    print(row) 

# REDUCE FUNCTION 
# use Python’s reduce() function to calculate a sequential value on a set of individual values.

from functools import reduce 
list_numbers = [2, 4, 6, 8] 
product = reduce(lambda x, y: x * y, list_numbers) 
print(type(product)) 
print(product) 

# using reduce and lambda to calculate a sum 
from functools import reduce 

value_list = [] 

while True:
    user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ") 
    if user_input.lower() == 'quit':
        break 
    else:
        value_list.append(int(user_input)) 
product = reduce(lambda x, y: x + y, value_list) 
print("The total is: " + str(product)) 

# FINDING THE LOWEST VALUE 
from functools import reduce 
value_list = [] 

while True:
    user_input = input("Enter the deposits to add to the series to sum [type quit to exit]: ") 
    if user_input.lower() == 'stop':
        break 
    else:
        value_list.append(int(user_input)) 

if len(value_list) > 0: 
    product = reduce(lambda x, y: x if y > x else y, value_list) 
else:
    product = "Nothing" 
print("The values you entered were: "+ str(value_list))
print("The lowest value is: " + str(product))


# EXCEPTION HANDLING => DESIGNED TO HANDLE NORMAL FLOW OF PROGRAM EXECUTIONS 
# TRY BLOCK IS CODE THAT ALLOWS DEVELOPERS TO TEST A BLOCK OF CODE FOR ERRORS 
# EXCEPT STATEMENTS HANDLE THE ERROR ENCOUNTERED IN CODE 

# handling a zerodivisionerror exception 
a = 1 
b = 0 

try:
    x = a / b 
except ZeroDivisionError as e:
    print("Oops! we cannot divide a number by zero")
    print(format(e)) 

# handling a file not found error 
try: 
    file_object = open("data/bank_transacts.txt", "r")
except FileNotFoundError as e:
    print("Oops! We cannot find the file you are looking for")
    print("The error was: \n" + str(e)) 

# raising an exception 

# adding exception handling to opening a file 
def read_csv(filepath, delimiter=", "):
    import csv 
    dataset = list() 
    try:
        with open(filepath) as f:
            csv_file = csv.DictReader(f, delimiter=delimiter) 
            for row in csv_file:
                dataset.append(row) 
        return dataset 
    except IOError as e:
        print("Unable to access file.") 
a = read_csv("file.txt", "r") 

# finally 
try: 
    f = open("data/text.txt", "r") 
    print(len(f.read())) 
except IOError as e: 
    print("Oops! file not found")
finally: 
    print("Thanks for trying")

