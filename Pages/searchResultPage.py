import time

from selenium.webdriver.support import wait


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.selectvideo_partialLink = "10 Best Places to Visit in Turkey"


    def select_video(self):
        self.driver.find_element_by_partial_link_text(self.selectvideo_partialLink).click()



