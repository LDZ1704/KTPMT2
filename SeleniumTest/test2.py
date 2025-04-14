from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.sendo.vn/bot-thong-cong-bon-cau-cuc-manh-hop-268g-114149051.html?source_block_id=feed&source_page_id=home&source_info=desktop2_60_1744595845126_f004b68d-1583-4514-8ba0-c6db6d3e5d19_-1_ishyperhome0_0_7_9_-1")
sleep(5)
driver.execute_script("scrollTo(0, 3000)")
wait = WebDriverWait(driver, 10)

i = 0
while True:
    sleep(2)
    i = i + 1
    print(f'================={i}=================')
    try:
        comments = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._39ab-aJ_2cA > div._39ab-OuyhLr > div._39ab-_2vzod > p')))
        for c in comments:
            print(c.text)
        driver.save_screenshot(f'{i}.png')
    except:
        print("Khong cos comment")

    while True:
        sleep(2)
        try:
            next = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#id-danh-gia > div > div._39ab-ZyAoEK.d7ed-fdSIZS.d7ed-OoK3wU.d7ed-AwHm4T > div > ul > li:nth-child(5) > button')))
            if not next.is_enabled():
                break
            else:
                next.click()
                break
        except:
            driver.execute_script("window.scrollBy(0, 500);")


driver.quit()