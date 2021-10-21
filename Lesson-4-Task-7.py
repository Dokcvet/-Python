def factorial_num(num):
    x = 1
    for i in range(num + 1):
        yield f'{i}! = {x}'
        x *= i + 1


for el in factorial_num(int(input("Введите число: "))):
    print(el)
