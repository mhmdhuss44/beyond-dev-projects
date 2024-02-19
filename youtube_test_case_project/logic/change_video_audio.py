import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from infra.basePage import base

# this is for trying to mute a video test case
class Audio(base):
    # note I didnt use any final parameters cause there was no need for them/to reuse things!
    def __init__(self,driver):
        super().__init__(driver)


    # function to open the first video after search
    def open_first_video(self):
        self.first_video = self._driver.find_element(By.CSS_SELECTOR, 'a#video-title')
        self.first_video_link = self.first_video.get_attribute('href')
        # Click on the first video link
        self._driver.get(self.first_video_link)

    # to continue the video if its posed (so we can hear things)
    def click_pause_button(self):
        try:
            # Find the pause/stop button
            pause_button = self._driver.find_element(By.CSS_SELECTOR, 'button.ytp-play-button')
            # Click the pause/stop button
            ActionChains(self._driver).move_to_element(pause_button).click().perform()
            # print("Pause/Stop button clicked successfully.")
        except Exception as e:
            print(f"Failed to click pause/stop button: {e}")

    # get the current volume level
    def get_volume_level(self):
        try:
            # Find the mute/unmute button
            mute_button = self._driver.find_element(By.CSS_SELECTOR, 'button.ytp-mute-button')
            # Check if the mute button has the class indicating muted state
            is_muted = 'ytp-svg-volume-animation-hider' not in mute_button.get_attribute('innerHTML')
            return 1 if is_muted else 0
        except Exception as e:
            print(f"Failed to get volume level: {e}")
            return None

    # change from mute to unmute or the oppsite
    def set_volume_level(self):
        try:
            # Find the mute/unmute button
            mute_button = self._driver.find_element(By.CSS_SELECTOR, 'button.ytp-mute-button')
            # Click on the mute/unmute button
            ActionChains(self._driver).move_to_element(mute_button).click().perform()
            # print("Mute/unmute button clicked successfully.")
        except Exception as e:
            print(f"Failed to click mute/unmute button: {e}")

    # the flow function to call all of the above methods
    def flow_volume(self):
        self.open_first_video()
        # self.click_pause_button()
        time.sleep(2)
        x = self.get_volume_level()
        self.set_volume_level()
        time.sleep(2)
        y = self.get_volume_level()
        # print("the values",x,y)
        return [x, y]





