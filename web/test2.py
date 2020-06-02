from selenium import webdriver
import bs4
import time

# https://brunch.co.kr/@jk-lab/18


chromedriver_dir = r'C:\chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)
driver.get('https://cargo.koreanair.com/ko/tracking')
time.sleep(5)
a = 1
while True:

    search = 'n'
    while True:
        search = driver.find_element_by_xpath('//*[@id="edit-awb-number--17"]')
        if search == 'n':
            continue
        else:
            break
    '//*[@id="edit-awb-number--14"]'
    driver.find_element_by_xpath('//*[@id="edit-awb-number--17"]').send_keys('66268366')

    '//*[@id="edit-submit--54"]'
    search = driver.find_element_by_xpath('//*[@id="edit-submit--54"]')
    search.click()
    time.sleep(10)
    POL_ATD = driver.find_element_by_xpath('//*[@id="myTabContent"]/div/div[2]/div/div/div[2]/div[3]')
    print(POL_ATD.text)
    a+= 1
    print(a)
    if a>3:
        break


