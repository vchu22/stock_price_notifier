import time
from yahoo_fin import stock_info
from notifier import os_notify

stock=input("Enter the stock name: ")
purchased_price=float(input("Enter the the price you purchased at: "))
higher_perc=float(input("Enter the percentage increase to watch for: "))
lower_perc=float(input("Enter the percentage decrease to watch for: "))

while True:
    curr_price=stock_info.get_live_price(stock)
    print(f"Current price of {stock} is at {curr_price}")
    print("purchased_price threshold: ", (purchased_price * (higher_perc + 100) / 100))
    if (purchased_price * (higher_perc + 100) / 100) <= curr_price:
        os_notify(f"{stock.upper()} increased to {curr_price}, sell the stock to get a profit")
    elif curr_price <= (purchased_price * (100-lower_perc) /100):
        os_notify(f"{stock.upper()} decreased to {curr_price}, sell the stock to prevent loss")
    time.sleep(30)
