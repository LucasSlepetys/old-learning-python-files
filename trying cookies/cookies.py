import requests
from bs4 import BeautifulSoup
import smtplib
from requests_html import HTMLSession
import json

session = requests.Session()

jar = requests.cookies.RequestsCookieJar()
jar.set('_session_id','')

session.cookies = jar

# r = session.get('https://fis.learning.powerschool.com/do/account/login')
r = session.get('https://fis.learning.powerschool.com/FIS/businesseconomics10-12johnson20-21/calendar')
with open("test_file.html", "w") as file:
        file.write(r.text)

#! -------------------------------------------------------------------

with open('test_file.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

class_name = soup.find(class_ = "event_title")
# print(class_name.get_text())

name = class_name
print(name.get_text())

# #!!!!!!!

# print("\n")

# class_name = soup.find(class_ = "eclass_12449555 eclass_filter")

# name = class_name.a
# print(name.get_text())

# #!!!!!!!!

# print("\n")

# class_name = soup.find(class_ = "eclass_12453933 eclass_filter")

# name = class_name.a
# print(name.get_text())



# print(r.iter_lines())
# for i in r.iter_lines():
#     with open("test_file.html", "w") as file:
#         file.write(i)