import random

class Cell:

    def __init__(self, quantity=1):
        self.quantity = int(quantity)

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity != other.quantity:
            return Cell(abs(self.quantity - other.quantity))
        else:
            print("Клетки равны вычитание не возможно")

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(max(self.quantity, other.quantity) / min((self.quantity, other.quantity))))

    def make_order(self, n):
        str = ""
        row = self.quantity // n
        for _ in range(row):
            str = str + "*" * n +"\n"
        str = str + "*" * (self.quantity % n) + "\n"
        return str


a = Cell(random.randint(1, 100))
print(f"Количество ячеек клетки A = {a}")
b = Cell(random.randint(1, 100))
print(f"Количество ячеек клетки B = {b}")
print(f"Количество ячеек клетки A + B =", a + b)
d = a - b
print(f"Количество ячеек клетки A - B = {d}")
e = a * b
print(f"Количество ячеек клетки A * B = {e}")
f = a / b
print(f"Количество ячеек клетки A / B = {f}")
print('Клетка A')
print(a.make_order(30))


