# Binance Profit Calculator
calculate profit based on current Market price.


## Configuration

1. Signup Binance ( Referral url: https://www.binance.com/?ref=23209789 )
2. Enable Two-factor Authentication
3. Go API Center, https://www.binance.com/userCenter/createApi.html
4. Create New Key

        [✓] Read Info [X] Enable Trading [X] Enable Withdrawals 
5. Open settings.py
6. Get an API and Secret Key, insert into config.py

        API key for account access
        api_key = ''
        Secret key for account access
        api_secret = ''
        The currency you trade,default BTC.
        currency = "BTC"


        API Docs: https://www.binance.com/restapipub.html

## Requirements

    sudo pip install python-binance
    
    
    Python 2.7
        import os
        import time
        import settings
        import binance


## Usage

    python calculator.py

Type the coin you want to calculate for example; storm its case incentive no need to worry about typing it in caps. The calculator outputs three profits; 1%. 3%, 5% it can be modified to your liking. The program automatically takes the last price of the coin to calculate the profit and tell you what amount to sell.


![calculator](http://excdn.pw/img/binance-calculator.png)

## Files

calculator.py main program

settings.py for the api key. secret and the currency you trade.


## Contributing
The code can be improved so any contributions are highly appreciated im always looking to learn new ways to do things.
