from config import account_info
import json
import requests

class Client(object):

    def __init__(self, dev=False):
        self.access_token = None
        self.url = "https://access-api.corelogic.asia/" if not dev else "https://access-api.corelogic.asia/sandbox/"
        self.authorise()
    

    def authorise(self):
        try:
            endpoint = 'access/oauth/token'
            payload = {'grant_type': 'client_credentials', 'client_id': account_info['secret'], 'client_secret': account_info['cid']}
            result = requests.get(self.url + endpoint, params=payload)
            
            self.access_token = result.json()['access_token']
        except Exception as e:
            print(e)




if __name__ == "__main__":
    pass