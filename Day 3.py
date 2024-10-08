print("Hello " * 5)
second = 10
while second >= 0:
    print("Seconds Remaining: " + str(second))
    second = second - 1
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1
gryffindor = ["Harry", "Hermione", "Ron"]
print(gryffindor)
print(gryffindor[1])
print(gryffindor[-1])
gryffindor[2] = "Neville"
print(gryffindor)
gryffindor[0] = "Lavender"
print(gryffindor)
print(gryffindor[0:2])

data = ["Apple", 1, "Banana", 2, "Orange", 3]
data.append(6)
print(data)
data.insert(3,3>2)
print(data)
data.remove("Orange")
print(data)
data.append("Ambivert")
print(data)
print("Orange" in data)
print(len(data))

marks = [10,20,30,40,50]
for subject in marks:
    print(subject * "@ ")

# (2nd Method) Applying While loop to a list
i = 0
while i < len(marks):
    print(marks[i] * "s ")
    i = i + 1

subject = 10
while subject <= 50:
    print(subject * "@ ")
    subject = subject + 10

assists = range(3, 16, 2)
for number in assists:
    print(number)

for value in range(5,21,5):
    print(value * ":) ")

numbers = (1,2,3,4,5,7,4)
print(numbers.index(7))
