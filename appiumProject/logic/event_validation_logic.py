import time
from selenium.webdriver.common.by import By


class checkEventsList():
    def __init__(self,driver,eventName):
        self.driver = driver
        self.eventName=eventName


    # this function will find the setting and press on it three times
    def find_settings(self):
        element_xpath = '//android.widget.ImageView[@resource-id="com.claudivan.taskagenda:id/hamburguer"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Save the element and press it three times
        for _ in range(3):
            element.click()


    # this function will press on the all events button
    def press_on_all_events(self):
        element_xpath = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/btEventos"]'
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

    # to go through everything on the page and check if our event is there - by event name
    def check_event(self, newName=None):
        if newName is None:
            newName = self.eventName
        try:
            # Find all TextView elements
            text_views = self.driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            # Check each TextView element for the text "food"
            for text_view in text_views:
                text = text_view.text.strip()  # Get the text of the TextView and strip any leading/trailing whitespace
                if text.lower() == newName.lower():
                    print("Found",newName," in a TextView:", text_view.get_attribute("resource-id"))
                    return True  # If found, return True

            return False
        except Exception as e:
            return False

    def verify_flow(self):
        self.find_settings()
        time.sleep(2)
        self.press_on_all_events()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        final_res=self.check_event()
        return final_res

    # press on the show calendar option
    def open_calendar(self):
        element_xpath = '//android.widget.LinearLayout[@content-desc="Calendar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    # click on the date on the caelndar
    def click_on_date(self):
        element_xpath = '//android.widget.TextView[@text="24"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def verify_flow_calendar(self):
        self.open_calendar()
        time.sleep(2)
        self.click_on_date()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        final_res=self.check_event()
        return final_res

    # press on the date we want on the week list
    def press_on_date_on_week_page(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/dia_mes" and @text="24"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def verify_flow_week(self):
        self.press_on_date_on_week_page()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        final_res=self.check_event()
        return final_res

    def press_on_event(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTitulo"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def press_on_delete(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_excluir"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def delete_confirm(self):
        element_xpath = '//android.widget.Button[@resource-id="android:id/button1"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def not_delete_confirm(self):
        element_xpath = '//android.widget.Button[@resource-id="android:id/button2"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def verify_delete_flow(self):
        self.find_settings()
        time.sleep(2)
        self.press_on_all_events()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        self.press_on_event()
        time.sleep(2)
        self.press_on_delete()
        time.sleep(2)
        self.delete_confirm()
        time.sleep(2)
        final_res=self.check_event()
        return final_res


    def verify_not_delete_flow(self):
        self.find_settings()
        time.sleep(2)
        self.press_on_all_events()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        self.press_on_event()
        time.sleep(2)
        self.press_on_delete()
        time.sleep(2)
        self.not_delete_confirm()
        time.sleep(2)
        final_res=self.check_event()
        return final_res

    def press_on_edit(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_editar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def modify_event_name(self,newName):
        # locate the text input and press on it then clear it then type a new name
        element_xpath = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etTitulo"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        # Clear any existing text
        element.clear()
        # Type a new name
        element.send_keys(newName)

    def click_on_save(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()


    def verify_modify_flow(self,newName):
        self.find_settings()
        time.sleep(2)
        self.press_on_all_events()
        time.sleep(2)
        self.handle_permission_button()
        time.sleep(2)
        self.press_on_event()
        time.sleep(2)
        self.press_on_edit()
        time.sleep(2)
        self.modify_event_name(newName)
        time.sleep(2)
        self.click_on_save()
        time.sleep(2)
        final_res=self.check_event(newName)
        return final_res







