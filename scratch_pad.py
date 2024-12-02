numbers = [10, 5, 8, 20, 3, 15]
maximum = numbers[0]
for num in numbers[1:]:
  if num > maximum:
    maximum = num

print(f'Largest Number: {maximum}')
