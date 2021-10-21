from functools import reduce

print([el for el in range(100, 1001, 2)])

print(reduce(lambda a, b: a * b, [el for el in range(100, 1001, 2)]))

