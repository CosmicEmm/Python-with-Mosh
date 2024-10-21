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
#Return Statement
def square(number):
    return number ** 3


result = square(2)
print(result)

def addition(first_number, second_number):
    print(first_number + second_number)


print(addition(6, 4)) #When we don't have a return statement in the function, Python returns None by default.

#Exercise: Reorganize the Emoji Converter code into a function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

