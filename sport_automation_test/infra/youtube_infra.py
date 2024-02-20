import json

class browserWrapper:
    def __init__(self):
        self.hub = None
        self.testing_mode = None
        self.webLink = None
        self.browsers_list = None
        self.link="confg_info.json"
        # self.load_configurations()

    def load_configurations(self):
        with open(self.link, 'r') as file:
            data = json.load(file)
            self.hub = data.get('hub_url')
            self.testing_mode = data.get('testing_mode')
            self.webLink = data.get('web_link')
            browsers = data.get('browsers', [])
            self.browsers_list = [(browser.get('browser_name'), browser.get('platform_name')) for browser in browsers]


    def get_all_configurations(self):
        # self.load_configurations()
        return {
            "browsers_list": self.browsers_list,
            "hub_url": self.hub,
            "testing_mode": self.testing_mode,
            "web_link": self.webLink
        }

# if __name__ == '__main__':
#     wrapper = browserWrapper()
#
#     # Load configurations from the JSON file
#
#
#     # Get all configurations and print them
#     configurations = wrapper.get_all_configurations()
#     print("All Configurations:")
#     print(configurations)





