from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='.\chromedriver.exe')
driver.get('https://tinder.com/app/matches')
time.sleep(30)
val = 1
while 1 == 1:
    driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
    time.sleep(2)
    print(val)
    val += 1
