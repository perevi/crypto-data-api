import alphavantage

class downloader:
    """
    Class to manage interface between different APIs
    """
    def __init__(self, source):
        self.source = source

    def get_daily_data(self, symbol, market):
        """
        :param symbol: str  eg. BTC
        :param market: str  eg. USD
        :return: pd.DataFrame
        """
        if(self.source=='alphavantage'):
            df = alphavantage.get_daily_data(symbol, market)
        else:
            raise NameError(f'API not defined for:{self.source}')
        return df


if __name__ == '__main__':
    mydownloader = downloader('alphavantage')
    df = mydownloader.get_daily_data('BTC', 'USD')
    print(df.head())


