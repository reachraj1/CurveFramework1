import sys
import pybbg
bbg = pybbg.Pybbg()
import pandas as pd

def saveData(date):
    tickers = pd.read_csv('tickers.csv')
    bbgDate = ''.join(date.split('-')[::-1])

    params = { "nonTradingDayFillOption": "NON_TRADING_WEEKDAYS" }
    data = bbg.bdh(tickers.ticker, 'PX_LAST', bbgDate, bbgDate, other_request_parameters=params)

    output = pd.DataFrame(data.iloc[0])
    output = output.join(tickers.set_index('ticker'))
    output.columns = ['value', 'quote']  

    mask = (output.quote.str.startswith('EUR')) & (output.quote.str.contains('BASIS6M12M'))
    output[mask] = output[mask].interpolate(method ='linear', limit_direction ='forward')

    mask = (output.quote.str.startswith('SGD')) & (output.quote.str.contains('BASIS6M3M'))
    output[mask] = output[mask].interpolate(method ='linear', limit_direction ='forward')

    filename = f'quotes//{bbgDate}.csv'
    output[['quote', 'value']].to_csv(filename, index=False)
    print(f"Market data saved to {filename}")


if len(sys.argv) < 2:
    print("Must add date string (DD-MM-YYYY) as parameter")
    exit

date = sys.argv[1]
if not isinstance(date, str):
    print("Parameter must be a string")
    exit

print(f"Getting market quotes for {date}")
saveData(str(date))
