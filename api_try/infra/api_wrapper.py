import json

import requests


class APIWrapper:
    PATH_JSON = r"C:\Users\mhmdh\PycharmProjects\api_try\config.json"

    def __init__(self):
        self.response = None
        self.my_request = requests
        self.load_config()



    def load_config(self):
        with open(self.PATH_JSON, 'r') as file:
            json_content = json.load(file)

        self.url = json_content.get('url')



    def api_get_request(self, url):
        self.response = self.my_request.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
