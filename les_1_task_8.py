#Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите, пожалуйста, год: '))

if year % 4 != 0:
    print('это не високосный год')
elif year % 100 == 0:
    if year % 400 == 0:
        print('это високосный год')
    else:
        print('это не високосный год')
else:
    print('это високосный год')
