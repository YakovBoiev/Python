class Zero_div(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите A: ")
b = input("Введите B: ")

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise Zero_div("Ошибка!!! В = 0, деление на ноль не возможно")
except ValueError:
    print("Ошибка!!! Вы ввели не число.")
except Zero_div as err:
    print(err)
else:
    print("A / B = ", a / b)

