from config import client_id, secret
import json
import requests
from requests.exceptions import HTTPError

class Authentication(object):

    def __init__(self, live=False):
        self.auth = "https://access-api.corelogic.asia"
        self.base = "https://access-api.corelogic.asia" if live  else "https://access-api.corelogic.asia/sandbox"
        self.access_token = self.generate_token(client_id, secret)
        
        self.headers = {'Content-Type': 'application/json', 'Authorization' : 'Bearer ' + self.access_token}

    def generate_token(self, cid, secret):
        endpoint = '/access/oauth/token'
        try:
            params = {'grant_type': 'client_credentials', 'client_id': cid, 'client_secret': secret}
            result = requests.get(self.auth + endpoint, params=params)

        except HTTPError as err:
            print(f'HTTP error occurred: {err}')

        return result.json()['access_token']





if __name__ == "__main__":
    a = Authentication()