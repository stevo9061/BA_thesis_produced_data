import time
import requests


def get_tx_count():
    url = "https://blockstream.info/liquid/api/blocks/tip/hash"
    response = requests.get(url)
    response = requests.get(url).text

    #TODO: ERROR
    # Sollte mir den letzten blockhash zurückliefern
    # atm wäre das: f525d45c1600159d9640c1c93711b4361e156b59e765edb49f3e5635e84d09ee
    #latest_block_hash = response.json()["blockhash"]
    #latest_block_hash = response.json()

    # https://blockstream.info/liquid/api/block/f525d45c1600159d9640c1c93711b4361e156b59e765edb49f3e5635e84d09ee
    #url = f"https://blockstream.info/liquid/api/block/{latest_block_hash}"
    url=f"https://blockstream.info/liquid/api/block/{response}"
    response = requests.get(url)
    #return len(response.json()["txids"])
    return response.json()["tx_count"]


start = time.time()
tx_count_start = get_tx_count()
time.sleep(1)
tx_count_end = get_tx_count()
end = time.time()

tx_per_second = (tx_count_end - tx_count_start) / (end - start)
print(f"Number of transactions per second: {tx_per_second:.2f}")