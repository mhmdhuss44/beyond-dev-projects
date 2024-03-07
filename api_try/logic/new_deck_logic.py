
class newDeck:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url

    def create_new_deck(self):
        new_url=self.url+"api/deck/new"
        result = self.my_api.api_get_request(new_url)
        return result


