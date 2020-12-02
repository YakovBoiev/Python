def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    return sum(list[1:])

print(my_func(5, 8, 3))
