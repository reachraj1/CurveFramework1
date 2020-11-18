import QuantLib as ql
import pandas as pd

objects = {
    # Calendars
    'AUSTRALIA': ql.Australia(),
    'TARGET': ql.TARGET(),
    'POLAND': ql.Poland(),
    'TAIWAN': ql.Taiwan(),
    'WEEKENDSONLY': ql.WeekendsOnly(),
    'SWITZERLAND': ql.Switzerland(),
    'HUNGARY': ql.Hungary(),
    'JAPAN': ql.Japan(),
    'SOUTHKOREA': ql.SouthKorea(),
    'SOUTHAFRICA': ql.SouthAfrica(),
    'UNITEDSTATES': ql.JointCalendar(ql.UnitedStates(), ql.UnitedKingdom()),
    'SWEDEN': ql.Sweden(),
    'HONGKONG': ql.HongKong(),
    'NEWZEALAND': ql.NewZealand(),
    'SINGAPORE': ql.Singapore(),
    'CANADA': ql.Canada(),
    'CHILE': ql.WeekendsOnly(),
    'CHINA': ql.China(),
    'THAILAND': ql.Thailand(),
    'CZECHREPUBLIC': ql.CzechRepublic(),
    'UNITEDKINGDOM': ql.UnitedKingdom(),
    'MEXICO': ql.Mexico(),
    'DENMARK': ql.Denmark(),
    'NORWAY': ql.Norway(),

    # Frequencies
    'ONCE': ql.Once,
    'QUARTERLY': ql.Quarterly,
    'SEMIANNUAL': ql.Semiannual,
    'ANNUAL': ql.Annual,
    'EVERYFOURWEEKS': ql.EveryFourthWeek,

    # DayCounters
    '30/360': ql.Thirty360(),
    'ACT/360': ql.Actual360(),
    'ACT/ACT': ql.ActualActual(),
    'ACT/365.FIXED': ql.Actual365Fixed(),
    'ACT/365': ql.Actual365Fixed(ql.Actual365Fixed.NoLeap),

    # Dates
    'FOLLOWING': ql.Following,
    'MODIFIEDFOLLOWING': ql.ModifiedFollowing,
    'BACKWARDS': ql.DateGeneration.Backward,
    'FORWARDS': ql.DateGeneration.Forward,

    # Overnight Indexes
    'AUD.OIS': ql.OvernightIndex('RBACOR', 0, ql.AUDCurrency(), ql.Australia(), ql.Actual365Fixed()),
    'CAD.OIS': ql.OvernightIndex('CAOREPO', 0, ql.CADCurrency(), ql.Canada(), ql.Actual365Fixed()),
    'CHF.OIS': ql.OvernightIndex('SARON', 0, ql.CHFCurrency(), ql.Switzerland(), ql.Actual360()),
    'CLP.OIS': ql.OvernightIndex('CLICP', 0, ql.CLPCurrency(), ql.WeekendsOnly(), ql.Actual360()),
    'CNY.OIS': ql.OvernightIndex('CNRR007', 0, ql.CNYCurrency(), ql.China(), ql.Actual365Fixed()),
    'COP.OIS': ql.OvernightIndex('COOVIBR', 0, ql.COPCurrency(), ql.WeekendsOnly(), ql.Actual360()),
    'DKK.OIS': ql.OvernightIndex('DETNTN', 1, ql.DKKCurrency(), ql.Denmark(), ql.Actual360()),
    'EUR.OIS': ql.Eonia(),
    'GBP.OIS': ql.Sonia(),
    'JPY.OIS': ql.OvernightIndex('MUTKCALM', 0, ql.JPYCurrency(), ql.Japan(), ql.Actual360()),
    'NZD.OIS': ql.OvernightIndex('NZOCRS', 0, ql.NZDCurrency(), ql.NewZealand(), ql.Actual365Fixed(ql.Actual365Fixed.NoLeap)),
    'SEK.OIS': ql.OvernightIndex('STIB1D', 0, ql.SEKCurrency(), ql.Sweden(), ql.Actual360()),
    'USD.OIS': ql.FedFunds(),

    # IBOR Indexes
    'AUD.3M': ql.IborIndex('BBSW3M', ql.Period('3M'), 2, ql.AUDCurrency(), ql.Australia(), ql.Following, True, ql.Actual365Fixed()),
    'AUD.6M': ql.IborIndex('BBSW6M', ql.Period('6M'), 2, ql.AUDCurrency(), ql.Australia(), ql.Following, True, ql.Actual365Fixed()),
    'CAD.1M': ql.CADLibor(ql.Period('1M')),
    'CAD.3M': ql.CADLibor(ql.Period('3M')),
    'CHF.3M': ql.CHFLibor(ql.Period('3M')),
    'CHF.6M': ql.CHFLibor(ql.Period('6M')),
    'CZK.3M': ql.Pribor(ql.Period('3M')),
    'CZK.6M': ql.Pribor(ql.Period('6M')),
    'DKK.3M': ql.DKKLibor(ql.Period('3M')),
    'DKK.6M': ql.DKKLibor(ql.Period('6M')),
    'EUR.6M': ql.Euribor6M(),
    'EUR.3M': ql.Euribor3M(),
    'EUR.1M': ql.Euribor1M(),
    'GBP.1M': ql.GBPLibor(ql.Period('1M')),
    'GBP.3M': ql.GBPLibor(ql.Period('3M')),
    'GBP.6M': ql.GBPLibor(ql.Period('6M')),
    'HKD.3M': ql.IborIndex('HIHD03M', ql.Period('3M'), 2, ql.HKDCurrency(), ql.HongKong(), ql.ModifiedFollowing, True, ql.Actual365Fixed()),
    'HUF.3M': ql.IborIndex('BUBOR3M', ql.Period('3M'), 2, ql.HUFCurrency(), ql.Hungary(), ql.Following, True, ql.Actual360()),
    'HUF.6M': ql.IborIndex('BUBOR6M', ql.Period('6M'), 2, ql.HUFCurrency(), ql.Hungary(), ql.Following, True, ql.Actual360()),
    'JPY.3M': ql.JPYLibor(ql.Period('3M')),
    'JPY.6M': ql.JPYLibor(ql.Period('6M')),
    'KRW.3M': ql.IborIndex('KWCDC', ql.Period('3M'), 1, ql.KRWCurrency(), ql.SouthKorea(), ql.ModifiedFollowing, True, ql.Actual365Fixed()),
    'MXN.28D': ql.IborIndex('MXIBTIIE', ql.Period(28, ql.Days), 2, ql.MXNCurrency(), ql.Mexico(), ql.Following, True, ql.Actual360()),
    'NOK.3M': ql.IborIndex('NIBOR3M', ql.Period('3M'), 2, ql.NOKCurrency(), ql.Norway(), ql.Following, True, ql.Actual360()),
    'NOK.6M': ql.IborIndex('NIBOR6M', ql.Period('6M'), 2, ql.NOKCurrency(), ql.Norway(), ql.Following, True, ql.Actual360()),
    'NZD.3M': ql.IborIndex('NDBB3M', ql.Period('3M'), 2, ql.NZDCurrency(), ql.NewZealand(), ql.ModifiedFollowing, True, ql.Actual365Fixed(ql.Actual365Fixed.NoLeap)),
    'PLN.3M': ql.IborIndex('WIBOR3M', ql.Period('3M'), 2, ql.PLNCurrency(), ql.Poland(), ql.ModifiedFollowing, True, ql.Actual365Fixed()),
    'PLN.6M': ql.IborIndex('WIBOR6M', ql.Period('6M'), 2, ql.PLNCurrency(), ql.Poland(), ql.ModifiedFollowing, True, ql.Actual365Fixed()),
    'SEK.3M': ql.SEKLibor(ql.Period('3M')),
    'SGD.3M': ql.IborIndex('SORF3M', ql.Period('3M'), 2, ql.SGDCurrency(), ql.Singapore(), ql.ModifiedFollowing, True, ql.Actual365Fixed(ql.Actual365Fixed.NoLeap)),
    'SGD.6M': ql.IborIndex('SORF6M', ql.Period('6M'), 2, ql.SGDCurrency(), ql.Singapore(), ql.ModifiedFollowing, True, ql.Actual365Fixed(ql.Actual365Fixed.NoLeap)),
    'THB.6M': ql.THBFIX(ql.Period('6M')),
    'TWD.3M': ql.IborIndex('Taibor3M', ql.Period('3m'), 2, ql.TWDCurrency(), ql.Taiwan(), ql.ModifiedFollowing, True, ql.Actual365Fixed()),
    'USD.1M': ql.USDLibor(ql.Period('1M')),
    'USD.3M': ql.USDLibor(ql.Period('3M')),
    'USD.6M': ql.USDLibor(ql.Period('6M')),
    'ZAR.3M': ql.Jibar(ql.Period('3M')),

    # Currencies
    'AUD': ql.AUDCurrency(),
    'CAD': ql.CADCurrency(),
    'CHF': ql.CHFCurrency(),
    'CLP': ql.CLPCurrency(),
    'COP': ql.COPCurrency(),
    'CZK': ql.CZKCurrency(),
    'DKK': ql.DKKCurrency(),
    'EUR': ql.EURCurrency(),
    'GBP': ql.GBPCurrency(),
    'HKD': ql.HKDCurrency(),
    'HUF': ql.HUFCurrency(),
    'JPY': ql.JPYCurrency(),
    'KFW': ql.KRWCurrency(),
    'MXN': ql.MXNCurrency(),
    'NOK': ql.NOKCurrency(),
    'NZD': ql.NZDCurrency(),
    'PLN': ql.PLNCurrency(),
    'SEK': ql.SEKCurrency(),
    'SGD': ql.SGDCurrency(),
    'THB': ql.THBCurrency(),
    'TWD': ql.TWDCurrency(),
    'ZAR': ql.ZARCurrency()
}

swap_configs = {
    'KRW.3M': {
        'calendar': ql.SouthKorea(),
        'fixedFreq': '3M',
        'fixedDayCount': ql.Actual365Fixed(),
        'floatIndex': objects['KRW.3M'],
        'discountCurve': 'KRW.3M'
    },
    'ZAR.3M': {
        'calendar': ql.SouthAfrica(),
        'fixedFreq': '1Y',
        'fixedDayCount': ql.ActualActual(),
        'floatIndex': objects['ZAR.3M'],
        'discountCurve': 'ZAR.3M'
    },
    'TWD.3M': {
        'calendar': ql.Taiwan(),
        'fixedFreq': '3M',
        'fixedDayCount': ql.Actual365Fixed(),
        'floatIndex': objects['TWD.3M'],
        'discountCurve': 'TWD.3M'
    },
    'JPY.3M': {
        'calendar': ql.Japan(),
        'fixedFreq': '3M',
        'fixedDayCount': ql.Actual365Fixed(),
        'floatIndex': objects['JPY.3M'],
        'discountCurve': 'JPY.OIS'

    }
}

index_tickers = {
    # Overnight Indexes
    'AUD.OIS': 'RBACOR Index',
    'CAD.OIS': 'CAONREPO Index',
    'CHF.OIS': 'SRFXON3 Index',
    'CLP.OIS': 'CLICP Index',
    'CNY.OIS': 'CNRR007 Index',
    'COP.OIS': 'COOVIBR Index',
    'DKK.OIS': 'DETNT/N Index',
    'EUR.OIS': 'EONIA Index',
    'GBP.OIS': 'SONIO/N Index',
    'JPY.OIS': 'MUTKCALM Index',
    'NZD.OIS': 'NZOCRS Index',
    'SEK.OIS': 'STIB1D Index',
    'USD.OIS': 'FEDL01 Index',

    # IBOR Indexes
    'AUD.3M': 'BBSW3M Index',
    'AUD.6M': 'BBSW6M Index',
    'CAD.1M': 'CDOR01 Index',
    'CAD.3M': 'CDOR03 Index',
    'CHF.3M': 'SF0003M Index',
    'CHF.6M': 'SF0006M Index',
    'CZK.3M': 'PRIB03M Index',
    'CZK.6M': 'PRIB06M Index',
    'DKK.3M': 'CIBO03M Index',
    'DKK.6M': 'CIBO06M Index',
    'EUR.6M': 'EUR006M Index',
    'EUR.3M': 'EUR003M Index',
    'EUR.1M': 'EUR001M Index',
    'GBP.1M': 'BP0001M Index',
    'GBP.3M': 'BP0003M Index',
    'GBP.6M': 'BP0006M Index',
    'HKD.3M': 'HIHD03M Index',
    'HUF.3M': 'BUBOR03M Index',
    'HUF.6M': 'BUBOR06M Index',
    'JPY.3M': 'JY0003M Index',
    'JPY.6M': 'JY0006M Index',
    'KRW.3M': 'KWCDC Curncy',
    'MXN.28D': 'MXIBTIIE Index',
    'NOK.3M': 'NIBOR3M Index',
    'NOK.6M': 'NIBOR6M Index',
    'NZD.3M': 'NDBB3M Curncy',
    'PLN.3M': 'WIBR3M Index',
    'PLN.6M': 'WIBR6M Index',
    'SEK.3M': 'STIB3M Index',
    'SGD.3M': 'SORF3M Index',
    'SGD.6M': 'SORF6M Index',
    'THB.6M': 'THFX6M Index',
    'TWD.3M': 'TAIBOR3M Index',
    'USD.1M': 'US0001M Index',
    'USD.3M': 'US0003M Index',
    'USD.6M': 'US0006M Index',
    'ZAR.3M': 'JIBA3M Index',
}


class MarketData():
    def __init__(self, dateString):
        self.dt = ql.Date(dateString, "%d-%m-%Y")
        ql.Settings.instance().evaluationDate = self.dt
        date = self.dt.ISO().replace('-', '')
        self.data = pd.read_csv(f"quotes/{date}.csv").set_index('quote')

    def getQuote(self, quote, shift=0):
        try:
            val = (self.data.loc[quote].item() + shift) / 100
        except:
            print(quote)
        else:
            if val:
                return val
            else:
                print(f"{quote} has no value!")


class CurveBuilder():
    def __init__(self, args, date, shift=0, curveDayCounter=ql.ActualActual()):
        self.marketData = MarketData(date)
        self.configurations = args['CONFIGURATIONS']
        self.calendar = self.convObj(self.configurations['CALENDAR'])
        self.instruments = args['INSTRUMENTS']
        self.shift = shift
        self.helpers = ql.RateHelperVector()
        self.makeHelpers()
        '''
        self.curve = ql.PiecewiseLogCubicDiscount(
            ql.Settings.instance().evaluationDate, self.helpers, curveDayCounter
        )
        self.curve = ql.PiecewiseLogLinearDiscount(
            ql.Settings.instance().evaluationDate, self.helpers, curveDayCounter
        )
        '''
        self.curve = ql.PiecewiseSplineCubicDiscount(
            ql.Settings.instance().evaluationDate, self.helpers, curveDayCounter
        )

        self.curve.enableExtrapolation()

    def convObj(self, string):
        return objects[string]

    def getPeriod(self, string):
        return string.split('.')[-1]

    def makeHelpers(self):
        for instrument, data in self.instruments.items():
            if 'DEPOSIT' in instrument:
                if 'INDEX' in data:
                    index = self.convObj(data['INDEX'])
                    for quote in data['QUOTES']:
                        value = self.marketData.getQuote(quote, self.shift)
                        self.helpers.append(
                            ql.DepositRateHelper(value, index)
                        )
                else:
                    dayCounter = self.convObj(data['DAYCOUNTER'])
                    convention = self.convObj(data['CONVENTION'])
                    fixingDays = data['FIXINGDAYS']
                    for quote in data['QUOTES']:
                        value = self.marketData.getQuote(quote, self.shift)
                        period = ql.Period(self.getPeriod(quote))
                        self.helpers.append(
                            ql.DepositRateHelper(
                                value, period, fixingDays, self.calendar,
                                convention, False, dayCounter
                            )
                        )
            if instrument == 'FRA':
                if 'INDEX' in data:
                    index = self.convObj(data['INDEX'])
                else:
                    raise Exception("Sorry, have to define index")
                for quote in data['QUOTES']:
                    value = self.marketData.getQuote(quote, self.shift)
                    period = ql.Period(self.getPeriod(quote))
                    self.helpers.append(
                        ql.FraRateHelper(value, period.length(), index)
                    )
            if instrument == 'IMMFRA':
                index = self.convObj(data['INDEX'])
                for quote in data['QUOTES']:
                    value = self.marketData.getQuote(quote, self.shift)
                    period = int(self.getPeriod(quote))
                    self.helpers.append(
                        ql.FraRateHelper(value, period, period+2, index)
                    )
            if instrument == 'FUTURE':
                if 'INDEX' in data:
                    index = self.convObj(data['INDEX'])
                else:
                    raise Exception("Sorry, have to define index")
                for quote in data['QUOTES']:
                    months = int(self.getPeriod(quote))
                    price = self.marketData.getQuote(quote) * 100
                    price -= self.shift
                    immDate = self.calendar.advance(
                        ql.Settings.instance().evaluationDate, 2, ql.Days)
                    for n in range(months):
                        immDate = ql.IMM().nextDate(immDate)
                    self.helpers.append(
                        ql.FuturesRateHelper(price, immDate, index)
                    )
            if 'SWAP' in instrument:
                fixedFrequency = self.convObj(data['FIXEDFREQUENCY'])
                fixedConvention = self.convObj(data['FIXEDCONVENTION'])
                fixedDayCounter = self.convObj(data['FIXEDDAYCOUNTER'])
                index = self.convObj(data['INDEX'])
                for quote in data['QUOTES']:
                    period = ql.Period(self.getPeriod(quote))
                    value = self.marketData.getQuote(quote, self.shift)
                    self.helpers.append(
                        ql.SwapRateHelper(
                            value, period, self.calendar, fixedFrequency,
                            fixedConvention, fixedDayCounter, index
                        )
                    )
            if 'BASIS' in instrument:
                fixedFrequency = self.convObj(data['FIXEDFREQUENCY'])
                fixedConvention = self.convObj(data['FIXEDCONVENTION'])
                fixedDayCounter = self.convObj(data['FIXEDDAYCOUNTER'])
                sign = data['BASISSIGN']
                index = self.convObj(data['INDEX'])
                for quote, spread in data['QUOTES']:
                    period = ql.Period(self.getPeriod(quote))
                    value = self.marketData.getQuote(quote, self.shift)
                    if isinstance(spread, list):
                        sprd = 0
                        for partial_spread in spread:
                            sprd += self.marketData.getQuote(
                                partial_spread) / 100
                        spread = sign * sprd
                    else:
                        if 'USD.BASIS3MOIS' in spread:
                            def sprd(swap, basis):
                                return 100*(100*(-swap+(((1.0 + ((1.0 + ((((1.0 + swap*(360.0/365.0)/2.0)**(2.0/4.0) - 1.0) * 4.0)-basis/100)/4.0)**4.0 - 1.0)/360.0)**90.0 - 1.0) * 4.0)))
                            spread = self.marketData.getQuote(spread)
                            spread = sprd(value, spread) / 10000
                        else:
                            spread = self.marketData.getQuote(spread) / 100

                        spread *= sign

                    spreadHandle = ql.QuoteHandle(ql.SimpleQuote(spread))
                    self.helpers.append(
                        ql.SwapRateHelper(
                            value, period, self.calendar, fixedFrequency,
                            fixedConvention, fixedDayCounter, index, spreadHandle
                        )
                    )
            if 'OIS' in instrument:
                fixedFrequency = self.convObj(data['FIXEDFREQUENCY'])
                fixedConvention = self.convObj(data['FIXEDCONVENTION'])
                fixedDayCounter = self.convObj(data['FIXEDDAYCOUNTER'])
                index = self.convObj(data['INDEX'])
                for quote in data['QUOTES']:
                    period = ql.Period(self.getPeriod(quote))
                    value = self.marketData.getQuote(quote)
                    quoteHandle = ql.QuoteHandle(ql.SimpleQuote(value))
                    self.helpers.append(
                        ql.OISRateHelper(2, period, quoteHandle,
                                         index, paymentFrequency=fixedFrequency)
                    )
