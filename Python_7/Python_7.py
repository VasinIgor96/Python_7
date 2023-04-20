
def capitalize_first_letters(s):
    return ' '.join(word.capitalize() for word in s.split())
s = input("Введіть рядок: ")
capitalized = capitalize_first_letters(s)
print(capitalized)
