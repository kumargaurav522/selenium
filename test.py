from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.set_page_load_timeout("10")
driver.get("https://www.google.com/")
driver.maximize_window()
que = driver.find_element_by_name("q")
que.send_keys("ITTroubleshooter.in")
time.sleep(3)
que.send_keys(Keys.ARROW_DOWN)
que.send_keys(Keys.RETURN)