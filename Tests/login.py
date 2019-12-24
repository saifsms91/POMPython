from selenium import webdriver
import time
import unittest

from config import getDriverDir


class SortTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('window-size=2560,1440')
        self.driver = webdriver.Chrome(executable_path=getDriverDir(), options=options)


    def test_OpenVideo(self,):
        self.driver.get('https://www.youtube.com/')
        self.driver.find_element_by_id("search").send_keys("lovely turkey place")
        self.driver.find_element_by_id("search-icon-legacy").click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text("10 Best Places to Visit in Turkey").click()
        time.sleep(4)
        self.driver.find_element_by_id("label-icon").click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text("Top comments").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
