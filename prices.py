import QuantLib as ql
from main import curves
from utils import objects, swap_configs, index_tickers

import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format

swaps = pd.read_csv('swaps.csv')

for key in index_tickers:
    filename = key.replace('.', '') + '.csv'
    fixings = pd.read_csv(f'fixings/{filename}', header=None).dropna()
    fixings.columns = ['date', 'value']
    fixingDates = [ql.Date(dt,  '%Y-%m-%d') for dt in fixings.date]
    fixingValues = [float(value) / 100 for value in fixings.value]
    floatingIndex = objects.get(key)
    # floatingIndex.addfixings(fixingDates, fixingValues) # Had to use a loop because BBG calendar and QuantLib calendars don't seem to mactch
    for day, fixing in zip(fixingDates, fixingValues):
        try:
            floatingIndex.addFixing(day, fixing)
        except:
            pass


class Swap:
    def __init__(self, config, notional, start, maturity, fixedRate, spread, *rest):
        self.config = swap_configs[config]

        self.notional = notional
        self.start = ql.Date(start, '%d-%m-%Y')
        self.maturity = ql.Date(maturity, '%d-%m-%Y')
        self.fixedRate = fixedRate / 100
        self.spread = spread / 100
        self.fixedFreq = ql.Period(self.config.get('fixedFreq'))
        self.fixedDayCount = self.config.get('fixedDayCount')
        self.calendar = self.config.get('calendar')

        self.fixedSchedule = ql.MakeSchedule(
            self.start,
            self.maturity,
            self.fixedFreq,
            calendar=self.calendar, rule=ql.DateGeneration.Backward)

        self.floatIndex = self.config.get('floatIndex')
        self.forwardCurve = curves.get(config)
        self.forwardCurve_yts = ql.RelinkableYieldTermStructureHandle()
        self.forwardCurve_yts.linkTo(self.forwardCurve)

        self.floatIndex = self.floatIndex.clone(self.forwardCurve_yts)

        self.floatSchedule = ql.MakeSchedule(
            self.start,
            self.maturity,
            self.floatIndex.tenor(),
            calendar=self.calendar, rule=ql.DateGeneration.Backward)

        self.swap = ql.VanillaSwap(
            ql.VanillaSwap.Payer, self.notional,
            self.fixedSchedule, self.fixedRate, self.fixedDayCount,
            self.floatSchedule, self.floatIndex, self.spread, self.floatIndex.dayCounter()
        )
        self.discountCurve = curves.get(self.config.get('discountCurve'))

        self.discountCurve_yts = ql.RelinkableYieldTermStructureHandle()
        self.discountCurve_yts.linkTo(self.discountCurve)

        engine = ql.DiscountingSwapEngine(self.discountCurve_yts)
        self.swap.setPricingEngine(engine)

    def DV01(self):
        spread = ql.SimpleQuote(0.00 / 100)

        forward_curve = ql.ZeroSpreadedTermStructure(
            ql.YieldTermStructureHandle(
                self.forwardCurve), ql.QuoteHandle(spread)
        )
        self.forwardCurve_yts.linkTo(forward_curve)

        discount_curve = ql.ZeroSpreadedTermStructure(
            ql.YieldTermStructureHandle(
                self.discountCurve), ql.QuoteHandle(spread)
        )
        self.discountCurve_yts.linkTo(forward_curve)

        spread.setValue(0.01 / 100)
        up_npv = self.swap.NPV()
        spread.setValue(-0.01 / 100)
        down_npv = self.swap.NPV()

        self.forwardCurve_yts.linkTo(self.forwardCurve)
        self.discountCurve_yts.linkTo(self.discountCurve)
        return (up_npv - down_npv) / 2

    def NPV(self):
        return self.swap.NPV()

    def fairRate(self):
        return self.swap.fairRate()

    def cfs(self, leg=0):
        data = []
        for cf in map(ql.as_coupon, self.swap.leg(leg)):
            if cf.date() > ql.Settings.instance().evaluationDate:
                data.append({
                    'accuralStart': cf.accrualStartDate(),
                    'accrualEnd': cf.accrualEndDate(),
                    'accrualDays': cf.accrualDays(),
                    'amount': cf.amount(),
                    'rate': cf.rate() * 100,
                    'discount': self.discountCurve_yts.discount(cf.date())
                })
        return pd.DataFrame(data).style.format({'discount': "{:.6f}", "amount": "{:,.2f}"})


for idx, swap in swaps.iterrows():
    sw = Swap(*swap)
    swaps.loc[idx, 'fixedLegNPV'] = sw.swap.fixedLegNPV()
    swaps.loc[idx, 'floatingLegNPV'] = sw.swap.floatingLegNPV()
    swaps.loc[idx, 'MtM'] = sw.NPV()
    swaps.loc[idx, 'PV01'] = sw.swap.fixedLegBPS()
    swaps.loc[idx, 'DV01'] = sw.DV01()
    swaps.loc[idx, 'faiRate'] = sw.fairRate() * 100

print(swaps)
