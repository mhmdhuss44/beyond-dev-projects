import time
from selenium.webdriver.common.by import By
from infra.basePage import base


# testing the filter comments - most recent filter
class commentFilter(base):
    # note I didnt use any final parameters cause there was no need for them/to reuse things!
    def __init__(self,driver):
        super().__init__(driver)


    # function to open the first video after the search
    def open_first_video(self):
        self.first_video = self._driver.find_element(By.CSS_SELECTOR, 'a#video-title')
        self.first_video_link = self.first_video.get_attribute('href')
        # Click on the first video link
        self._driver.get(self.first_video_link)

    # function to scroll down to comments
    def scroll_down_to_comments(self):
        # Scroll down to see comments
        for _ in range(1):
            self._driver.execute_script("window.scrollBy(0, 500)")  # Scroll down by 500 pixels
            time.sleep(1)

    # finding the filter button in the comments
    def filter_comments_accroding_button(self):
        # Find the parent element containing the filter button
        parent_element = self._driver.find_element(By.ID, 'sort-menu')
        assert parent_element, "Parent element containing filter button not found"
        filter_button = parent_element.find_element(By.CSS_SELECTOR,
                                                    'yt-sort-filter-sub-menu-renderer yt-dropdown-menu')
        assert filter_button, "Filter button not found"
        filter_button.click()


    # finding the wanted filter type button (most recent)
    def click_filter_by_most_recent(self):
        parent_element = self._driver.find_element(By.ID, 'sort-menu')
        assert parent_element, "Parent element containing filter button not found"
        # Find all filter options
        filter_options = parent_element.find_elements(By.CSS_SELECTOR, 'tp-yt-paper-item')
        if len(filter_options) >= 2:
            filter_options[1].click()

    # caaling all of the avove methods
    def filter_comment_flow(self):
        self.open_first_video()
        time.sleep(2)
        self.scroll_down_to_comments()
        time.sleep(2)
        self.filter_comments_accroding_button()
        time.sleep(2)
        self.click_filter_by_most_recent()
        time.sleep(2)





