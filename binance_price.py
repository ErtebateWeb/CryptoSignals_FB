import requests
import json
import time
from datetime import timedelta

def get_price(symbol):
    base_url="https://api.binance.com/api/v3/ticker/price?symbol="+symbol
    print("BaseUrl:",base_url)
    response = requests.get(base_url).json()
    #print(json.dumps(response["price"],indent=4))
    #print(type(response["price"]))
    price=response["price"]
    Price = float(price)
    # print(Price)
    return Price

def get_Symbol_Price_Ticker():
    base_url="https://api.binance.com/api/v3/ticker/price"
    # print("BaseUrl:",base_url)
    response = requests.get(base_url).json()
    #print(json.dumps(response["price"],indent=4))
    #print(type(response["price"]))
    #price=response["price"]
    #Price = float(price)
    # print(Price)
    return response
