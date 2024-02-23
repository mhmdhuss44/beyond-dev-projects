import time
from selenium.webdriver.common.by import By


class vibrateFeature():
    def __init__(self,driver):
        self.driver = driver



    # this function will find the setting and press on it three times
    def find_settings(self):
        element_xpath = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Save the element and press it three times
        for _ in range(3):
            element.click()

    # method to click on the overall settings
    def find_overall_setting(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvAjustes"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # method to find the alarms window
    def press_on_alarms_and_notif(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvAlarmesENotificacoes"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()


    # method to click on vibrate and change it from check to unchecked
    def click_on_vibrate(self):
        element_xpath = '//android.widget.Switch[@resource-id="com.claudivan.taskagenda:id/swVibracaoAlarmeEvento"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Get the current state of the checkbox
        self.old_state = element.get_attribute("checked") == "true"
        # Click the checkbox to save changes
        element.click()
        time.sleep(2)
        self.new_state = element.get_attribute("checked") == "true"


    # the over all process function
    def change_vibrate_flow(self):
        self.find_settings()
        time.sleep(2)
        self.find_overall_setting()
        time.sleep(3)
        self.press_on_alarms_and_notif()
        time.sleep(2)
        self.click_on_vibrate()
        time.sleep(2)
        return [self.old_state,self.new_state]














