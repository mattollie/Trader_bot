# Returns analytics
from alpha_vantage.techindicators import TechIndicators as tech
from alpha_vantage.timeseries import TimeSeries as timeseries
from Tradebot import WallStreetBets_Scraper as wsb
import easygui
import time
import pandas as pd
from Tradebot import trade_notifier
from findiff import FinDiff
import numpy as np
import csv


def gettickers():
    while True:
        choice = input("Manually enter tickers or take from WallStreetBets? - m or w")
        if choice == "m":
            fieldValues = input("Enter Ticker Names Separated By Commas")
            fieldValueList = fieldValues.split(",")
            return fieldValueList
        elif choice == "w":
            ticks = wsb.main()
            return ticks
        else:
            print("Please try again")
            continue


def get_daily(api_key, ticks):
    onetick = ticks[0]
    twotick = ticks[1]
    threetick = ticks[2]
    fourtick = ticks[3]
    fivetick = ticks[4]
    ts = timeseries(key=api_key, output_format='pandas')
    print('Getting Daily Stock Data for ' + onetick)
    data_elev, meta_data_elev = ts.get_daily(symbol=onetick, outputsize='full')
    print('Daily for ' + onetick + ':')
    print(data_elev)
    df = pd.DataFrame(data_elev)
    df.iloc[0:30].to_csv(r'/Users/Lakefork15/Desktop/stockprices.csv')
    return data_elev


def trend_lines(dailyData, isMin):
    dx = 1  # 1 day interval
    d_dx = FinDiff(0, dx, 1)
    d2_dx2 = FinDiff(0, dx, 2)
    clarr = np.asarray(dailyData)
    mom = d_dx(clarr)
    momacc = d2_dx2(clarr)
    print(mom)
    print("hi")
    print(momacc)
    np.fft



def get_Tech_Indicators(api_key, ticks):
    onetick = ticks[0]
    twotick = ticks[1]
    threetick = ticks[2]
    fourtick = ticks[3]
    fivetick = ticks[4]
    ti = tech(key=api_key, output_format='pandas')
    # print('Getting HT Trendline for ' + onetick)
    # data_twelve, meta_data_twelve = ti.get_ht_trendline(symbol=onetick, interval='daily', series_type='close')
    # print('HT Trendline for ' + onetick)
    # print(data_twelve)
    # df = pandas.DataFrame(data_twelve)
    # df.to_csv(r'/Users/Lakefork15/Desktop/htline.csv')



    # DO NOT DELETE NEXT 3 LINES - 1ST TWO EXPORT DAILY VALUES TO CSV FILE AND 3RD LINE SENDS EMAIL NOTIFICATION

    #MIGHT WANT TO HAVE NEXT LINE JUST BEFORE PROGRAM EXECUTES BUY/SELL
    # trade_notifier.main(onetick)





    # print('Getting SMA for ' + onetick)
    # data_one, meta_data_one= ti.get_sma(symbol=onetick, interval='15min', time_period='60', series_type='close')
    # print('Getting SMA for ' + twotick)
    # data_two, meta_data_two = ti.get_sma(symbol=twotick, interval='15min', time_period='60', series_type='close')
    # print('Getting SMA for ' + threetick)
    # data_three, meta_data_three = ti.get_sma(symbol=threetick, interval='15min', time_period='60', series_type='close')
    # print('Getting SMA for ' + fourtick)
    # data_four, meta_data_four = ti.get_sma(symbol=fourtick, interval='15min', time_period='60', series_type='close')
    # print('Getting SMA for ' + fivetick)
    # data_five, meta_data_five = ti.get_sma(symbol=fivetick, interval='15min', time_period='60', series_type='close')
    # print('SMA for ' + onetick + ':')
    # print(data_one)
    # print('SMA for ' + twotick + ':')
    # print(data_two)
    # print('SMA for ' + threetick + ':')
    # print(data_three)
    # print('SMA for ' + fourtick + ':')
    # print(data_four)
    # print('SMA for ' + fivetick + ':')
    # print(data_five)
    # time.sleep(60)
    # print('Getting EMA for ' + onetick)
    # data_six, meta_data_six = ti.get_ema(symbol=onetick, interval='15min', time_period='60', series_type='close')
    # print('Getting EMA for ' + twotick)
    # data_seven, meta_data_seven = ti.get_ema(symbol=twotick, interval='15min', time_period='60', series_type='close')
    # print('Getting EMA for ' + threetick)
    # data_eight, meta_data_eight = ti.get_ema(symbol=threetick, interval='15min', time_period='60', series_type='close')
    # print('Getting EMA for ' + fourtick)
    # data_nine, meta_data_nine = ti.get_ema(symbol=fourtick, interval='15min', time_period='60', series_type='close')
    # print('Getting EMA for ' + fivetick)
    # data_ten, meta_data_ten = ti.get_ema(symbol=fivetick, interval='15min', time_period='60', series_type='close')
    # print('EMA for ' + onetick + ':')
    # print(data_six)
    # print('EMA for ' + twotick + ':')
    # print(data_seven)
    # print('EMA for ' + threetick + ':')
    # print(data_eight)
    # print('EMA for ' + fourtick + ':')
    # print(data_nine)
    # print('EMA for ' + fivetick + ':')
    # print(data_ten)


def get_resistance_line(api_key, ticks):
    # This should be able to draw the resistance lines
    # Might have to include helper functions
    return


def get_support_line(api_key, ticks):
   # This should be able to draw the support lines
   return



def main():
    api_key = '***'
    top5_tickers = gettickers()
    daily_Data = get_daily(api_key, top5_tickers)
    minimaIdxs, maximaIdxs = trend_lines(True)
    #trend_lines(daily_Data)
   # get_Tech_Indicators(api_key, top5_tickers)


if __name__ == '__main__':
    main()
