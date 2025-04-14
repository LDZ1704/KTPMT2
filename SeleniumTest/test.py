from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/ram-laptop-samsung-4gb-ddr4-2133mhz-sodimm-hang-nhap-khau-p10001324.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.186470_Y.1768797_Z.3442229_CN.15%2F10%2F2022-Ram-laptop&itm_medium=CPC&itm_source=tiki-ads&spid=11602000')

driver.execute_script('window.scroll(0,2265)')

pages = WebDriverWait(driver, 10).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.customer-reviews__pagination a'))
)

pages = pages[1:6]

for p in pages:
    try:
        if p.text.strip() == str(p.text):
            driver.execute_script("arguments[0].click();", p)
        # p.click()
        # driver.execute_script("arguments[0].click();", p)
        print('--------Trang ', p.text)
        comments = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'review-comment__content'))
        )
        sleep(2)
        for c in comments:
            print(c.text)

        driver.save_screenshot(f'{p.text}.png')
        sleep(2)
        driver.execute_script('window.scrollBy(0,2000)')
    except:
        pass

driver.quit()