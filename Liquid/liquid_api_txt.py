from datetime import datetime
import requests


def get_latest_block():
    url = "https://blockstream.info/liquid/api/blocks/tip/height"
    response = requests.get(url).text # e.g. 2218887
    return response


def get_block_hash(block_height):
    url = f"https://blockstream.info/liquid/api/block-height/{block_height}"
    response = requests.get(url).text
    return response


def get_tx_count(block_hash):
    url = f"https://blockstream.info/liquid/api/block/{block_hash}"
    response = requests.get(url)
    return response.json()["tx_count"] # e.g. 1539

# Open file stream
# Append new report to the end of the file
liquid_tps_file = open("C:\\Users\\sbitt\PycharmProjects\\pythonProject\\Liquid\\liquid_tps.txt", "a")

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
liquid_tps_file.write(f"\nToday's date is {current_time}")


block_count = int(get_latest_block())
tx_count = 0
# (60 x 1 = 1 minutes) https://help.blockstream.com/hc/en-us/articles/900001390903-What-is-the-transaction-capacity-of-Liquid-
# wrong -> (60 x 2 = 2 minutes)https://hackernoon.com/a-beginners-guide-to-the-liquid-network
block_time_sec = 60
blocksToCalc = 100

for i in range(block_count, block_count - blocksToCalc, -1):
    block_hash = get_block_hash(i)
    liquid_tps_file.write(f"\nBlockcount: {i} Blockhash: {block_hash}")
    tx_count += get_tx_count(block_hash)
    liquid_tps_file.write(f"\nTransaction count = {get_tx_count(block_hash)}")

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"\nToday's date is {current_time}")
print(f"\nLiquid Network: In the most recent and last {blocksToCalc} blocks {tx_count} transactions were performed *.* ")
liquid_tps_file.write(f"\nLiquid Network: In the most recent and last {blocksToCalc} blocks {tx_count} transactions were performed *.* ")

avgTransactionsPerBlock = tx_count / blocksToCalc

# Fulfill first requirement
print(f"The average transactions per block are {avgTransactionsPerBlock}")
liquid_tps_file.write(f"\nThe average transactions per block are {avgTransactionsPerBlock}")

# Fulfill second requirement
print(f"The blocktime of the Liquid Network Sidechain protocol is about {block_time_sec} seconds.")
liquid_tps_file.write(f"\nThe blocktime of the Liquid Network Sidechain protocol is about {block_time_sec} seconds.")

liquid_tps = avgTransactionsPerBlock / block_time_sec


print(f"Number of transactions per second: {liquid_tps:.2f}")
liquid_tps_file.write(f"\nNumber of transactions per second: {liquid_tps:.2f}\n\n")

# 1 get average transactions per block
# 2 get average block time in seconds
# https://medium.com/@alephium/transactions-per-second-tps-f13217a49e39
# https://blockstream.info/liquid/blocks/recent
