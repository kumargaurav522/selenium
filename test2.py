import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ITTroubleshooterSearchTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('firefox', 'firefox')}
        self.browser = webdriver.Remote(
            command_executor='http://192.168.1.2:4444/wd/hub',
            desired_capabilities=caps
        )

    def search_for_ittroubleshooter(self):
        browser = self.browser
        browser.get('https://www.google.com/')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('ittroubleshooter.in')
        search_box.send_keys(Keys.RETURN)
        browser.get('https://ittroubleshooter.in/')
        time.sleep(3)  # simulate long running test

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()