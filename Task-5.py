profit = float(input('Введите Вашу прибыль: '))
outlay = float(input('Введите Ваш убыток: '))
staff = int(input('Введите численнность Вашего персонала: '))
result = profit - outlay
if result > 0:
    print(f"Ваша фирма работала с прибылью. Рентабельность составила {100 * profit / outlay:.1f} %."
          f" На каждого из сотрудников пришлось {profit / staff:.2f}")
elif result < 0:
    print('Ваша фирма работала с убылью.')
else:
    print('Ваша фирма работала без прибыли, но и без убытка')
