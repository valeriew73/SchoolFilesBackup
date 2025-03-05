# Object-oriented programming makes it easier to solve real-world problems (by looking at objects in the real world as objects)
# Class = a collection of all the attributes (called properties), and methods for each object of that class
# Object = an instance of a class, and from 1 class you can create any number of instances
# Abstraction, Encapsulation (Combining all the data and methods that can be done together, this is also used in data hiding) are used in OOP
# OOP uses data hiding so that private data cannot be accessed
# Convention standard for defining a class = make the first letter
# You can put all the classes in one file separate from the main program and use it as a library
# Class diagrams are drawn when creating classes (check notes)
# Two types of variables: Class variables and instance variable


class Car: #Car is a class, which can later be used in declaring an object
    car_count = 0 #class variable = not part of the constructor, which means that it belongs to every object so when it is updated, it gets updated for every object
    def __init__(self, make, model, colour): #Constructor (python calls it initialiser) = A special method inside the class used to construct the object to create personalised objects which can be changed while methods are running
        self.make = make # instance variable (because they are different for each object and belongs to each object)
        self.model = model # all the attributes are public (means you can access them without verifying you are allowed access/change the data)
        self.colour = colour
        Car.car_count += 1 #accessing the class variable for each instance created
    def start(self): #You can create methods for classes, unlike records
        print("The car has started.")
    def stop(self): #self (the object itself) has to be passed into all the methods in python or else this error occurs: TypeError: car.stop() takes 0 positional arguments but 1 was given
        print("The car has stopped.")

# Below is if you don't create a constructor
# python already makes a special constructor by default if you don't use init, thats why you need to use brackets in instantiation
# car1 = Car() #car1 is an object of class car, this is instantiation (to create an instance of something)/constructing an object
# car1.make = "Toyota"
# car1.model = "2001"
# car1.colour = "Red"

car1 = Car("Toyota", 2001, "Red")
car2 = Car("Honda", 2021, "Black")

#Equivalent in pseudocode (doesn't support classes)
#TYPE car
#   DECLARE make : STRING
#   DECLARE model : STRING
#   DECLARE colour : STRING
#ENDTYPE

#DECLARE car1: car
#car1.make <- "Toyota"
#car1.model <- "2001" 
#car1.colour <- "Red"

# Always comment data type in class diagram question
class Person:
    person_count = 0 #class variable
    def __init__(self, name, DoB, gender):
        self.name = name # of type string, this is an instance variable
        self.__DoB = DoB # of type Date (putting a double underscore (__) makes a public attribute private, so it can't be accessed and altered)
        self.__gender = gender # of type string
        Person.person_count += 1 #this is accessing the class variable everytime an instance is made
    
    def walk(self):
        print("Person is walking. ")
    
    def run(self):
        print("Person is running.")

    #Getters/accessers and setters/mutators (used to access and alter private attributes):
    def getDoB(self):
        # Now instead of just being able to access the DoB, you can put an authenticator here
        return self.__DoB
    def getGender(self):
        return self.__gender
    
    def setDoB(self, new_DoB):
        self.__DoB = new_DoB

person1 = Person("Shuaib", "20/07/1960", "Male")
person2 = Person("John", "01/02/1999", "Male")
person3 = Person("Aliyah", "25/09/2005", "Female")
#To print
print(person1.name, person1.getDoB(), person1.getGender())
#Alternative
print(person1.__dict__)
person1.setDoB("09/08/1998")


