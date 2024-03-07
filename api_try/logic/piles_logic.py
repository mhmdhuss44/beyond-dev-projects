
class PilesLogic:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url


    def list_cards_in_piles(self,deck_id,formatted_card_codes):
        deck_name="mhmds"
        url = f"{self.url}api/deck/{deck_id}/pile/{deck_name}/add/?cards={formatted_card_codes}"
        response = self.my_api.api_get_request(url)
        print(response.json())
        return response
