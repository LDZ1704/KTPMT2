from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/ky-luat-ban-than-p190238356.html?spid=190238357')
# driver.set_window_size(1920, 1080)

driver.execute_script('window.scroll(0,3600)')

# pages = driver.find_elements(By.CSS_SELECTOR, '.customer-reviews__pagination a')[1:6]

pages = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.customer-reviews__pagination a'))
)

pages = pages[1:6]

for p in pages:
    p.click()
    print('---------------Trang ', p.text)
    comments = WebDriverWait(driver, 10).until(
        ec.presence_of_all_elements_located((By.CLASS_NAME, 'review-comment__content'))
    )
    for c in comments:
        print(c.text)

    driver.save_screenshot(f'{p.text}.png')

driver.quit()