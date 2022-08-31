# TEST CLASS
import MetaTrader5 as mt5
import matplotlib.pyplot as plt
from LiveRate import ForexMarket

currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CHF']  # , 'CAD', 'AuD', ]  # 'NZD']
fx = ForexMarket(currencies)
##
xt = fx.get_all_rates(time_shift=120 * 6, time_frame=mt5.TIMEFRAME_M1, start_from=0 )
x_symbol_df = xt['USDJPY_i']