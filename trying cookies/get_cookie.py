import requests 
from bs4 import BeautifulSoup
# from requests import Session
# from bs4 import BeautifulSoup as bs

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'
}

login_data = {
    "login": "",
    "password": ""
}

with requests.Session() as s:
    url = ("https://fis.learning.powerschool.com/u/roberto.slepetysferreira/portal")
    r = s.get(url, headers=headers)    

    r = s.post(url, data=login_data, headers=headers)
    print(r.content)




# with Session() as s:
#     site = s.get("https://fis.learning.powerschool.com/do/account/login")
#     # print(site.content)

#     bs_content = bs(site.content, "html.parser")


#     login_data = {"login":"roberto.slepetysferreira","password":"Lucas2017!"}
#     s.post("https://fis.learning.powerschool.com/do/account/login",login_data)


#     home_page = s.get("https://fis.learning.powerschool.com/do/account/login")
#     print(home_page.content)