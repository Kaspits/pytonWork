# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом
# пробелов или символами конца строки. Определите,
# сколько различных слов содержится в этом тексте.

string = '''Пользователь вводит текст(строка).
 Словом считается последовательность непробельных символов
 идущих подряд, слова разделены одним или большим числом'''
list_string = string.lower().split()

print(string)
print(list_string)

catalog = {}

for word in list_string:
    catalog[word] = catalog.get(word, 0) + 1
count = 0
for _ in catalog:
    count += 1
print(count)

key = catalog.keys()
print(len(key))

print(len(set(list_string)))

# or

string2 = input("Enter: ")
set = set(string.split())
print(len(set))
