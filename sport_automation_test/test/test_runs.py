import concurrent.futures.thread
import time
import unittest
from selenium import webdriver
import concurrent.futures
from selenium.webdriver.common.by import By
from infra.basePage import base
from infra.youtube_infra import browserWrapper
from logic.filter_logic import filterLive
from logic.language_logic import LanguageChange
from logic.search_logic import SearchAndEnter
from logic.theme_logic import ThemeChange


class gridProject(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.infra_layer.load_configurations()
        self.basePage=base(self.infra_layer.get_all_configurations())
        self.basePage.preapare_cab_list()


    def test_run_grid_serial(self):
        print(self.basePage.cab_list)
        for cab,num in self.basePage.cab_list:
            self.test_execute_live_filter(cab,num)

    # def test_run_grid_parell(self):
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.basePage.cab_list)) as executor:
    #         futures = []
    #
    #         for cab, num in self.basePage.cab_list:
    #             futures.append(executor.submit(self.test_execute_language, cab, num))
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             future.result()
    #
    #         futures = []
    #
    #         for cab, num in self.basePage.cab_list:
    #             futures.append(executor.submit(self.test_execute_theme, cab, num))
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             future.result()
    #
    #         futures = []
    #
    #         for cab, num in self.basePage.cab_list:
    #             futures.append(executor.submit(self.test_execute_search, cab, num))
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             future.result()
    #
    #         futures = []
    #
    #         for cab, num in self.basePage.cab_list:
    #             futures.append(executor.submit(self.test_execute_live_filter, cab, num))
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             future.result()

    def test_execute_language(self, caps,num):
        self.basePage.driver_set_up(caps)
        time.sleep(3)
        self.page_language = LanguageChange(self.basePage._driver,num)
        result=self.page_language.execute_all()
        assert "he" not in result, "the language didnt change succefully"
        self.basePage._driver.quit()

    def test_execute_theme(self, caps,num):
        self.basePage.driver_set_up(caps)
        time.sleep(3)
        self.page_theme=ThemeChange(self.basePage._driver)
        self.page_theme.execute_all()
        self.basePage._driver.quit()
        # Assert that there are no errors
        self.assertTrue(True)



    def test_execute_search(self, caps,num):
        self.basePage.driver_set_up(caps)
        time.sleep(3)
        self.page_serach=SearchAndEnter(self.basePage._driver,num)
        results=self.page_serach.execute_all()
        assert results[2] in results[1], "Searched word 'barcelona' not found in the title after search."
        self.basePage._driver.quit()


    def test_execute_live_filter(self, caps,num):
        self.basePage.driver_set_up(caps)
        time.sleep(3)
        self.page_live=filterLive(self.basePage._driver,num)
        result=self.page_live.execute_all()
        assert "live" in result, "we are not on a live page , the live doesnt appear in the title"
        self.basePage._driver.quit()










