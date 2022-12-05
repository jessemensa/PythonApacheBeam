# Tools => Visual studio code 
# Requirements => a client wants a simple income tax calculator that will calculate the tax obligation 
# for an individual, single filer, based only on income from wages and tips, 

# User Interface 
# 1. Accept the following inputs from the user => Gross income, number of dependents 

# design the program => pseudocode 
# userinput = gross income 
# userinput = number of dependents 
# taxable income = gross income - 12,200 - (2000 * number of dependents) 
# tax due = amount calculated from tax table
# print tax due 


# PROGRAM 

# PART 1 
# define user input 
grossIncome = input("Enter your gross income: ")  
numberOfDependents = input("Enter the number of dependents: ") 

# convert user input which is strings to numbers 
grossIncomefloat = float(grossIncome) 
numberofDependentsInt = int(numberOfDependents) 

# calculate tax die 
tax_income = grossIncomefloat - 12200 - (2000 * numberofDependentsInt) 
print(tax_income) 

# calculate the tax due 
tax_due = tax_income * 0.1 

# print the result 
print("Your tax due is: ", tax_due) 



# PROMPTING FOR AN ADDRESS 

# PART 1 => PROMPT FOR USER INPUT 
user_address = input("Enter your postcode: ")
if user_address.strip(): # check that address is not empty after removing leading and trailing spaces 
    print(user_address) 
    print("Your address is: "+ user_address) 