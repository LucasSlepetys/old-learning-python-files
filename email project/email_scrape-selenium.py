from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Password from veracross and username
username = ""
password = ""

# initialize the Chrome driver
driver = webdriver.Chrome("./chromee")
loginUrl = ("https://accounts.veracross.eu/fis/portals/login/password")
gradeLevelOrder = ["First Steps", "Pre-Primary", "Primary", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"]

driver.get(loginUrl)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("recaptcha").click()

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div/div/a/div[1]").click()

all_grades = (driver.find_elements_by_class_name("DirectoryCard_FieldName"))

count = 0

with open('list_emails.txt', 'w') as f:
    f.write(" ")

for grade in all_grades:
    grade.click()
    next_btn = (driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/a"))
    while(len(next_btn) > 0):

        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/a").click()
        except:
            print(".")
        try:
            next_btn = (driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/a"))
        except:
            print("..")

    elements = (driver.find_elements_by_class_name("directory-Entry_FieldLink"))

    with open('list_emails.txt', 'a') as f:
        message = str("------ " + str(gradeLevelOrder[count]) + " ------")
        print(message)
        f.write(message)
        f.write('\n')

        for element in elements:
            f.write(element.text)
            f.write('\n')

    driver.execute_script("window.history.go(-1)")
    count += 1

    
    
driver.close()