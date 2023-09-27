from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard  # Đảm bảo bạn đã cài đặt thư viện keyboard trước
import time
import pickle
from selenium import webdriver
import pandas as pd 


def check_q_pressed():
    return keyboard.is_pressed('q')

def launchBrowser():
    # Tạo tùy chọn cho trình duyệt Chrome
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--disable-notifications")  # Thêm tùy chọn vô hiệu hóa thông báo

    # chrome_options.add_experimental_option("detach", True)  # Tùy chọn --no-exit

    # Khởi tạo trình duyệt Chrome với tùy chọn
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.facebook.com')
    return driver

driver = launchBrowser()
# full screen
driver.maximize_window()

# Login by Cookie
cookies = pickle.load(open('my_cookie.pkl', 'rb'))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('https://www.facebook.com')

time.sleep(2)

def TextTraight(text):
    # Loại bỏ các ký tự khoảng trắng và chia thành các phần tử
    lines = text.split("\n")
    # Loại bỏ các phần tử rỗng (có thể xuất hiện do các dấu xuống dòng)
    lines = [line for line in lines if line]

    # Gộp các phần tử thành một chuỗi duy nhất
    result = "".join(lines)
    return result


def crawl (driver) :
    result = []
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 300)")
    match = False
    while(match==False):
        time.sleep(1)

        numberPost = driver.find_elements(By.XPATH, '//div[@class="x1lliihq"]')
        container_element = driver.find_elements(By.CSS_SELECTOR, 'div.x1lliihq')
        print(len(numberPost))

        for item in container_element :
            try:
                valueHelp = 0

                header = item.find_element(By.CSS_SELECTOR, "h4.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz.x1gslohp.x1yc453h").text
                print(header)
                content = item.find_element(By.CSS_SELECTOR, "div.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13").text

                if "Xem thêm" in content:
                    addButton = item.find_element(By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f")
                    addButton.click()
                    content = item.find_element(By.CSS_SELECTOR, "div.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13").text

                time.sleep(0.2)
                identifyLabel = item.find_element(By.CSS_SELECTOR, "div.xmjcpbm.xdppsyt.x1n2onr6.x1lku1pv").text
                # print("identify",identifyLabel)

                if (identifyLabel):
                    valueHelp = 1
                    time.sleep(0.2)
                    result.append([header, valueHelp, content if content else ''])

            except:
                next
        
        print("Có thể nhấn phím 'q'")
        time.sleep(0.5)
        if check_q_pressed():
            print("Phím 'q' đã được nhấn. Dừng vòng lặp.")
            break
        
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 200)")
        if(len(numberPost) > 500):
            match = True


        
    df = pd.DataFrame(result,columns=['header', 'subHeader', 'content'])
    return df


while True:
    key = input("crawl : ")
    if(key == "yes"):
        df = crawl(driver=driver)
        print(df)
        df.to_csv('data.csv',encoding='utf-8',mode='a', index=False)
    else:
        break




