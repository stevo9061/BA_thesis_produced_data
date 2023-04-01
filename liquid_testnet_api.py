from datetime import datetime
import requests


def get_latest_block():
    url = "https://blockstream.info/liquidtestnet/api/blocks/tip/height"
    response = requests.get(url).text # e.g. 2218887
    return response


def get_block_hash(block_height):
    url = f"https://blockstream.info/liquidtestnet/api/block-height/{block_height}"
    response = requests.get(url).text
    return response


def get_tx_count(block_hash):
    url = f"https://blockstream.info/liquidtestnet/api/block/{block_hash}"
    response = requests.get(url)
    return response.json()["tx_count"] # e.g. 1539


block_count = int(get_latest_block())
tx_count = 0
# (60 x 1 = 1 minutes) https://help.blockstream.com/hc/en-us/articles/900001390903-What-is-the-transaction-capacity-of-Liquid-
# wrong -> (60 x 2 = 2 minutes)https://hackernoon.com/a-beginners-guide-to-the-liquid-network
block_time_sec = 60
blocksToCalc = 10

for i in range(block_count, block_count - blocksToCalc, -1):
    block_hash = get_block_hash(i)
    tx_count += get_tx_count(block_hash)

current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Today's date is {current_time}")
print(f"Liquid Network: In the most recent and last {blocksToCalc} blocks {tx_count} transactions were performed *.* ")

avgTransactionsPerBlock = tx_count / blocksToCalc

# Fulfill first requirement
print(f"The average transactions per block are {avgTransactionsPerBlock}")

# Fulfill second requirement
print(f"The blocktime on the Liquid Network L2 Off-Chain solution is about {block_time_sec} minutes.")

bitcoin_tps = avgTransactionsPerBlock / block_time_sec


print(f"Number of transactions per second: {bitcoin_tps:.2f}")


# 1 get average transactions per block
# 2 get average block time in seconds
# https://medium.com/@alephium/transactions-per-second-tps-f13217a49e39