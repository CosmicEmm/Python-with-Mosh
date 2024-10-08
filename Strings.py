game = 'Mortal Combat has a "sick" Engine'
print(game)
# Use triple quotes to define strings that consist of multiple lines
email = '''
Hi Muhammad,
Hope you're doing well. I just wanted to inform you that you are promoted to the position of \
CEO. Congratulations and good luck!

Best Regards,
Microsoft Support Team
'''
print(email)
# Call characters from a string using their index
print(game[2])
print(game[-2])
print(game[1:8])
print(game[2:])
print(game[:5])
# not providing both the starting and ending index will clone a string
xbox = game[:]
print(xbox)

first = "Andrew"
last = "Ng"
# print 'Andrew [Ng] is an AI scientist' on the terminal
# Method 1 (String Concatenation)
message = first + " [" + last + "] is an AI scientist"
print(message)
#Method 2 (Formatted String) - Recommended
msg = f"{first} [{last}] is an AI scientist"
print(msg)

color = "brown"
verb = "jumps"
adjective = "lazy"
sentence = f"A quick {color} fox {verb} over the {adjective} dog."
print(sentence)
# len function is used to count the no. of characters
name = input("Enter your name: ")
if len(name) <= 10:
    print("Welcome to the underworld")
else:
    print("Error")
# String Methods are functions specific to string objects.
# String Methods don't modify the original string because strings are immutable.
print(game.upper())
print(game)
print(game.lower())
print(game.find("has"))
print(game.replace("sick", "swell"))
print(game)
print("Mortal" in game)
print(game.title())


