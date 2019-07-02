from bs4 import BeautifulSoup
import requests
import config 
import csv
from datetime import datetime as d
def get_price(address):
    source = requests.get(address, headers=config.headers).text
    soup = BeautifulSoup(source, 'lxml')
    price = soup.find(
        "span", 
        {"id": "priceblock_ourprice"}
        ).text

    # print(f'The price of Bose QC35 is {price}')
    return price

# print(get_price(config.address))
def log_in_csv(data:list):
    file = open("price_history.csv","a") # will append
    writer= csv.writer(file)  
    writer.writerow(data)
    file.close 


price = get_price(config.address)
date_part = f"{d.now():%Y-%m-%d}"
time_part = f"{d.now():%H:%S}"

data = [date_part,time_part,price]

log_in_csv(data)

print('~'*50)
print('Done!')