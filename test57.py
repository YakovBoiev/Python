import json

def profit():
    profit = {}
    with open("text57.txt", "r") as infile:
        for line in infile:
            word = line.split()
            profit[word[0]] = float(word[2]) - float(word[3])
    posprofitval = list(filter(lambda x: x > 0, profit.values()))
    averpofit = {"average_profit": sum(posprofitval) / len(posprofitval)}
    print(posprofitval, averpofit)
    listprofit = [profit, averpofit]
    with open("test57.json", "wt", encoding="utf-8") as outfile:
        json.dump(listprofit, outfile)

profit()



