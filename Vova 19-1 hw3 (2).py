print('Чтобы остановить программу,напишите-sstopp')
while True:
    r = input('введите слово: ')
    if r =='sstopp':
        break
    count = 0
    L = 'ауоыиэяюёеaeiouАУОЫИЭЯЁЕAEIOU'
    for i in r:
        if i in L:
            count += 1
    count1 = 0
    g = 'бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyzБВГДЖЭЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPRSTVWYZ'
    for i in r:
         if i in g:
            count1 += 1
    print(f"Слово: {r}")
    print(f"количество букв: {len(r)}")
    print(f"гласные буквы: {count}")
    print(f"согласные буквы: {count1}")
    print(f'Гласные: {round(count / len(r) * 100, 2)}%'"/"f'Согласные: {round(count1 / len(r) * 100, 2)}%')




