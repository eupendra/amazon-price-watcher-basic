import datetime
import config
import csvhandler
import pricehandler as ph
import os
import mailhandler

price = ph.return_price(config.address)   
price_sony = ph.return_price(config.address_sony)

date_stamp = datetime.datetime.now().date()
time_stamp = datetime.datetime.now().time()

file_name = "price_list.csv"
abs_file_path = os.path.join(r'c:\learnPython', file_name)
row_to_write = [date_stamp, time_stamp, price, price_sony]

csvhandler.writetocsv(row_to_write, abs_file_path)

subject = "Price is " + price
body = f"The price of Bose QC35 on {date_stamp} is {price}"

mailhandler.sendmail(subject, body)


