def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введіть номер елемента послідовності Фібоначчі: "))

result = fibonacci(n)
print(f"n-ий елемент послідовності Фібоначчі: {result}")
