import time, os, settings
from binance.client import Client,BinanceAPIException
from colorama import init
init()
from colorama import Fore

def calculate(x, y):
    z = (x * y)
    final = x + z
    return final

client = Client(settings.api_key, settings.api_secret)

while True:
    try:
        to_buy = str(raw_input("Enter coin to buy: "))
        to_buy = to_buy.upper()
        tickers = client.get_ticker(symbol=to_buy + settings.currency)
        lastp = float(tickers['lastPrice'])

        print Fore.LIGHTBLUE_EX + "Buy:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(lastp), Fore.LIGHTMAGENTA_EX + "Sell:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(calculate(lastp, 0.01)), "@" + Fore.LIGHTGREEN_EX + " 1% Gain" + Fore.RESET
        print Fore.LIGHTBLUE_EX + "Buy:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(lastp), Fore.LIGHTMAGENTA_EX + "Sell:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(calculate(lastp, 0.03)), "@" + Fore.LIGHTGREEN_EX + " 3% Gain" + Fore.RESET
        print Fore.LIGHTBLUE_EX + "Buy:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(lastp), Fore.LIGHTMAGENTA_EX + "Sell:" + Fore.LIGHTWHITE_EX, '{0:.8f}'.format(calculate(lastp, 0.05)), "@" + Fore.LIGHTGREEN_EX + " 5% Gain" + Fore.RESET
        raw_input("press [ENTER] to calculate another coin. ")
        os.system('cls||clear')
    except BinanceAPIException as e:
        print e.status_code
        print e.message
        print time.asctime(time.localtime(time.time()))
