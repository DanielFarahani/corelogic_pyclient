import requests
from client import Client

class Auction(Client):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    

    def summaries(self, state, capitalCityOnly=True, stats=""):
        params = {'capitalCityOnly': capitalCityOnly, 'stats':stats}
        res = requests.get(self.url, params=params)

        return res.json()
        