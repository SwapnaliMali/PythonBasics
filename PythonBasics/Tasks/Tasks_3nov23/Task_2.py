# Create a Class Person , Two Objects by taking (name, age, address) Input
# from users and print details in the end.

class Person():
    name = None
    age = None
    address = None

    user_name = input("Enter name of user : \n")
    user_age = input("Enter age of user : \n")
    user_address = input("Enter address of user : \n")

    def Walk(self):
        print(self.name + " is walking and lives in " + self.address)

    def Talk(self):
        print(self.name + " is talking and her age is " + self.age)

    def Eat(self):
        print(self.name + " is eating")

    name = user_name
    age = user_age
    address = user_address


user1_obj = Person()
user1_obj.Walk()
user1_obj.Eat()
user1_obj.Talk()

print(user1_obj)
