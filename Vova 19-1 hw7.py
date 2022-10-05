ten = [x for x in range(1,11)]
evens = list(filter(lambda x: x % 2 == 0, ten))

evens_by_2 = list(map(lambda x: x**2, evens))

print(evens_by_2)

while True:
    def spisok(n = ten):
        print(ten)
        a = input('Введите индекс: ')
        try:
            print(n[int(a)])
        except IndexError:
            print('only index from list ten')
            if a == 'q':
                exit()
    spisok()











