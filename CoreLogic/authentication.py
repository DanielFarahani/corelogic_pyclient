# from config import client_id, secret
import json
import requests
from requests.exceptions import HTTPError
import os

class Authentication(object):

    def __init__(self, **kwargs):
        # prod (api), test (api-uat), dev (+ /sandbox)
        env = {'prod' : "https://api.corelogic.asia",
                'test' : "https://api-uat.corelogic.asia",
                'dev' : "https://api-uat.corelogic.asia/sandbox",}
        
        self.base = env[kwargs['config']] if kwargs['config'] else env['dev']
        self.auth = "https://access-api.corelogic.asia"

        client_id = os.environ['client_id']
        secret = os.environ['secret'] 

        self.access_token = 'Bearer ' + self.generate_token(client_id, secret)
        self.headers = {'Content-Type': 'application/json', \
                        'Authorization' : self.access_token}


    # Generate Authentication token
    def generate_token(self, cid, secret):
        url = self.auth + '/access/oauth/token'
        try:
            params = {'grant_type': 'client_credentials', 'client_id': cid, \
                        'client_secret': secret}

            result = requests.get(url, params=params)
            token = result.json()['access_token']

        except HTTPError as err:
            print(f'HTTP error occurred: {err}')

        return token
