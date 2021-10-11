n = int(input('Введите число больше 0: '))
max_digit = 0
n_current = n
while n_current > 0:
    digit = n_current % 10
    if digit > max_digit:
        max_digit = digit
        if max_digit == 9:
            break
    n_current = n_current // 10
print(f'Самая большая цифра в числе {n} это {max_digit}.')



