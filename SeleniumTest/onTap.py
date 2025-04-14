import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep

# Tạo thư mục lưu ảnh
os.makedirs("screenshots", exist_ok=True)

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/chat-gpt-thuc-chien-p275702538.html')

i = 0
while True:
    i += 1
    print(f"Trang {i}...")

    driver.execute_script('window.scrollTo(0, 3200);')
    sleep(2)

    try:
        comments = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, 'review-comment__content'))[1:6]
        )
        for c in comments:
            print("-", c.text)

        # Chụp màn hình sau khi load bình luận
        driver.save_screenshot(f'screenshots/page_{i}.png')

    except:
        print("Không tìm thấy bình luận nào.")
        break

    try:
        next_btn = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.customer-reviews__pagination a.next'))
        )

        if 'disabled' in next_btn.get_attribute("class"):
            print("Đã tới trang cuối cùng.")
            break

        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        sleep(1)
        next_btn.click()
        sleep(2)

    except Exception as e:
        print(f"Không tìm thấy nút 'Next' hoặc xảy ra lỗi: {e}")
        break

driver.quit()
