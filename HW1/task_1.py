# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = int(input('Введите число: '))
suma = 0

while number > 0:
    digit = number % 10  # извлекли последднюю цифру числа, присвоили
    suma += digit  # добавили
    number = number//10  # уменьшили на один

print(suma)

# Я сначала сделала, а потом вспомнила, чвто вроде бы нужно без цикла.
# Вот второе решение, чтобы не били тапками :)

n = int(input('Enter number: '))

c = n % 10
n = n // 10
b = n % 10
a = n // 10

print(a + b + c)

# решение учителя
number = 123
summa = number % 10 + number//10 % 10 + number//100
print(summa)
