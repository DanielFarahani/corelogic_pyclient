from config import client_id, secret
import json
import requests
from requests.exceptions import HTTPError

class Authentication(object):

    def __init__(self, dev=True):
        # dev (+ sandbox), test (api-uat), prod (api)
        self.prod = "https://api.corelogic.asia"
        self.test = "https://api-uat.corelogic.asia"
        self.dev = "https://api-uat.corelogic.asia/sandbox"
        
        self.base = self.dev if dev else self.test 
        self.auth = "https://access-api.corelogic.asia"

        self.access_token = 'Bearer ' + self.generate_token(client_id, secret)
        self.headers = {'Content-Type': 'application/json', \
                        'Authorization' : self.access_token}

    # Generate Authentication token
    def generate_token(self, cid, secret):
        endpoint = self.auth + '/access/oauth/token'
        try:
            params = {'grant_type': 'client_credentials', \
                        'client_id': cid, 'client_secret': secret}

            result = requests.get(endpoint, params=params)
            token = result.json()['access_token']

        except HTTPError as err:
            print(f'HTTP error occurred: {err}')

        return token



if __name__ == "__main__":
    a = Authentication()