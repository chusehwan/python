from selenium import webdriver


TEST_URL = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")

driver_dir = r'C:\chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(driver_dir, options=options)

driver.get(TEST_URL)
#driver.implicitly_wait(3)
#driver.get_screenshot_as_file('naver_main.png')
user_agent = driver.find_element_by_css_selector('#user-agent').text

print('User-Agent: ', user_agent)
driver.quit()