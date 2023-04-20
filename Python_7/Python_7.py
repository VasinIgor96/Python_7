
def unique_elements_in_order(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
lst = [1, 2, 4, 3, 3, 3, 4, 4, 5, 6, 9, ]
unique_lst = unique_elements_in_order(lst)
print(unique_lst)
