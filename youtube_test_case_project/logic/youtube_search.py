from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from infra.basePage import base

# this test was done in class-IGNORE
class youtube_page(base):
    SEARCH_INPUT="//input[@id='search']"
    def __init__(self,driver):
        super().__init__(driver)
        self.serach_input=self._driver.find_element(By.XPATH,self.SEARCH_INPUT)

    def fill_serach_input(self,text):
        self.serach_input.send_keys(text)

    def press_enter_on_search(self):
        self.serach_input.send_keys(Keys.RETURN)


    def search_flow(self,text):
        self.fill_serach_input(text)
        self.press_enter_on_search()



