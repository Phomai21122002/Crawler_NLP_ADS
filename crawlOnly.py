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
    time.sleep(1)

    numberPost = driver.find_elements(By.XPATH, '//a[@class="x1i10hfl x9f619 xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1a2a7pz xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x1heor9g x1ypdohk xjb2p0i x1qlqyl8 x15bjb6t xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1r8a4m5 xsj2dmf x144v4sp x1edh9d7 x1lliihq xh8yej3 x1pdlv7q"]')
    container_element = driver.find_elements(By.CSS_SELECTOR, '.x1i10hfl.x9f619.xe8uvvx.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1n2onr6.x87ps6o.x1a2a7pz.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1heor9g.x1ypdohk.xjb2p0i.x1qlqyl8.x15bjb6t.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1r8a4m5.xsj2dmf.x144v4sp.x1edh9d7.x1lliihq.xh8yej3.x1pdlv7q')
    print(len(numberPost))

    for item in container_element :
        try:
            valueHelp = 1

            header = item.find_element(By.CSS_SELECTOR, "span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.x1j85h84").text
            print(header)
            content = item.find_element(By.CSS_SELECTOR, "span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xk50ysn.xzsf02u.x1yc453h").text
            print(content)

            # if "Xem thêm" in content:
            #     addButton = item.find_element(By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f")
            #     addButton.click()
            #     content = item.find_element(By.CSS_SELECTOR, "div.x1iorvi4.x1pi30zi.x1l90r2v.x1swvt13").text

            # time.sleep(0.2)
            # identifyLabel = item.find_element(By.CSS_SELECTOR, "div.xmjcpbm.xdppsyt.x1n2onr6.x1lku1pv").text
            # # print("identify",identifyLabel)

            # if (identifyLabel):
            #     valueHelp = 1

            # time.sleep(0.2)
            result.append([header, valueHelp, content])

        except:
            next
        
        
    df = pd.DataFrame(result,columns=['header', 'subHeader', 'content'])
    return df


while True:
    key = input("crawl : ")
    if(key == "yes"):
        df = crawl(driver=driver)
        print(df)
        df.to_csv('dataOnly.csv',encoding='utf-8',mode='a', index=False)
    else:
        break




