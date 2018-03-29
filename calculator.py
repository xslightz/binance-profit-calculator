#/usr/bin/python
import time, os, settings
from binance.client import Client,BinanceAPIException

def calculate_profit(last_price, profit_percentage):
   return last_price * (profit_percentage + 1)

def print_stats(last_price, profit_percent):
   to_percent = 100
   print("Buy:", '{0:.8f}'.format(last_price),
       'Sell: ', '{0:.8f}'.format(calculate_profit(last_price, profit_percent)),
       '@' + ' {0}%% Gain'.format(profit_percent * to_percent))

#[MAIN]
client = Client(settings.api_key, settings.api_secret)
PROFIT_PERCENTAGES = [0.01, 0.03, 0.05]

while True:
   try:
       to_buy = str(raw_input("Enter coin to buy: "))
       to_buy = to_buy.upper()
       tickers = client.get_ticker(symbol=to_buy + settings.currency)
       last_price = float(tickers['lastPrice'])

       for percent in PROFIT_PERCENTAGES:
           print_stats(last_price, percent)

       raw_input("press [ENTER] to calculate another coin. ")
       os.system('cls||clear')
   except BinanceAPIException as e:
       print(e.status_code)
       print(e.message)
       print(time.asctime(time.localtime(time.time())))
