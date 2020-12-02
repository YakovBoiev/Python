def divis(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        return "деление на ноль невозможно"
    return c

def div(a, b):
    print("a / b = ", divis(a, b))
    print("b / a = ", divis(b, a))

div(float(input("Введите число а: ")), float(input("Bвведите чило b: ")))
