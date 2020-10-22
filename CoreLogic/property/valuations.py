from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime

# TODO confirm request url (or atleast prepare both until CoreLogic confirmation)
class Valuations(Authentication):

    def __init__(self):
        super().__init__()
        self.version = 1
        # website: self.base += "avm/au/properties/2/avm/intellival/origination/current"
        # postman: self.base += /property//au/v1/property/avm.json	

        self.base += "/property/au/v{self.version}/property/avm"

    # current, historic, live
    def origination(self, propertyId, current=True, date=""):
        r'''
            Descriptions: Valuations for collateral risk decisions. 
            Current=True (default) gives current valuations
            Current=False w/o date: gives past 90 days valuation
            current=False w/ data: gives valuation at specific date (yyyy-mm-dd)
            returns: { "valuations": 
                        [ { "confidence": "LOW",
                            "estimate": 0,
                            "fsd": 0,
                            "highEstimate": 0,
                            "lowEstimate": 0,
                            "isCurrent": false,
                            "valuationDate": "string"}
                        ]}
        '''

        rtype = "/current" if current else "/{date}"
        endpoint = "/intellival/origination" + rtype
        url = self.base + endpoint
        params = {'countryCode': 'au', 'propertyId': propertyId}
        print(self.base + endopint)
        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err 

        return res


    def consumer(self, current=True, date=""):
        r'''
            Description: Gets current or historical consumer valutions. 
            Current=True (default) gives current valuations
            Current=False w/o date: gives past 52 week valuation
            current=False w/ data: gives valuation at specific date (yyyy-mm-dd)
            returns: { "valuations": 
                         [ { "confidence": "LOW",
                            "estimate": 0,
                            "fsd": 0,
                            "highEstimate": 0,
                            "isCurrent": false,
                            "lowEstimate": 0,
                            "valuationDate": "string"}
                        ] }
        '''

        rtype = "/current" if current else "/{date}"
        endpoint = "/intellival/consumer" + rtype
        params = {'countryCode': 'au', 'propertyId': propertyId}
        try:
            res = requests.get(self.base + endpoint, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err 
        return res


    # valution based on 
    def custom_valutions(self, propertyId):
        r'''
        Description: Get valuation for a hypothetical or ronovation house.
        '''
        
        base = super.base + "/liveavm/intellival/origination"
        return {}


if __name__ == "__main__":

    v = Valuations()
    v.test()