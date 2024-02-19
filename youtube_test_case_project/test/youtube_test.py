import time
import unittest
from infra.youtube_infra import browserWrapper
from logic.change_video_audio import Audio
from logic.youtube_comments import commentFilter
from logic.youtube_filter_search import filter_check
from logic.youtube_playlist import playList
from logic.youtube_search import youtube_page
from logic.youtube_shorts import shorts_pause

# NOTE: i wrote all the tests in the same class cause only have 5 tests
# and its not worth it to seperate them to different test classes

class youTubePageTest(unittest.TestCase):
    def setUp(self):
        # infra/setup
        self.browser = browserWrapper()
        self.driver = self.browser.get_driver("https://www.youtube.com/")
        self.the_youtube_page = youtube_page(self.driver)
        time.sleep(2)


    def search_process(self):
        self.the_youtube_page.search_flow("python programming")
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()

    # this one we did in class together
    def test_check_title_for_search(self):
        # logic
        self.search_process()
        # test
        self.assertIn("python programming",self.the_youtube_page.get_page_title(),"title not show!")

    # this test is ti check if the mute button in the video works correctly
    def test_check_video_sound_mute(self):
        # logic
        self.search_process()
        self.audio_try = Audio(self.driver)
        arr = self.audio_try.flow_volume()
        # test
        self.assertNotEqual(arr[0], arr[1], "Volume level did not change")


    # this is a test for trying the "less than for minutes" filter on the search results
    def test_check_filter_less_than_four(self):
        # logic
        self.search_process()
        try:
            self.filters = filter_check(self.driver)
            self.filters.filter_flow()
            time.sleep(2)
        #     test
        except AssertionError as e:
            self.fail(f"Assertion error occurred: {e}")


    # this test is to make sure that the suggestion of the search are releavnt
    def test_filter_comment_most_recent(self):
        # logic
        self.search_process()
        try:
            self.comments=commentFilter(self.driver)
            self.comments.filter_comment_flow()
        #     test
        except AssertionError as e:
             self.fail(f"Assertion error occurred: {e}")


    # this test is to check if we can pause a short on youtube by clicking on it
    def test_pause_video_on_shorts_by_click(self):
        # logic
        try:
            time.sleep(1)
            self.shorts = shorts_pause(self.driver)
            self.shorts.shorts_pause_flow()
        #     test
        except AssertionError as e:
            self.fail(f"Assertion error occurred: {e}")

    # this test is to make sure that soemone can open a user profile and open a playlist from it succefully
    def test_open_playlist_from_user_profile(self):
         # logic
         self.search_process()
         try:
            self.playlists = playList(self.driver)
            self.playlists.playlist_open_flow()
            time.sleep(3)
         # test
         except AssertionError as e:
             self.fail(f"Assertion error occurred: {e}")


















