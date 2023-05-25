from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/lucasslepetys/Desktop/web scraping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://10ff.net/login")

name = driver.find_element_by_id("username")
name.clear()
name.send_keys("Am I a Bot?")
name.send_keys(Keys.RETURN)
run = "true"
breaking = False
def fast_type(go):
    global breaking
    if go == "go":
        breaking = False
        print("it's working")
        for i in range(1000):
            ("It worked again!")
            try:
                word = driver.find_element_by_class_name("highlight")
            except Exception:
                print("Error!")
                breaking = True
            if breaking == False:
                word = word.text
                
                search = driver.find_element_by_xpath("//div[@class='interface']/input[1]")
                search.clear()
                search.send_keys(word)
                search.send_keys(Keys.SPACE)

            else:
                break

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