weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    print("Weight in lbs: " + str(weight / 0.45))
else:
    print("Weight in kg: " + str(weight * 0.45))
