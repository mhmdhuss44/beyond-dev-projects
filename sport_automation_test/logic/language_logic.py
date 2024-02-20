from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class LanguageChange:
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
            time.sleep(10)
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
        time.sleep(1)
        section_containers = self.driver.find_elements(By.CLASS_NAME, "settings-module-section-container")
        time.sleep(1)
        if self.number==1:
            # Check if there is a third section container
            if len(section_containers) >= 4:
                # Get the third section container
                fourth_section_container = section_containers[3]

                # Find the button within the fourth section container
                button = fourth_section_container.find_element(By.CLASS_NAME, "language-menu_collapsed_button__5fw-7")

                # Click the button
                button.click()

                time.sleep(2)  # Add a short delay for any animations or transitions to complete
            else:
                print("There are less than 3 section containers with the class name 'settings-module-section-container'.")
        else:
            # Check if there is a third section container
            if len(section_containers) >= 5:
                # Get the third section container
                fourth_section_container = section_containers[4]

                # Find the button within the fourth section container
                button = fourth_section_container.find_element(By.CLASS_NAME, "language-menu_collapsed_button__5fw-7")

                # Click the button
                button.click()

                time.sleep(2)  # Add a short delay for any animations or transitions to complete
            else:
                print(
                    "There are less than 3 section containers with the class name 'settings-module-section-container'.")

    def press_first_language(self):
        time.sleep(7)
        language_item = self.driver.find_element(By.CLASS_NAME, "language-menu_item__n4ICI")
        language_item.click()
        print("Clicked on the first language button successfully.")



    def execute_all(self):
        self.agree_to_notice()
        self.click_popup_button()
        self.click_settings_button()
        self.click_third_toggle_button()
        time.sleep(1)
        self.press_first_language()
        time.sleep(5)  # Add a short delay for any further actions
        url_after_search = self.driver.current_url
        return url_after_search
