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
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)

#2-D Lists: a list where each item is another list. Used to model matrices in Python
#3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
#Access individual items in a matrix
print(matrix[0][1])
#Modify individual items in a matrix
matrix[1][2] = 36
print(matrix[1][2])
print(matrix)

#Use Nested Loops to iterate over all the items in a matrix
for row in matrix:
    for item in row:
        print(item)








