from flask import Flask,request
from bs4 import BeautifulSoup
import requests
application= Flask(__name__)
@application.route('/')
def home():
    return "Welcome to homepage"
@application.route('/review')
def review():
    try:
        url= 'https://www.flipkart.com/hp-ryzen-5-hexa-core-5500u-16-gb-512-gb-ssd-windows-11-home-15s-eq2182au-thin-light-laptop/p/itm09b322c037285?pid=COMGFRHGDB9G3Z9C&lid=LSTCOMGFRHGDB9G3Z9CBGKRA6&marketplace=FLIPKART&q=hp+laptop&store=6bo%2Fb5g&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=en_DsbkIaD3XlPlQWHKznNygIp2zxHNp6KnxeOvhMXx-m5j7DxYGjap12s3DbF15ngjOvzSrnEXVPy969ObdXoWAA%3D%3D&ppt=hp&ppn=homepage&ssid=la8jmtc1ao0000001691042439246&qH=9d1edd3d0f6d1b3c'
        response= requests.get(url)
        soup= BeautifulSoup(response.text, "lxml")
        reviews= soup.find_all('p', class_= "_2-N8zT")
        rev= [i.text for i in reviews]
        return " ".join(rev)
    except Exception as e:
        return str(e)
if __name__== "__main__":
    application.run(debug= True)

