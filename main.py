# CREATING AN ORDER 

from thirdtest import combo, fufu, order, fishSide, get_meat_order, get_fishside_order, get_fufu_order, get_combo_order, order_once, order_many


# definining constants 
FUFU_PRICE = 6.99 
FUFU_CONDIMENTS = ["Lightsoup", "Okro"] 
MEAT_TYPES = ["chicken", "Beef", "Goat"] 
FISHSIDE_TYPE = ["Snapper", "Tilapia"] 
MEAT_PRICES = [1.00, 2.00, 3.00] 
FISHSIDE_PRICE = 3.00 
COMBO_DISCOUNT = 2.00 


# ADDING A SIDE ORDER 
def get_side_order():
    print("There are available fish sides: ")
    print(FISHSIDE_TYPE) 
    choice = False 
    side_name = None 
    while choice == False: 
        q1 = input("What fish side do you want?")
        if q1.lower() in FISHSIDE_TYPE:
            choice = True 
            side_name = q1.lower() 
        else:
            print("Please enter a valid fish side.")
    s = fishSide(side_name, FISHSIDE_PRICE)
    return s 



# getting the fufu order 
def get_fufu_order():
    b = fufu("Fufu", FUFU_PRICE) 
    q1 = input("Do you want any condiments on your fufu? (y for yes) ")
    if q1.lower() == "y":
        for condiment in FUFU_CONDIMENTS:
            q = input("Do you want " + str(condiment)+"? (y/n): ")
            if q.lower() == "y":
                b.add_condiment(condiment) 
    return b 



# order once funtion 
def order_once():
    possible_options = [1, 2, 3, 4] 
    print("Type 1 for Fufu") 
    print("Type 2 for Meat")
    print("Type 3 for FishSide")
    print("Type 4 for Combo")
    choice = None 
    while choice == None:
        q1 = input("Please enter youe choice")
        if int(q1) in possible_options:
            choice = int(q1) 
    item = None 

    if choice == 1:
        item = get_fufu_order() 
    elif choice == 2:
        item = get_meat_order() 
    elif choice == 3:
        item = get_fishside_order() 
    elif choice == 4:
        item = get_combo_order() 
    return item 

def order_many():
    print('Welcome to Chop Bar Bouttique') 
    q1 = input("May i have your name for your order? ") 
    o = order(q1) 
    print("Lets get your order in!")
    done = True
    while done != True:
        item = order_once() 
        o.add_item(item) 
        q1 = input("Do you need more items? (Enter n to shop) ")
        if q1.lower() == 'n':
            done = True 
    return o 

# GETTING THE COMBO 
def get_combo_order():
    print("Lets get you a combo meal!") 
    print("First, lets order the Fufu for you combo")
    f = get_fufu_order() 
    print("Now, lets order the meat for your combo") 
    m = get_meat_order() 
    print("Now, lets order the fish side for your combo") 
    f = get_fishside_order() 
    c = combo("Combo", f, m, f, COMBO_DISCOUNT) 
    return c 