import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from infra.wrapperPage import base


class changeThemeColor():
    def __init__(self,driver,num):
        self.driver = driver
        self.number = num


    # this function will find the setting and press on it three times
    def find_settings(self):
        element_xpath = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Save the element and press it three times
        for _ in range(3):
            element.click()

    # method to click on the colors setting
    def find_color_setting(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btCores"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # method to find the change color window
    def press_on_main_color(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/item_background"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # method to choose a new color as theme
    def change_color(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/container_cores"]/android.widget.LinearLayout[1]/android.view.View[3]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # method to save the changes we have done
    def click_save_changes(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()


    # Method to handle notification button if it appear
    def handle_permission_button(self):
        try:
            permission_button_xpath = '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]'
            permission_button = self.driver.find_element(By.XPATH, permission_button_xpath)
            permission_button.click()
        except:
            pass

    # the over all process function
    def change_color_flow(self):
        self.find_settings()
        time.sleep(2)
        self.find_color_setting()
        time.sleep(3)
        self.press_on_main_color()
        time.sleep(2)
        self.change_color()
        time.sleep(2)
        self.click_save_changes()
        time.sleep(2)
        self.handle_permission_button()













