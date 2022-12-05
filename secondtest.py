# PROMPTING FOR AN ADDRESS 

# PART 1 => PROMPT FOR USER INPUT 
user_address = input("Enter your postcode: ")
if user_address.strip(): # check that address is not empty after removing leading and trailing spaces 
    print(user_address) 
    print("Your address is: "+ user_address) 
    # split the address into pieces 
    split_address = user_address.split() 
    print(split_address) 
    # get out post code 
    print("Your postcode is: " + split_address[3])
    # get out your street address 
    print("Your street address is: " + split_address[0] + " " + split_address[1] + " " + split_address[2])