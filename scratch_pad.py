data = [1, 2, 3]

def append_element(some_list, element):
    some_list.append(element)
    data = [5, 6, 7] # won't overwrite the variable 'data' outside the function
    print(data)


append_element(data, 4)
print(data)