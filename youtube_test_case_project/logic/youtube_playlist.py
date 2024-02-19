import time
from selenium.webdriver.common.by import By
from infra.basePage import base

# this class is related to the playlist test - to make sure that we cam open a playlist successfullly from a user profile
class playList(base):
    # note I didnt use any final parameters cause there was no need for them/to reuse things!
    def __init__(self,driver):
        super().__init__(driver)


    # this function is to open the first video after the results
    def open_first_video(self):
        self.first_video = self._driver.find_element(By.CSS_SELECTOR, 'a#video-title')
        self.first_video_link = self.first_video.get_attribute('href')
        # Click on the first video link
        self._driver.get(self.first_video_link)


    # this function is to click on the user profile on the video page
    def click_on_user_profile(self):
        user_profile_link = self._driver.find_element(By.CSS_SELECTOR, 'ytd-video-owner-renderer a.yt-simple-endpoint')
        user_profile_link.click()


    # this function is to click on the playlist tab on the user profile
    def click_On_Playlist_Tab(self):
        # Find the fourth element of the specified class
        playlist_tab = self._driver.find_element(By.CSS_SELECTOR, '.yt-tab-shape-wiz.yt-tab-shape-wiz--host-clickable:nth-child(4)')
        # Click on the playlist tab
        playlist_tab.click()


    # this function is used to open the first playlist
    def open_first_playlist(self):
        # Find the first playlist element
        playlist_element = self._driver.find_element(By.CSS_SELECTOR, 'ytd-playlist-thumbnail')
        # Click on the playlist element
        playlist_element.click()

    # a flow function to call of the above methods!
    def playlist_open_flow(self):
        self.open_first_video()
        time.sleep(3)
        self.click_on_user_profile()
        time.sleep(3)
        self.click_On_Playlist_Tab()
        time.sleep(3)
        self.open_first_playlist()






