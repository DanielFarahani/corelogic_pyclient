import requests

class healthcheck:

    def __init__(self):
        self.url = "https://api-uat.corelogic.asia/sandbox/" 
        self.description = { "GREEN": "available and normal.", "BLUE": "going through the release process.", 
        "AMBER": "partially stable." ,"RED": "not available."}

    def healthcheck_statistics(self):
        r'''
            Statistics endpoint health check
            returns: 
            State: boolean for logic flow 
            Info: for status and description
        '''
        endpoint = "/statistics/env/health"
        try:
            payload = {}
            headers= {}
            response = requests.get(self.url + endpoint, headers=headers, data = payload)
            response = response.json()
            response['description'] = self.description[response['status']
            state = True if response['status'] == 'GREEN' else False
        except Exception as error:
            return error

        return state, response


if __name__ == "__main__":
    hc = healthcheck()
    print(hc.healthcheck_statistics()),