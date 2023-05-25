from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/lucasslepetys/Desktop/web scraping/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/arquivos-para-download/")

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='collapse']/div/div/div[1]/div[2]/p[2]/a[1]"))
    )
    print("Found it!")
finally:
    driver.quit()

