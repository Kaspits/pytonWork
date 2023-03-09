# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и
# -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

number_a = int(input('Input a: '))
number_b = int(input('Input b: '))


def recursive(number_a, number_b):
    if number_a >= 0 and number_b >= 0:
        print(number_a + number_b)


recursive(number_a, number_b)
