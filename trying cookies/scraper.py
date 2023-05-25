import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/GoPro-CHDHX-901-RW-HERO9-Black/dp/B08G2HBBB6/ref=sr_1_3?__mk_de_DE=ÅMÅŽÕÑ&dchild=1&keywords=gopro+hero+9&qid=1605383141&quartzVehicle=93-291&replacementKeywords=gopro+hero&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

def check_price():
    global converted_price
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    price = soup.find(id="price_inside_buybox")
    price = price.get_text()
    converted_price = float(price[0:4])

    print(converted_price)

    if (converted_price > 400):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lucas.slepetyss@gmail.com', '')

    final_price = 500 - converted_price

    subject = 'Price fell down!'    
    body = 'Price fell down by: ' + str(round(final_price)) + "€" + "<-----" "\n" + "\n" + 'Click here to check the amazon link: https://www.amazon.de/GoPro-CHDHX-901-RW-HERO9-Black/dp/B08G2HBBB6/ref=sr_1_3?__mk_de_DE=ÅMÅŽÕÑ&dchild=1&keywords=gopro+hero+9&qid=1605383141&quartzVehicle=93-291&replacementKeywords=gopro+hero&sr=8-3'

    FROM = 'lucas.slepetyss@gmail.com'
    TO = 'lucas.slepetys@hotmail.com'
    MSG = f"Subject: {subject}\n\n{body}".encode('utf-8')

    server.sendmail(FROM, TO, MSG)

    print('HEY EMAIL HAS BEEN SEND')

    server.quit()


check_price()