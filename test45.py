from functools import reduce

def even_list100_1000():
       list = [i for i in range(100, 1001) if i % 2 == 0]
       return list

mult = reduce(lambda el, elnext: el * elnext, even_list100_1000())
print(mult)
