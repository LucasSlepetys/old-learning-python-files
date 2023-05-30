from email import header
import requests
from bs4 import BeautifulSoup

loginUrl = ("https://accounts.veracross.eu/fis/portals/login/password")
middleUrl = ("https://portals.veracross.eu/fis/session")
secureUrl = ("https://portals.veracross.eu/fis/home")



login_payload = { 
    "utf8": '✓',
    "authenticity_token": None,
    'username': "Jinpil_Lee@fis.edu",
    # 'username': "lucas_slepetys@fis.edu",
    "password": None,
    "commit" : "Log In"
}

middle_payload = {
    "authenticity_token": None,
    "account": None
}


def request_pass_veracross(current_password):
    with requests.session() as s:
        page = s.get(loginUrl)
        soup = BeautifulSoup(page.text, "lxml")

        login_payload["password"] = current_password

        try:
            login_payload["authenticity_token"] = soup.find_all(["form", "input"])[2].get("value")
        except:
            print("error")
            return "error"
            
        r_middle = s.post(loginUrl, data=login_payload)
    
        # print("middle response: ", r_middle)

        soupMiddle = BeautifulSoup(r_middle.text, "lxml")

        try:
            middle_payload["authenticity_token"] = soupMiddle.find_all(["form", "input"])[2].get("value")
            middle_payload["account"] = soupMiddle.find_all(["form", "input"])[3].get("value")
        except:
            print("error")
            return "error"

        r_final = s.post(middleUrl, data=middle_payload)
        return r_final


