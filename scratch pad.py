text = "    Hello    "
print(text.strip())

n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 1 < n < 6:
    print("Not Weird")
elif n % 2 == 0 and 5 < n < 21:
    print("Weird")
else:
    print("Not Weird")
