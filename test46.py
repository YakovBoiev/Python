from itertools import count, cycle

def iter_int(n):
    for el in count(n):
        if el > 10:
            break
        else:
            print(el)

def iter_name(listname):
    i = 0
    for el in cycle(listname):
        if i > 5:
            break
        print(el)
        i += 1


iter_int(6)
iter_name(["Василий", "Петр", "Иван"])
