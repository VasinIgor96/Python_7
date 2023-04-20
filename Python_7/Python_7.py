
def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

# Перевірка
num = int(input("Введіть ціле число: "))
print("Дільники числа", num, ":", find_divisors(num))