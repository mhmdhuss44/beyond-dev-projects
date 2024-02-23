import time

from selenium.webdriver.common.by import By


class addEventType():
    def __init__(self,driver,eventTypeName):
        self.driver = driver
        self.eventTypeName=eventTypeName

    # this function will find the setting and press on it three times
    def find_settings(self):
        element_xpath = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Save the element and press it three times
        for _ in range(3):
            element.click()

    # method to click on the typing setting
    def find_type_setting(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btCores"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

# method to click on add new type setting
    def find_new_type_button(self):
        element_xpath = '//android.widget.TextView[@text="Add new"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # write the type name
    def write_type_name(self):
        element_xpath = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etNome"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        element.clear()
        element.send_keys(self.eventTypeName)

    # choose a color to your type
    def choose_type_color(self):
        element_xpath = '//android.view.View[@resource-id="com.claudivan.taskagenda:id/cvCor"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        time.sleep(2)
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/container_cores"]/android.widget.LinearLayout[4]/android.view.View[5]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # choose an icon for the new type
    def choose_type_icon(self):
        element_xpath = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/ivIcone"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        time.sleep(2)
        element_xpath = '(//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/ivIcone"])[7]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # after fininshing click ok to save the new type added
    def click_on_ok(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_ok"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # to go through everything on the page and check if our event is there - by event name
    def check_type(self):
        try:
            # Find all TextView elements
            text_views = self.driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            # Check each TextView element for the text "food"
            for text_view in text_views:
                text = text_view.text.strip()  # Get the text of the TextView and strip any leading/trailing whitespace
                if text.lower() == self.eventTypeName.lower():
                    print("Found",self.eventTypeName," in a TextView:", text_view.get_attribute("resource-id"))
                    return True  # If found, return True
            return False
        except Exception as e:
            return False

    # method to save the changes we have done
    def click_save_changes(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # method to save the changes we have done
    def back_to_home(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/containerColunasHorarios"]/android.widget.RelativeLayout[7]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()



    def add_new_type_flow(self):
        self.find_settings()
        time.sleep(2)
        self.find_type_setting()
        time.sleep(2)
        self.find_new_type_button()
        time.sleep(2)
        self.write_type_name()
        time.sleep(2)
        self.choose_type_color()
        time.sleep(2)
        self.choose_type_icon()
        time.sleep(2)
        self.click_on_ok()
        time.sleep(2)
        result=self.check_type()
        time.sleep(2)
        self.click_save_changes()
        time.sleep(1)
        self.back_to_home()
        return result








