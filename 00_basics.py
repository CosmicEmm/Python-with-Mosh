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

# While Loop: executes a block of code repeatedly as long as a condition is True
i = 1
while i <= 5:
    print(i)
    i += 1

a = 1
while a <= 10:
    print(a * '*') # multiplying a number by a string repeats the string based on the value of the number
    a += 1

# Data Types in Python
"""
Basic/Primitive Types:
- String
- Number (Integer & Float)
- Boolean

Complex Types: useful in building real applications
- List
- Tuple
- Set
- Dictionary
"""

# List: used to represent a list of objects separated by commas
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)

# Retrieving individual objects from the list
print(names[0])   # [index of the object we want to retrieve]
# Retrieving a range of values from the list
print(names[0 : 3]) # [starting index : ending index should be +1 to the object we want to retrieve]

# In Python we can also use negative indexes, a feature not seen in other programming languages
print(names[-1]) # -1 represents the last object in the list

# Changing an object in the list at a particular index for e.g. change the spelling of "John" to "Jon"
names[0] = "Jon"
print(names)

# List Methods: Objects in programming are similar to real-life objects — they have specific capabilities. In Python, lists come with built-in methods as well.
numbers = [1, 2, 3, 4, 5]
# Append Method: adds a new object at the end of the list
numbers.append(6)
# Insert Method: inserts an object somewhere in the middle or at the beginning
numbers.insert(0, -2)  # insert(index of insert positon, object)
print(numbers)
# Remove Method: removes an object from the list
numbers.remove(3)
print(numbers)
# Clear Method: clears all values in the list
numbers.clear()
print(numbers)

# in Operator: checks whether certain objects occur within a list and returns a boolean
digits = [1, 2, 3, 4, 5]
print(1 in digits) # returns True
print(7 in digits) # returns False

# In-built len function: returns the number of items in a list
print(len(digits))

# For Loop: used to iterate over an iterable (like a list, tuple, or string), accessing each item one at a time
# Print each item within a list on a separate line
alphabets = ['a', 'b', 'c', 'd', 'e']

for alphabet in alphabets: # alphabet is the loop variable. In each iteration, it'll hold one value, starting from a, then b and so on.
    print(alphabet)

numerals = [1, 2, 3, 4, 5]

for numeral in numerals:
    print(numeral)

# We can achieve the same with a while loop but it's much more complex than the for loop
i = 0

while i < len(numerals): # while i < 5
    print(numerals[i])   # here i is the index of the numeral we want to print. In first iteration, it will be numerals[0], then numerals[1] and so on.
    i = i + 1

# In-built range function: returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
values = range(5) # will return a range object
print(values)     # Terminal: range(0, 5)

# range(0, 5) is the default representation of a range object and represents numbers 0 till 4.
# In order to see the actual numbers, we need to iterate over this range object using a for loop just like we iterate over a list.
for value in values:
    print(values)

# We can also define the starting point ourselves instead of the default value of 0.
numbers = range(5, 10) # where: 5 is the starting number and 10 is the ending number which is to be excluded

for number in numbers:
    print(number) # prints numbers from 5 till 9

# We can also define the incremental value ourselves instead of the default value of 1.
numbers = range(5, 10, 2) # where: 5 is the starting number, 10 is the ending number which is to be excluded, and 2 is the incremental value
for number in numbers:
    print(number) # prints 5, 7, 9

# You don't need to store the range function in a separate variable. You can use it directly as part of a for loop.
for number in range(5):
    print(number)

# Tuple: similar to a list, it is used to store a sequence of objects. Defined by () and immutable i.e. cannot be changed after creation
numbers = (1, 2, 3)
numbers[1] = 4  # TypeError: 'tuple' object does not support item assignment

# Tuple Methods:
# Count Method: returns the number of occurences of an element within a tuple
numbers = (1, 2, 3, 3)
numbers.count(3)  # Terminal: 2
# Index Method: returns the index of the first occurence of a given element
winners = ("Harry", "Ron", "Hermoine", "Luna", "Harry")
print(winners.index("Luna"))  # Terminal: 3
print(winners.index("Harry")) # Terminal: 0

# Magic Methods: they start with an underscore