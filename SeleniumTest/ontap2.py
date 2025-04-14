import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

urls = []
names = []
cates = driver.find_elements(By.CSS_SELECTOR, '.navbar-nav li')[1:-3]
for c in cates:
    # print(c.text)
    names.append(c.text)
    urls.append(c.find_element(By.TAG_NAME, 'a').get_attribute('href'))

for n, u in zip(names, urls):
    print("========")
    print(n)
    driver.get(u)

    time.sleep(1)
    product = driver.find_elements(By.CLASS_NAME, 'card')
    for p in product:
        try:
            title = p.find_element(By.CLASS_NAME, 'card-title')
            price = p.find_element(By.CLASS_NAME, 'card-text')
            img = p.find_element(By.TAG_NAME, 'img')
        except:
            pass
        else:
            print(title.text)
            print(price.text)
            print(img.get_attribute('src'))

driver.quit()