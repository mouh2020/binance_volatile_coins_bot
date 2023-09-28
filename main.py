import websocket,json,_thread,time,rel,math
from utils import get_stream_link
from config import bot_token,chat_id
from telebot import TeleBot

bot = TeleBot(bot_token)
bot.remove_webhook()
most_volatile_coins = {}
send_notifications  = False

def on_message(ws, message):
    global send_notifications
    global most_volatile_coins
    message = json.loads(message)
    candle =  message['data']['k']
    high    = float(candle['h'])
    low     = float(candle['l'])
    close   = float(candle['c'])
    open    = float(candle['o'])
    is_closed_candle = candle['x']
    candle_symbol = message['data']['s']
    if is_closed_candle : 
        candle_length = ((high/low)-1)*100
        most_volatile_coins[candle_symbol] = round(candle_length,2)
        send_notifications = True
        return
    if send_notifications == True : 
        coin = max(most_volatile_coins, key=most_volatile_coins.get)
        alert = f'{coin} : {most_volatile_coins[coin]}'
        print(alert)
        bot.send_message(chat_id=chat_id,
                         text=alert)
        most_volatile_coins = {}
        send_notifications = False
        return

def on_error(ws, error):
    print(f"error occured : {str(error)}")

def on_close(ws, close_status_code, close_msg):
    print("Stop listening ...")

def on_open(ws):
    print("Start listening ...")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(get_stream_link(),
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
    rel.signal(2, rel.abort)