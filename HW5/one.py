# Задача 26:  Напишите программу, которая на вход
# принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number_a = int(input('Input a: '))
number_b = int(input('Input b: '))


def recursive(number_a, number_b):
    print(number_a ** number_b)


recursive(number_a, number_b)
