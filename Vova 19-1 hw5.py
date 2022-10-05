d =print('Чтобы завршить программу введие"stopp"')
stran ={
"ru": {'red', 'blue', 'white'},
"kg": {'red', 'yellow'},
"ua": {'blue', 'yellow'},
"tr": {'red', 'white'},
"kz": {'blue', 'yellow'},
"usa": {'red', 'blue','white'},
"kr": {'blue', 'black','red'},
"jp": {'red', 'white'},
"fr": {'blue', 'red','white'},
"pk": {'white', 'green'},
"br": {'blue', 'yellow','green','white'},

}
while True:
    ing = input('Ведите цвет или команду для выхода- ')
    if ing == 'stopp':
        break
    else:
        print('Неправильный ввод,такой страны нет в базе!')
    for k, v in stran.items():
        if ing in v :
            print(k)



