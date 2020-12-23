class Date:

    def __init__(self, dd_mm_yy="0-0-0"):
        self.day, self.month, self.year = Date.take_string(dd_mm_yy)

    @classmethod
    def take_string(cls, dd_mm_yyyy):
        if Date.valid(dd_mm_yyyy):
            return list(map(int, dd_mm_yyyy.split("-")))
        else:
            return None, None, None

    @staticmethod
    def valid(string):
        date = list(map(int, string.split("-")))
        return date[0] <= 31 and date[1] <= 12 and date[2] <= 100000


a = Date("1-12-3000")
print(a.day, a.month, a.year)
for el in (Date.take_string("2-12-8")):
    print(type(el))
print(Date.valid("1-1-1"))
print(Date.valid("1-15-1"))
