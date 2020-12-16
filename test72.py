from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def qty_cloth(self):
        pass


class Coat(Clothes):

    @property
    def qty_cloth(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    @property
    def qty_cloth(self):
        return self.size * 2 + 0.3


def list_clothes(clothes):
    list_size = []
    while True:
        quan = input(f'Введите количество {clothes}: ')
        if quan.isdigit():
            break
    for i in range(int(quan)):
        while True:
            size = input(f"Введите размер {clothes} № {i + 1}: ")
            if size.isdigit():
                break
        list_size.append(int(size))
    return list_size


tot_qty_cloth = []
for el in list_clothes("костюмов"):
    exm = Costume(el)
    tot_qty_cloth.append(exm.qty_cloth)
for el in list_clothes("пальто"):
    exm = Coat(el)
    tot_qty_cloth.append(exm.qty_cloth)
print(f'Необходимое количество ткани -  {sum(tot_qty_cloth)}')
