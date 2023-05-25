import requests
from bs4 import BeautifulSoup
import smtplib
from requests_html import HTMLSession
import json

session = requests.Session()
print(session.cookies.get_dict())

response = session.get('https://fis.learning.powerschool.com/FIS/businesseconomics10-12johnson20-21/calendar')
dic = session.cookies.get_dict()
_session_id = dic['_session_id']


#*******************************************************************#
    #! starting a session with the requests module !#
#! A session is a way of getting and sedding cookies from a server !#
#*******************************************************************#

session = requests.Session()

jar = requests.cookies.RequestsCookieJar()

#*******************************************************************#
            #! adding the cookie taken from powerschool !#
                #! after loggin in to the session !#
#*******************************************************************#

jar.set('_session_id', _session_id)

session.cookies = jar

#*******************************************************************#
#! passing the url of the website + session (cokkies from the website) !#
                                #! + !#  
            #! Receveing the html elements from the website !#
#*******************************************************************#

r = session.get('https://fis.learning.powerschool.com/FIS/businesseconomics10-12johnson20-21/calendar')

#*******************************************************************#
    #! creating and writing the html page in a .text file !#
#*******************************************************************#

with open("test_file.html", "w") as file:
    file.write(r.text)

#*******************************************************************#
    #! opening and reading the html page from the .text file !#
            #! by using the mudule "BeautifulSoup" !#
#*******************************************************************#

with open('test_file.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#*******************************************************************#
    #! Finding the id: "header-body" on the html page !#
                         #! + !#  
                #! Finding a h1 from this id !#
                        #! + !#  
            #! printing only the text from the h1 !#
#*******************************************************************#

# class_name = soup.find(id = "header-body")

# name = class_name.h1
# print(name.get_text())

#*******************************************************************#
    #! Same thing again but instead of an id, i'm using a class now !#
    #! then I am finding a link on this class and printing its text !#
#*******************************************************************#

# print("\n")

# class_name = soup.find(class_ = "eclass_12449555 eclass_filter")

# name = class_name.a
# print(name.get_text())

#*******************************************************************#
    #! Same thing here, but now I am using a different class !#
#*******************************************************************#

# print("\n")

# class_name = soup.find(class_ = "event_title")

# name = class_name
# print(name.get_text())

