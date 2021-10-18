def my_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Введите как договорено!))"
    return res


print(f"{round(my_fun(1.5, -2.5), 4)}")
