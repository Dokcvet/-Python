from sys import argv

script_name, time, rate, bonus = argv


def paypal():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Зарплата - {time * rate + bonus}")
    except ValueError:
        print("Wrong")


paypal()
