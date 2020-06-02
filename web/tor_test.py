from selenium import webdriver

driver_dir = r'C:\chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(driver_dir)

options = webdriver.ChromeOptions()
options.add_argument("network.proxy.type", 1)
options.add_argument("network.proxy.socks", "127.0.0.1")
options.add_argument("network.proxy.socks_port", 9050)


driver.get('http://icanhazip.com/')
print(driver.page_source)

driver.quit()