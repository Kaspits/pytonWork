import random
# coins = [random.randint(0, 1) for _ in range(9)]
# print(coins)

# print('Перевернуть единички' if coins.count(1) <
#       coins.count(0) else 'перевернуть нолики')

my_list = [random.randint(1000, 9999) for _ in range(5)]
print(my_list)
my_list_2 = []
my_list_3 = []
num = (input('Input number: '))

for value in my_list:
    el = str(value)
    if num in el:
        el = el.replace(num, '')
    my_list_2.append(el)
print(my_list_2)

for value in my_list_2:
    sum_num = sum([(int(el)) for el in value])
    while sum_num > 9:
        sum_num = sum([(int(el)) for el in str(sum_num)])
    my_list_3.append(sum_num)
print(my_list_3)
print(set(my_list_3))
