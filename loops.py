#While Loop: as long as the condition is true, the indented block of code will be executed repeatedly
number = 1
while number <= 5:
    print("*" * number)
    number += 1

#GUESSING GAME
#Program a game where a user can only make three guesses to get the right number. If they guess right, "You won!" will\
# appear on the terminal otherwise in case of failing all three attempts, "Sorry, you failed!" will be displayed.

secret_number = 7
guess_count = 0
guess_limit= 3
while guess_count < 3:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

#CAR GAME
started = False
while True:
    command = input(">").lower() #instead of calling the string method (lower) again and again to reference the\
    # variable, convert the input directly into lower caps by following it by .lower()
    if command == "help":
        print('''
start - to start the car 
stop - to stop the car
quit - to exit
        ''')
    elif command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car Stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")

