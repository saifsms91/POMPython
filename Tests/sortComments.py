from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from config import getDriverDir
from Pages.homePage import homePage
from Pages.searchResultPage import SearchResultPage
from Pages.videoDisplayPage import VideoDisplayPage


class SortTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument('window-size=2560,1440')
        self.driver = webdriver.Chrome(executable_path=getDriverDir(), options=options)
        self.driver.implicitly_wait(20)

    def test_OpenVideo(self, ):
        driver = self.driver
        driver.get('https://www.youtube.com/')

        home = homePage(driver)
        home.enter_textinhome("lovely turkey place")
        home.tap_searchicon()
        #time.sleep(4)

        srp = SearchResultPage(driver)
        srp.select_video()
        #time.sleep(4)

        vdp = VideoDisplayPage(driver)
        vdp.select_labelicon()
        vdp.select_sorttopcomment
       # time.sleep(4)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
