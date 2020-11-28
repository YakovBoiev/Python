product = list()
count = 0
while input("Довавить товар? (Введите y  для продолжения) ") == "y":
    count += 1
    proper = dict()
    proper["название"] = input("Введите наименование товара ")
    proper["цена"] = input("Введите цену товара ")
    proper["количество"] = input("Введите количество товара ")
    proper["ед"] = input("Веедите еденицу измерения товара ")
    product.append(tuple((count, proper)))
if product:
    print("Cписок товаров:")
    for elem in product:
        print(elem)
    print("Аналитика товаров:")
    analys = dict()
    list_product_key = product[0][1].keys()
    for key in list_product_key:
        list_val = list()
        for i in range(len(product)):
            list_val.append(product[i][1].get(key))
        analys[key] = list(set(list_val))
    for key, value in analys.items():
        print(f'{key}:{value}')
else:
    print("Список товаров пуст")
