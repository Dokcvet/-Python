def int_fun():
    for word in input("Введите слова строчными буквами в английской раскладке: ").split():
        num = 0
        for n in word:
            if 97 <= ord(n) <= 122:
                num += 1
        print(word.title() if num == len(word) else f"{word} - Только маленькие английские!")


int_fun()
