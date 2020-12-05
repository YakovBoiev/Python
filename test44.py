def non_recurr(list):
    listnew = [el for el in list if list.count(el) == 1]
    return listnew


list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(non_recurr(list))
