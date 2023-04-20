
def sort_tuples_by_age(lst):
    return sorted(lst, key=lambda x: x[1])

people = [('Олександр', 25), ('Олена', 20), ('Іван', 30), ('Вікторія', 15),('Сергій', 10)]
sorted_people = sort_tuples_by_age(people)
print(sorted_people)