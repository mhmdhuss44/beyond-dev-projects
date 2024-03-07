import unittest
from infra.api_wrapper import APIWrapper
from logic.draw_cards_logic import drawCardsLogic
from logic.new_deck_logic import newDeck
from logic.piles_logic import PilesLogic


class cardsPiles(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.api_logic = newDeck(self.my_api,self.my_api.url)
        self.deck=self.api_logic.create_new_deck()
        self.cards=drawCardsLogic(self.my_api,self.my_api.url)
        self.piles=PilesLogic(self.my_api,self.my_api.url)

    # test for creating a pile and adding 3 cards to it
    def test_listing_piles(self):
        drawed_cards_result = self.cards.draw_cards(self.deck.json()["deck_id"], 3)
        response_json = drawed_cards_result.json()
        card_codes = [card["code"] for card in response_json["cards"]]
        # Format card codes for sending to the function
        formatted_card_codes = ",".join(card_codes)

        piles_result = self.piles.list_cards_in_piles(self.deck.json()["deck_id"],formatted_card_codes)
        self.assertTrue(piles_result.json()["success"], "Expected success to be true")









