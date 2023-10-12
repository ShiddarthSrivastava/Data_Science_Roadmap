import math
import statistics as st
stocks={
'info':[600,630,620],
"ril"	:[1430,1490,1567],
"mtl"	:[234,180,160]}

def print_stocks():
    for i in stocks:
        avg=round(st.mean(stocks[i]),2)
        print(i+"==>"+str(stocks[i])+" avg==> "+str(avg))



def add_stocks():
    stock_name=input("Please enter the Stock name")
    stock_price= input("Please enter the Stock Price")
    stock_price=int(stock_price)
    if stock_name.lower() in stocks:
        stocks[stock_name].append(stock_price)
        print_stocks()
    else:
        stocks[stock_name]=[stock_price]
        print_stocks()

def main():
    user_input=input("Do you want to print or add a new stock in the database?\n")
    if user_input.lower()=="print":
        print_stocks()
    elif user_input.lower()=='add':
        add_stocks()
    else:
        print("Please type add or print to continue.:)")

if __name__=='__main__':
    while(1):
        main()