from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from click._compat import raw_input
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

key = 'PH2SVH5EIR56RTXD'
ti = TechIndicators(key, output_format='pandas')
ts = TimeSeries(key, output_format='pandas')

AAPL_MACD, meta_data =ti.get_macd(symbol='AAPL',interval='daily',series_type="close")
AAPL_RSI, meta_data = ti.get_rsi(symbol='AAPL', interval='daily',series_type="close")
AAPL_BBANDS, meta_data = ti.get_bbands(symbol="AAPL", interval='daily', series_type="close")
AAPL_PRICE, meta_data = ts.get_daily(symbol="AAPL", outputsize='full')

AAPL = AAPL_MACD.join(AAPL_RSI["RSI"])
AAPL = AAPL.join(AAPL_BBANDS["Real Lower Band"])
AAPL = AAPL.join(AAPL_BBANDS['Real Middle Band'])
AAPL = AAPL.join(AAPL_BBANDS['Real Upper Band'])
AAPL = AAPL.join(AAPL_PRICE['4. close'])

AAPL.to_csv('C:/Users/akeats97/Desktop/AAPL.csv')



'''

#print(AAPL_MACD)



class TechnicalIndicators:
    def __init__(self):
        self.api_key= 'KMOA5YH5JT2Z2A1B'
        self.stock_name=self.question()
        self.macd_data=self.macd()
        self.rsi_data=self.rsi()
        self.bbands_data=self.bbands()
        self.close_data=self.close()
        self.sma_data=self.sma()
    def question(self):
        stock_name=raw_input("Enter stock name:")
        return stock_name
    def macd(self):
        a = TechIndicators(key=self.api_key, output_format='pandas')
        data, meta_data = a.get_macd(symbol=self.stock_name,interval='daily')
        return data
    def rsi(self):
        b=TechIndicators(key=self.api_key,output_format='pandas')
        data,meta_data = b.get_rsi(symbol=self.stock_name,interval='daily',time_period=14)
        return data
    def bbands (self):
        c=TechIndicators(key=self.api_key,output_format='pandas')
        data,meta_data=c.get_bbands(symbol=self.stock_name)
        return data
    def sma(self):
        d= TechIndicators(key=self.api_key, output_format='pandas')
        data, meta_data = d.get_sma(symbol=self.stock_name,time_period=30)
        return data
    def close(self):
        d=TimeSeries(key=self.api_key,output_format='pandas')
        data,meta_data=d.get_daily(symbol=self.stock_name,outputsize='full')
        return data

#if __name__ == "__main__":

TI=TechnicalIndicators()
#close_data = TI.close_data
#macd_data = TI.macd_data
#rsi_data=TI.rsi_data
#bbands_data=TI.bbands_data
#sma_data = TI.sma_data
#plt.plot(macd_data)
#plt.show()
print(TI.macd_data)
'''