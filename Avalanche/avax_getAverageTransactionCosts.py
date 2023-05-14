import json

# Data fetched from https://explorer.bitquery.io/avalanche/gas
with open("C:\\Users\\sbitt\\PycharmProjects\\pythonProject\\Avalanche\\average_transactions.json") as f:
    data = json.load(f)

#print(data)
#print(data["ethereum"]["transactions"])
keyVal = 'date'
averageTransactionCosts = 0
transactionCounter = 0
leastExpensiveTransaction = 1
mostExpensiveTransaction = 0
avalanche_costs_file = open("C:\\Users\\sbitt\PycharmProjects\\pythonProject\\Avalanche\\avalanche_costs.txt", "w")

for keyVal in data['ethereum']['transactions']:
    averageTransactionCosts += keyVal['average']
    transactionCounter += 1
    print("%s" %keyVal)

averageTransactionCosts /= transactionCounter


for iterator in data['ethereum']['transactions']:
    if(leastExpensiveTransaction > iterator['average']):
        leastExpensiveTransaction = iterator['average']

for iterator in data['ethereum']['transactions']:
    if(mostExpensiveTransaction < iterator['average']):
        mostExpensiveTransaction = iterator['average']

print()
print("On Average, the transaction cost is", averageTransactionCosts,  "AVAX, and $", 17.67*averageTransactionCosts, "USD")
avalanche_costs_file.write(f"On Average, the transaction cost is {averageTransactionCosts} AVAX, and $ {17.67*averageTransactionCosts} USD\n")
print("On 08/04/2023 the AVAX price is $ 17.67 USD")
avalanche_costs_file.write(f"On 08/04/2023 the AVAX price is $ 17.67 USD\n")
print("The most expensive transaction has cost", mostExpensiveTransaction, "AVAX, and $", 17.67*mostExpensiveTransaction, "USD")
avalanche_costs_file.write(f"The most expensive transaction has cost {mostExpensiveTransaction} AVAX, and $ {17.67*mostExpensiveTransaction} USD\n")
print("The least expensive transaction has cost", leastExpensiveTransaction, "AVAX, and $", 17.67*leastExpensiveTransaction, "USD")
avalanche_costs_file.write(f"The least expensive transaction has cost {leastExpensiveTransaction} AVAX, and $ {17.67*leastExpensiveTransaction} USD\n")




