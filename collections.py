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

#Dictionary: used to store information in the form of key-value pairs
customer = {
    "name" : "Mohammad",
    "age" : 27,
    "is_verified" : True
}
#we can access an item in a dictionary using its key.
print(customer["age"])
#to avoid displaying an error on the terminal when we enter the wrong key, we can use the get method.
print(customer.get("height"))
#we can optionally supply a default value for the key that isn't present in the dictionary.
print(customer.get("mood", "happy"))
#we can update the value associated with a key in the dictionary.
customer["name"] = "Muhammad"
print(customer["name"])
#we can add a new key-value pair to the dictionary.
customer["birth_year"] = 1996
print(customer)

#EXERCISE: 
numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
phone = input("Phone: ")
print(numbers[phone[0]] + " " + numbers[phone[1]] + " " + numbers[phone[2]] + " " + numbers[phone[3]])