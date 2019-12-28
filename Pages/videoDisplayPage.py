from selenium.webdriver.support import wait


class VideoDisplayPage:

    def __init__(self, driver):
        self.driver = driver

        self.select_labelicon_id = "label-icon"
        self.sort_topcomments_partiallinkText = "Top comments"

    def select_labelicon(self):
        self.driver.find_element_by_id(self.select_labelicon_id).click()


    def select_sorttopcomment(self):
        self.driver.find_element_by_partial_link_text(self.sort_topcomments_partiallinkText).click()





