import requests
from bs4 import BeautifulSoup
import smtplib

#*--------------------------------------------------------------------------------------*#
#! Function to get articles name, what it is related to and link for article from first 5 articles 
#*--------------------------------------------------------------------------------------*#


def new_news():
    global articles
    global related
    global links
    URL = 'https://www.economist.com'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html5lib')

    articles = []
    for artc in soup.find_all(class_ = "headline-link"):
        text = artc.get_text()
        articles.append(text)
        
    related = []
    for rel in soup.find_all(class_ = "section-fly"):
        text = rel.get_text()
        related.append(text)

    links = []
    for lin in soup.find_all("a", class_ = "headline-link"):
        text = lin.attrs.get("href")
        links.append("https://www.economist.com" + text)

#*--------------------------------------------------------------------------------------*#
#! Funtion that takes links, open them and first first paragraph of each of the 5 pages and gets first 300 characters from it
#*--------------------------------------------------------------------------------------*#
def first_paragraph():
    global final_intro_text
    ending = "..." + "(Click on the link to continue reading it) ---->"

    x = 0
    final_intro_text = []
    while x < 5:
        intro_text = ""
        URL = links[x]

        headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.320'}
        try:
            page = requests.get(URL, headers=headers)
        except requests.exceptions.ConnectionError:
            return

        soup = BeautifulSoup(page.content, 'html5lib')

        text = soup.find(class_ = "article__body-text")
        text = text.get_text()
        intro_text = text

        final_text = intro_text
        final_text = (final_text[0:300] + ending)
        final_intro_text.append(final_text)

        final_text = ""
        URL = ""
        page = ""
        soup = ""
        text = ""
        x += 1

#*--------------------------------------------------------------------------------------*#
#! Function to write the information in a clear way (more organized)
#*--------------------------------------------------------------------------------------*#

def print_message():
    global save
    x = 0
    save = ""

    if len(final_intro_text) == 5:
            number = 5
    elif len(final_intro_text) == 4:
        number = 4
    else:
        number = 3

    while x < number:
        # print("Name of the article: " + articles[x])
        # print("Related to: " + related[x])
        # print("A brief text from the new: " + "\n" + final_intro_text[x] + " " + links[x])
        # print("\n" + "\n")
        # x += 1
        save += ("Name of the article: " + articles[x] + "\n")
        save += ("Related to: " + related[x] + "\n")
        try:
            save += ("A brief text from the news: " + "\n" + final_intro_text[x] + " " + links[x])
        except requests.exceptions.ConnectionError:
            return
        save += ("\n" + "\n" + "\n" + "-------------------------------------------------------------------------------------------------------------------------------------------" + "\n")
        x += 1
        

#*--------------------------------------------------------------------------------------*#
#! Function that sends me the email with the information taken from all 5 articles
#*--------------------------------------------------------------------------------------*#

# def send_email():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

#     server.login('lucas.slepetyss@gmail.com', #Password goes here!)

#     subject = 'News! The Economist' 
#     text = str(save)   
#     body = save

#     FROM = 'lucas.slepetyss@gmail.com'
#     TO = 'lucas.slepetys@hotmail.com'
#     MSG = f"Subject: {subject}\n\n{body}".encode('utf-8')

#     server.sendmail(FROM, TO, MSG)

#     print('HEY EMAIL HAS BEEN SEND')

#     server.quit()
#*--------------------------------------------------------------------------------------*#
#! Run all function in order:
#*--------------------------------------------------------------------------------------*#
new_news()
first_paragraph()
print_message()
# ! This is commented:
#* send_email()
# ! Print the information taken
print(save)
