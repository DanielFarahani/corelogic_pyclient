import requests
from requests.exceptions import HTTPError
from datetime import datetime

import sys, os
# sys.path.append('../')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from authentication import Authentication


class Suggest(Authentication):
    def __init__(self, country='au', type='v2'):
        super().__init__()

        # website: /property/au/v2/suggest.json
        # website: /property/au/parcel/suggest.json
        # self.base += /property/{country}/{type}

        # postman: /places/places/suggest
        self.stype = "address, street, locality, postcode"


    def suggest_places(self, search, 
        stype="address, street, locality, postcode", 
        limit=10, 
        units=True, 
        bodycorp=True, 
        returnSuggest='datail'):
        """Description: Gives a list of suggestions based on location (street, suburb, state, etc.) input.
            input: address, street (min 3 char), suburb or state (min 2 char). 
            suggestType: "address, street, locality, postcode, territorialAuthority, councilArea, state, country"
            Limit: number of suggestions returned (default 10)
            includesUnits: unit property type (default True)
            includesBodyCorp: include body corporates (default True)
            returnSuggestion: {only, byType, detail}
            returns: {"suggestions": [{
                "councilAreaId": 0,
                "countryId": 0,
                "isBodyCorporate": true,
                "isUnit": true,
                "localityId": 0,
                "postcodeId": 0,
                "propertyId": 0,
                "stateId": 0,
                "streetId": 0,
                "suggestion": "string",
                "suggestionId": 0,
                "suggestionType": "string",
                "territorialAuthorityId": 0}
                ]
                "systemInfo": {
                    "instanceName": "string",
                    "requestDate": "string"}
            }
        """
        # NOTE state abbreviation doesnt work (Contant corelogic)

        # endpoint = '/places/places/suggest'
        # endpoint = '/property/au/parcel/suggest.json'
        endpoint = '/property/au/v2/suggest.json'
        url = self.base + endpoint

        params = {
            'q': search,
            'type': stype,
            'limit': limit,
            'units': units,
            'bodycorp': bodycorp,
            'returnSuggest': returnSuggest,
        }

        try:
            res = requests.get(url, params=params, headers=self.headers)
            res = res.json()

        except HTTPError as err:
            return err
        
        return res


if __name__ == "__main__":
    import sys
    
