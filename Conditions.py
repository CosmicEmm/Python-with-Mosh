price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down Payment: ${down_payment}")
#Line 8 : value will be assigned to down_payment on the basis of the IF statement.

photographs = 2
received_degree = False
if received_degree:
    payment = photographs * 250
else:
    payment = photographs * 500
print(f"Payment: Rs.{payment}")

#Logical Operators (AND, OR & NOT)
was_individually_brilliant = True
won_team_trophies = True
if was_individually_brilliant and not won_team_trophies:
    print("Eligible for Ballond'Or")
else:
    print("Try again next year")

#Comparison Operators
name = input("Enter Your Name: ")
if len(name) < 3:
    print("Name must be at least three characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")
