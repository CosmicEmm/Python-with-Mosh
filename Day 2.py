course = "Welcome to Devland"
print(course.upper())
print(course.lower())
print(course.find("D"))
print(course.replace("to", "2"))
print("Welcome" in course)
print(10.5 % 5)
print(2 ** 5)
x = 20
x *= 5
print(x)
y = 5 == 4
print(y)
price = 25
print(price < 10 and price < 30)
print(price < 10 or price < 30)
print(not price > 30)
temperature = 4
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("It's a nice day")
elif temperature > 10: # (10, 20]
    print("It's a bit cold")
elif temperature > 5: # (5, 10]
    print("It's very cold")
else:
    print("It's freezing")
# (Method 1)
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    print("Weight in Lbs: " + str(weight * 2.2))
else:
    print("Weight in Kg: " + str(weight / 2.2))
# (Method 2)
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit == "K" or unit == "k":
    print("Weight in Lbs: " + str(weight * 2.2))
elif unit == "L" or unit == "l":
    print("Weight in Kg: " + str(weight / 2.2))



