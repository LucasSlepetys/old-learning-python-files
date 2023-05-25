from bs4 import BeautifulSoup
import requests

#! Start the session
session = requests.Session()

#! Create the payload
payload = {'login':'.', 
          'password':''
         }

#! Post the payload to the site to log in
s = session.post("https://fis.learning.powerschool.com/do/account/login", data=payload)

#! Navigate to the next page and scrape the data
s = session.get('https://fis.learning.powerschool.com/u/roberto.slepetysferreira/portal')

soup = BeautifulSoup(s.text, 'html.parser')
print(soup.find('img')['src'])