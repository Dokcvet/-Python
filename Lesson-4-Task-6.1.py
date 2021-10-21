from itertools import count, cycle

list_1 = count(x := int(input()))

for _ in range(8):
    print(f"(Цифры) = ({next(list_1)})")

