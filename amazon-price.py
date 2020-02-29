# Webscraping on Amazon.com - Track Amazon Prices
import requests
from bs4 import BeautifulSoup
import smtplib
import time 

# Insert URL that you would like to check on Amazon
URL = "https://www.amazon.com/BenQ-Response-Equalizer-Adjustable-XL2546/dp/B06XT6XQ6V/ref=pd_sbs_147_2/130-7703647-3877737?_encoding=UTF8&pd_rd_i=B06XT6XQ6V&pd_rd_r=dff86c53-1768-41f8-867e-b8b4ef1f7525&pd_rd_w=fq8zi&pd_rd_wg=aCBLs&pf_rd_p=5873ae95-9063-4a23-9b7e-eafa738c2269&pf_rd_r=3164PG4ZY538D01XBMCR&psc=1&refRID=3164PG4ZY538D01XBMCR"

# User-Agent, this depends on your main web browser
headers = {"User-Agent": 'Chrome/78.0.3904.108'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    # Insert a price you want to check
    if(converted_price < 450):
        send_mail()
    
    if(converted_price > 450):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Your email and password. For gmail you can use App password to create a new one
    server.login('@gmail.com', 'temp pass by google')

    # Add URL or else as you want to see in your email
    subject = 'Price has dropped!!'
    body = 'Check the Amazon link - https://www.amazon.com/BenQ-Response-Equalizer-Adjustable-XL2546/dp/B06XT6XQ6V/ref=pd_sbs_147_2/130-7703647-3877737?_encoding=UTF8&pd_rd_i=B06XT6XQ6V&pd_rd_r=dff86c53-1768-41f8-867e-b8b4ef1f7525&pd_rd_w=fq8zi&pd_rd_wg=aCBLs&pf_rd_p=5873ae95-9063-4a23-9b7e-eafa738c2269&pf_rd_r=3164PG4ZY538D01XBMCR&psc=1&refRID=3164PG4ZY538D01XBMCR'

    msg = f"Subject: {subject}\n\n{body}"

    # Send email first, to email second
    server.sendmail(
        '@gmail.com',
        'to email address',
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()

#For time.sleep (comment for now)
#while(True):
#   check_price()
#   time.sleep(60*60)
