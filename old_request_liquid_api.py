import time
import requests


def get_block_count():
    url = "https://blockstream.info/liquid/api/blocks/tip/height"
    response = requests.get(url).text # 2218887
    return response

def get_block_hash(block_height):
    url = f"https://blockstream.info/liquid/api/block-height/{block_height}"
    response = requests.get(url).text
    return response

def get_tx_count(block_hash):
    url = f"https://blockstream.info/liquid/api/block/{block_hash}"
    response = requests.get(url)
    return response.json()["tx_count"]



start = time.time()
block_count = int(get_block_count())
tx_count = 0

for i in range(block_count, block_count - 2000, -1):
    block_hash = get_block_hash(i)
    # Print ausgabe machen welcher hash er gerade ist, und vllt alle hashs in ein file speichern als überprüfung
    # ob wirklich 1000 hashs überprüft wurden
    tx_count += get_tx_count(block_hash)

end = time.time()

tx_per_second = tx_count / (end - start)
print(f"Number of transactions per second: {tx_per_second:.2f}")
