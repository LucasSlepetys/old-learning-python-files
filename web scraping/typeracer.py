from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/lucasslepetys/Desktop/web scraping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://play.typeracer.com")



run = "true"
breaking = False
def fast_type(go):
    global breaking
    send = driver.find_element_by_class_name("txtInput")
    
    words = []
    listing = driver.find_element_by_class_name("gameStatusLabel")
    listing = listing.text

    print(listing)
    for i in listing:
        i.append(words)

    print(words)

while run == "true":
    go = ""
    go = input("-->")
    print(go)
    if go == "go":
        fast_type(go)
        go = ""
    else:
        time.sleep(3)
        run = False
        driver.quit()