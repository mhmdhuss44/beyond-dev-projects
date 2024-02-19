import time
from selenium.common.exceptions import NoSuchElementException
from infra.basePage import base


# this class is for pausing a short test case
class shorts_pause(base):
    # note I didnt use any final parameters cause there was no need for them/to reuse things!
    def __init__(self,driver):
        super().__init__(driver)

    # this function is for locating the shorts button on the home page and clciking on it
    def click_on_shorts(self):
        try:
            # Find the Shorts button
            shorts_button = self._driver.find_element_by_xpath("//a[@title='Shorts']")
            shorts_button.click()
        except NoSuchElementException as e:
            print("Failed to click on Shorts button:", e)
            assert False, "Failed to click on Shorts button"


    # this function is for trying to poause a short video
    def pause_short(self):
        try:
            # Find the video player
            video_player = self._driver.find_element_by_id("shorts-player")
            # Pause the video
            video_player.click()
        except NoSuchElementException as e:
            # print("Failed to pause the video:", e)
            assert False, "Failed to pause the video"

    # flow functon to call of the above methods!
    def shorts_pause_flow(self):
        self.click_on_shorts()
        time.sleep(3)
        self.pause_short()
        time.sleep(3)


