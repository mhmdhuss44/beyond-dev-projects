import time
import traceback
from selenium.webdriver.common.by import By


class addEvent():
    def __init__(self,driver,eventName,message,taskNum):
        self.driver = driver
        self.eventName=eventName
        self.describtion=message
        self.taskNumber=taskNum

    def click_on_add_event(self):
        element_xpath = '//android.widget.ImageButton[@resource-id="com.claudivan.taskagenda:id/btNovoEvento"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def click_on_tommorw(self):
        element_xpath = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Tomorrow"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def write_event_name(self):
        element_xpath = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etTitulo"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        element.clear()
        element.send_keys(self.eventName)

    def write_event_descp(self):
        element_xpath = '//android.widget.EditText[@resource-id="com.claudivan.taskagenda:id/etDescricao"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        element.clear()
        element.send_keys(self.describtion)


    def choose_task(self):
        element_xpath = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvTipo"]'
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()
        time.sleep(2)
        element_xpath = '//android.widget.ListView[@resource-id="android:id/select_dialog_listview"]/android.widget.RelativeLayout['+str(self.taskNumber)+']'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def save_task_button(self):
        element_xpath = '//android.widget.Button[@resource-id="com.claudivan.taskagenda:id/item_salvar"]'
        # Find the element
        element = self.driver.find_element(By.XPATH, element_xpath)
        element.click()

    def add_task_flow(self):
        self.click_on_add_event()
        time.sleep(2)
        self.click_on_tommorw()
        time.sleep(2)
        self.write_event_name()
        time.sleep(2)
        self.write_event_descp()
        time.sleep(2)
        self.choose_task()
        time.sleep(2)
        self.save_task_button()










