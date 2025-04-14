from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

product = driver.find_elements(By.CLASS_NAME, 'card')
urls = []
for p in product:
    title = p.find_element(By.CLASS_NAME, 'card-title')
    print(title.text)
    urls.append(p.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary').get_attribute('href'))

for u in urls:
    print(u)

    driver.get(u)

    comments = WebDriverWait(driver, 10).until(
        ex.presence_of_all_elements_located((By.CSS_SELECTOR, '#comments li p'))
    )
    for c in comments:
        print(c.text)


driver.quit()
