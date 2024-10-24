#Exceptions: errors detected during execution are called exceptions.
age = int(input("Age: "))
print(age)

#Terminal Terminology:
#exit code 0: program completed successfully
#exit code 1: program crashed

#ValueError: this error occurs when we try to convert a non-numerical value into an integer
#In Python, we have a construct called try-except to handle errors
try:
    age = int(input("Age: "))
    print(age)
except ValueError: #this block of code will be executed if an error of the type ValueError is detected
    print("Invalid value")

try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(risk)
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError: #we cannot divide a number by 0
    print("Age cannot be zero")

try:
    birth_year = int(input("Birth year: "))
    age = 2024 - birth_year
    print("Age: " + str(age))
except ValueError:
    print("Invalid value")
except TypeError:
    print("Can't concatenate int to str")


