#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:           #Class

                    #Attributes
    name: None
    color: None
    seating: None
    accessories: None
    model: None
    type: None

                    #Methods
    def drive(self):
        print("I am driving a  " + self.name + " car which is of " + self.color + "  color")

    def park(self):
        print("I have parked my car which has " + str(self.seating) + " seating" + " and has model as " + self.model)

    

car1_obj = Car()
car1_obj.name = "Waganor"
car1_obj.color = "White"
car1_obj.model = "VXI"
car1_obj.seating = 5

print(car1_obj)
car1_obj.drive()
car1_obj.park()

print("---------------------------------------------")

car2_obj = Car()
car2_obj.name = "Audi"
car2_obj.model = "Q8"
car2_obj.color = "Black"
car2_obj.seating = 4

print(car2_obj)
car2_obj.drive()
car2_obj.park()