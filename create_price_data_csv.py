import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pycoingecko
from pycoingecko import CoinGeckoAPI
import csv
import datetime

tickers = {
    "2y": "ZT=F",
    "3y": "Z3=F",
    "5y": "ZF=F",
    "10y": "ZN=F",
    "ultra 10y": "TN=F",
    "20y": "TWE=F",
    "Classic Long Bond": "ZB=F",
    "Ultra Long Bond 30y": "UB=F",
    "Emini SP500": "ES=F",
    "Crude Oil": "CL=F",
    "Nasdaq 100": "NQ=F",
    "Gold": "GC=F",
    "Copper":"HG=F",
    "Silver": "SI=F"
}

import csv
import datetime
from pycoingecko import CoinGeckoAPI
from alpha_vantage.cryptocurrencies import CryptoCurrencies

def save_to_csv(coin_data, coin_name):
    filename = f'{coin_name}_price.csv'
    
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Date', 'Open*', 'High', 'Low', 'Close**', 'Volume', 'Market Cap']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for entry in coin_data:
            writer.writerow(entry)

def get_alpha_vantage_data(symbol, api_key):
    cc = CryptoCurrencies(key=api_key)
    data, _ = cc.get_digital_currency_daily(symbol=symbol, market='USD')
    return data

def get_coin_data(coin_id, coin_symbol, api_key):
    cg = CoinGeckoAPI()
    historical_data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency='usd', days='max', interval='daily')
    av_data = get_alpha_vantage_data(coin_symbol, api_key)

    parsed_data = []

    for ohlc, volume, market_cap in zip(historical_data['prices'], historical_data['total_volumes'], historical_data['market_caps']):
        date = datetime.datetime.fromtimestamp(ohlc[0] / 1000).strftime('%Y-%m-%d')

        if date in av_data:
            av_entry = av_data[date]
            parsed_data.append({
                'date': date,
                'open': av_entry['1b. open (USD)'],
                'high': av_entry['2b. high (USD)'],
                'low': av_entry['3b. low (USD)'],
                'close': av_entry['4b. close (USD)'],
                'volume': volume[1],
                'market_cap': market_cap[1],
            })

    return parsed_data

def main():
    api_key = 'GET YOUR OWN API KEY'  # Replace with your actual Alpha Vantage API key

    print("Please choose a cryptocurrency:")
    print("Enter 1   for Bitcoin")
    print("Enter 2   for Ethereum")
    choice = int(input("Enter the number corresponding to your choice: "))

    coin = None
    coin_symbol = None

    if choice == 1:
        coin = 'bitcoin'
        coin_symbol = 'BTC'
    elif choice == 2:
        coin = 'ethereum'
        coin_symbol = 'ETH'
    else:
        print("Invalid choice. Please run the script again and choose a valid option.")
        return

    coin_data = get_coin_data(coin, coin_symbol, api_key)
    save_to_csv(coin_data, coin)

if __name__ == "__main__":
    main()
