import requests, datetime
import pandas as pd

URL_BASE = 'https://www.alphavantage.co'
API_KEY = 'NN8SN9J3TZENT811'

def basic_getter(func, symbol, market):
    """
    :param func:    str     eg. DIGITAL_CURRENCY_DAILY 
    :param symbol:  str     eg. BTC 
    :param market:  str     eg. USD
    :return: dictionary (json)
    """""

    url = f'{URL_BASE}/query?function={func}&symbol={symbol}&market={market}&apikey={API_KEY}'
    r = requests.get(url)
    return r.json()


def get_daily_data(symbol, market):
    """
    :param symbol:  str     eg. BTC
    :param market:  str     eg. USD
    :return: pandas.DataFrame
    """
    dataall = basic_getter('DIGITAL_CURRENCY_DAILY', symbol, market)
    datats = dataall['Time Series (Digital Currency Daily)']
    dates, opens, highs, lows, closes, volumes, marketcaps = [], [], [], [], [], [], []

    for datestr, data in datats.items():
        year, month, day = list(map(int, datestr.split('-')))
        dates.append(datetime.date(year, month, day))
        opens.append(float(data[f'1a. open ({market})']))
        highs.append(float(data[f'2a. high ({market})']))
        lows.append(float(data[f'3a. low ({market})']))
        closes.append(float(data[f'4a. close ({market})']))
        volumes.append(float(data[f'5. volume']))
        marketcaps.append(float(data[f'6. market cap ({market})']))

    tabledata = {'open': opens, 'high': highs, 'low':lows, 'close':closes}
    index = pd.Index(dates, name='date')
    df = pd.DataFrame(tabledata, index=index)
    return df

if __name__ == "__main__":
    symbol = 'BTC'
    market = 'USD'
    df = get_daily_data(symbol, market)
    print(df.head())




