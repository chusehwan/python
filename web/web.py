from selenium import webdriver
import requests
import time

url = "https://cargo.koreanair.com/ko/tracking?awbNO=18066268366"
driver = webdriver.Chrome('C:\\chrome_driver\\chromedriver.exe')
driver.get(url)
a = driver.find_element_by_class_name('tl-labels-date pt-1')

