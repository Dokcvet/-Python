def my_f(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        my_f_err = s_1 / s_2
    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "Division by zero forbidden!"
    return round(my_f_err, 4)


print(my_f(input("Введите первое число: "), input("Введите второе число: ")))
