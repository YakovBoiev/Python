class Worker:

    def __init__(self, name=None, surname=None, position=None, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum(self._income.values())

empl_1 = Position(surname="Иванов", name="Иван", position="программист", wage=100000, bonus=50000)
print(empl_1.surname)
print(empl_1.name)
print(empl_1.position)
print(empl_1._income)
print(empl_1.get_full_name())
print(empl_1.get_total_income())
