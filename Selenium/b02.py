from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

kw = input("Your keyword: ")

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

e = driver.find_element(By.NAME, 'keyword')
e.send_keys(kw)

driver.find_element(By.CSS_SELECTOR, 'nav button[type=submit]').click()

driver.implicitly_wait(5000)

urls = []
cates = driver.find_elements(By.CSS_SELECTOR, '.navbar-nav li')[1:-3]
for c in cates:
    print(c.text)
    urls.append(c.find_element(By.TAG_NAME, 'a').get_attribute('href'))

print(urls)