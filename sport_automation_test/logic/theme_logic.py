from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class ThemeChange:
    def __init__(self, driver):
        self.driver = driver

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

    def click_settings_button(self):
        settings_button = self.driver.find_element(By.CLASS_NAME, "main-header-module-settings-button")
        settings_button.click()
        time.sleep(3)

    def click_third_toggle_button(self):
        section_containers = self.driver.find_elements(By.CLASS_NAME, "settings-module-section-container")

        # Check if there is a third section container
        if len(section_containers) >= 3:
            # Get the third section container
            third_section_container = section_containers[2]

            # Find the button within the third section container
            button = third_section_container.find_element(By.CLASS_NAME, "switch-button_toggle__-GOkP")

            # Click the button
            button.click()

            time.sleep(2)  # Add a short delay for any animations or transitions to complete
        else:
            print("There are less than 3 section containers with the class name 'settings-module-section-container'.")

    def execute_all(self):
        self.agree_to_notice()
        self.click_popup_button()
        self.click_settings_button()
        self.click_third_toggle_button()
        time.sleep(5)  # Add a short delay for any further actions