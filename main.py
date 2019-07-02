from bs4 import BeautifulSoup
import requests
import config 
source = requests.get(configaddress, headers=config.headers).text
soup = BeautifulSoup(source, 'lxml')
price = soup.find(
    "span", 
    {"id": "priceblock_ourprice"}
    ).text
print(f'The price is {price}')