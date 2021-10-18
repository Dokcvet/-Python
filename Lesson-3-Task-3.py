def my_f(num_1=int(input("Введите первое число: ")), num_2=int(input("Введите второе число: ")),
         num_3=int(input("Введите третье число: "))):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(my_list))
    return sum(my_list)

print(my_f())
