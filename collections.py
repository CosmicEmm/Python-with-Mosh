#Tuple: used to store items but unlike a list, it can't be modified. It's immutable.
values = (5,8,7,5,3)
#Tuple Methods
#Count Method
print(values.count(5))
#Index Method
print(values.index(8))
#we can access individual items in a tuple using []
print(values[2])

#Unpacking
#when we create a list or a tuple, we normally assign values to it. This is called packing.
straw_hats = ("Luffy", "Zoro", "Sanji", "Nami", "Robin")
#In Python, we are also allowed to extract the values back into variables. This is called unpacking.
red, green, yellow, orange, purple = straw_hats
print(red)
print(f"{green} has a crush on {purple}.")
