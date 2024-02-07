# dynamically imports config from the provided config module
from typing import List
HUBBLE_RPC_URL = "https://nd-125-878-356.hubble.ext.p2pify.com/a056b03e8307044756c0a92ce1dd2f15/ext/bc/2jfjkB7NkK4v8zoaoWmh5eaABNW6ynjQvemPFZpgPQ7ugrmUXv/rpc"
HUBBLE_WS_URL = "wss://ws-nd-125-878-356.hubble.ext.p2pify.com/a056b03e8307044756c0a92ce1dd2f15/ext/bc/2jfjkB7NkK4v8zoaoWmh5eaABNW6ynjQvemPFZpgPQ7ugrmUXv/ws"
HUBBLE_ENV = "hubblemundus"
# Hubble Indexer
HUBBLE_INDEXER_API_URL = "https://hubblenet-api.hubble.exchange/"

def init_config(config_module):
    for attr_name in dir(config_module):
        if not attr_name.startswith("_"):  # skip internal names
            globals()[attr_name] = getattr(config_module, attr_name)


def get_minimum_quantity(market: int) -> float:
    try:
        return min_quantity[market]
    except KeyError:
        raise ValueError(f"Market {market} does not exist")


def get_price_precision(market: int) -> int:
    try:
        return price_precision[market]
    except KeyError:
        raise ValueError(f"Market {market} does not exist")


def get_allowed_candle_intervals() -> List[str]:
    return list(allowed_candle_intervals)
