class InputNumbError(Exception):
    def __init__(self, text):
        self.text = text
list = []
print("Заполнение списка числами, для остановки введите - stop ")
el = input("Вводите числa: \n")
while el != "stop":
    try:
        if el.isdigit():
            list.append(el)
            el = input()
        else:
            raise InputNumbError("Ошибка!!! Вводите только числа!")
    except InputNumbError as err:
        print(err)
        el = input()

print("Сформированный список")
print(list)

