# In-built print Function
print("Hello World")

# Variable: used to temporarily store data in a computer's memory
age = 20
age = 30
print(age) # Python code gets executed from top to bottom

first_name = 'Mosh'
is_online = False   # Boolean: can be either True or False

# ---------- EXERCISE --------------------------------------
patient_name = 'John Smith'
age = 20
status = 'new'
print(patient_name, age, status)
# ----------------------------------------------------------

# In-built input Function: returns the user's input as a string and stores it in a variable
name = input('What is your name? ')
print('Hello ' + name)  # String Concatenation: combines one string with another string


# Type Casting: converts the value of a variable from one type to another
birth_year = input('Enter your birth year: ')
age = 2025 - int(birth_year)  # int function converts the value to an integer
print(age)

# float function: converts the value to a floating point number (with decimal point)
# bool function: converts the value to a bool
# str function: converts the value to a string

# ---------- EXERCISE ---------------------------------------
first = input('First: ')
second = input('Second: ')
sum = float(first) + int(second)
print('SUM: ' + str(sum))

# Alternative:
first = float(input('First: '))
second = int(input('Second: '))
sum = first + second
print('SUM: ' + str(sum))
# ------------------------------------------------------------

# String Methods (When a function is part of an object, it's called a method)
course = 'Python for Beginners' # A string object has various methods. Methods don't modify the original string but return a new one.
print(course.upper()) # make the string uppercase
print(course.lower()) # make the string lowercase
print(course.find('o')) # return the index of the first occurrence of 'o'. In Python, the index of the first character of a string is 0.
print(course.replace('Beginners', 'Absolute Beginners')) # replace a substring with another substring


# in Operator: checks whether certain character(s) occur within a string and returns a boolean
print('Python' in course) # returns True
print('Java' in course) # returns False

# Arithmetic Operators
print(10 + 3)   # sum
print(10 - 3)   # subtraction
print(10 * 3)   # multiplication
print(10 / 3)   # division (single slash): returns a floating point number
print(10 // 3)  # division (double slash): returns an interger
print(10 % 3)   # modulus: returns the remainder after dividing 10 by 3
print(10 ** 3)  # exponent: computes 10 raised to the power 3

# Augmented Assignment Operator
x = 10     # Case: Increment the value of x by 3

x = x + 3  # Method 1: adds 3 to x and assigns the result back to x
x += 3     # Method 2: the assignment operator (=) gets augmented with the addition operator (+)

x -= 3
x *= 3

# Operator Precedence: the order in which arithmetic operators are applied. Follows DMAS but can be changed via parentheses.
y = 10 + 3 * 2
print(y) # prints 16

z = (10 + 3) * 2
print(z) # prints 26

# Comparison Operators: used to compare values
x = 3 > 2   # a boolean expression produces a boolean value (True/False)
print(x)

x = 3 >= 2  # greater than or equal to
x = 3 < 2   # lesser than
x = 3 <= 2  # lesser than or equal to
x = 3 == 2  # equality operator; not to be confused with assignment operator (=)
x = 3 != 2  # not equality operator

# Logical Operators: used to build complex rules and conditions
# and Operator: when both boolean expressions are True, the overall result will be True
price = 25
print(price > 10 and price < 30) # True
print(10 < price < 30)  # alternate simplified version

# or operator: atleast one of the boolean expressions must be True for the overall result to be True
price = 5
print(price > 10 or price < 30) # True because 5 < 30

# not operator: inverses any values you give it
price = 5
print(not price > 10) # True because the not operator inverses the False from price > 10

# If Statements: used to make decisions in our programs
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")

# Adding more conditions
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:  # this will be executed if none of the above condition are True
    print("It's cold")

# ---------- EXERCISE ---------------------------------------------
weight = float(input('Weight: '))
unit = input('(K)g or (L)bs: ')

if unit.upper() == 'K':
    print('Weight in (L)bs: ' + str(weight * 2.2))
elif unit.upper() == 'L':
    print('Weight in (K)g: ' + str(weight / 2.2))
else:
    print('Wrong unit of measure. Try again!')
# -----------------------------------------------------------------
