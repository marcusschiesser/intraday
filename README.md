# intraday

Download and caches intraday finance market data and makes it available as [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

Data is retrieved by using [yfinance](https://pypi.org/project/yfinance/), a library 
to download historical market data from Yahoo! finance.
Due to the limitations of yfinance, intraday data can only by downloaded for the last 30 days and only for 7 days per request.

Therefore this module is caching all retrieved data using CSV files. The goal of this project is to store as much 
intraday data as possible, so please send pull requests with data updates. 

## Usage

1. Save this module in the same directory as your Python file:
```
$ git clone https://github.com/marcusschiesser/intraday.git
```

2. Then you can call `get_ticker` to retrieve a Dataframe for a ticker symbol, e.g.: for `SPY`:
```python
import intraday
df = intraday.get_ticker('SPY')
df.head()
```
This method gets the data from the cache (if it exists) and appends 7 days of data from `yfinance`. 

3. Alternatively, you can also just get the Dataframe currently stored in the cache for a ticker symbol by calling `get_cache`:
```python
df = intraday.get_cache('SPY')
```
