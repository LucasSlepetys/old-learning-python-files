from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/lucasslepetys/Desktop/virtualEnv/chromeDrive"
driver = webdriver.Chrome(PATH)
driver.get("https://accounts.veracross.eu/fis/portals/login")

time.sleep(2)
user = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

user.clear()
password.clear()

user.send_keys("lucas_slepetys@fis.edu") 
password.send_keys("lsls2207")

password.send_keys(Keys.RETURN)

time.sleep(3)

day = driver.find_elements_by_class_name("day")
print(len(day))
for i in day:
    date = i.find_element_by_class_name("day-header")
    try:
        letter_day = i.find_element_by_class_name("event-link")
    except Exception:
        print("Error!")
        letter_day = "Nothing here!"

    try:
        letter_day = letter_day.text
    except Exception:
        pass

    print(date.text + "--> " + letter_day)

driver.quit()



