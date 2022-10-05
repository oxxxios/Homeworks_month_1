
day = int(input('введите день рождения- '))
mon = int(input('введите месяц рждения- '))
if (day >= 21 and day <= 31 and mon == 3) or (mon == 4 and day >= 1 and day <= 19):
    print('Знак зодиака: Овен')
elif day >= 20 and day <= 30 and mon == 4 or (mon == 5 and day >= 1 and day <= 20):
    print('Знак зодиака: Телец')
elif day >= 21 and day <= 31 and mon == 5 or (mon == 6 and day >= 1 and day <= 20):
    print('Знак зодиака: Близнецы')
elif day >= 21 and day <= 30 and mon == 6 or (mon == 7 and day >= 1 and day <= 22):
    print('Знак зодиака: Рак ')
elif day >= 23 and day <= 31 and mon == 7 or (mon == 8 and day >= 1 and day <= 22):
    print('Знак зодиака: Лев')
elif day >= 23 and day <= 30 and mon == 8 or (mon == 9 and day >= 1 and day <= 22):
    print('Знак зодиака: Дева ')
elif day >= 23 and day <= 31 and mon == 9 or (mon == 10 and day >= 1 and day <= 22):
    print('Знак зодиака: Весы')
elif day >= 23 and day <= 30 and mon == 10 or (mon == 11 and day >= 1 and day <= 21):
    print('Знак зодиака: Скорпион ')
elif day >= 22 and day <= 31 and mon == 11 or (mon == 12 and day >= 1 and day <= 21):
    print('Знак зодиака: Стрелец')
elif day >= 22 and day <= 30 and mon == 12 or (mon == 1 and day >= 1 and day <= 19):
    print('Знак зодиака: Козерог ')
elif day >= 20 and day <= 31 and mon == 1 or (mon == 2 and day >= 1 and day <= 18):
    print('Знак зодиака: Водолей')
elif day >= 19 and day <= 30 and mon == 2 or (mon == 3 and day >= 1 and day <= 20):
    print('Знак зодиака: Рыбы ')
else:
    print('некорректная дата!Убедитесь в правильности написания даты. ')









