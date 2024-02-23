import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

class base:
    URL = 'http://localhost:4723'
    CAPS =dict(
        platformName="Android",
        deviceName="sdk_gphone64_x86_64",
        platformVersion="14.0",
        automationName="UiAutomator2",
        appPackage="com.claudivan.taskagenda",
        appActivity=".Activities.MainActivity"
    )
    def __init__(self):
        # we want it to be protected
        self.driver=None


    def driver_set_up(self):
        self.capabilities_options = UiAutomator2Options().load_capabilities(self.CAPS)
        return webdriver.Remote(
            command_executor=self.URL,
            options=self.capabilities_options
        )



