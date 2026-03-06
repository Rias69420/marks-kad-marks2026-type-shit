import csv
import statistics

prices = []

with open("preces.csv", newline='') as csvfile:
    preces = csv.reader(csvfile)
    next(preces) 

    for line in preces:
        print(line)
        price = float(line[2]) 
        prices.append(price)

avg = statistics.mean(prices)

print("Average price:", avg)