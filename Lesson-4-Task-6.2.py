from itertools import cycle

list = cycle(x := input())

for _ in range(8):
    print(f"Знаки = {next(list)}")

