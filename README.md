# Updated Readme @ 4/11/2023 from JonathaSheets517

## Tom-Demark-Indicator
Financial charting with Tom DeMark indicator overlay



~Step 1~ - I recommend sourcing free historical crypto data from [CoinGeckoAPI](https://www.coingecko.com/en/api/documentation) combined with OHLC data from [Alpha Vantage API Key Generator](https://www.alphavantage.co/support/#api-key). You'll need a free API key from alphaVantage.

*Step 2* - Place all files in this repo into a common directory on your pc, set it as your current working directory

*Step 3* - navigate in terminal and run the NEW create_price_data_csv.py file
* choose BTC or ETH for historical data

*Step 4* - in terminal run updated other_indicators.py 
* choose the CSV file created from new py function.

*Step 5* - in terminal run updated TD_plotter.py file
* removes other indicators as starting view
* updates candlestick code to use mplfinance.original_flavor since matplotlib.finance is deprecated
* reverses the x-axis of the chart so its not plotting backwards  
* adjusts DeMark 9 and 13 day signal arrows so they're more visible
* prompts user to choose different CSV files in directory    


*The updated TD_plotter.py still looks at Bitcoin.* There's a new sample btc_price.csv in the repo.

In addition to moving averages, exponential moving averages, MACD, volume, and volume trend,
TD_plotter.py will also display the lesser known Tom DeMark indicator on a candle chart.
Details on how this indicator works and how it should be interpreted can be found [here](http://cs.calstatela.edu/wiki/images/c/cb/DeMark.pdf).

By default TD_plotter.py *will NOT* show 10 and 30 day exponential moving averages, MACD,
volume, and a 28 day moving average for volume. These can be changed by commenting/uncommenting
clearly marked sections of the code.

Note that TD_plotter.py uses Python modules outside the standard library. Specifically,
[requests](http://docs.python-requests.org/en/master/), [matplotlib](https://matplotlib.org/), [numpy](https://www.numpy.org/), and [pandas](https://pandas.pydata.org/). *And a bunch of other ones outlined in the respective .py files*

Sample data is provided in the price_data.csv file *and the NEW btc_price.csv file.*  

