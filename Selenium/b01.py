#https://dhthanhit.pythonanywhere.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

kw = input("Your keyword: ")

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

e = driver.find_element(By.NAME, 'keyword')
e.send_keys(kw)

driver.find_element(By.CSS_SELECTOR, 'nav button[type=submit]').click()

driver.implicitly_wait(5000)

print(driver.title)

import time
time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, 'card')
for c in products:
    try:
        title = c.find_element(By.CLASS_NAME, 'card-title')
        price = c.find_element(By.CLASS_NAME, 'card-text')
        img = c.find_element(By.CLASS_NAME, 'card-img-top')
    except:
        pass
    else:
        print(title.text)
        print(price.text)
        print(img.get_attribute('src'))

urls = []
cates = driver.find_elements(By.CSS_SELECTOR, '.navbar-nav li')[1:-3]
for c in cates:
    print(c.text)
    urls.append(c.find_element(By.TAG_NAME, 'a').get_attribute('href'))

print(urls)

driver.quit()