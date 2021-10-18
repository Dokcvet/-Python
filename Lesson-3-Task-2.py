def inf(name=input("Введите ваше имя: "), surname=input("Введите вашу фамилию: "),
        birthday=input("Введите дату рождения: "), city=input("Введите свой город: "),
        email=input("Введите адрес электронной почты: "),
        phone=input("Введите номер телефона:")):
    return f"Name - {name}; Surname - {surname}; Birthday - {birthday}; " \
           f"City - {city}; Email - {email}; Phone - {phone}"


print(inf())
