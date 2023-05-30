from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import random
import threading
import concurrent.futures

start = time.perf_counter()


PATH = "/Users/lucasslepetys/Desktop/virtualEnv/chromeDrive"


def open_chrome():
    driver = webdriver.Chrome(PATH)
    driver.get("https://kahoot.it")
    time.sleep(1)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/div/button[1]')))
        
    except TimeoutException:
        print ("Loading took too much time!")


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(open_chrome) for _ in range(3)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')


