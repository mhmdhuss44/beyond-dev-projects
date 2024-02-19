import time
from selenium.webdriver.common.by import By
from infra.basePage import base


# this class is to filter the search results we get after searching
class filter_check(base):
    # note I didnt use any final parameters cause there was no need for them/to reuse things!
    def __init__(self,driver):
        super().__init__(driver)

    # finding the filter button and clciking on it
    def click_on_filter_button(self):
        filter_button = self._driver.find_element(By.CSS_SELECTOR,
                                              "button.yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-trailing")

        # Click on the filter button
        filter_button.click()

    # finsing the less than 4 mins filter button and clicking on it
    def video_less_than_four_filter(self):
        less_than_four_filter = self._driver.find_element(By.CSS_SELECTOR, "a[href*='sp=EgIYAQ']")
        less_than_four_filter.click()

    # the filter flow , for calling all of the above functions
    def filter_flow(self):
        try:
            self.click_on_filter_button()
            time.sleep(2)
            self.video_less_than_four_filter()
        except Exception as e:
            raise AssertionError(f"Error in filter_check: {e}")
