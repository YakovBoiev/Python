def langer_next_item(list):
    listnew = [list[i] for i in range(1, len(list)) if list[i] > list[i - 1]]
    return listnew


list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print("Исходный список", list, sep="\n")
print("Новый список", langer_next_item(list), sep="\n")
