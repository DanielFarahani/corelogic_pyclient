import requests
from datetime import datetime
from ..authentication import Authentication

class Valuations(Authentication):

    def __init__(self, env=""):
        super().__init__(config=env)
        # website: self.base += "avm/au/properties/2/avm/intellival/origination/current"
        # postman: self.base += /property//au/v1/property/avm.json	

        self.base += "/​avm/au​/properties​/"

    # current, historic, live
    def origination(self, propertyId, current=True, date=""):
        """
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
        """

        rtype = "/current" if current else "/{date}"
        endpoint = "/intellival/origination" + rtype
        url = self.base + endpoint
        params = {'countryCode': 'au', 'propertyId': propertyId}

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err 

        return res



    def consumer(self, propertyId, date=""):
        """
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
        """

        # /{propertyId}​/avm​/intellival​/consumer​/current
        rtype = '/current' if not date else f'/{date}'
        endpoint = f'{propertyId}/avm/intellival/consumer' + rtype
        url = self.base + endpoint

        params = {'countryCode': 'au', 'propertyId': propertyId}
        
        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err 

        return res


    # valution based on modified house attributes
    def custom_valution(self, propertyId):
        """
            Description: Get valuation for a hypothetical prperty or renovation project.
        """
        # /origination, /consumer/band
        
        endpoint = str(propertyId) + "/liveavm/intellival/origination"
        url = self.base + endpoint

        return {}

