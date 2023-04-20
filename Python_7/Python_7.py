import re

def count_vowels_consonants(s):
    vowels = ''.join(re.findall(r'[aeiouаеиоуюяіїє]', s, re.IGNORECASE | re.UNICODE))
    consonants = ''.join(re.findall(r'[bcdfghjklmnpqrstvwxyzбвгґджзйклмнпрстфхцчшщ]', s, re.IGNORECASE | re.UNICODE))
    return len(vowels), len(consonants)

s = input("Введіть рядок: ")
vowels, consonants = count_vowels_consonants(s)
print(f"Кількість голосних: {vowels}")
print(f"Кількість приголосних: {consonants}")