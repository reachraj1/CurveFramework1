import QuantLib as ql
from main import curves
from utils import objects, swap_configs, index_tickers

def usd_1m_example():
    calendar = ql.UnitedStates()
    start = ql.Date(17, 11, 2019)
    maturity = calendar.advance(start, ql.Period('5y'))

    fixedSchedule = ql.MakeSchedule(start, maturity, ql.Period('6M'))
    floatSchedule = ql.MakeSchedule(start, maturity, ql.Period('1M'))

    usd_1m_crv = curves['USD.1M']
    usd_1m_yts = ql.YieldTermStructureHandle(usd_1m_crv)
    usd_libor_1m = ql.USDLibor(ql.Period('1M'), usd_1m_yts)

    usd_yts = ql.YieldTermStructureHandle(curves['USD.OIS'])
    engine = ql.DiscountingSwapEngine(usd_yts)

    fixedRate = 0.354500 / 100
    swap = ql.VanillaSwap(
        ql.VanillaSwap.Receiver, 10e6,
        fixedSchedule, fixedRate, ql.Thirty360(),
        floatSchedule, usd_libor_1m, 0, ql.Actual360()
    )
    swap.setPricingEngine(engine)

    bbg_mtm = -573192.53
    print(f"Swap NPV  : {swap.NPV():,.2f}")
    print(f"BBG  NPV  : {bbg_mtm:,.2f}")
    print(f"Swap PV01 : {swap.fixedLegBPS():,.2f}")
    dif = bbg_mtm - swap.NPV()
    print(f"Diff      : {dif:,.2f}")
    print(f"Diff (bps): {dif / swap.fixedLegBPS():,.2f}")    


def jpy_3m_example():
    calendar = objects.get('JAPAN')
    start = ql.Date(15,3,2020)
    maturity = ql.Date(15,6,2020)

    fixedSchedule = ql.MakeSchedule(start, maturity, ql.Period('3M'), calendar=calendar)
    floatSchedule = ql.MakeSchedule(start, maturity, ql.Period('3M'), calendar=calendar)

    jpy_3m_crv = curves.get('JPY.3M')
    jpy_3m_yts = ql.YieldTermStructureHandle(jpy_3m_crv)

    jpy_libor_3m = objects.get('JPY.3M').clone(jpy_3m_yts)

    jpy_yts = ql.YieldTermStructureHandle(curves.get('JPY.OIS'))
    engine = ql.DiscountingSwapEngine(jpy_yts)

    swap = ql.VanillaSwap(
        ql.VanillaSwap.Receiver, 1e9,
        fixedSchedule, -0.15 / 100, ql.Actual365Fixed(),
        floatSchedule, jpy_libor_3m, 0, ql.Actual360()
    )
    swap.setPricingEngine(engine)

    print(f"Swap NPV  : {swap.NPV():,.2f}")    
    print(f"Swap Rate  : {swap.fairRate() * 100:,.6f}")

#usd_1m_example()
jpy_3m_example()