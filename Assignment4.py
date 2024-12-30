"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user's information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name 
        # self.age = input("Enter age: ")
        # self.gender = input("Enter gender: ")
        # self.race = input("Enter race: ")
        # self.ethnicity = input("Enter ethnic group: ")
        # self.education_level = input("Enter education_level: ")
        # self.employment_status = input("Enter emplyment status: ")
        # self.marital_status = input("Enter maarital status: ")
        # self.language_spoken = input("Enter language_spoken: ")
        # self.state_of_origin = input("Enter state of Origin: ")
        # self.religion = input("Enter religion: ")
        # self.occupation = input("Enter occupation: ")
        # self.login_attempts = 0

    def descibe_user(self):
        print(f"Summary of {self.first_name.title()} {self.last_name.title()}'s Demographic Profile:\n")
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.age}-year-old {self.gender.lower()} of {self.race} race "
              f"and {self.ethnicity} ethnicity. They have achieved an education level of {self.education_level} and are currently "
              f"{self.employment_status.lower()}.")
        print(f"They are {self.marital_status.lower()} and speak {self.language_spoken}. They originate from {self.state_of_origin.title()} "
              f"state and follow the {self.religion} religion. Their occupation is {self.occupation.lower()}")
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!\n Can we meet you?")

    """
    Add an attribute called login_attempts to your User
    class from Exercise 9-3 (page 166). Write a method called increment_
    login_attempts() that increments the value of login_attempts by 1. Write
    another method called reset_login_attempts() that resets the value of login_
    attempts to 0.
    Make an instance of the User class and call increment_login_attempts()
    several times. Print the value of login_attempts to make sure it was incremented
    properly, and then call reset_login_attempts(). Print login_attempts again to
    make sure it was reset to 0.
    """
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"You have logged in {self.login_attempts} so far")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Reset complete! No of times logged in is now {self.login_attempts}")

"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator's set of
privileges. Create an instance of Admin, and call your method.
"""        
# class Admin(User):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name) 
#         self.privileges = [
#     "can add post",
#     "can delete post",
#     "can ban user",
#     "can edit post",
#     "can view analytics",
#     "can manage user roles",
#     "can approve comments",
#     "can deactivate accounts",
#     "can manage advertisements",
#     "can send notifications"
# ] 
       
#     def show_privileges(self):
#        print(f"The following are the privileges of Admin {self.first_name}:")
#        for privilege in self.privileges:
#           print(f"- {privilege}") 

"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.          
"""
class Privileges():
     def __init__(self):
         self.privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    "can edit post",
    "can view analytics",
    "can manage user roles",
    "can approve comments",
    "can deactivate accounts",
    "can manage advertisements",
    "can send notifications" ]
         

     def show_privileges(self):
       print(f"The following are the privileges of the Admin: ")
       for privilege in self.privileges:
          print(f"- {privilege}") 

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name) 
        "Making a Privileges instance as an attribute in the Admin class"
        self.admin_privileges = Privileges()           


users_first_name = input("Enter first name: ")    
users_last_name = input("Enter last name: ")  
user1 = User(users_first_name,users_last_name) 
# user1.descibe_user()
# print(f"\n_____Number of log in attempts before account is used_____\n")
# print(user1.login_attempts)
# print(f"\n_____Number of log in attempts after incremental usage use before account is used_____\n")
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(f"\n_____Login attempt after reset_____\n")
# user1.reset_login_attempts()

print(f"\n--------------Admin Privileges:-----------------------\n")
"Creating a new instance of Admin"
admin1 = Admin(users_first_name,users_last_name)

# admin1.descibe_user()
# admin1.show_privileges()

"using the show_privileges method to show its privileges."      
admin1.admin_privileges.show_privileges()






