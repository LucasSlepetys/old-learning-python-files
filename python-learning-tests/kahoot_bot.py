from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import random
import concurrent.futures


# list of stages:
global stages_list
stages_list = ["Pin entered...", "Name entered...", "Waiting for game to begin...", "Answer has been clicked!","Multiple choice has been clicked!" ,"Waiting for next question..."]


#* Setting basics settings for selenium:
global PATH
PATH = "/Users/lucasslepetys/Desktop/virtualEnv/chromeDrive"

#* Pin Input
global PIN_GAME
PIN_GAME = input("Enter PIN_GAME: ")

def input_name(id, input, stage):
    input_name = driver.find_element_by_id(id)
    input_name.clear()
    input_name.send_keys(input)
    input_name.send_keys(Keys.RETURN)
    print(stages_list[stage])

def click_answer(xpath_ans,xpath_button, stage):
    answer_field = driver.find_element_by_xpath(xpath_ans)
    answer_field.click()
    try:
        button_mult_question = driver.find_element_by_xpath(xpath_button)
        button_mult_question.click()
        print(stages_list[stage + 1])
    except NoSuchElementException:
        print(stages_list[stage])

def bot(name, driver):
    # Continue loop
    continuing = True
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # driver = webdriver.Chrome(PATH, options=option)
    
    

    driver.get("https://kahoot.it")

    time.sleep(0.5)
    input_name("game-input", PIN_GAME, 0)
    time.sleep(2)
    input_name("nickname", name, 1)

    # wait until it is found ("https://kahoot.it/v2/gameblock")
    print(stages_list[2])
    while continuing:
        try:
            print("goingggg")
            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/main/div[2]/div/div/button[1]')))
            click_answer('//*[@id="root"]/div[1]/main/div[2]/div/div/button[1]','//*[@id="root"]/div[1]/main/div[2]/div/div[3]/button', 3)
            
        except TimeoutException:
            print ("Loading took too much time!")
            continuing = False

        print(stages_list[5] + "\n")

with concurrent.futures.ThreadPoolExecutor() as executor:

    # list of names:
    names_list = ["Uhm", "Uhm", "Uhm", "Uhm"]

    driver = webdriver.Chrome(PATH)
    # driver2 = webdriver.Chrome(PATH)

    driver_list = [driver, driver]
    

    results = [executor.submit(bot, "Uhm", driver_list[i]) for i in range(1)]

    for f in concurrent.futures.as_completed(results):
        print("Completed")





    
