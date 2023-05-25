from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/lucasslepetys/Desktop/web scraping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://10ff.net/login")

name = driver.find_element_by_id("username")
name.clear()
name.send_keys("TheFlash")
name.send_keys(Keys.RETURN)

time.sleep(3)
go = ""
go = raw_input("-->")
print(go)
if go == "go":
    print("it's working")
    for i in range(1000):
        ("It worked again!")
        word = driver.find_element_by_class_name("highlight")
        word = word.text

        search = driver.find_element_by_xpath("//div[@class='interface']/input[1]")
        search.clear()
        search.send_keys(word)
        search.send_keys(Keys.SPACE)
time.sleep(3)
driver.quit()