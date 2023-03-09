# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет
# оценки Василия, но наоборот: все максимальные – на
# минимальные.
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 5))
print(numbers)

max_count = max(numbers)
min_count = min(numbers)
print(max_count)
print(min_count)
for i in range(len(numbers)):
    if numbers[i] == max_count:
        numbers[i] == min_count
print(numbers)
