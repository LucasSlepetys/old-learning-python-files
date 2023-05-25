import webbrowser
import requests
from bs4 import BeautifulSoup as bs

#! Start the session
session = requests.Session()

#! Create the payload
payload = {
    'client_id': "gNkK5XuPZRmMdwzTb8lum4Wc5Z35lZba",
    'connection': "Drupal",
    'password': "",
    'redirect_uri': "https://www.economist.com/api/login-callback?state=state-12c9db91f6e9b7a27d45353b292d81ec",
    'response_type': "code",
    'scope': "openid",
    'state': "g6Fo2SBZTHVHcmhhd2FsTFhZaW1XOHZCVFFna25VNzZGRTRmaKN0aWTZIDNPelF2OGk2WmlKT0RrcllJcHZqYVFGMnliem9JUk5Xo2NpZNkgZ05rSzVYdVBaUm1NZHd6VGI4bHVtNFdjNVozNWxaYmE",
    'tenant': "theeconomist",
    'username': "",
    '_csrf': "sWf6xqq7-TA1ONd7Je9iTDquxEC0f-i0pdSI",
    '_intstate': "deprecated"
}

#! Post the payload to the site to log in
s = session.post("https://authenticate.economist.com/login?state=g6Fo2SAwWXZKRjltZVlVdmJSRGROb0dMNXo1VlQ2QTlNMjVxN6N0aWTZIFN0eGVPbWdKOWllejY4QVdUWk9SNTJRQUpDNWMyNGlxo2NpZNkgZ05rSzVYdVBaUm1NZHd6VGI4bHVtNFdjNVozNWxaYmE&client=gNkK5XuPZRmMdwzTb8lum4Wc5Z35lZba&protocol=oauth2&response_type=code&scope=openid&additional_parameters=eyJyb3V0ZSI6ImxvZ2luIn0%3D&redirect_uri=https%3A%2F%2Fwww.economist.com%2Fapi%2Flogin-callback%3Fstate%3Dstate-3cccf16d641363cef5794d4183883e6e", data=payload)

#! Navigate to the next page and scrape the data
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

s = session.get('https://www.economist.com', headers=headers)

soup = bs(s.text, 'html5lib')
soup = str(soup)

with open("test_file.html", "w") as file:
    file.write(soup)

with open('test_file.html') as html_file:
    soup = bs(html_file, 'lxml')


text = soup.find(class_ = "ds-masthead-nav-beta__item ds-masthead-nav-beta__item--log-in")
print(text)