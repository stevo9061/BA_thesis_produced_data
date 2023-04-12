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
print("On Average, the transaction costs are", averageTransactionCosts, "AVAX, and $", 17.67*averageTransactionCosts, "USD")
print("On 08/04/2023 the AVAX price is $ 17.67 USD")
print("The most expensive transaction costs", mostExpensiveTransaction, "AVAX, and $", 17.67*mostExpensiveTransaction, "USD")
print("The least expensive transaction costs", leastExpensiveTransaction, "AVAX, and $", 17.67*leastExpensiveTransaction, "USD")



