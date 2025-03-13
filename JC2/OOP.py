# Object-oriented programming makes it easier to solve real-world problems (by looking at objects in the real world as objects)
# Class = a collection of all the attributes (called properties), and methods for each object of that class
# Object = an instance of a class, and from 1 class you can create any number of instances
# Abstraction, Inheritance, Polymotphism, Encapsulation (Combining all the data and methods that can be done together, this is also used in data hiding) are used in OOP
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
        self.__DoB = DoB # of type Date (putting a double underscore (__) makes a public attribute private, so it can't be accessed and altered without a getter/setter)
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
    def setGender(self, new_gender):
        self.__gender = new_gender

    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.__DoB}, Gender: {self.__gender}")


person1 = Person("Shuaib", "20/07/1960", "Male")
person2 = Person("John", "01/02/1999", "Male")
person3 = Person("Aliyah", "25/09/2005", "Female")
#To print
print(person1.name, person1.getDoB(), person1.getGender())
#Alternative
print(person1.__dict__)
person1.setDoB("09/08/1998")

# Inheritance: classes can be based off an existing class, which means the child/sub class inherits all the methods and properties from the parent/super class
# Any number of classes can be inherited from a parent class
# The subclass can have its own specific methods and properties that are not shared between them
# (Don't use this: ) Multiple Inheritance = A subclass can have multiple superclasses (complexity, errors and inconsistency problems) (Usually using the constructor from the parent = ParentClass.init())
# Polymorphism = When a subclass redefines/modifies a method inherited from a superclass
# Method overriding = allows you to have multiple methods of the same name but with different numbers/types/orders of arguments (not to be confused with polymorphism)

# Teacher is a subclass of Person, and it inherits all the methods and properties
class Teacher(Person): #Teacher is a Person
    #pass (if you put pass here everything from the parent class will be passed. The constructor being used is the parent's)
    def __init__(self, name, DoB, gender, salary): 
        super().__init__(self, name, DoB, gender) #inherits the constructor from the parent class
        self.salary = salary #salary is a property unique to Teacher
    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.getDoB()}, Gender: {self.getGender()}, Salary: {self.salary}") # Private properties of a parent class cannot be accessed directly when creating a subclass, you need to use a getter

teacher1 = Person("Allan", "15/04/2009", "Male", 2000)
teacher1.printDetails()

class Student(Person):
    def __init__(self, name, DoB, gender, grade): 
        super().__init__(self, name, DoB, gender)
        self.grade = grade
    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.getDoB()}, Gender: {self.getGender()}, Grade: {self.grade}") 

student1 = Student("Valerie", "25/01/2008", "Female", "12")
student1.printDetails()

# Containment/Aggregation and Composition: 
# Class A has Class B (instead of Class A is Class B like in inheritance)

# Composition = life expectancy of one class is dependent of the other class. if the part cannot exist when the whole is destroyed, the relationship between the two classes is composition 
# Containment = life expectancy of one class is not dependent of the other class. if the part can exist when the whole is destroyed, the relationship between the two classes is containment

class Library:
    def __init__(self, name):
        self.__name = name # of type string
        self.books = []

    def getSelf(self):
        return self.__name
    
    def addBook(self, book):
        self.books.append(book)

    def printLibraryBooks(self):
        for book in self.books:
            print(f"  {book.title}\nBy: {book.author}\nPrice: {book.price}")

class Book:
    def __init__(self, title, author, price):
        self.title = title # of type string
        self.author = author # of type string
        self.price = price # of type real

bbs_library = Library("Bina Bangsa School Library")
book1 = Book("Frankenstein", "Mary Shelley", 23.00)
book2 = Book("Learning Kali Linux", "Ric Messier", 49.99)

# bbs_library.addBook(book1)
# bbs_library.printLibraryBooks()

#Method overriding
a = 5
b = 6 
c = 7 
def add(a, b):
    print(a + b)
def add(a, b, c):
    print(a + b + c)

add(a, b)
add(a, b, c)
