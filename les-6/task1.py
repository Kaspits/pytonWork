# from decimal import Decimal
# number = 0.56
# number_d = Decimal('0.56')   #Красивое округление
# print(number*10)
# print(number_d*10)

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в
# первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в
# первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
import random
length_mass_1 = int(input('Input length of the 1st list: '))
random_mass_1 = [random.randint(1, 30) for _ in range(length_mass_1)]
length_mass_2 = int(input('Input length of the 2nd list: '))
random_mass_2 = [random.randint(1, 30) for _ in range(length_mass_2)]
temp_list = []
print(random_mass_1, random_mass_2)
for i in random_mass_1:
    if i not in random_mass_2:
        temp_list.append(i)
print(temp_list)
# or temp_list = [i for i in random_mass_1 if i not in random_mass_2]
# print(temp_list)
