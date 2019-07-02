from bs4 import BeautifulSoup
import requests
import request_headers as h
address = 'https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B0756CYWWD/ref=sr_1_3?crid=24411Z9VDNZZN&keywords=bose+qc35+ii&qid=1562061017&s=gateway&sprefix=bose+qc%2Caps%2C377&sr=8-3'
source = requests.get(address, headers=h.headers).text
soup = BeautifulSoup(source, 'lxml')
price = soup.find(
    "span", 
    {"id": "priceblock_ourprice"}
    ).text
print(f'The price is {price}')