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
    def origination(self, propertyId):
        country_code = 'au'
        params = { 'locationId': location_id, 'locationTypeId': location_type_id}

        try:
            res = requests.get(self.base + "/census/summary", params=params, headers=self.headers)
            res = res.json() # description components: size, parks (#, %), age group, household, repayment (range/m), occupation type, median salary
        except HTTPError as err:
            print(err) 
        
        return res

    def consumer(self):
        pass

    def custom_valutions(self):
        pass
    


if __name__ == "__main__":
    v = Valuations()
    v.test()


'''
Origination (current, historical, live)
/au/properties/{propertyId}/avm/intellival/origination/current
--
/au/properties/{propertyId}/avm/intellival/origination
/au/properties/{propertyId}/avm/intellival/origination/{valuationDate}
--
/au/properties/{propertyId}/liveavm/intellival/origination


Consumer (current, historical, live)


'''