# Object-oriented programming makes it easier to solve real-world problems (by looking at objects in the real world as objects)
# Class = a collection of all the attributes (called properties), and methods for each object of that class
# Object = an instance of a class, and from 1 class you can create any number of instances
# Abstraction, Encapsulation (Combining all the data and methods that can be done together, this is also used in data hiding) are used in OOP
# Convention standard for defining a class = make the first letter


class Car: #Car is a class, which can later be used in declaring an object
    def __init__(self, make, model, colour): #Constructor (python calls it initialiser) = A special method inside the class used to construct the object to create personalised objects which can be changed while methods are running
        self.make = make   
        self.model = model
        self.colour = colour
    def start(self): #You can create methods for classes, unlike records
        print("The car has started.")
    def stop(self): #self (the object itself) has to be passed into all the methods in python or else this error occurs: TypeError: car.stop() takes 0 positional arguments but 1 was given
        print("The car has stopped.")

# Below is if you don't create a constructor
# python already makes a special constructor by default if you don't use init thats why you need to use brackets in instantiation
# car1 = Car() #car1 is an object of class car, this is instantiation (to create an instance of something)/constructing an object
# car1.make = "Toyota"
# car1.model = "2001"
# car1.colour = "Red"

car1 = Car("Toyota", 2001, "Red")
car2 = Car("Honda", 2021, "Black")

#TYPE car
#   DECLARE make : STRING
#   DECLARE model : STRING
#   DECLARE colour : STRING
#ENDTYPE

#DECLARE car1: car
#car1.make <- "Toyota"
#car1.model <- "2001" 
#car1.colour <- "Red"



