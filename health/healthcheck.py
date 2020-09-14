import requests

class healthcheck:

    def __init__(self):
        self.url = "https://api-uat.corelogic.asia/sandbox/" 
        self.description = { "GREEN": "Available and normal.", "BLUE": "Going through the release process.", 
        "AMBER": "Partially stable." ,"RED": "Not available."}

    def healthcheck_all(self):
        r''' 
            healthcheck all currently implemented endpoints
            return: 
            endpoint and status 
        '''
        pass

    def healthcheck_statistics(self):
        r'''
            Statistics endpoint health check
            returns: 
            State: boolean for logic flow 
            Info: for status and description
        '''
        endpoint = "/statistics/env/health"
        try:
            payload, headers = {}, {}
            response = requests.get(self.url + endpoint, headers=headers, data = payload)
            response = response.json()
            response['description'] = self.description[response['status']]
            state = True if response['status'] == 'GREEN' else False
        except Exception as error:
            return error
        return state, response

    def healthcheck_property(self):
        r'''
            AU property endpoint health check
            returns: 
            State: boolean for logic flow 
            Info: for status and description
        '''
        endpoint = "/property/au/env/health"
        try:
            payload, headers = {}, {}
            response = requests.get(self.url + endpoint, headers=headers, data = payload)
            response = response.json()
            response['description'] = self.description[response['status']]
            state = True if response['status'] == 'GREEN' else False
        except Exception as error:
            return error
        return state, response



if __name__ == "__main__":
    hc = healthcheck()
    print(hc.healthcheck_property())
