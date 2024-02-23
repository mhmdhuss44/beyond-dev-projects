import time
from selenium.webdriver.common.by import By


class checkArrows():
    def __init__(self,driver):
        self.driver = driver

    # we save the current date
    def save_prev_date(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvVisor"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        self.old_date=element.get_attribute('text')

    # we press on the next arrow
    def locate_right_arrows_and_press(self):
        element_xpath = '(//android.widget.ImageView[@content-desc="Image"])[2]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # we press on the prev arrow
    def locate_left_arrows_and_press(self):
        element_xpath = '(//android.widget.ImageView[@content-desc="Image"])[1]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # we save the date we get after the arrow was pressed
    def save_after_date(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvVisor"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        self.new_date=element.get_attribute('text')

    # the press arrow flow
    def arrows_flow(self,flag):
        self.save_prev_date()
        time.sleep(2)
        if flag=="next":
            self.locate_right_arrows_and_press()
        else:
            self.locate_left_arrows_and_press()
        time.sleep(2)
        self.save_after_date()
        # Extracting the first two elements from each string in the arr list
        first_string = self.old_date[:2]
        second_string = self.new_date[:2]
        # Converting the first two elements of each string to integers
        first_number = int(first_string)
        second_number = int(second_string)
        # Calculating the difference between the two numbers
        difference = abs(first_number - second_number)
        return difference


