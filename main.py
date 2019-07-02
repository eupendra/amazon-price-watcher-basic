from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1', # Do Not Track Request Header 
    'Connection' : 'close'
}
address='https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B0756CYWWD/ref=sr_1_3?crid=24411Z9VDNZZN&keywords=bose+qc35+ii&qid=1562061017&s=gateway&sprefix=bose+qc%2Caps%2C377&sr=8-3'
source = requests.get(address, headers=headers).text
soup = BeautifulSoup(source,'lxml')
# print(soup.encode("utf-8"))
print(soup.find("span", {"id": "priceblock_ourprice"}).text)
# print(p)
# #priceblock_ourprice
