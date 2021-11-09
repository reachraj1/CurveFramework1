"""
Notional :1 million GBP
Valuation date: 14th May 2021
Effective date: 26th Jan 2006
Maturity date: 26th Jan 2055
Fixed rate: 3.5%
Leg2 index : GBPUK-RPI1T
"""

import QuantLib as ql
import datetime
import pandas as pd


valuation_date = ql.Date(14, 5, 2021)
ql.Settings.instance().setEvaluationDate(valuation_date)

# Build GBP OIS Curve
sonia_data = pd.DataFrame(
    [
        {
            "tenor": "1D",
            "tenor_ticker": "SONIO/N  Index",
            "ask_yield": 0.05,
            "mid_yield": 0.05,
            "bid_yield": 0.05,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "1W",
            "tenor_ticker": "BPSWS1Z  Curncy",
            "ask_yield": 0.054,
            "mid_yield": 0.05,
            "bid_yield": 0.046,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "2W",
            "tenor_ticker": "BPSWS2Z  Curncy",
            "ask_yield": 0.054,
            "mid_yield": 0.05,
            "bid_yield": 0.046,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "1M",
            "tenor_ticker": "BPSWSA   Curncy",
            "ask_yield": 0.053,
            "mid_yield": 0.05,
            "bid_yield": 0.047,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "2M",
            "tenor_ticker": "BPSWSB   Curncy",
            "ask_yield": 0.058,
            "mid_yield": 0.05,
            "bid_yield": 0.043,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "3M",
            "tenor_ticker": "BPSWSC   Curncy",
            "ask_yield": 0.055,
            "mid_yield": 0.051,
            "bid_yield": 0.047,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "4M",
            "tenor_ticker": "BPSWSD   Curncy",
            "ask_yield": 0.059,
            "mid_yield": 0.051,
            "bid_yield": 0.043,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "5M",
            "tenor_ticker": "BPSWSE   Curncy",
            "ask_yield": 0.061,
            "mid_yield": 0.051,
            "bid_yield": 0.042,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "6M",
            "tenor_ticker": "BPSWSF   Curncy",
            "ask_yield": 0.055,
            "mid_yield": 0.052,
            "bid_yield": 0.049,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "7M",
            "tenor_ticker": "BPSWSG   Curncy",
            "ask_yield": 0.06,
            "mid_yield": 0.052,
            "bid_yield": 0.044,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "8M",
            "tenor_ticker": "BPSWSH   Curncy",
            "ask_yield": 0.06,
            "mid_yield": 0.053,
            "bid_yield": 0.045,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "9M",
            "tenor_ticker": "BPSWSI   Curncy",
            "ask_yield": 0.057,
            "mid_yield": 0.055,
            "bid_yield": 0.052,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "10M",
            "tenor_ticker": "BPSWSJ   Curncy",
            "ask_yield": 0.067,
            "mid_yield": 0.058,
            "bid_yield": 0.049,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "11M",
            "tenor_ticker": "BPSWSK   Curncy",
            "ask_yield": 0.071,
            "mid_yield": 0.061,
            "bid_yield": 0.051,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "1Y",
            "tenor_ticker": "BPSWS1   Curncy",
            "ask_yield": 0.068,
            "mid_yield": 0.065,
            "bid_yield": 0.063,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "18M",
            "tenor_ticker": "BPSWS1F  Curncy",
            "ask_yield": 0.104,
            "mid_yield": 0.1,
            "bid_yield": 0.097,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "2Y",
            "tenor_ticker": "BPSWS2   Curncy",
            "ask_yield": 0.151,
            "mid_yield": 0.147,
            "bid_yield": 0.144,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "3Y",
            "tenor_ticker": "BPSWS3   Curncy",
            "ask_yield": 0.273,
            "mid_yield": 0.269,
            "bid_yield": 0.265,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "4Y",
            "tenor_ticker": "BPSWS4   Curncy",
            "ask_yield": 0.385,
            "mid_yield": 0.383,
            "bid_yield": 0.38,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "5Y",
            "tenor_ticker": "BPSWS5   Curncy",
            "ask_yield": 0.489,
            "mid_yield": 0.486,
            "bid_yield": 0.483,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "6Y",
            "tenor_ticker": "BPSWS6   Curncy",
            "ask_yield": 0.577,
            "mid_yield": 0.574,
            "bid_yield": 0.572,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "7Y",
            "tenor_ticker": "BPSWS7   Curncy",
            "ask_yield": 0.654,
            "mid_yield": 0.651,
            "bid_yield": 0.648,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "8Y",
            "tenor_ticker": "BPSWS8   Curncy",
            "ask_yield": 0.721,
            "mid_yield": 0.718,
            "bid_yield": 0.715,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "9Y",
            "tenor_ticker": "BPSWS9   Curncy",
            "ask_yield": 0.776,
            "mid_yield": 0.773,
            "bid_yield": 0.77,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "10Y",
            "tenor_ticker": "BPSWS10  Curncy",
            "ask_yield": 0.829,
            "mid_yield": 0.826,
            "bid_yield": 0.823,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "12Y",
            "tenor_ticker": "BPSWS12  Curncy",
            "ask_yield": 0.906,
            "mid_yield": 0.904,
            "bid_yield": 0.901,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "15Y",
            "tenor_ticker": "BPSWS15  Curncy",
            "ask_yield": 0.978,
            "mid_yield": 0.975,
            "bid_yield": 0.972,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "20Y",
            "tenor_ticker": "BPSWS20  Curncy",
            "ask_yield": 1.017,
            "mid_yield": 1.014,
            "bid_yield": 1.011,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "25Y",
            "tenor_ticker": "BPSWS25  Curncy",
            "ask_yield": 1.016,
            "mid_yield": 1.013,
            "bid_yield": 1.01,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "30Y",
            "tenor_ticker": "BPSWS30  Curncy",
            "ask_yield": 0.996,
            "mid_yield": 0.993,
            "bid_yield": 0.99,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "40Y",
            "tenor_ticker": "BPSWS40  Curncy",
            "ask_yield": 0.917,
            "mid_yield": 0.914,
            "bid_yield": 0.911,
            "last_update": datetime.date(2021, 5, 14),
        },
        {
            "tenor": "50Y",
            "tenor_ticker": "BPSWS50  Curncy",
            "ask_yield": 0.856,
            "mid_yield": 0.853,
            "bid_yield": 0.85,
            "last_update": datetime.date(2021, 5, 14),
        },
    ]
)


print("Building GBP OIS Curve...")
index = ql.Sonia()
helpers = []
for idx, row in sonia_data.iterrows():
    rate = row["mid_yield"] / 100
    tenor = row.tenor
    if tenor == "1D":
        helpers.append(ql.DepositRateHelper(rate, index))
    else:
        helpers.append(
            ql.OISRateHelper(
                0, ql.Period(tenor), ql.QuoteHandle(ql.SimpleQuote(rate)), index
            )
        )
gbp_ois = ql.PiecewiseLogCubicDiscount(0, ql.TARGET(), helpers, ql.Actual365Fixed())
gbp_ois.enableExtrapolation()


# Build Inflation Curve

infl_data = pd.DataFrame(
    [
        {
            "px_last": 3.653,
            "security_tenor_two": "1Y",
            "maturity": datetime.date(2022, 11, 15),
        },
        {
            "px_last": 3.597,
            "security_tenor_two": "2Y",
            "maturity": datetime.date(2023, 11, 15),
        },
        {
            "px_last": 3.6083,
            "security_tenor_two": "3Y",
            "maturity": datetime.date(2024, 11, 15),
        },
        {
            "px_last": 3.665,
            "security_tenor_two": "4Y",
            "maturity": datetime.date(2025, 11, 15),
        },
        {
            "px_last": 3.682,
            "security_tenor_two": "5Y",
            "maturity": datetime.date(2026, 11, 15),
        },
        {
            "px_last": 3.6957,
            "security_tenor_two": "6Y",
            "maturity": datetime.date(2027, 11, 15),
        },
        {
            "px_last": 3.7119999999999997,
            "security_tenor_two": "7Y",
            "maturity": datetime.date(2028, 11, 15),
        },
        {
            "px_last": 3.725,
            "security_tenor_two": "8Y",
            "maturity": datetime.date(2029, 11, 15),
        },
        {
            "px_last": 3.735,
            "security_tenor_two": "9Y",
            "maturity": datetime.date(2030, 11, 15),
        },
        {
            "px_last": 3.7116,
            "security_tenor_two": "10Y",
            "maturity": datetime.date(2031, 11, 15),
        },
        {
            "px_last": 3.6837999999999997,
            "security_tenor_two": "12Y",
            "maturity": datetime.date(2033, 11, 15),
        },
        {
            "px_last": 3.638,
            "security_tenor_two": "15Y",
            "maturity": datetime.date(2036, 11, 15),
        },
        {
            "px_last": 3.601,
            "security_tenor_two": "20Y",
            "maturity": datetime.date(2041, 11, 15),
        },
        {
            "px_last": 3.504,
            "security_tenor_two": "25Y",
            "maturity": datetime.date(2046, 11, 15),
        },
        {
            "px_last": 3.424,
            "security_tenor_two": "30Y",
            "maturity": datetime.date(2051, 11, 15),
        },
        {
            "px_last": 3.287,
            "security_tenor_two": "40Y",
            "maturity": datetime.date(2061, 11, 15),
        },
        {
            "px_last": 3.278,
            "security_tenor_two": "50Y",
            "maturity": datetime.date(2071, 11, 15),
        },
    ]
)

print("Build RPI Curve...")
observationLag = ql.Period("2M")
dc = ql.ActualActual()
frequency = ql.Monthly
cal = ql.UnitedKingdom()
bdc = ql.ModifiedFollowing
inflationIndex = ql.UKRPI(True)

instruments = []
for idx, row in infl_data.iterrows():
    maturity = ql.Date().from_date(row.maturity)
    quote = ql.QuoteHandle(ql.SimpleQuote(row.px_last / 100.0))
    helper = ql.ZeroCouponInflationSwapHelper(
        quote,
        observationLag,
        maturity,
        cal,
        bdc,
        dc,
        inflationIndex,
        ql.YieldTermStructureHandle(gbp_ois),
    )
    instruments.append(helper)

baseZeroRate = infl_data.iloc[0].px_last / 100
inflationCurve = ql.PiecewiseZeroInflation(
    valuation_date,
    cal,
    dc,
    observationLag,
    frequency,
    inflationIndex.interpolated(),
    baseZeroRate,
    instruments,
)
inflationCurve.enableExtrapolation()


discountYTS = ql.RelinkableYieldTermStructureHandle()
inflationYTS = ql.RelinkableZeroInflationTermStructureHandle()


discountYTS.linkTo(gbp_ois)
inflationYTS.linkTo(inflationCurve)


# RPI History

rpi = pd.DataFrame(
    [
        {"index": datetime.date(2004, 1, 31), "PX_LAST": 183.1},
        {"index": datetime.date(2004, 2, 29), "PX_LAST": 183.8},
        {"index": datetime.date(2004, 3, 31), "PX_LAST": 184.6},
        {"index": datetime.date(2004, 4, 30), "PX_LAST": 185.7},
        {"index": datetime.date(2004, 5, 31), "PX_LAST": 186.5},
        {"index": datetime.date(2004, 6, 30), "PX_LAST": 186.8},
        {"index": datetime.date(2004, 7, 31), "PX_LAST": 186.8},
        {"index": datetime.date(2004, 8, 31), "PX_LAST": 187.4},
        {"index": datetime.date(2004, 9, 30), "PX_LAST": 188.1},
        {"index": datetime.date(2004, 10, 31), "PX_LAST": 188.6},
        {"index": datetime.date(2004, 11, 30), "PX_LAST": 189.0},
        {"index": datetime.date(2004, 12, 31), "PX_LAST": 189.9},
        {"index": datetime.date(2005, 1, 31), "PX_LAST": 188.9},
        {"index": datetime.date(2005, 2, 28), "PX_LAST": 189.6},
        {"index": datetime.date(2005, 3, 31), "PX_LAST": 190.5},
        {"index": datetime.date(2005, 4, 30), "PX_LAST": 191.6},
        {"index": datetime.date(2005, 5, 31), "PX_LAST": 192.0},
        {"index": datetime.date(2005, 6, 30), "PX_LAST": 192.2},
        {"index": datetime.date(2005, 7, 31), "PX_LAST": 192.2},
        {"index": datetime.date(2005, 8, 31), "PX_LAST": 192.6},
        {"index": datetime.date(2005, 9, 30), "PX_LAST": 193.1},
        {"index": datetime.date(2005, 10, 31), "PX_LAST": 193.3},
        {"index": datetime.date(2005, 11, 30), "PX_LAST": 193.6},
        {"index": datetime.date(2005, 12, 31), "PX_LAST": 194.1},
        {"index": datetime.date(2006, 1, 31), "PX_LAST": 193.4},
        {"index": datetime.date(2006, 2, 28), "PX_LAST": 194.2},
        {"index": datetime.date(2006, 3, 31), "PX_LAST": 195.0},
        {"index": datetime.date(2006, 4, 30), "PX_LAST": 196.5},
        {"index": datetime.date(2006, 5, 31), "PX_LAST": 197.7},
        {"index": datetime.date(2006, 6, 30), "PX_LAST": 198.5},
        {"index": datetime.date(2006, 7, 31), "PX_LAST": 198.5},
        {"index": datetime.date(2006, 8, 31), "PX_LAST": 199.2},
        {"index": datetime.date(2006, 9, 30), "PX_LAST": 200.1},
        {"index": datetime.date(2006, 10, 31), "PX_LAST": 200.4},
        {"index": datetime.date(2006, 11, 30), "PX_LAST": 201.1},
        {"index": datetime.date(2006, 12, 31), "PX_LAST": 202.7},
        {"index": datetime.date(2007, 1, 31), "PX_LAST": 201.6},
        {"index": datetime.date(2007, 2, 28), "PX_LAST": 203.1},
        {"index": datetime.date(2007, 3, 31), "PX_LAST": 204.4},
        {"index": datetime.date(2007, 4, 30), "PX_LAST": 205.4},
        {"index": datetime.date(2007, 5, 31), "PX_LAST": 206.2},
        {"index": datetime.date(2007, 6, 30), "PX_LAST": 207.3},
        {"index": datetime.date(2007, 7, 31), "PX_LAST": 206.1},
        {"index": datetime.date(2007, 8, 31), "PX_LAST": 207.3},
        {"index": datetime.date(2007, 9, 30), "PX_LAST": 208.0},
        {"index": datetime.date(2007, 10, 31), "PX_LAST": 208.9},
        {"index": datetime.date(2007, 11, 30), "PX_LAST": 209.7},
        {"index": datetime.date(2007, 12, 31), "PX_LAST": 210.9},
        {"index": datetime.date(2008, 1, 31), "PX_LAST": 209.8},
        {"index": datetime.date(2008, 2, 29), "PX_LAST": 211.4},
        {"index": datetime.date(2008, 3, 31), "PX_LAST": 212.1},
        {"index": datetime.date(2008, 4, 30), "PX_LAST": 214.0},
        {"index": datetime.date(2008, 5, 31), "PX_LAST": 215.1},
        {"index": datetime.date(2008, 6, 30), "PX_LAST": 216.8},
        {"index": datetime.date(2008, 7, 31), "PX_LAST": 216.5},
        {"index": datetime.date(2008, 8, 31), "PX_LAST": 217.2},
        {"index": datetime.date(2008, 9, 30), "PX_LAST": 218.4},
        {"index": datetime.date(2008, 10, 31), "PX_LAST": 217.7},
        {"index": datetime.date(2008, 11, 30), "PX_LAST": 216.0},
        {"index": datetime.date(2008, 12, 31), "PX_LAST": 212.9},
        {"index": datetime.date(2009, 1, 31), "PX_LAST": 210.1},
        {"index": datetime.date(2009, 2, 28), "PX_LAST": 211.4},
        {"index": datetime.date(2009, 3, 31), "PX_LAST": 211.3},
        {"index": datetime.date(2009, 4, 30), "PX_LAST": 211.5},
        {"index": datetime.date(2009, 5, 31), "PX_LAST": 212.8},
        {"index": datetime.date(2009, 6, 30), "PX_LAST": 213.4},
        {"index": datetime.date(2009, 7, 31), "PX_LAST": 213.4},
        {"index": datetime.date(2009, 8, 31), "PX_LAST": 214.4},
        {"index": datetime.date(2009, 9, 30), "PX_LAST": 215.3},
        {"index": datetime.date(2009, 10, 31), "PX_LAST": 216.0},
        {"index": datetime.date(2009, 11, 30), "PX_LAST": 216.6},
        {"index": datetime.date(2009, 12, 31), "PX_LAST": 218.0},
        {"index": datetime.date(2010, 1, 31), "PX_LAST": 217.9},
        {"index": datetime.date(2010, 2, 28), "PX_LAST": 219.2},
        {"index": datetime.date(2010, 3, 31), "PX_LAST": 220.7},
        {"index": datetime.date(2010, 4, 30), "PX_LAST": 222.8},
        {"index": datetime.date(2010, 5, 31), "PX_LAST": 223.6},
        {"index": datetime.date(2010, 6, 30), "PX_LAST": 224.1},
        {"index": datetime.date(2010, 7, 31), "PX_LAST": 223.6},
        {"index": datetime.date(2010, 8, 31), "PX_LAST": 224.5},
        {"index": datetime.date(2010, 9, 30), "PX_LAST": 225.3},
        {"index": datetime.date(2010, 10, 31), "PX_LAST": 225.8},
        {"index": datetime.date(2010, 11, 30), "PX_LAST": 226.8},
        {"index": datetime.date(2010, 12, 31), "PX_LAST": 228.4},
        {"index": datetime.date(2011, 1, 31), "PX_LAST": 229.0},
        {"index": datetime.date(2011, 2, 28), "PX_LAST": 231.3},
        {"index": datetime.date(2011, 3, 31), "PX_LAST": 232.5},
        {"index": datetime.date(2011, 4, 30), "PX_LAST": 234.4},
        {"index": datetime.date(2011, 5, 31), "PX_LAST": 235.2},
        {"index": datetime.date(2011, 6, 30), "PX_LAST": 235.2},
        {"index": datetime.date(2011, 7, 31), "PX_LAST": 234.7},
        {"index": datetime.date(2011, 8, 31), "PX_LAST": 236.1},
        {"index": datetime.date(2011, 9, 30), "PX_LAST": 237.9},
        {"index": datetime.date(2011, 10, 31), "PX_LAST": 238.0},
        {"index": datetime.date(2011, 11, 30), "PX_LAST": 238.5},
        {"index": datetime.date(2011, 12, 31), "PX_LAST": 239.4},
        {"index": datetime.date(2012, 1, 31), "PX_LAST": 238.0},
        {"index": datetime.date(2012, 2, 29), "PX_LAST": 239.9},
        {"index": datetime.date(2012, 3, 31), "PX_LAST": 240.8},
        {"index": datetime.date(2012, 4, 30), "PX_LAST": 242.5},
        {"index": datetime.date(2012, 5, 31), "PX_LAST": 242.4},
        {"index": datetime.date(2012, 6, 30), "PX_LAST": 241.8},
        {"index": datetime.date(2012, 7, 31), "PX_LAST": 242.1},
        {"index": datetime.date(2012, 8, 31), "PX_LAST": 243.0},
        {"index": datetime.date(2012, 9, 30), "PX_LAST": 244.2},
        {"index": datetime.date(2012, 10, 31), "PX_LAST": 245.6},
        {"index": datetime.date(2012, 11, 30), "PX_LAST": 245.6},
        {"index": datetime.date(2012, 12, 31), "PX_LAST": 246.8},
        {"index": datetime.date(2013, 1, 31), "PX_LAST": 245.8},
        {"index": datetime.date(2013, 2, 28), "PX_LAST": 247.6},
        {"index": datetime.date(2013, 3, 31), "PX_LAST": 248.7},
        {"index": datetime.date(2013, 4, 30), "PX_LAST": 249.5},
        {"index": datetime.date(2013, 5, 31), "PX_LAST": 250.0},
        {"index": datetime.date(2013, 6, 30), "PX_LAST": 249.7},
        {"index": datetime.date(2013, 7, 31), "PX_LAST": 249.7},
        {"index": datetime.date(2013, 8, 31), "PX_LAST": 251.0},
        {"index": datetime.date(2013, 9, 30), "PX_LAST": 251.9},
        {"index": datetime.date(2013, 10, 31), "PX_LAST": 251.9},
        {"index": datetime.date(2013, 11, 30), "PX_LAST": 252.1},
        {"index": datetime.date(2013, 12, 31), "PX_LAST": 253.4},
        {"index": datetime.date(2014, 1, 31), "PX_LAST": 252.6},
        {"index": datetime.date(2014, 2, 28), "PX_LAST": 254.2},
        {"index": datetime.date(2014, 3, 31), "PX_LAST": 254.8},
        {"index": datetime.date(2014, 4, 30), "PX_LAST": 255.7},
        {"index": datetime.date(2014, 5, 31), "PX_LAST": 255.9},
        {"index": datetime.date(2014, 6, 30), "PX_LAST": 256.3},
        {"index": datetime.date(2014, 7, 31), "PX_LAST": 256.0},
        {"index": datetime.date(2014, 8, 31), "PX_LAST": 257.0},
        {"index": datetime.date(2014, 9, 30), "PX_LAST": 257.6},
        {"index": datetime.date(2014, 10, 31), "PX_LAST": 257.7},
        {"index": datetime.date(2014, 11, 30), "PX_LAST": 257.1},
        {"index": datetime.date(2014, 12, 31), "PX_LAST": 257.5},
        {"index": datetime.date(2015, 1, 31), "PX_LAST": 255.4},
        {"index": datetime.date(2015, 2, 28), "PX_LAST": 256.7},
        {"index": datetime.date(2015, 3, 31), "PX_LAST": 257.1},
        {"index": datetime.date(2015, 4, 30), "PX_LAST": 258.0},
        {"index": datetime.date(2015, 5, 31), "PX_LAST": 258.5},
        {"index": datetime.date(2015, 6, 30), "PX_LAST": 258.9},
        {"index": datetime.date(2015, 7, 31), "PX_LAST": 258.6},
        {"index": datetime.date(2015, 8, 31), "PX_LAST": 259.8},
        {"index": datetime.date(2015, 9, 30), "PX_LAST": 259.6},
        {"index": datetime.date(2015, 10, 31), "PX_LAST": 259.5},
        {"index": datetime.date(2015, 11, 30), "PX_LAST": 259.8},
        {"index": datetime.date(2015, 12, 31), "PX_LAST": 260.6},
        {"index": datetime.date(2016, 1, 31), "PX_LAST": 258.8},
        {"index": datetime.date(2016, 2, 29), "PX_LAST": 260.0},
        {"index": datetime.date(2016, 3, 31), "PX_LAST": 261.1},
        {"index": datetime.date(2016, 4, 30), "PX_LAST": 261.4},
        {"index": datetime.date(2016, 5, 31), "PX_LAST": 262.1},
        {"index": datetime.date(2016, 6, 30), "PX_LAST": 263.1},
        {"index": datetime.date(2016, 7, 31), "PX_LAST": 263.4},
        {"index": datetime.date(2016, 8, 31), "PX_LAST": 264.4},
        {"index": datetime.date(2016, 9, 30), "PX_LAST": 264.9},
        {"index": datetime.date(2016, 10, 31), "PX_LAST": 264.8},
        {"index": datetime.date(2016, 11, 30), "PX_LAST": 265.5},
        {"index": datetime.date(2016, 12, 31), "PX_LAST": 267.1},
        {"index": datetime.date(2017, 1, 31), "PX_LAST": 265.5},
        {"index": datetime.date(2017, 2, 28), "PX_LAST": 268.4},
        {"index": datetime.date(2017, 3, 31), "PX_LAST": 269.3},
        {"index": datetime.date(2017, 4, 30), "PX_LAST": 270.6},
        {"index": datetime.date(2017, 5, 31), "PX_LAST": 271.7},
        {"index": datetime.date(2017, 6, 30), "PX_LAST": 272.3},
        {"index": datetime.date(2017, 7, 31), "PX_LAST": 272.9},
        {"index": datetime.date(2017, 8, 31), "PX_LAST": 274.7},
        {"index": datetime.date(2017, 9, 30), "PX_LAST": 275.1},
        {"index": datetime.date(2017, 10, 31), "PX_LAST": 275.3},
        {"index": datetime.date(2017, 11, 30), "PX_LAST": 275.8},
        {"index": datetime.date(2017, 12, 31), "PX_LAST": 278.1},
        {"index": datetime.date(2018, 1, 31), "PX_LAST": 276.0},
        {"index": datetime.date(2018, 2, 28), "PX_LAST": 278.1},
        {"index": datetime.date(2018, 3, 31), "PX_LAST": 278.3},
        {"index": datetime.date(2018, 4, 30), "PX_LAST": 279.7},
        {"index": datetime.date(2018, 5, 31), "PX_LAST": 280.7},
        {"index": datetime.date(2018, 6, 30), "PX_LAST": 281.5},
        {"index": datetime.date(2018, 7, 31), "PX_LAST": 281.7},
        {"index": datetime.date(2018, 8, 31), "PX_LAST": 284.2},
        {"index": datetime.date(2018, 9, 30), "PX_LAST": 284.1},
        {"index": datetime.date(2018, 10, 31), "PX_LAST": 284.5},
        {"index": datetime.date(2018, 11, 30), "PX_LAST": 284.6},
        {"index": datetime.date(2018, 12, 31), "PX_LAST": 285.6},
        {"index": datetime.date(2019, 1, 31), "PX_LAST": 283.0},
        {"index": datetime.date(2019, 2, 28), "PX_LAST": 285.0},
        {"index": datetime.date(2019, 3, 31), "PX_LAST": 285.1},
        {"index": datetime.date(2019, 4, 30), "PX_LAST": 288.2},
        {"index": datetime.date(2019, 5, 31), "PX_LAST": 289.2},
        {"index": datetime.date(2019, 6, 30), "PX_LAST": 289.6},
        {"index": datetime.date(2019, 7, 31), "PX_LAST": 289.5},
        {"index": datetime.date(2019, 8, 31), "PX_LAST": 291.7},
        {"index": datetime.date(2019, 9, 30), "PX_LAST": 291.0},
        {"index": datetime.date(2019, 10, 31), "PX_LAST": 290.4},
        {"index": datetime.date(2019, 11, 30), "PX_LAST": 291.0},
        {"index": datetime.date(2019, 12, 31), "PX_LAST": 291.9},
        {"index": datetime.date(2020, 1, 31), "PX_LAST": 290.6},
        {"index": datetime.date(2020, 2, 29), "PX_LAST": 292.0},
        {"index": datetime.date(2020, 3, 31), "PX_LAST": 292.6},
        {"index": datetime.date(2020, 4, 30), "PX_LAST": 292.6},
        {"index": datetime.date(2020, 5, 31), "PX_LAST": 292.2},
        {"index": datetime.date(2020, 6, 30), "PX_LAST": 292.7},
        {"index": datetime.date(2020, 7, 31), "PX_LAST": 294.2},
        {"index": datetime.date(2020, 8, 31), "PX_LAST": 293.3},
        {"index": datetime.date(2020, 9, 30), "PX_LAST": 294.3},
        {"index": datetime.date(2020, 10, 31), "PX_LAST": 294.3},
        {"index": datetime.date(2020, 11, 30), "PX_LAST": 293.5},
        {"index": datetime.date(2020, 12, 31), "PX_LAST": 295.4},
        {"index": datetime.date(2021, 1, 31), "PX_LAST": 294.6},
        {"index": datetime.date(2021, 2, 28), "PX_LAST": 296.0},
        {"index": datetime.date(2021, 3, 31), "PX_LAST": 296.9},
        {"index": datetime.date(2021, 4, 30), "PX_LAST": 301.1},
        {"index": datetime.date(2021, 5, 31), "PX_LAST": 301.9},
        {"index": datetime.date(2021, 6, 30), "PX_LAST": 304.0},
        {"index": datetime.date(2021, 7, 31), "PX_LAST": 305.5},
        {"index": datetime.date(2021, 8, 31), "PX_LAST": 307.4},
        {"index": datetime.date(2021, 9, 30), "PX_LAST": 308.6},
    ]
).set_index("index")


# Swap
inflationIndex = ql.UKRPI(True, inflationYTS)
for idx, row in rpi.iterrows():
    fixing_date = ql.Date().from_date(idx)
    inflationIndex.addFixing(fixing_date, row.PX_LAST, True)


notional = 1e6
startDate = ql.Date(26, 1, 2006)
endDate = ql.Date(26, 1, 2055)
fixedRate = 0.035
swapType = ql.ZeroCouponInflationSwap.Payer
swap = ql.ZeroCouponInflationSwap(
    swapType,
    notional,
    startDate,
    endDate,
    cal,
    ql.ModifiedFollowing,
    dc,
    fixedRate,
    inflationIndex,
    observationLag,
)
swapEngine = ql.DiscountingSwapEngine(discountYTS)
swap.setPricingEngine(swapEngine)


npv = swap.NPV()
print(f"NPV: {npv:,.2f}")
print(f"Swap Rate: {swap.fairRate():.3%}")
