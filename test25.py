rating = [8, 7, 6, 6, 5, 5, 1]
print("Рейтинг")
print(rating)
new_el = int(input("Ведите новый элемент рейтинга "))
if new_el <= rating[-1]:
    rating.append(new_el)
else:
    for i in range(len(rating)):
        if new_el > rating[i]:
            rating.insert(i, new_el)
            break
print("Новый рейтинг ")
print(rating)
