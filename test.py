from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
# chrome_options.add_argument('--disable-infobars')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument("--user-data-dir=/home/gaurav/.config/google-chrome/Default")
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--remote-debugging-port=9222')

# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver = webdriver.Remote("http://192.168.1.2:4444/wd/hub", DesiredCapabilities.CHROME)
driver.set_page_load_timeout("10")
driver.get("https://www.google.com/")
driver.maximize_window()
que = driver.find_element_by_name("q")
que.send_keys("ITTroubleshooter.in")
time.sleep(3)
que.send_keys(Keys.ARROW_DOWN)
que.send_keys(Keys.RETURN)