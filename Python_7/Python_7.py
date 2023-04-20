
def get_first_last_chars(s):
    if len(s) < 6:
        return "Недостатньо символів"
    return s[:3] + s[-3:]

s = input("Введіть рядок: ")

result = get_first_last_chars(s)
print(result)
