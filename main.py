import time
from yahoo_fin import stock_info
from notifier import os_notify

stock=input("Enter the stock name: ")
purchased_price=float(input("Enter the the price you purchased at: "))
profit_perc=float(input("Enter the percentage increase to watch for: "))
loss_perc=float(input("Enter the percentage decrease to watch for: "))
state = "neutral"

while True:
    curr_price=stock_info.get_live_price(stock)
    print(f"Current price of {stock} is at {curr_price}")
    print("purchased_price threshold: ", (purchased_price * (profit_perc + 100) / 100))
    if state != "profit" and (purchased_price * (profit_perc + 100) / 100) <= curr_price:
        state = "profit"
        os_notify(f"{stock.upper()} increased to {curr_price}, sell the stock to get a profit")
    elif state != "loss" and curr_price <= (purchased_price * (100-loss_perc) /100):
        state = "loss"
        os_notify(f"{stock.upper()} decreased to {curr_price}, sell the stock to prevent loss")
    if (state == "profit" and curr_price < (purchased_price * (profit_perc + 100) / 100))\
            or (state == "loss" and (purchased_price * (100-loss_perc) /100) < curr_price):
        state = "neutral"
        os_notify(f"{stock.upper()} price fell back to neutral at {curr_price}")
    time.sleep(30)
