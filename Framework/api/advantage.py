
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='S4D1VXSRJZTYJQZV',output_format='pandas')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday(symbol='MSFT',interval='30min', outputsize='full')
print(data.head(50))

data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.savefig('demo.png', bbox_inches='tight')

