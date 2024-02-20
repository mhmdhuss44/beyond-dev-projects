from selenium import webdriver
class base:
    def __init__(self,list_info):
        # we want it to be protected
        self._driver=None
        self.info=list_info
        self.cab_list=[]


    def preapare_cab_list(self):
        print("hey")
        browser_names = [name for name, _ in self.info['browsers_list']]
        if "chrome" in browser_names:
            print("Chrome found")
            self.chrome_cab = webdriver.ChromeOptions()
            platform = [platform for name, platform in self.info['browsers_list'] if name == "chrome"][0]
            self.chrome_cab.capabilities['platformName'] = platform
            self.cab_list.append((self.chrome_cab,1))

        if "firefox" in browser_names:
            print("Firefox found")
            self.fire_cab = webdriver.FirefoxOptions()
            platform = [platform for name, platform in self.info['browsers_list'] if name == "firefox"][0]
            self.fire_cab.capabilities['platformName'] = platform
            self.cab_list.append((self.fire_cab,2))


    def driver_set_up(self,cap):
        hub_url = self.info.get('hub_url')
        web_url = self.info.get('web_link')

        if not hub_url:
            raise ValueError("Hub URL not provided in the configuration.")

        if not web_url:
            raise ValueError("Web URL not provided in the configuration.")

        if not self.cab_list:
            raise ValueError("No browsers specified in the configuration.")

        self._driver = webdriver.Remote(command_executor=hub_url, options=cap)
        self._driver.get(web_url)



