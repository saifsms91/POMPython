class homePage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textboxhome_id = "search"
        self.search_icon_id = "search-icon-legacy"



    def enter_textinhome(self,textbox ):
        self.driver.find_element_by_id(self.search_textboxhome_id).send_keys(textbox)


    def tap_searchicon(self):
     self.driver.find_element_by_id(self.search_icon_id).click()
