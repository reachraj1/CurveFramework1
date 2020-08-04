import QuantLib as ql
from main import curves
from utils import objects, swap_configs, index_tickers

import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format


class BasisSwap:
    def __init__(self, index1, index2, discount, spread, notional, start, maturity):
        self.swapType = ql.VanillaSwap.Payer
        self.notional = notional
        self.start = ql.Date(start, '%d-%m-%Y')
        self.maturity = ql.Date(maturity, '%d-%m-%Y')
        self.yts1 = ql.YieldTermStructureHandle(curves.get(index1))

        self.index1 = objects.get(index1).clone(self.yts1)
        self.yts2 = ql.YieldTermStructureHandle(curves.get(index2))
        self.index2 = objects.get(index2).clone(self.yts2)
        self.spread = spread / 100 / 100
        self.discount_yts = ql.YieldTermStructureHandle(curves.get(discount))
        self.engine = ql.DiscountingSwapEngine(self.discount_yts) 
        self.swap = self.makeInstrument(
            notional, self.start, self.maturity, self.index1, self.index2, self.spread)
        self.swap.setPricingEngine(self.engine)

    def makeInstrument(self, notional, start, maturity, index1, index2, spread):
        schedule1 = ql.MakeSchedule(start, maturity, index1.tenor())
        n1 = len(schedule1)-1
        schedule2 = ql.MakeSchedule(start, maturity, index1.tenor())
        n2 = len(schedule2)-1
        return ql.FloatFloatSwap(
            self.swapType, [notional] * n1, [notional] * n2,
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
            swap = self.makeInstrument(
                self.notional, self.start, self.maturity, self.index1, self.index2, spread)
            swap.setPricingEngine(self.engine)
            return swap.NPV()
        return ql.Brent().solve(basisFairValue, accuracy, guess, step)


swaps = pd.read_csv('basis_swaps.csv')

# Fixings
for key in index_tickers:
    filename = key.replace('.', '') + '.csv'
    fixings = pd.read_csv(f'fixings/{filename}', header=None).dropna()
    fixings.columns = ['date', 'value']
    fixingDates = [ql.Date(dt,  '%Y-%m-%d') for dt in fixings.date]
    fixingValues = [float(value) / 100 for value in fixings.value]
    floatingIndex = objects.get(key)
    for day, fixing in zip(fixingDates, fixingValues):
        if day < ql.Settings.instance().evaluationDate:
            try:
                floatingIndex.addFixing(day, fixing)
            except:
                pass

for idx, swap in swaps.iterrows():
    sw = BasisSwap(*swap)
    swaps.loc[idx, 'MtM'] = sw.NPV()
    swaps.loc[idx, 'faiRate'] = sw.basisSpread() * 10000

print(swaps)
