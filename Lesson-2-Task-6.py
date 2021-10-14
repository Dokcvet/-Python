basis = []
tovar = {"Название": "", "Цена": "", "Количество": "", "Единица измерения": ""}
analis = {"Название": [], "Цена": [], "Количество": [], "Единица измерения":[]}
num = 0
while True:
    if input("Для выхода нажмите Q, для продолжения Enter: ").upper() == "Q":
        break
    num += 1
    f_copy = tovar.copy()
    for f in tovar:
        pro = input(f'Введите свойство "{f}": ')
        f_copy[f] = int(pro) if f == "Цена" or f == "Количество" else pro
        analis[f].append(f_copy[f])
    basis.append((num, f_copy))
    print(f"\n Структура товаров\n {basis}")
    print(f'\n Анализ по товарам: \n {"*" * 30}')
    for key, value in analis.items():
        print(f"{key:>30} {value}")
    print("*" *30)