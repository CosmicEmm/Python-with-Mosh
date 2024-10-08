# (Practice Day-02)
attendance = "Attendance Sheet"
print(attendance.upper())
title = input("Title: ")
name = input("Name: ")
roll_no = input("Roll No: ")
if title.upper() == "MR":
    print("Gender: Male")
elif title.upper() == "MRS" or title == "MISS":
    print("Gender: Female")
mba_student = "MBA" in roll_no
print("Currently Studying MBA: " + str(mba_student))
marks = int(input("Marks Obtained: "))
print("Enter your attendance status from Monday till Wednesday (P for Present & A for Absent)")
monday = input("Monday: ")
tuesday = input("Tuesday: ")
wednesday = input("Wednesday: ")
if monday.upper() == "P" and tuesday.upper() == "P" and wednesday.upper() == "P":
    print("Attendance:" + str(((1+1+1)//3)*100) + "%")
    print("Well done! Your attendance record is perfect. You get +3 bonus marks for punctuality.")
    marks += 3
    print("Updated Marks: " + str(marks))
elif monday.upper() == "A" and tuesday.upper() == "A" and wednesday.upper() == "A":
    print("Attendance: 0%")
    print("You aren't allowed to sit in the upcoming semester and 3 marks will be deducted for your misconduct.")
    marks -= 3
    print("Updated Marks:" + str(marks))
else:
    print("You have got room for improvement. Do better next time.")

#Weight Converter
weight = float(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() =="K":
    converted = weight / 0.45
    print(f"You are {converted} pounds.")
else:
    converted = weight * 0.45
    print(f"You are {converted} kilos")
