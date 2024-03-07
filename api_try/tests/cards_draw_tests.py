import unittest
from infra.api_wrapper import APIWrapper
from logic.draw_cards_logic import drawCardsLogic
from logic.new_deck_logic import newDeck


class cardsDraw(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = newDeck(self.my_api,self.my_api.url)
        self.deck=self.api_logic.create_new_deck()
        self.cards = drawCardsLogic(self.my_api, self.my_api.url)

    def test_draw_cards_sucess(self):
        new_deck_result = self.cards.draw_cards(self.deck.json()["deck_id"], 3)
        self.assertEqual(new_deck_result.status_code, 200, "Expected status code 200")

    def test_remaining_cards_count(self):
        new_deck_result = self.cards.draw_cards(self.deck.json()["deck_id"],3)
        response_json=new_deck_result.json()
        self.assertEqual(response_json["remaining"], 49, "Expected remaining cards count to be 49")













