def append_to_list(list, item):
    """Appends an item to the input list (modifies the list in place)."""
    list.append(item)
    return list

def create_new_list(list, item):
    """Returns a new list, leaving the original list unchanged."""
    return list + [item]

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
item = 4
print(append_to_list(list_1, item))
print(create_new_list(list_2, item))
print(list_1)
print(list_2)