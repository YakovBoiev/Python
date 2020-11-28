word = input("Введите строку ").split()
for ind, el in enumerate(word, 1):
    print(ind, el[:10])
