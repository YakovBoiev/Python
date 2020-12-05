def fact(n):
    factor = 1
    for i in range(1, n + 1):
        factor = factor * i
        yield factor

for el in fact(6):
    print(el)
