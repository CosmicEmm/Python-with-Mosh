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

#List Methods: operations that we can perform on a list
#Append Method: adds an item to the end of the list
num = [5,2,1,7,4,5]
num.append(20)
print(num)
#Insert Method: insert an item anywhere in the list
num.insert(2, "Three")
print(num)
#Remove Method: removes the first occurrence of an item from the list
num.remove(5)
print(num)
#Pop Method: removes the last item in a list
num.pop()
print(num)
#Index Method: checks the existence of an item in a list and returns the index of its first occurrence
print(num.index(7))
#Alternate Method: use in Operator
print(9 in num)
print("Three" in num)
#Clear Method: clears the entire list
num.clear()
print(num)
#Count Method: counts the number of occurrences of an item within a list
marks = [2,4,7,5,7,2,6,3,7]
print(marks.count(7))
#Sort Method: sorts all the items in the list in ascending order
marks.sort()
print(marks)
#Reverse Method: reverses the order of the list
marks.reverse()
print(marks)
#Copy Method: makes a copy of a list. The copy is independent and doesn't get affected by any changes in the original
marks2 = marks.copy()
marks.append("100")
print(f"Original List : {marks}")
print(f"Copy: {marks2}") #doesn't get affected after appending 100 to the original

#EXERCISE: Write a program to remove the duplicates in a list.
#Method 1:
numbers = [2, 2, 4, 6, 2, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Method 2:
numbers = [2, 2, 4, 6, 2, 3, 4, 6, 1]
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print(numbers)





