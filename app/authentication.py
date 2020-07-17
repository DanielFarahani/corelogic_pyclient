from config import account_info
import json
import requests
from requests.exceptions import HTTPError
from auctions import Auction

class Authentication(object):

    def __init__(self, dev=False):
        self.url = "https://access-api.corelogic.asia" if not dev else "https://access-api.corelogic.asia/sandbox"
        self.access_token = self.generate_token()
        self.headers = {'Content-Type': 'application/json',
                        'Authorization' : 'Bearer ' + self.access_token}

        self.auction_class = Auction(self.url, self.headers)

    def generate_token(self):
        endpoint = '/access/oauth/token'
        try:
            payload = {'grant_type': 'client_credentials', 'client_id': account_info['cid'], 'client_secret': account_info['secret']}
            result = requests.get(self.url + endpoint, params=payload)
        
        except HTTPError as err:
            print(f'HTTP error occurred: {err}')

        return result.json()['access_token']





if __name__ == "__main__":
    c = Authentication()