# Most Volatile Coins Bot
This project is a Python-based bot that monitors cryptocurrency markets on Binance to identify the most volatile coins based on their price movements. It uses Binance WebSocket API to stream real-time market data and calculate the volatility of each coin.

## How it Works
The bot connects to the Binance WebSocket API and listens to the Kline/Candlestick data for specified cryptocurrency pairs. When a candle closes, it calculates the volatility of the coin and keeps track of the most volatile ones for a specific interval. It then notifies the user with the symbol and the percentage change in price for the coin with the largest candlestick in that interval.

## Project Files

main.py: Contains the main script for the bot, including the WebSocket connection setup and functions for processing messages and detecting volatile coins.

utils.py: Contains utility functions to fetch coin pairs and construct the WebSocket stream link.

config.py: Holds configuration parameters like the coin pair, number of coins to track, and candlestick interval.


## How to Use
Clone the repository: git clone https://github.com/mouh2020/binance_volatile_coins_bot.git

Install the required Python packages: pip install -r requirements.txt

Ensure you have valid Binance API credentials and update them in the config.py file.

Set up a Telegram bot and obtain the bot token and chat ID. Update bot_token and chat_id in config.py.

Configure the desired candlestick interval in config.py.
Run the bot: python main.py

The bot will start monitoring the specified coin pairs and notify you of the most volatile coins whenever a significant change in volatility is detected.