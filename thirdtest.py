
# CHOP BAR APP 
# FEATURES 
#1. ask customer if they want fufu, meat, fish or combo 
#  combo must include fufu, meat and fish. 
# 2. prompt them for details about their selection ie condiments for fufu, what kind and size of meat etc 
# 3. create the item based on their selection 
# 4. add the item to the order 
# 5. repeat these steps until the customer is doesnt want anything else to order 
# 6. display the order details including the price 
# 7. Thank the customer for their business 
# 8. Give the customer the option to pay or cancel the order 


# CLASSES 
# 1. ORDER ITSELF 
# 2. ITEMS (FUFU, MEAT, FISH, COMBO) 

# ALL ITEMS IN FUFU SHOP MENU HAVE TWO PROPERTIES IN COMMON 
# THE NAME OF THE ITEM & THE PRICE OF THE ITEM 
# CREATE A PARENT CLASS THAT REFRENCES THOSE PROPERTIES AND THEN CHILD CLASSES 
# FOR INDIVIDUAL MENU ITEMS AND THEIR SPECIFIC PROPERTIES 

class food_item:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 
    # str method => creates a string representation of an object derived from the food item class 
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
    # returns the price of the food item 
    def get_price(self):
        return self.price 

class fufu(food_item):
    # init method calls the super method to initialise name and price from the parent class 
    # then initialise the condiment list to empty 
    def __init__(self, name, price):
        super(fufu, self).__init__(name, price)
        self.condiments = [] 
    # method condiments to the condiment lists 
    def add_condiment(self, condiment):
        # if condiment is not in the list of condiments 
        if condiment not in self.condiments:
            # then add it 
            self.condiments.append(condiment) 
    def __str__(self):
        s = super(fufu, self).__str__() 
        s = s + "Condiments: " + " , ".join(self.condiments) 
        return s 

# CREATE MEAT CLASS 
class meat(food_item):
    def __init__(self, name, price, size):
        super(meat, self).__init__(name, price)
        self.size = size 
    def __str__(self):
        s = super(meat, self).__str__() 
        s = s + "Size: " + str(self.size) + "oz" 
        return s 

# CREATE A FISH CLASS 
class fishSide(food_item):
    def __init__(self, name, price):
        super(fishSide, self).__init__(name, price) 

# COMBO CLASS 
class combo(food_item):
    def __init__(self, name, f, m, fs, discount):
        self.name = name 
        self.fufu = f 
        self.meat = m 
        self.fishside = fs
        self.discount = discount 
        self.price = self.fufu.get_price() + self.meat.get_price() + self.fishside.get_price() - self.discount 
    def __str__(self):
        s = "" 
        s = s + "Combo: " + self.name + "\n" 
        s = s + str(self.fufu) + "\n" + str(self.meat) + "\n" + str(self.fishside) + "\n" 
        s = s + "Combo Price before discount: $" + str(self.fufu.get_price() + self.meat.get_price() + self.fishside.get_price()) + "\n" 
        s = s + "Discount: $" + str(self.discount) + "\n" 
        s = s + "Combo Price After Discount: $" + str(self.price) + "\n" 
        return s 

# CREATE THE ORDER CLASS 
class order:
    def __init__(self, name):
        self.name = name 
        self.items = [] 
    def add_item(self, item):
        self.items.append(item) 
    def get_price(self):
        price = 0.0 
        for item in self.items:
            price = price + item.get_price() 
        return price 
    def __str__(self):
        s = [str(item) for item in self.items] 
        return "\n".join(s) 
    def display(self):
        print("=====================================") 
        print("Here is a summary of your order:")
        print("Order for " + self.name) 
        print('Here is a list of items in your order')

        for item in self.items:
            print("-------------------------------------") 
            print(str(item)) 
            print("-------------------------------------") 
            print("Total Order Price: $" + str(self.get_price())) 
            print("=====================================")


# NEXT CREATE THE MAIN FILE 
