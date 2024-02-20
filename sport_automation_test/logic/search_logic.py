from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class SearchAndEnter:
    def __init__(self, driver,num):
        self.driver = driver
        self.number=num

    def agree_to_notice(self):
        try:
            agree_button = self.driver.find_element(By.ID, "didomi-notice-agree-button")
            agree_button.click()
            time.sleep(7)
        except NoSuchElementException:
            print("Popup button not found. Continuing execution without clicking.")

    def click_popup_button(self):
        try:
            time.sleep(5)
            popup_button = self.driver.find_element(By.CLASS_NAME, "popup_button__zfc0e")
            popup_button.click()
            print("Clicked on popup button successfully.")
        except NoSuchElementException:
            print("Popup button not found. Continuing execution without clicking.")
        time.sleep(2)

    def search_and_enter(self):
        url_before_search = self.driver.current_url

        if self.number==1:
            search_button = self.driver.find_element(By.CSS_SELECTOR,
                                                     "button.main-header-module-mobile-buttons-button img.main-header-module-mobile-buttons-search-icon")
            search_button.click()  # Click on the search button
            print("Pressed the search button successfully.")
            time.sleep(3)
            print("Pressed the search button successfully.")
            search_bar = self.driver.find_element(By.CLASS_NAME, "main-header-module-mobile-input")
            time.sleep(2)  # Add a short delay for typing to complete
            search_bar.clear()  # Clear any existing text in the search bar
            search_bar.send_keys("barcelona")  # Type "barcelona" into the search bar
            time.sleep(2)  # Add a short delay for typing to complete
            search_results = self.driver.find_elements(By.CSS_SELECTOR, ".search-widget-item-container")
            time.sleep(2)
            if search_results:
                first_result = search_results[0].find_element(By.CSS_SELECTOR, "a.search-widget-item-content-container")
                first_result.click()  # Click on the first search result
        else:
            search_bar = self.driver.find_element(By.CSS_SELECTOR,
                                                  "div.main-header-module-desktop-search-bar input.main-header-module-desktop-search-input")
            search_bar.click()  # Click on the search bar
            time.sleep(2)  # Add a short delay for typing to complete
            search_bar.clear()  # Clear any existing text in the search bar
            search_bar.send_keys("barcelona")  # Type "barcelona" into the search bar
            time.sleep(2)  # Add a short delay for typing to complete
            print("Entered 'barcelona' into the search bar and performed search successfully.")
            search_results = self.driver.find_elements(By.CSS_SELECTOR, ".search-widget-item-container")
            time.sleep(2)
            if search_results:
                first_result = search_results[0].find_element(By.CSS_SELECTOR, "a.search-widget-item-content-container")
                first_result.click()  # Click on the first search result

        # Store the title after search
        url_after_search = self.driver.current_url

        # Return the titles and searched text in an array
        # print(url_before_search, url_after_search, "barcelona")
        return [url_before_search, url_after_search, "barcelona"]



    def execute_all(self):
        self.agree_to_notice()
        self.click_popup_button()
        time.sleep(3)  # Add a short delay for any further actions
        final=self.search_and_enter()
        time.sleep(2)
        return final

