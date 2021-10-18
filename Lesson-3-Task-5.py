def sum():
    n = 0
    while True:
        my_list = input("Введите число, или 'q' для выхода: ").split()
        for num in my_list:
            if num.lower() == 'q':
                return n
            else:
                try:
                    n+= int(num)
                except ValueError:
                    print("Для выхода из программы введите 'q'")
        print(f"Сумма = {n}")


print(sum())
