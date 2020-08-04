import json
import glob

import pandas as pd

curves = glob.glob('curves/*.json')

tickers = []
for curve in curves:
    d = json.load(open(curve))
    for crv, data in d.items():
        for instrument, rows in data.get('INSTRUMENTS').items():
            for quote in rows.get('QUOTES'):
                if isinstance(quote, str):
                    tickers.append(quote)
                else:
                    for q in quote:
                        if isinstance(q, str):
                            tickers.append(q)
                        else:
                            for qq in q:
                                tickers.append(qq)


print("\nBloomberg tickers not in curves")
print("----------------------------------")
bbg = pd.read_csv('tickers.csv')
print(bbg[~bbg.quote.isin(tickers)].quote.to_list())

print("")
print("\nCurve Quotes not in tickers")
print("----------------------------------")
print(
    list(filter(lambda x: x not in bbg.quote.to_list(), tickers))
)
