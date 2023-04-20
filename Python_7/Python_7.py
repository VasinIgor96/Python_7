def find_most_common_number(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    most_common_num = lst[0]
    for num in lst:
        if freq[num] > freq[most_common_num]:
            most_common_num = num
        elif freq[num] == freq[most_common_num]:
            most_common_num = min(num, most_common_num)

    return most_common_num

lst_str = input("Введіть список чисел через пробіл: ")
lst = [int(num) for num in lst_str.split()] 
most_common = find_most_common_number(lst)
print(f"Найчастіше число у списку: {most_common}")
