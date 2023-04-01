from datetime import datetime
import requests

def get_latest_block():
    url = "https://api.snowtrace.io/api?module=proxy&action=eth_blockNumber&apikey=99BRJK9QAN7CVY8Y5VT27AHGHTYXI1JEUX"
    response = requests.get(url)
    responseResult = response.json()["result"]
    return responseResult


def get_tx_count(block_hash):
    url = f"https://api.snowtrace.io/api?module=proxy&action=eth_getBlockTransactionCountByNumber&tag={block_hash}&apikey=99BRJK9QAN7CVY8Y5VT27AHGHTYXI1JEUX"
    response = requests.get(url)
    return response.json()["result"]



# Open file stream
# Append new report to the end of the file
avalanche_tps_file = open("C:\\Users\\sbitt\PycharmProjects\\pythonProject\\Avalanche\\avalanche_tps.txt", "a")

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
avalanche_tps_file.write(f"\nToday's date is {current_time}")

block_count_hex = (get_latest_block())
block_count_int = int(block_count_hex, 16)


avalanche_tps_file.write(f"\nRecent block count is: {block_count_int}\n\n")

tx_count_int = 0
block_time_sec = 2  # https://snowtrace.io/chart/blocktime -> Average Blocktime from 1.1.2022 - 12.03.2023
blocksToCalc = 100


for i in range(block_count_int, block_count_int - blocksToCalc, -1):
    current_block_hash = hex(i)
    avalanche_tps_file.write(f"\nBlockcount: {i} Blockhash: {current_block_hash}")
    tx_count_hash = get_tx_count(current_block_hash)
    tx_count_int += int(tx_count_hash, 16)
    avalanche_tps_file.write(f"\nTransaction count = {int(tx_count_hash, 16)}")

print(f"\nToday's date is {current_time}")
print(f"\nAvalanche: In the most recent and last {blocksToCalc} blocks {tx_count_int} transactions were performed *.* ")
avalanche_tps_file.write(f"\nAvalanche: In the most recent and last {blocksToCalc} blocks {tx_count_int} transactions were performed *.* ")

avgTransactionsPerBlock = tx_count_int / blocksToCalc

# Fulfill first requirement
print(f"The average transactions per block are {avgTransactionsPerBlock}")
avalanche_tps_file.write(f"\nThe average transactions per block are {avgTransactionsPerBlock}")

# Fulfill second requirement
print(f"The blocktime on the Avalanche blockchain is 2 seconds")
avalanche_tps_file.write(f"\nThe blocktime on the Avalanche blockchain is 2 seconds")

avalanche_tps = avgTransactionsPerBlock / block_time_sec

print(f"Number of transactions per second: {avalanche_tps:.2f}")
avalanche_tps_file.write(f"\nNumber of transactions per second: {avalanche_tps:.2f}\n\n")

# 1 get average transactions per block
# 2 get average block time in seconds
# https://medium.com/@alephium/transactions-per-second-tps-f13217a49e39


