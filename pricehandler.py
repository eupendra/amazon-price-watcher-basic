import config
import requests
from bs4 import BeautifulSoup

def return_price(address):
    response = requests.get(address, headers=config.header_values)
    response_text = response.text
    soup = BeautifulSoup(response_text,'lxml')
    
    regular_price_element = soup.find("span",{"id":"priceblock_ourprice"})
    deal_price_element = soup.find("span",{"id":"priceblock_dealprice"})
    
    if deal_price_element is not None:
        price = deal_price_element.text
    elif regular_price_element is not None:
        price  = regular_price_element.text
    else:
        price = 0
    
    return price