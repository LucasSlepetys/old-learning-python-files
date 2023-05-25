from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/lucasslepetys/Desktop/web scraping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://10fastfingers.com/typing-test/english")

go = input("--->")
time.sleep(3)
if go == "go":
    for i in range(1000):
        word = driver.find_element_by_class_name("highlight")
        word = word.text

        search = driver.find_element_by_id("inputfield")
        search.clear()
        search.send_keys(word)
        search.send_keys(Keys.SPACE)
time.sleep(5)
driver.quit()



