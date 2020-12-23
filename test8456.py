class InputNumbError(Exception):
    def __init__(self, text):
        self.text = text


class Store:

    def __init__(self, name):
        self.name = name
        self.st_list = {
            "printer": [],
            "scanner": [],
            "xerox":   []}

    def __str__(self):
        str = f"{self.name} список товаров :\n"
        for eup in self.st_list:
            str = str + f"Всего {eup} - {len(self.st_list.get(eup))} шт:\n"
            for i, obj in enumerate(self.st_list.get(eup), 1):
                str = str + f"{i}. {obj}\n"
        return str

    def put_store(self, eup):
        self.st_list[eup.name].append(eup)

    def take_store(self, eup):
        return self.st_list[eup].pop(0)


class Equipment:

    def __init__(self, data):
        self.model = data[0]
        self.price = data[1]

    def work_fun(self, text):
        pass

    def __str__(self):
        return f"{self.name}, модель: {self.model}, цена: {self.price}"

    @classmethod
    def move(cls, store1, store2):
        store2.put_store(store1.take_store(cls.name))


class Printer(Equipment):

    name = "printer"

    def work_fun(self, text):
        print(f"Печатаю - {text}")


class Scanner(Equipment):

    name = "scanner"

    def work_fun(self, text):
        print(f"Сканирую - {text}")


class Xerox(Equipment):
    name = "xerox"

    def work_fun(self, text):
        print(f"Копирую -  {text}")


def check_numb_input(str):
    qty = input(f"Введите {str} ")
    while True:
        try:
            if qty.isdigit():
                return qty
            else:
                raise InputNumbError("Ошибка!!! Введите число!")
        except InputNumbError as err:
            print(err)
            qty = input(f"Введите {str} ")


def inp_mod_price():
    model = input("Введите модель ")
    price = check_numb_input("цену")
    return model, float(price)


def create_obj(eup):
    if eup == "printer":
        eup = Printer(inp_mod_price())
        return eup
    if eup == "scanner":
        eup = Scanner(inp_mod_price())
        return eup
    if eup == "xerox":
        eup = Xerox(inp_mod_price())
        return eup


def input_store(name_store):
    print(f"Заполнение {name_store.name}:")
    eup_list = ["printer", "scanner", "xerox"]
    for eup in eup_list:
        qty = check_numb_input(f"количетво {eup}")
        for i in range(int(qty)):
            obj = create_obj(eup)
            name_store.put_store(obj)


store = Store("склад")
input_store(store)
print(store)
chop = Store("магазин")
print(chop)
Printer.move(store, chop)
print(store)
print(chop)
Scanner.move(store, chop)
print(store)
print(chop)
Xerox.move(store, chop)
print(store)
print(chop)
