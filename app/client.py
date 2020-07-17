from config import account_info
import json
import requests
from requests.exceptions import HTTPError


class Client(object):

    def __init__(self, dev=False):
        self.access_token = None
        self.url = "https://access-api.corelogic.asia" if not dev else "https://access-api.corelogic.asia/sandbox"
        self.authorise()
    

    def authorise(self):
        endpoint = '/access/oauth/token'
        try:
            payload = {'grant_type': 'client_credentials', 'client_id': account_info['cid'], 'client_secret': account_info['secret']}
            result = requests.get(self.url + endpoint, params=payload)
            self.access_token = result.json()['access_token']

        except HTTPError as err:
            print(f'HTTP error occurred: {err}')
        except requests.exceptions.RequestException as e:
            print(e.text)
        
        




if __name__ == "__main__":
    c = Client()