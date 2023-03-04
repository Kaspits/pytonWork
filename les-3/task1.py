# import random

# my_list = [random.randint(0, 10) for _ in range(20)]
# print(my_list)
# print(len(set(my_list)))
# или
# new_list = []
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)

# print(new_list)
# print(len(new_list))
# .........................................................

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

# n = int(input('N: '))
# k = int(input('K: '))

# my_list = [i for i in range(n)]

# print(my_list)

# print(my_list[k:] + my_list[: k])

# или
my_list = [i for i in range(10)]
print(my_list)
k = int(input('K: '))
for i in range(k):
    # поп берет элемент и двигаем его на поз. 0
    my_list.insert(0, my_list.pop(-1))

print(my_list)
