x = -3.67587
#Round Function
print(round(x,3))
#Absolute Function - returns the positive representation of a value
print(abs(x))

#Import the Math module for writing programs that involve complex mathematical calculations
import math
#The Math module has functions that can be accessed using the dot operator
value = 3.52
#Ceiling Function
print(math.ceil(value))
#Floor Function
print(math.floor(value))
#Fabs Function: returns the absolute value of x (alternative to the inbuilt abs function in Python)
print(math.fabs(-2.5))
#Exp2 Function: returns 2 raised to the power x
print(math.exp2(5))
#Power Function: returns x raised to the power y
print(math.pow(3,3))
#Square Root Function: returns the square root of x
print(math.sqrt(100))

#EXERCISE: Print Prime Numbers in a given interval
#Prime Number: A number that can only be divided by itself and 1 without remainders.
l = int(input("Beginning of the interval: "))
u = int(input("End of the interval: "))
#For Loop is used to iterate on every number in the interval and check if it's a prime number or not
for possible_prime in range(l, u+1): #Since the range function excludes the last value by default, we add 1 to \
    #include the entire interval the user has specified
    if possible_prime > 1: #All prime numbers are > 1. The IF statement will narrow down the for loop execution.
        for num in range(2, possible_prime): #This nested for loop will take each individual value from the first\
            #loop and check if it's divisible by any number except 1 and itself without a remainder.
            if possible_prime % num == 0: #Modulus Operator(%) returns the remainder of a division.
                break #If the condition holds true, then it's not a prime number and the loop will break. Then we\
                #repeat the whole process from the top for the next value in the given interval.
        else: #If the loop doesn't break, then the for else statement will be executed indicating the value to be prime.
            print(possible_prime)










