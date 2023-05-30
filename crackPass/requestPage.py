import requests
from bs4 import BeautifulSoup


canvasUrl = ("https://fis.instructure.com/login/ldap")

login_payload = { 
    "utf8": '✓',
    "authenticity_token": None,
    "redirect_to_ssl": 1,
    'pseudonym_session[unique_id]': "lucas_slepetys@fis.edu",
    "pseudonym_session[password]": None,
    "pseudonym_session[remember_me]": 0
}


def request_page(current_password):
    with requests.session() as s:
        page = s.get(canvasUrl)

        soup = BeautifulSoup(page.text, "lxml")

        login_payload["pseudonym_session[password]"] = current_password
        login_payload["authenticity_token"] = soup.find_all(["form", "input"])[2].get("value")

        r = s.post(canvasUrl, data=login_payload)

        return r

