"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""
"""
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number
of customers that have been served. 
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
         print(f"The name of this restaurant is {self.name} and they serve {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open now!")

    def set_number_served(self,numbers_served):
        self.number_served = int(numbers_served)    
        print(f"The number of customers served here is {(self.number_served)}")

    def increment_number_served(self,increments):
        self.number_served2 = self.number_served + int(increments)
        if self.number_served2 >= self.number_served:
            print(f"The current number of customers that have been served by {self.name} is {int(self.number_served2)}.")
        else:
            print(f"Its not possible to serve less people from the last time!")   


"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""            

class IceCreamStand(Restaurant):      
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)    
        self.flavors =  ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookies and Cream", "Butter Pecan", "Rocky Road", "Pistachio", "Salted Caramel", "Coffee"]

    def display_flavors(self):
         flavors_list = ", ".join(self.flavors)
 
         print(f"These are the different flavours of icecream {flavors_list} that is currently available in {self.name}")
  
        


# fav_restaurant =restaurant("diba","international")
# print(fav_restaurant.name)
# print(fav_restaurant.cuisine_type)
# print(fav_restaurant.number_served)

# res_name = input("What is the name of the restaurant: ").title()
# cuis_type = input("What type of cuisine do they serve: ").title()
# restaurant1 = Restaurant(res_name,cuis_type)     
# restaurant1.describe_restaurant()
# print(f"_______________Before setting new numbers:______________________\n")
# print(restaurant1.number_served)

# print(f"_______________After setting new numbers without method:___________________________\n")
# restaurant1.number_served = 6
# print(restaurant1.number_served)


# print(f"___________After setting new numbers with method:_________________\n")
# restaurant1.set_number_served(input("Enter number served: "))

# print(f"___________After incrementing numbers with method:_________________\n")
# restaurant1.increment_number_served(input("How many people have been served since the last time?"))

print(f"---------------Instance of the icecreamstand----------------------------------------------\n")

"Creating an instance of class icecreamstand"
icecreamstand1 = IceCreamStand("coldstone creamry","ice creme")

"Calling the display_flavors method to display all the flavours of icecream"
icecreamstand1.display_flavors()

