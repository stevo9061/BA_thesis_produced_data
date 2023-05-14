import json
from datetime import datetime
import requests


def get_avg_transactions_block():
    url= "https://api.blockchair.com/ethereum/stats"
    response = requests.get(url).text
    response_to_json = json.loads(response)
    transactions_24h = response_to_json['data']['transactions_24h']
    blocks_24h = response_to_json['data']['blocks_24h']

    avg_transactions_block = transactions_24h / blocks_24h
# Fulfill first requirement
    print(f"The average transactions per block are {avg_transactions_block}")
    ethereum_tps_file.write(f"\nThe average transactions per block are {avg_transactions_block}")

    return avg_transactions_block


# Open file stream
# Append new report to the end of the file
ethereum_tps_file = open("C:\\Users\\sbitt\PycharmProjects\\pythonProject\\Ethereum\\ethereum_tps.txt", "a")
current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
ethereum_tps_file.write(f"\nToday's date is {current_time}")

avg_tx_block = get_avg_transactions_block()

# No measurable fluctuation rate of the block time anymore
# (since switching from PoW to PoS -> 12.06 lowest - 12.25 highest)
# -> since no mining difficulty anymore
# https://ycharts.com/indicators/ethereum_average_block_time
# https://ethereum.org/en/developers/docs/blocks/
ethereum_blocktime = 12  # seconds

ethereum_tps = avg_tx_block / ethereum_blocktime

# Fulfill second requirement
print("The blocktime on the Ethereum blockchain is about 12 seconds")
ethereum_tps_file.write("\nThe blocktime on the Ethereum blockchain is about 12 seconds")


print(f"\nEthereum: Number of transactions per second: {ethereum_tps:.2f}")
ethereum_tps_file.write(f"\nNumber of transactions per second: {ethereum_tps:.2f}\n")


# 1 get average transactions per block
# 2 get average block time in seconds
# https://medium.com/@alephium/transactions-per-second-tps-f13217a49e39
