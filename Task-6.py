while True:
    day = 1
    start = float(input("Введите дистанцию, с которой хотите начать: "))
    end = float(input('Введите дистанцию, которую хотите достигнуть: '))
    if start <= 0 or end <= 0:
        print('Недопустимые значения!')
    else:
        while start < end:
            start += start * 0.1
            day += 1
        print(f'Вы получите желаемый результат на {day} день.')
        break
