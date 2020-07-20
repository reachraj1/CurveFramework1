import QuantLib as ql
from main import curves
from utils import objects, swap_configs, index_tickers

import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format

class BasisSwap:
    def __init__(self, swapType, notional, start, maturity, index1, index2, spread, discount):
        self.swapType = swapType
        self.notional = notional
        self.start = start
        self.maturity = maturity
        self.yts1 = ql.YieldTermStructureHandle(curves.get(index1))
        self.index1 = objects.get(index1).clone(self.yts1)
        self.yts2 = ql.YieldTermStructureHandle(curves.get(index2))
        self.index2 = objects.get(index2).clone(self.yts2)
        self.spread = spread / 100 / 100
        self.discount_yts = ql.YieldTermStructureHandle(curves.get(discount))
        self.engine = ql.DiscountingSwapEngine(self.discount_yts)
        self.swap = self.makeInstrument(swapType, notional, start, maturity, self.index1, self.index2, spread)
        self.swap.setPricingEngine(self.engine)
    def makeInstrument(self, swapType, notional, start, maturity, index1, index2, spread):
        schedule1 = ql.MakeSchedule(start, maturity, index1.tenor())
        n1 = len(schedule1)-1
        schedule2 = ql.MakeSchedule(start, maturity, index2.tenor())
        n2 = len(schedule2)-1        
        return ql.FloatFloatSwap(
            swapType, [notional] * n1, [notional] * n2,
            schedule1, index1, index1.dayCounter(),
            schedule2, index2, index2.dayCounter(),
            False, False,
            [1] * n1, [0.0] * n1, [ql.nullDouble()] * n1, [ql.nullDouble()] * n1,
            [1] * n2, [spread] * n2            
        )
    def NPV(self):
        return self.swap.NPV()
    def basisSpread(self):
        accuracy = 0.00001
        guess = 0.002
        step = 0.0001
        def basisFairValue(spread):
            swap = self.makeInstrument(self.swapType, self.notional, self.start, self.maturity, self.index1, self.index2, spread)
            swap.setPricingEngine(self.engine)
            return swap.NPV()                
        return ql.Brent().solve(basisFairValue, accuracy, guess, step)
    
swapType = ql.VanillaSwap.Payer

notional = 10e6
start = ql.Date(18,9,2019)
maturity = ql.Date(18,9,2024)

swaps = [
    # index1, index2, sprd (bps), discountCurve, bbgSpread
    ('USD.3M', 'USD.1M', 0.0, 'USD.OIS', 12.308),
    ('USD.3M', 'USD.6M', 0.0, 'USD.OIS', -6.708),
    ('USD.3M', 'USD.OIS', 0.0, 'USD.OIS', 27.434),
    ('AUD.6M', 'AUD.3M', 0.0, 'AUD.3M', -7.888),
    ('GBP.3M', 'GBP.OIS', 0.0, 'GBP.OIS', 14.929),
    ('JPY.6M', 'JPY.3M', 0.0, 'JPY.OIS', 6.64),   
]

df = pd.DataFrame(swaps, columns=['index1', 'index2', 'sprd', 'discountCurve', 'bbgSpread'])
df['start'] = start.ISO()
df['maturity'] = maturity.ISO()
for idx, (index1, index2, spread, discount, bbgSpread) in enumerate(swaps):
    basis = BasisSwap(swapType, notional, start, maturity, index1, index2, spread, discount)
    df.loc[idx, 'MtM'] = basis.NPV()
    df.loc[idx, 'modelSpread'] = basis.basisSpread() * 10000
    
df['dif'] = df.modelSpread - df.bbgSpread
print(  df)

