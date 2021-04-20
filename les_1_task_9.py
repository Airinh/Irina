# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа a, b, c: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if b < a < c or c < a < b:
    print('среднее число - ', a)
elif a < b < c or c < b < a:
    print('среднее число - ', b)
else:
    print('среднее число - ', c)
