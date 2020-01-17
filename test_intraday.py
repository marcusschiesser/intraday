import intraday
import pandas as pd
import os

TEST_TICKER = "__test__"

def test_get_lastday_emptyframe():
    df = pd.DataFrame(columns = ['Datetime'])
    assert intraday.get_lastday(df) == intraday.START_DATE, "empty dataframe must return start date"

def test_get_lastday():
    df = intraday.get_cache(TEST_TICKER)
    date = intraday.get_lastday(df)
    assert date == date.fromisoformat("2019-11-20"), "test dataframe must return 2019-11-20"

def test_get_tickers():
    tickers = intraday.get_tickers(TEST_TICKER)
    assert len(tickers) == 1
    assert tickers[0] == 'test', "test ticker must be 'test'"

def test_get_ticker():
    df = intraday.get_ticker('SPY')
    print(df.head())

if __name__ == "__main__":
    test_get_lastday_emptyframe()
    test_get_lastday()
    test_get_tickers()
    test_get_ticker()
    print("Everything passed")


