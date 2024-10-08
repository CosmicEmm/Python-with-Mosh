academic_year = 2024
name = input("Enter your Name: ")
roll_no = input("Enter your Roll No: ")
birth_year = int(input("Enter your Birth Year: "))
age = 2024 - birth_year
print("Age: " + str(age))
print("Hello " + name +"! Welcome to the club. Enter your test results for the academic year " + str(academic_year))
english = float(input("English: "))
accounting = float(input("Accounting: "))
artificial_intelligence = float(input("Artificial Intelligence: "))
deep_learning = float(input("Deep Learning: "))
total = english + accounting + artificial_intelligence + deep_learning
print("TOTAL: " + str(total) + "/400")
print("Congratulations on earning the first position in the entire batch.")




