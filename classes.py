class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10,20)
point.x = 15 #we can also change the value of the attribute later
print(point.x)

class Person:
    def __init__(self, name, birth_year, occupation, hobbies): #Constructor Method
        self.name = name
        self.age = 2024 - birth_year
        self.occupation = occupation
        self.hobbies = hobbies

    def talk(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and I work as a {self.occupation}.")


    def add_hobby(self, hobby):
        self.hobbies.append(hobby)


    def reader(self):
        if "Reading" in self.hobbies:
            print(f"{self.name} is an avid reader")
        else:
            print(f"{self.name} needs to read more often.")


emm = Person("Muhammad", 1996, "Finance Manager", ["Reading", "Coding", "Journaling"])
emm.talk()
emm.twitter = "@PhilomathAI" #Attributes can also be set outside the class anywhere in our program
print(emm.twitter)
emm.reader()
emm.add_hobby("Gaming")
print(emm.hobbies)
print("\n")
maria = Person("Maria", 1997, "Graphic Designer", ["Gardening", "Cooking", "Knitting"])
maria.talk()
maria.instagram = "@MariaSharapova"
print(maria.instagram)
maria.reader()
maria.add_hobby("Window-shopping")
print(maria.hobbies)
print(f"{emm.name} and {maria.name} are friends.")

#Inheritance:
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):# the Dog class will inherit all the methods defined in the Mammal class
    def bark(self):
        print(5 * "woof! ")

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()

import wunderkammern
#the module wunderkammern is an object which means we can access its members using the dot operator
wunderkammern.activate()

podcasts = wunderkammern.Podcasts()
podcasts.topics()
podcasts.hosts()

#we can also import specific classes or functions instead of the entire module
from wunderkammern import CommonplaceBook
c_book = CommonplaceBook() #here we don't need to prefix the class name with the module name
c_book.insights()
aot = c_book.anime()
print(aot)

