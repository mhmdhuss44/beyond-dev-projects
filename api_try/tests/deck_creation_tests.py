import unittest
from infra.api_wrapper import APIWrapper
from logic.new_deck_logic import newDeck


class MainTesrt(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = newDeck(self.my_api,self.my_api.url)
        self.deck=self.api_logic.create_new_deck()

    def test_check_status_new_deck(self):
        self.assertEqual(self.deck.status_code, 200, "Expected status code 200")

    def test_check_success_new_deck(self):
        response_json = self.deck.json()
        self.assertTrue(response_json["success"], "Expected success to be true")

    def test_check_remaining_cards_count(self):
        response_json = self.deck.json()
        self.assertEqual(response_json["remaining"], 52, "Expected remaining cards count to be 52")

    def test_check_shuffled_is_false(self):
        response_json = self.deck.json()
        self.assertFalse(response_json["shuffled"], "Expected shuffled to be false")











