from authentication import Authentication
import requests
from requests.exceptions import HTTPError
from datetime import datetime


class Valuations(Authentication):

    def __init__(self, version=1):
        super().__init__(False)
        # self.base += "avm/au/properties/2/avm/intellival/origination/current"
        self.base += "/property/au/v{version}/property/avm"

    def test(self):
        print("testing")

    # current, historic, live
    def origination(self, propertyId, current=True, date=""):
        r'''
            Valuations for collateral risk decisions. Can get current valutions. A list of historic
            valuations. A valuation at a point of time based on yyyy-mm-dd date format. 
            returns: { "valuations": 
                        [ {"confidence": "LOW",
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
        params = {'countryCode': 'au', 'propertyId': propertyId}
        try:
            res = requests.get(self.base + endpoint, params=params, headers=self.headers)
            res = res.json()
        except HTTPError as err:
            return err 
        return res

    def consumer(self):
        pass

    def custom_valutions(self, propertyId):
        base = super.base + "/liveavm/intellival/origination"
    


if __name__ == "__main__":
    v = Valuations()
    v.test()


'''
Origination (current, historical, live)
/au/properties/{propertyId}/avm/intellival/origination
/au/properties/{propertyId}/avm/intellival/origination/current
/au/properties/{propertyId}/avm/intellival/origination/{valuationDate}


Consumer (current, historical, live)


'''