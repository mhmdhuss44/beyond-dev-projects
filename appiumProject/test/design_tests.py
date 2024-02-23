import time
import traceback
import unittest
from infra.wrapperPage import base
from logic.arrows_logic import checkArrows
from logic.theme_color_logic import changeThemeColor
from logic.vibrate_logic import vibrateFeature


# more focused on design!
class TestAppium(unittest.TestCase):
    def setUp(self):
        self.baseCade=base()
        self.driver = self.baseCade.driver_set_up()

    def tearDown(self) -> None:
        self.driver.quit()

    # first test is to try and change theme color
    def test_change_theme_color(self):
        try:
            self.themes = changeThemeColor(self.driver, 1)
            self.themes.change_color_flow()
            time.sleep(3)
        except Exception as e:
            traceback.print_exc()
            self.fail(f"An unexpected error occurred: {e}")
            # Assert that there were no errors
        self.assertTrue(True, "No errors occurred during execution")


    # verify that the right arrows are working correct! (to front)
    def test_arrows_right_moves(self):
        self.arrows = checkArrows(self.driver)
        difference=self.arrows.arrows_flow("next")
        # Asserting that the difference is equal to 7
        assert difference == 7, f"The difference between the numbers ({difference}) is not equal to 7"

    # verify that the left arrows are working correct! (toback)
    def test_arrows_left_moves(self):
        self.arrows = checkArrows(self.driver)
        difference=self.arrows.arrows_flow("prev")
        # Asserting that the difference is equal to 7
        assert difference == 7, f"The difference between the numbers ({difference}) is not equal to 7"

    # verify that we can changes the vibrate button to true/false whenever we want
    def test_vibrate_change(self):
        self.vibes = vibrateFeature(self.driver)
        arr=self.vibes.change_vibrate_flow()
        # Asserting that the difference is equal to 7
        assert arr[0] != arr[1], f"The vibrate state didnt change"











