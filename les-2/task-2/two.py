# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
f_one = 0
f_two = 1
f = 0
count = 1
number = int(input('input number: '))

while f < number:
    f = f_one + f_two
    f_one, f_two = f_two, f
    count += 1

print(count if number == f else '-1')
