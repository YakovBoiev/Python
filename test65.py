class Stationery:

    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print("-" * 40)


class Pencil(Stationery):

    def draw(self):
        print("=" * 40)


class Handle(Stationery):

    def draw(self):
        print("*" * 40)


stat_0 = Stationery("stat_0")
stat_0.draw()
stat_1 = Pen("stat_1")
stat_1.draw()
stat_2 = Pencil("stat_2")
stat_2.draw()
stat_3 = Handle("stat_3")
stat_3.draw()
