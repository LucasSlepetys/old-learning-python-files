import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://en.wikipedia.org/wiki/Parkour'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html5lib')

match = soup.find(class_ ="infobox")
match = match.get_text()
print(match)