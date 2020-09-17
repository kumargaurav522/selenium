from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/gaurav/selenium/chromedriver")
driver.set_page_load_timeout("10")
driver.get("https://www.google.com/")
driver.maximize_window()
que = driver.find_element_by_name("q")
que.send_keys("ITTroubleshooter.in")
time.sleep(3)
que.send_keys(Keys.ARROW_DOWN)
que.send_keys(Keys.RETURN)