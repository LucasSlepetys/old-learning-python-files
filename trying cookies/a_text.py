import requests
from bs4 import BeautifulSoup
import smtplib
from requests_html import HTMLSession
import json

session = requests.Session()
session.headers.update({'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320"})
mydata = json.dumps({'login': '.','password': ''})
response = session.post('https://fis.learning.powerschool.com/do/account/login',data=mydata)
session.get('https://fis.learning.powerschool.com/u/roberto.slepetysferreira/portal')
session.post('https://fis.learning.powerschool.com/u/roberto.slepetysferreira/portal')

with open('cookies.json', 'w') as f:
    json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
with open('cookies.json', 'r') as f:
    session.cookies = requests.utils.cookiejar_from_dict(json.load(f))
    _session_id = (session.cookies['_session_id'])


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

r = session.get('https://fis.learning.powerschool.com/u/roberto.slepetysferreira/portal')

#*******************************************************************#
    #! creating and writing the html page in a .text file !#
#*******************************************************************#

with open("test_file.html", "w") as file:
    file.write(r.text)

#*******************************************************************#
    #! opening and reading the html page from the .text file !#
            #! by using the mudule "BeautifulSoup" !#
#*******************************************************************#

# with open('test_file.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

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

