#!/usr/bin/python
'''
# Cameron Merrick
# SALT Lending
# 3.6.2018
# py-coin-pricer.py
# Tool used to interact with coinmarketcap's API for r/t pricing data

'''
# Import modules needed
import requests
import json

# Define API URLs
tickerURL = 'http://api.coinmarketcap.com/v1/ticker/'
globalURL = 'http://api.coinmarketcap.com/v1/global/'

# Make REST API calls using python-requests module
r1 = requests.get(globalURL)
r1_data = r1.json()
global_market_cap = r1_data["total_market_cap_usd"]


# Define the function to make the API call for a specific coin
def userDefinedCoinCheck(choice):
    tickerapi = ((tickerURL) + (choice) + "/")
    # Account for the 'all' condition
    if choice == "all":
        req1 = requests.get(tickerURL)
        reqdata = req1.json()
        for x in reqdata:
            ticker = x["symbol"]
            price = x["price_usd"]
            print(str(ticker) + ":\t\t$" + str(price))
            print()
        return
    r2 = requests.get(tickerapi)
    r2_data = r2.json()
    symb = r2_data[0]["symbol"]
    price = r2_data[0]["price_usd"]
    print(str(symb) + " : $" + str(price))
    # print((str(symb)) + " : $ " + str(pric))
    return


# Define main()
def main():
    print()
    print("Welcome to the py-coin-pricer tool")
    print()
    print("Total & combined value (market cap) of all coins:\n")
    print("$ " + str(global_market_cap) + "\n")
    print("Want the price of a specific coin?")
    choice = input("Enter coin name: ")
    userDefinedCoinCheck(choice)


if __name__ == '__main__':
    main()
