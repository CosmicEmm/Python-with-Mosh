#importing the entire module: prefix the module name with the name of its package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

#importing a specific function from the module
from ecommerce.shipping import calc_shipping
calc_shipping()

#alterative approach
from ecommerce import shipping
shipping.calc_shipping()

#random is one of Python's in-built modules
import random

#return a random value between 0 and 1
print(random.random())

#return a random value from a particular range
for i in range(3):
    print(random.randint(10,20))

#randomnly return an item from a list
members = ["Luffy", "Zoro", "Sanji", "Nami", "Robin", "Chopper"]
captain = random.choice(members)
print(captain)

#EXERCISE: Write a program to roll a dice. Every time we call the roll method, we get a tuple of two random values.
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll())

