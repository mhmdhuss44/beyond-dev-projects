
class drawCardsLogic:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url

    def draw_cards(self,deck_id,cardnum):
        url = f"{self.url}api/deck/{deck_id}/draw/?count={cardnum}"
        response = self.my_api.api_get_request(url)
        return response

