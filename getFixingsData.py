import pybbg
from utils import index_tickers

bbg = pybbg.Pybbg()

def fixings():
    fixings_path = 'fixings/'
    fixing_tickers = list(index_tickers.values())
    inv_map = {v: k for k, v in index_tickers.items()}
    fixings = bbg.bdh(fixing_tickers, 'PX_LAST', '20180101')
    fixings.rename(columns=inv_map, inplace=True)
    for col in fixings.columns:
        values = fixings[col].dropna()
        filename = col.replace('.', '') + '.csv'
        values.to_csv(fixings_path + filename)    
       
fixings()
