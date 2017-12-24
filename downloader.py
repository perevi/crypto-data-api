import alphavantage

class downloader:
    """
    Class to manage interface between different APIs
    """
    def __init__(self, source):
        self.source = source

    def gen_file_name(self, head):
        """
        :param signature: str
        :return: str
        """
        return f'./data/{head}'

    def get_daily_data(self, symbol, market, save=False, filename=None):
        """
        :param symbol: str  eg. BTC
        :param market: str  eg. USD
        :return: pd.DataFrame
        """
        if(self.source=='alphavantage'):
            df = alphavantage.get_daily_data(symbol, market)
        else:
            raise NameError(f'API not defined for:{self.source}')
        df['source'] = self.source

        if(save):
            if(filename==None):
                filename = self.gen_file_name(f'{symbol}-{market}.daily.{source}.csv')
            df.to_csv(filename, sep=',')
        return df


if __name__ == '__main__':
    source = 'alphavantage'
    symbol = 'BTC'
    market = 'USD'
    mydownloader = downloader(source)
    df = mydownloader.get_daily_data(symbol, market, save=True)
    print(df.head())


