my_list = [1, 2, 'Привет', (1, 1, 2), 1.1, [1, 1], {"01": 'январь'}, None, {'2', 3}]
for i, item in enumerate(my_list):
    print(f'{i} {item} - {type(item)}')