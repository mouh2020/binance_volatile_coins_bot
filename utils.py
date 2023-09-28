from binance.client import Client
from config import *

client = Client()
tickers = client.get_all_tickers()

def get_coin_pairs() : 
    usdt_coins = []
    for ticker in tickers : 
        ##### Filter USDT pairs only.
        if ticker["symbol"].endswith(coin_pair) and "DOWN" not in ticker['symbol'] and "UP" not in ticker['symbol']: 
            if ticker['symbol'].startswith('USD') or ticker['symbol'].startswith('EUR')  : 
                continue
            usdt_coins.append(ticker['symbol'])
    return usdt_coins[:coins_number]

def get_stream_link() :
    coins :list[str] = get_coin_pairs()
    url =  "wss://stream.binance.com:9443/stream?streams="
    for coin in coins : 
        url+=coin.lower()+f"@kline_{str(candle_interval)}/"
    return url[:-1]