from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class filterLive:
    def __init__(self, driver,num):
        self.driver = driver
        self.number=num

    def agree_to_notice(self):
        try:
            agree_button = self.driver.find_element(By.ID, "didomi-notice-agree-button")
            agree_button.click()
            time.sleep(10)
        except NoSuchElementException:
            print("Popup button not found. Continuing execution without clicking.")

    def click_popup_button(self):
        try:
            popup_button = self.driver.find_element(By.CLASS_NAME, "popup_button__zfc0e")
            popup_button.click()
            print("Clicked on popup button successfully.")
        except NoSuchElementException:
            print("Popup button not found. Continuing execution without clicking.")
        time.sleep(2)

    def click_on_live_filter(self):
        if self.number==1:
            live_button = self.driver.find_element(By.CSS_SELECTOR, ".main-header-module-mobile-buttons-switch")
            live_button.click()
            time.sleep(2)  # Add a short delay for any actions triggered by the button click to complete
        else:
            live_button = self.driver.find_element(By.CSS_SELECTOR, ".scores-bar-widget-toolbar_live_toggle__8E2sQ")
            # Click the live button
            live_button.click()
            time.sleep(2)  # Add a short delay for any actions triggered by the button click to complete
        url_after_search = self.driver.current_url

        return  url_after_search



    def execute_all(self):
        self.agree_to_notice()
        self.click_popup_button()
        time.sleep(3)  # Add a short delay for any further actions
        result = self.click_on_live_filter()
        time.sleep(2)
        return result

