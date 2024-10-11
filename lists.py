names = ["Gon", "Killua", "Kirapika", "Hisoka", "Mereum"]
print(names)
#We can access individual items form the list using the index
print(names[1])
print(names[-1])
#We can print a range of items from the list on the terminal
print(names[2:4])
#Calling items from the list doesn't change the original list. Instead, a new list is returned each time.
print(names)

#Modify items within the list
names[0] = "Gon Freecss"
print(names)

#EXERCISE: Write a program to find the largest number in a list.
numbers = [24, 60, 144, 89, 11, 137]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(max)



