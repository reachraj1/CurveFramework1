#!/usr/bin/env python
# coding: utf-8

import QuantLib as ql
import os
import platform


from main import curves
from utils import objects, swap_configs, CurveBuilder
import pandas as pd

curve_path = 'curves/*.json'


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
        self.swap = self.makeInstrument(
            swapType, notional, start, maturity, self.index1, self.index2, spread)
        self.swap.setPricingEngine(self.engine)

    def makeInstrument(self, swapType, notional, start, maturity, index1, index2, spread):
        schedule1 = ql.MakeSchedule(start, maturity, index1.tenor())

        leg1 = ql.IborLeg([notional], schedule1, index1,)
        schedule2 = ql.MakeSchedule(start, maturity, index1.tenor())
        #leg2 = ql.OvernightLeg([notional], schedule2, index2, ql.Actual360(), ql.Following, [1],[spread], True)
        leg2 = ql.IborLeg([notional], schedule2, index2, spreads=[spread])
        return ql.Swap(leg1, leg2)

    def NPV(self):
        return self.swap.NPV()

    def BR01(self):
        return self.swap.legBPS(0)

    def basisSpread(self):
        accuracy = 0.00001
        guess = 0.002
        step = 0.0001

        def basisFairValue(spread):
            swap = self.makeInstrument(
                self.swapType, self.notional, self.start, self.maturity, self.index1, self.index2, spread)
            swap.setPricingEngine(self.engine)
            return swap.NPV()
        return ql.Brent().solve(basisFairValue, accuracy, guess, step)


swapType = ql.VanillaSwap.Payer

notional = 10e6
start = ql.Date(18, 9, 2019)
maturity = ql.Date(18, 9, 2024)

basis = BasisSwap(swapType, notional, start, maturity,
                  'USD.3M', 'USD.1M', 0.00275, 'USD.OIS')

indexes = ['USD.3M', 'USD.OIS', 'USD.1M']
for key in indexes:
    filename = key.replace('.', '') + '.csv'
    fixings = pd.read_csv(f'fixings/{filename}', header=None).dropna()
    fixings.columns = ['date', 'value']
    fixingDates = [ql.Date(dt,  '%Y-%m-%d') for dt in fixings.date]
    fixingValues = [float(value) / 100 for value in fixings.value]
    floatingIndex = objects.get(key)
    for day, fixing in zip(fixingDates, fixingValues):
        if day < ql.Settings.instance().evaluationDate:
            floatingIndex.addFixing(day, fixing)

print(f"Swap Fair Spread: \t{basis.basisSpread():,.3%}")
print(f"Swap BR01: \t\t{basis.BR01():,.2f}")
print(f"Swap NPV: \t\t{basis.NPV():,.2f}")


swapType = ql.VanillaSwap.Payer

notional = 10e6
start = ql.Date(10, 1, 2019)
maturity = ql.Date(10, 1, 2023)

basis = BasisSwap(swapType, notional, start, maturity,
                  'USD.3M', 'USD.OIS', 0.0010, 'USD.OIS')

print(f"Swap Fair Spread: \t{basis.basisSpread():,.3%}")
print(f"Swap BR01: \t\t{basis.BR01():,.2f}")

print(f"Rec Leg NPV: \t\t{basis.swap.legNPV(0):,.2f}")
print(f"Pay Leg NPV: \t\t{basis.swap.legNPV(1):,.2f}")

print(f"Swap NPV: \t\t{basis.NPV():,.2f}")


for cf in basis.swap.leg(1):
    print(f"{cf.date().ISO()} \t {cf.amount():,.2f}")


# #### Check Fixings for an index

# In[16]:


im = ql.IndexManager.instance()
index2_name = basis.index2.name()

fixings = pd.DataFrame(
    im.getHistory(index2_name).values(),
    columns=['fixing'],
    index=map(lambda x: x.to_date(), im.getHistory(index2_name).dates())
)
fixings.index = pd.to_datetime(fixings.index)
fx = fixings.loc['2019-7-10':'2019-10-10'].copy()
fx.style.format({"fixing": "{:,.3%}"})


# In[ ]:


# In[ ]:
