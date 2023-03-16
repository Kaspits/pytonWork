# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые два
# элемента, равные друг другу образуют одну пару, которую
# необходимо посчитать.  Вводится список чисел.
# Все числа списка находятся на разных строках.
import random
# length_mass_1 = int(input('Input length of the 1st list: '))
# random_mass_1 = [random.randint(1, 10) for _ in range(length_mass_1)]
# print(random_mass_1)
# count = 0
# for item in random_mass_1:
#     if random_mass_1.count(item) > 1:
#         count += 1
# print(count // 2)
# or
n = int(input("Input number: "))
arr = list(random.randint(0, 10) for _ in range(n))
print(arr)
count = 0
temp = set(arr)
for item in temp:
    count += arr.count(item) // 2
print(count)
