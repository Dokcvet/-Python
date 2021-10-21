from itertools import count

list = count(x := int(input()))

for _ in range(8):
    print(f"Цифры = {next(list)}")

