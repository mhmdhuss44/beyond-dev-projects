class base:
    def __init__(self,driver):
        # we want it to be protected
        self._driver=driver

    def get_page_title(self):
        return self._driver.title