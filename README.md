# crypto-data-api
Api that pulls historical crypto currency data from several sources

Standardized data grabbing for different sources of crypto-currency historical data.
- coinmarketcap.com
- alphavantage.co
- cryptocompare.com

The intial idea is to have a class that will wrap methods specific to those APIs

Class: DataGrabber  
Attributes: 
  - source ( website from where the api will be connecting )
  - ...
Methods:
  - grab_daily_price
  - grab_daily_volume
  - ...
  
    
  
