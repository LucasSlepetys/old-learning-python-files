from bs4 import BeautifulSoup
import requests

with open('test_website.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#! Finding a text from the first element of the page:

# article = soup.find('div', class_ = 'article')
# # print(article)

# headline = article.h2.a.text
# print(headline)

# sumarry = article.p.text
# print(sumarry)

#! Finding texts from all the elements selected of the page:

for article in soup.find_all('div', class_ = 'article'):
    headline = article.h2.a.text
    print(headline)

    sumarry = article.p.text
    print(sumarry)