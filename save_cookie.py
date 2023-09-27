import pickle
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def launchBrowser():
    # Tạo tùy chọn cho trình duyệt Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")  # Thêm tùy chọn vô hiệu hóa thông báo

    # chrome_options.add_experimental_option("detach", True)  # Tùy chọn --no-exit

    # Khởi tạo trình duyệt Chrome với tùy chọn
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com')
    return driver

driver = launchBrowser()
driver.maximize_window()

user_name = driver.find_element(By.ID, 'email').send_keys('thanhmai.20570@gmail.com')
pass_word = driver.find_element(By.ID, 'pass').send_keys('@Pho123456789')

login_user = driver.find_element(By.NAME, 'login').click()



time.sleep(5)

pickle.dump(driver.get_cookies(), open('my_cookie.pkl', 'wb'))
driver.close()




