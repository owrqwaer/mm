a = 10
b = 0
qwerty = "Server"
while True:
    try:
        print(qwerty)
        c = a / b
    except NameError:
        print("Такої змінної немає")
        qwerty = 0
        print(f"qwerty = {qwerty}")
    except ZeroDivisionError:
        print("Ділення на 0 заборонено")
        b = 1
        c = a / b