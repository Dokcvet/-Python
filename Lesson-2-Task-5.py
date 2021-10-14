list = [7, 5, 3, 3, 2]
new_element = int(input("Введите натуральное число: "))
i = 0
for n in list:
    if new_element <= n:
        i += 1
    else:
        break
list.insert(i, new_element)
print(list)
