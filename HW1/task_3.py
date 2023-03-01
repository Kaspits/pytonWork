# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket = int(input('введите номер билета: '))
firstTemp = ticket // 1000
print(firstTemp)
c1 = firstTemp % 10
firstTemp = firstTemp // 10
b1 = firstTemp % 10
a1 = firstTemp // 10
secondTemp = ticket % 1000
print(secondTemp)
c2 = secondTemp % 10
secondTemp = secondTemp // 10
b2 = secondTemp % 10
a2 = secondTemp // 10

firstHalf = a1+b1+c1
secondHalf = a2+b2+c2

if firstHalf == secondHalf and ticket < 1000000:
    print('Yes')
else:
    print('No')
