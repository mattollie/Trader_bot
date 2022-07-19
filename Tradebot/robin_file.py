import robin_stocks as rs
import pandas as pd


def login():
    rs.login("*** "***")


def getprofile():
    stock = rs.get_all_option_positions()

    print('Profile:')
    for each in range(len(stock)):
        for key,val in stock[each].items():
            print(key, ':', val)
        print('-'*10)


def main():
    login()
    getprofile()

if __name__ == '__main__':
    main()
