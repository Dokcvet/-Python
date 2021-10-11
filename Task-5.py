profit = int(input('Введите Вашу прибыль: '))
outlay = int(input('Введите Ваш убыток: '))
staff = int(input('Введите численнность Вашего персонала: '))
if profit - outlay > 0:
    print(f"Ваша фирма работала с прибылью. Рентабельность составила {profit / outlay * 100:02} %."
          f"На каждого из сотрудников пришлось {profit / staff:02}")
elif pro
