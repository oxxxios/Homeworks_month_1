from datetime import datetime
print('Ты загадываешь от 1 до 100\nА я попытаюсь найти!')
print("Если цифра больше чем ты загадал пиши '<' \nЕсли цифра меньше чем ты загадал пиши '>'")
low = 0
big = 100
sred = (big + low) // 2
c = 0
namber = int(input("Введите число которое вы загадали!: "))
with open('results.txt', 'a', encoding="utf-8") as a:
    start = datetime.now()
    while True:
        c += 1
        if sred == namber:
            print(f'Ты выигрываешь за {c} попытки!')
            finish = datetime.now() - start
            a.write(f'Ты начал в: {start.strftime("%X")} \n')
            a.write(f'Ты закончил в: {datetime.now().strftime("%X")} \n')
            a.write(f'Ты выигываешь с {c}-попытки\nТы угадал за-{finish.seconds} секунд\n')
            break
        print(f"Вы это загадали {str(sred)}?")
        check_ans = input()
        if check_ans == '<':
            big = sred
            sred = (big + low) // 2
        elif check_ans == '>':
            low = sred
            sred = (big + low) // 2
        else:
            print("Ты что-то не правильно делаешь!\n")