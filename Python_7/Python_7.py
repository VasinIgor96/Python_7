
def dot_product(list1, list2):
    if len(list1) != len(list2):
        return None
    return sum([list1[i] * list2[i] for i in range(len(list1))])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = dot_product(list1, list2)
print("Скалярний добуток:",result)