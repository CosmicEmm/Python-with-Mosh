#Function: a container for a few lines of code that perform a specific task
def greetings(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard the Manhattan Project")


print("Start")
#Positional Argument: the order of the arguments matter
greetings("Robert", "Oppenheimer")
#Keyword Argument: the order of the arguments doesn't matter; improves readability of the code
greetings(last_name="Einstein", first_name="Albert")
#when mixing both positional and keyword arguments, always use the positional arguments before the keyword arguments
greetings("Beth", last_name="Harmon")
print("Finish")



