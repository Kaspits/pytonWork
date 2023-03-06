
# Задача 12: Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# for i in range(x):
#     for j in range(y):
#         if x == i+j and y == i*j:
#             print(f'Загаданные цифры {i},{j}')
# но лучше

summa = int(input('Введите summa: '))
multi = int(input('Введите mult: '))

x = y = 0
a, b, c = -1, summa, -multi


def roots(a, b, c):
    discr = b**2 - 4*a*c
    if discr > 0:
        x1 = (-b - discr**0.5)/2*a
        x2 = (-b + discr**0.5)/2*a
        return int(x1), int(x2)
    elif discr == 0:
        x = -b / 2 * a
        return int(x)
    else:
        return "Петя обманул Катю"
